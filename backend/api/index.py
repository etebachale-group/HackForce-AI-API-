"""
Vercel serverless function entry point for HackForce AI API
"""
import sys
import os

# Get the backend directory (parent of api/)
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path if not already there
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

try:
    # Change to backend directory for relative imports
    os.chdir(backend_dir)
    
    # Import the FastAPI app
    from app import app
    
    # Vercel handler
    handler = app
    
except Exception as e:
    # If import fails, create a minimal error app
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    @app.get("/")
    @app.get("/{path:path}")
    async def error_handler(path: str = ""):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Failed to load application",
                "message": str(e),
                "path": path,
                "backend_dir": backend_dir,
                "sys_path": sys.path[:3]
            }
        )
    
    handler = app
