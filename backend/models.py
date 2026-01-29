"""
SQLAlchemy ORM Models for HackForce AI API
Defines database tables: developers, bugs, predictions_log
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Developer(Base):
    """
    Developer model - stores information about developers
    """
    __tablename__ = "developers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    skills = Column(ARRAY(String), default=[])
    workload = Column(Integer, default=0)
    status = Column(String(20), default="Active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationship with bugs
    bugs = relationship("Bug", back_populates="developer")
    
    def __repr__(self):
        return f"<Developer(id={self.id}, name='{self.name}', email='{self.email}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "workload": self.workload,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class Bug(Base):
    """
    Bug model - stores bug reports and their classifications
    """
    __tablename__ = "bugs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(20), nullable=False, index=True)
    predicted_severity = Column(String(20))
    confidence_score = Column(Float)
    status = Column(String(20), default="Open", index=True)
    source = Column(String(100), default="Manual", index=True)
    assigned_developer_id = Column(Integer, ForeignKey("developers.id", ondelete="SET NULL"))
    assigned_developer = Column(String(100))
    notion_page_id = Column(String(100))
    jira_issue_key = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationship with developer
    developer = relationship("Developer", back_populates="bugs")
    
    # Relationship with predictions
    predictions = relationship("PredictionLog", back_populates="bug", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Bug(id={self.id}, title='{self.title}', severity='{self.severity}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "severity": self.severity,
            "predicted_severity": self.predicted_severity,
            "confidence_score": self.confidence_score,
            "status": self.status,
            "source": self.source,
            "assigned_developer_id": self.assigned_developer_id,
            "assigned_developer": self.assigned_developer,
            "notion_page_id": self.notion_page_id,
            "jira_issue_key": self.jira_issue_key,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }


class PredictionLog(Base):
    """
    Prediction Log model - stores AI prediction history
    """
    __tablename__ = "predictions_log"
    
    id = Column(Integer, primary_key=True, index=True)
    bug_id = Column(Integer, ForeignKey("bugs.id", ondelete="CASCADE"), index=True)
    model_version = Column(String(50))
    predicted_severity = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    features_used = Column(Text)
    prediction_time = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationship with bug
    bug = relationship("Bug", back_populates="predictions")
    
    def __repr__(self):
        return f"<PredictionLog(id={self.id}, bug_id={self.bug_id}, severity='{self.predicted_severity}')>"
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            "id": self.id,
            "bug_id": self.bug_id,
            "model_version": self.model_version,
            "predicted_severity": self.predicted_severity,
            "confidence": self.confidence,
            "features_used": self.features_used,
            "prediction_time": self.prediction_time.isoformat() if self.prediction_time else None
        }
