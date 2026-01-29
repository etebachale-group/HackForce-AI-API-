"""
HackForce AI API - Main Application
FastAPI backend for bug classification and developer assignment
Now with PostgreSQL database integration (Supabase)
"""

from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

# Import database components
from database import get_db, test_connection, engine, Base
from models import Bug, Developer, PredictionLog
import crud

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="HackForce AI API",
    description="AI-powered bug classification and developer assignment system with PostgreSQL",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Startup Event - Create tables and test connection
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """
    Run on application startup
    Creates database tables if they don't exist
    """
    print("🚀 Starting HackForce AI API...")
    
    # Test database connection
    if test_connection():
        print("✅ Database connection successful")
    else:
        print("❌ Database connection failed - check DATABASE_URL")
    
    # Create tables if they don't exist
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables ready")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

# ============================================================================
# Pydantic Models for Request/Response
# ============================================================================

class BugCreate(BaseModel):
    """Model for creating a new bug"""
    title: str = Field(..., min_length=5, max_length=255, description="Bug title")
    description: str = Field(..., min_length=10, description="Bug description")
    source: str = Field(default="Manual", description="Source of the bug report")

class BugUpdate(BaseModel):
    """Model for updating a bug"""
    title: Optional[str] = Field(None, min_length=5, max_length=255)
    description: Optional[str] = Field(None, min_length=10)
    status: Optional[str] = Field(None, pattern="^(Open|In Progress|Resolved|Closed)$")
    assigned_developer: Optional[str] = None
    severity: Optional[str] = Field(None, pattern="^(Low|Medium|High|Critical)$")

class BugResponse(BaseModel):
    """Model for bug response"""
    id: int
    title: str
    description: str
    severity: str
    predicted_severity: Optional[str]
    confidence_score: Optional[float]
    assigned_developer: Optional[str]
    status: str
    source: str
    created_at: str
    updated_at: Optional[str]

    class Config:
        from_attributes = True

class PredictionRequest(BaseModel):
    """Model for prediction request"""
    title: str = Field(..., min_length=5, description="Bug title")
    description: str = Field(..., min_length=10, description="Bug description")

class PredictionResponse(BaseModel):
    """Model for prediction response"""
    severity: str
    confidence: float
    suggested_developer: Optional[str]
    reasoning: Optional[str]

class DeveloperCreate(BaseModel):
    """Model for creating a developer"""
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    skills: List[str] = Field(default=[])
    status: str = Field(default="Active", pattern="^(Active|Inactive|On Leave)$")

class DeveloperResponse(BaseModel):
    """Model for developer response"""
    id: int
    name: str
    email: str
    skills: List[str]
    workload: int
    status: str
    created_at: str

    class Config:
        from_attributes = True

# ============================================================================
# Helper Functions
# ============================================================================

def predict_severity_simple(title: str, description: str) -> tuple[str, float]:
    """
    Simple rule-based severity prediction
    TODO: Replace with Groq AI integration
    """
    text = f"{title} {description}".lower()
    
    # Critical keywords
    critical_keywords = [
        "crash", "security", "data loss", "critical", "urgent", 
        "vulnerability", "exploit", "breach", "sql injection"
    ]
    
    # High severity keywords
    high_keywords = [
        "error", "bug", "broken", "not working", "fails", "failure",
        "cannot", "unable", "doesn't work", "500 error", "timeout"
    ]
    
    # Low severity keywords
    low_keywords = [
        "typo", "cosmetic", "minor", "suggestion", "improvement",
        "enhancement", "ui", "text", "color", "spacing"
    ]
    
    # Check for keywords
    if any(keyword in text for keyword in critical_keywords):
        return "Critical", 0.85
    elif any(keyword in text for keyword in high_keywords):
        return "High", 0.75
    elif any(keyword in text for keyword in low_keywords):
        return "Low", 0.70
    else:
        return "Medium", 0.60

def suggest_developer_simple(severity: str) -> str:
    """
    Simple developer suggestion based on severity
    TODO: Replace with smart assignment logic
    """
    suggestions = {
        "Critical": "Senior Developer",
        "High": "Mid-Level Developer",
        "Medium": "Junior Developer",
        "Low": "Intern"
    }
    return suggestions.get(severity, "Available Developer")

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "message": "Welcome to HackForce AI API",
        "version": "2.0.0",
        "status": "running",
        "database": "PostgreSQL (Supabase)",
        "docs": "/docs",
        "endpoints": {
            "bugs": "/api/bugs",
            "developers": "/api/developers",
            "predict": "/api/predict",
            "stats": "/api/stats"
        }
    }

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Health check endpoint"""
    try:
        # Test database connection
        db.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return {
        "status": "healthy",
        "database": db_status,
        "version": "2.0.0"
    }

# ============================================================================
# Bug Endpoints
# ============================================================================

@app.post("/api/bugs", response_model=BugResponse, status_code=201)
async def create_bug(bug: BugCreate, db: Session = Depends(get_db)):
    """
    Create a new bug with AI severity prediction
    """
    # Predict severity using simple rules (TODO: use Groq AI)
    predicted_severity, confidence = predict_severity_simple(bug.title, bug.description)
    suggested_dev = suggest_developer_simple(predicted_severity)
    
    # Prepare bug data
    bug_data = {
        "title": bug.title,
        "description": bug.description,
        "source": bug.source,
        "severity": predicted_severity,
        "predicted_severity": predicted_severity,
        "confidence_score": confidence,
        "assigned_developer": suggested_dev,
        "status": "Open"
    }
    
    # Create bug in database
    db_bug = crud.create_bug(db, bug_data)
    
    # Create prediction log
    prediction_data = {
        "bug_id": db_bug.id,
        "model_version": "rule-based-v1",
        "predicted_severity": predicted_severity,
        "confidence": confidence,
        "features_used": "keyword_matching"
    }
    crud.create_prediction_log(db, prediction_data)
    
    return db_bug.to_dict()

@app.get("/api/bugs", response_model=List[BugResponse])
async def list_bugs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    severity: Optional[str] = Query(None, pattern="^(Low|Medium|High|Critical)$"),
    status: Optional[str] = Query(None, pattern="^(Open|In Progress|Resolved|Closed)$"),
    source: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get list of bugs with optional filters
    """
    bugs = crud.get_bugs(db, skip=skip, limit=limit, severity=severity, status=status, source=source)
    return [bug.to_dict() for bug in bugs]

@app.get("/api/bugs/{bug_id}", response_model=BugResponse)
async def get_bug(bug_id: int, db: Session = Depends(get_db)):
    """
    Get a specific bug by ID
    """
    bug = crud.get_bug(db, bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail=f"Bug with id {bug_id} not found")
    return bug.to_dict()

@app.put("/api/bugs/{bug_id}", response_model=BugResponse)
async def update_bug(bug_id: int, bug_update: BugUpdate, db: Session = Depends(get_db)):
    """
    Update a bug
    """
    # Prepare update data (only include non-None values)
    update_data = {k: v for k, v in bug_update.dict().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    updated_bug = crud.update_bug(db, bug_id, update_data)
    if not updated_bug:
        raise HTTPException(status_code=404, detail=f"Bug with id {bug_id} not found")
    
    return updated_bug.to_dict()

@app.delete("/api/bugs/{bug_id}")
async def delete_bug(bug_id: int, db: Session = Depends(get_db)):
    """
    Delete a bug
    """
    success = crud.delete_bug(db, bug_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Bug with id {bug_id} not found")
    
    return {"message": f"Bug {bug_id} deleted successfully"}

@app.get("/api/bugs/search/{search_term}")
async def search_bugs(search_term: str, db: Session = Depends(get_db)):
    """
    Search bugs by title or description
    """
    bugs = crud.search_bugs(db, search_term)
    return [bug.to_dict() for bug in bugs]

# ============================================================================
# Developer Endpoints
# ============================================================================

@app.post("/api/developers", response_model=DeveloperResponse, status_code=201)
async def create_developer(developer: DeveloperCreate, db: Session = Depends(get_db)):
    """
    Create a new developer
    """
    # Check if email already exists
    existing = crud.get_developer_by_email(db, developer.email)
    if existing:
        raise HTTPException(status_code=400, detail="Developer with this email already exists")
    
    developer_data = developer.dict()
    db_developer = crud.create_developer(db, developer_data)
    return db_developer.to_dict()

@app.get("/api/developers", response_model=List[DeveloperResponse])
async def list_developers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    status: Optional[str] = Query(None, pattern="^(Active|Inactive|On Leave)$"),
    db: Session = Depends(get_db)
):
    """
    Get list of developers
    """
    developers = crud.get_developers(db, skip=skip, limit=limit, status=status)
    return [dev.to_dict() for dev in developers]

@app.get("/api/developers/{developer_id}", response_model=DeveloperResponse)
async def get_developer(developer_id: int, db: Session = Depends(get_db)):
    """
    Get a specific developer by ID
    """
    developer = crud.get_developer(db, developer_id)
    if not developer:
        raise HTTPException(status_code=404, detail=f"Developer with id {developer_id} not found")
    return developer.to_dict()

@app.get("/api/developers/{developer_id}/workload")
async def get_developer_workload(developer_id: int, db: Session = Depends(get_db)):
    """
    Get workload statistics for a developer
    """
    workload = crud.get_developer_workload(db, developer_id)
    if not workload:
        raise HTTPException(status_code=404, detail=f"Developer with id {developer_id} not found")
    return workload

# ============================================================================
# Prediction Endpoint
# ============================================================================

@app.post("/api/predict", response_model=PredictionResponse)
async def predict_severity(prediction: PredictionRequest):
    """
    Predict bug severity without saving to database
    """
    severity, confidence = predict_severity_simple(prediction.title, prediction.description)
    suggested_dev = suggest_developer_simple(severity)
    
    return {
        "severity": severity,
        "confidence": confidence,
        "suggested_developer": suggested_dev,
        "reasoning": f"Based on keyword analysis, this bug appears to be {severity} severity"
    }

# ============================================================================
# Statistics Endpoint
# ============================================================================

@app.get("/api/stats")
async def get_statistics(db: Session = Depends(get_db)):
    """
    Get overall statistics for dashboard
    """
    stats = crud.get_statistics(db)
    return stats

# ============================================================================
# Run Application
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
