"""
AI Bug Classification API - Main Application
FastAPI backend for bug classification and developer assignment
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="AI Bug Classification API",
    description="API for automated bug classification and developer assignment",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Pydantic Models
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

class StatsResponse(BaseModel):
    """Model for statistics response"""
    total_bugs: int
    by_severity: dict
    by_status: dict
    open_bugs: int
    closed_bugs: int

# ============================================================================
# In-Memory Storage (Temporary - Replace with Database)
# ============================================================================

bugs_db: List[dict] = []
bug_id_counter = 1

# ============================================================================
# Helper Functions
# ============================================================================

def predict_severity_simple(title: str, description: str) -> tuple[str, float]:
    """
    Simple rule-based severity prediction
    TODO: Replace with trained ML model
    """
    text = f"{title} {description}".lower()
    
    # Critical keywords
    critical_keywords = ["critical", "crash", "security", "data loss", "vulnerability", 
                        "exploit", "breach", "corruption", "fatal"]
    
    # High severity keywords
    high_keywords = ["error", "bug", "broken", "not working", "failure", "exception",
                    "cannot", "unable", "blocked"]
    
    # Medium severity keywords
    medium_keywords = ["issue", "problem", "slow", "performance", "delay", "warning",
                      "incorrect", "unexpected"]
    
    # Low severity keywords
    low_keywords = ["typo", "cosmetic", "minor", "suggestion", "enhancement", "improvement"]
    
    # Check for keywords
    if any(keyword in text for keyword in critical_keywords):
        return "Critical", 0.9
    elif any(keyword in text for keyword in high_keywords):
        return "High", 0.8
    elif any(keyword in text for keyword in medium_keywords):
        return "Medium", 0.7
    elif any(keyword in text for keyword in low_keywords):
        return "Low", 0.6
    else:
        return "Medium", 0.5

def suggest_developer_simple(severity: str) -> str:
    """
    Simple developer assignment
    TODO: Replace with ML-based assignment
    """
    developer_map = {
        "Critical": "Senior Developer",
        "High": "Mid-Level Developer",
        "Medium": "Junior Developer",
        "Low": "Junior Developer"
    }
    return developer_map.get(severity, "Unassigned")

# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "AI Bug Classification API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", tags=["Root"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.post("/api/bugs", response_model=BugResponse, tags=["Bugs"])
async def create_bug(bug: BugCreate):
    """
    Create a new bug report
    - Automatically predicts severity using AI
    - Suggests developer assignment
    - Stores in database
    """
    global bug_id_counter
    
    # Predict severity
    predicted_severity, confidence = predict_severity_simple(bug.title, bug.description)
    
    # Suggest developer
    suggested_developer = suggest_developer_simple(predicted_severity)
    
    # Create bug entry
    new_bug = {
        "id": bug_id_counter,
        "title": bug.title,
        "description": bug.description,
        "severity": predicted_severity,
        "predicted_severity": predicted_severity,
        "confidence_score": confidence,
        "assigned_developer": suggested_developer,
        "status": "Open",
        "source": bug.source,
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": None
    }
    
    bugs_db.append(new_bug)
    bug_id_counter += 1
    
    return new_bug

@app.get("/api/bugs", response_model=List[BugResponse], tags=["Bugs"])
async def list_bugs(
    severity: Optional[str] = Query(None, description="Filter by severity"),
    status: Optional[str] = Query(None, description="Filter by status"),
    source: Optional[str] = Query(None, description="Filter by source"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of results"),
    skip: int = Query(0, ge=0, description="Number of results to skip")
):
    """
    List all bugs with optional filters
    - Filter by severity, status, or source
    - Pagination support
    """
    filtered_bugs = bugs_db.copy()
    
    # Apply filters
    if severity:
        filtered_bugs = [b for b in filtered_bugs if b["severity"] == severity]
    if status:
        filtered_bugs = [b for b in filtered_bugs if b["status"] == status]
    if source:
        filtered_bugs = [b for b in filtered_bugs if b["source"] == source]
    
    # Apply pagination
    paginated_bugs = filtered_bugs[skip:skip + limit]
    
    return paginated_bugs

@app.get("/api/bugs/{bug_id}", response_model=BugResponse, tags=["Bugs"])
async def get_bug(bug_id: int):
    """Get a specific bug by ID"""
    bug = next((b for b in bugs_db if b["id"] == bug_id), None)
    if not bug:
        raise HTTPException(status_code=404, detail=f"Bug with ID {bug_id} not found")
    return bug

@app.put("/api/bugs/{bug_id}", response_model=BugResponse, tags=["Bugs"])
async def update_bug(bug_id: int, bug_update: BugUpdate):
    """Update a bug"""
    bug = next((b for b in bugs_db if b["id"] == bug_id), None)
    if not bug:
        raise HTTPException(status_code=404, detail=f"Bug with ID {bug_id} not found")
    
    # Update fields
    if bug_update.title:
        bug["title"] = bug_update.title
    if bug_update.description:
        bug["description"] = bug_update.description
    if bug_update.status:
        bug["status"] = bug_update.status
    if bug_update.assigned_developer:
        bug["assigned_developer"] = bug_update.assigned_developer
    
    bug["updated_at"] = datetime.utcnow().isoformat()
    
    return bug

@app.delete("/api/bugs/{bug_id}", tags=["Bugs"])
async def delete_bug(bug_id: int):
    """Delete a bug"""
    global bugs_db
    bug = next((b for b in bugs_db if b["id"] == bug_id), None)
    if not bug:
        raise HTTPException(status_code=404, detail=f"Bug with ID {bug_id} not found")
    
    bugs_db = [b for b in bugs_db if b["id"] != bug_id]
    return {"message": f"Bug {bug_id} deleted successfully"}

@app.post("/api/predict", response_model=PredictionResponse, tags=["AI"])
async def predict_severity(request: PredictionRequest):
    """
    Predict bug severity without saving
    - Uses AI model to classify severity
    - Suggests developer assignment
    - Returns confidence score
    """
    severity, confidence = predict_severity_simple(request.title, request.description)
    suggested_developer = suggest_developer_simple(severity)
    
    return {
        "severity": severity,
        "confidence": confidence,
        "suggested_developer": suggested_developer,
        "reasoning": "Based on keyword analysis (ML model coming soon)"
    }

@app.get("/api/stats", response_model=StatsResponse, tags=["Statistics"])
async def get_stats():
    """
    Get bug statistics
    - Total bugs
    - Distribution by severity
    - Distribution by status
    """
    total = len(bugs_db)
    
    by_severity = {
        "Low": len([b for b in bugs_db if b["severity"] == "Low"]),
        "Medium": len([b for b in bugs_db if b["severity"] == "Medium"]),
        "High": len([b for b in bugs_db if b["severity"] == "High"]),
        "Critical": len([b for b in bugs_db if b["severity"] == "Critical"]),
    }
    
    by_status = {
        "Open": len([b for b in bugs_db if b["status"] == "Open"]),
        "In Progress": len([b for b in bugs_db if b["status"] == "In Progress"]),
        "Resolved": len([b for b in bugs_db if b["status"] == "Resolved"]),
        "Closed": len([b for b in bugs_db if b["status"] == "Closed"]),
    }
    
    return {
        "total_bugs": total,
        "by_severity": by_severity,
        "by_status": by_status,
        "open_bugs": by_status["Open"],
        "closed_bugs": by_status["Closed"]
    }

# ============================================================================
# Run Application
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
