"""
CRUD operations for HackForce AI API
Database operations for bugs, developers, and predictions
"""

from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import List, Optional
from models import Bug, Developer, PredictionLog
from datetime import datetime

# ============================================================================
# Bug CRUD Operations
# ============================================================================

def create_bug(db: Session, bug_data: dict) -> Bug:
    """
    Create a new bug in the database
    """
    db_bug = Bug(**bug_data)
    db.add(db_bug)
    db.commit()
    db.refresh(db_bug)
    return db_bug


def get_bug(db: Session, bug_id: int) -> Optional[Bug]:
    """
    Get a bug by ID
    """
    return db.query(Bug).filter(Bug.id == bug_id).first()


def get_bugs(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    severity: Optional[str] = None,
    status: Optional[str] = None,
    source: Optional[str] = None
) -> List[Bug]:
    """
    Get list of bugs with optional filters
    """
    query = db.query(Bug)
    
    # Apply filters
    if severity:
        query = query.filter(Bug.severity == severity)
    if status:
        query = query.filter(Bug.status == status)
    if source:
        query = query.filter(Bug.source == source)
    
    # Order by created_at descending and apply pagination
    return query.order_by(desc(Bug.created_at)).offset(skip).limit(limit).all()


def update_bug(db: Session, bug_id: int, bug_data: dict) -> Optional[Bug]:
    """
    Update a bug
    """
    db_bug = db.query(Bug).filter(Bug.id == bug_id).first()
    if not db_bug:
        return None
    
    # Update fields
    for key, value in bug_data.items():
        if value is not None and hasattr(db_bug, key):
            setattr(db_bug, key, value)
    
    db.commit()
    db.refresh(db_bug)
    return db_bug


def delete_bug(db: Session, bug_id: int) -> bool:
    """
    Delete a bug
    """
    db_bug = db.query(Bug).filter(Bug.id == bug_id).first()
    if not db_bug:
        return False
    
    db.delete(db_bug)
    db.commit()
    return True


def get_bug_count(db: Session) -> int:
    """
    Get total count of bugs
    """
    return db.query(Bug).count()


def get_bugs_by_severity_count(db: Session) -> dict:
    """
    Get count of bugs grouped by severity
    """
    results = db.query(
        Bug.severity,
        func.count(Bug.id).label('count')
    ).group_by(Bug.severity).all()
    
    return {severity: count for severity, count in results}


# ============================================================================
# Developer CRUD Operations
# ============================================================================

def create_developer(db: Session, developer_data: dict) -> Developer:
    """
    Create a new developer
    """
    db_developer = Developer(**developer_data)
    db.add(db_developer)
    db.commit()
    db.refresh(db_developer)
    return db_developer


def get_developer(db: Session, developer_id: int) -> Optional[Developer]:
    """
    Get a developer by ID
    """
    return db.query(Developer).filter(Developer.id == developer_id).first()


def get_developer_by_email(db: Session, email: str) -> Optional[Developer]:
    """
    Get a developer by email
    """
    return db.query(Developer).filter(Developer.email == email).first()


def get_developers(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None
) -> List[Developer]:
    """
    Get list of developers with optional filters
    """
    query = db.query(Developer)
    
    if status:
        query = query.filter(Developer.status == status)
    
    return query.offset(skip).limit(limit).all()


def update_developer(db: Session, developer_id: int, developer_data: dict) -> Optional[Developer]:
    """
    Update a developer
    """
    db_developer = db.query(Developer).filter(Developer.id == developer_id).first()
    if not db_developer:
        return None
    
    for key, value in developer_data.items():
        if value is not None and hasattr(db_developer, key):
            setattr(db_developer, key, value)
    
    db.commit()
    db.refresh(db_developer)
    return db_developer


def delete_developer(db: Session, developer_id: int) -> bool:
    """
    Delete a developer
    """
    db_developer = db.query(Developer).filter(Developer.id == developer_id).first()
    if not db_developer:
        return False
    
    db.delete(db_developer)
    db.commit()
    return True


def get_developer_workload(db: Session, developer_id: int) -> dict:
    """
    Get workload statistics for a developer
    """
    developer = db.query(Developer).filter(Developer.id == developer_id).first()
    if not developer:
        return None
    
    total_bugs = db.query(Bug).filter(Bug.assigned_developer_id == developer_id).count()
    open_bugs = db.query(Bug).filter(
        Bug.assigned_developer_id == developer_id,
        Bug.status == "Open"
    ).count()
    in_progress = db.query(Bug).filter(
        Bug.assigned_developer_id == developer_id,
        Bug.status == "In Progress"
    ).count()
    resolved = db.query(Bug).filter(
        Bug.assigned_developer_id == developer_id,
        Bug.status == "Resolved"
    ).count()
    
    return {
        "developer_id": developer_id,
        "developer_name": developer.name,
        "total_bugs": total_bugs,
        "open_bugs": open_bugs,
        "in_progress_bugs": in_progress,
        "resolved_bugs": resolved
    }


# ============================================================================
# Prediction Log CRUD Operations
# ============================================================================

def create_prediction_log(db: Session, prediction_data: dict) -> PredictionLog:
    """
    Create a new prediction log entry
    """
    db_prediction = PredictionLog(**prediction_data)
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction


def get_prediction_logs(
    db: Session,
    bug_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100
) -> List[PredictionLog]:
    """
    Get prediction logs with optional bug_id filter
    """
    query = db.query(PredictionLog)
    
    if bug_id:
        query = query.filter(PredictionLog.bug_id == bug_id)
    
    return query.order_by(desc(PredictionLog.prediction_time)).offset(skip).limit(limit).all()


# ============================================================================
# Statistics and Analytics
# ============================================================================

def get_statistics(db: Session) -> dict:
    """
    Get overall statistics for the dashboard
    """
    total_bugs = db.query(Bug).count()
    
    # Count by severity
    severity_counts = db.query(
        Bug.severity,
        func.count(Bug.id).label('count')
    ).group_by(Bug.severity).all()
    
    severity_dict = {
        "Critical": 0,
        "High": 0,
        "Medium": 0,
        "Low": 0
    }
    for severity, count in severity_counts:
        severity_dict[severity] = count
    
    # Count by status
    status_counts = db.query(
        Bug.status,
        func.count(Bug.id).label('count')
    ).group_by(Bug.status).all()
    
    status_dict = {}
    for status, count in status_counts:
        status_dict[status] = count
    
    # Average confidence score
    avg_confidence = db.query(func.avg(Bug.confidence_score)).scalar() or 0
    
    # Total developers
    total_developers = db.query(Developer).count()
    
    return {
        "total_bugs": total_bugs,
        "severity": severity_dict,
        "status": status_dict,
        "average_confidence": round(float(avg_confidence), 2),
        "total_developers": total_developers
    }


def search_bugs(db: Session, search_term: str, limit: int = 50) -> List[Bug]:
    """
    Search bugs by title or description
    """
    search_pattern = f"%{search_term}%"
    return db.query(Bug).filter(
        (Bug.title.ilike(search_pattern)) | 
        (Bug.description.ilike(search_pattern))
    ).order_by(desc(Bug.created_at)).limit(limit).all()
