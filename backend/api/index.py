"""
Vercel serverless function entry point for HackForce AI API
"""
import sys
import os

# Get the backend directory (parent of api/)
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add to Python path
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Change working directory  
try:
    os.chdir(backend_dir)
except:
    pass

# Import the FastAPI app
try:
    from app import app
    # Export for Vercel
    handler = app
except Exception as e:
    # Create a minimal error app if import fails
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    handler = app
    
    @app.get("/")
    async def error_root():
        return JSONResponse(
            status_code=500,
            content={
                "error": "Failed to initialize app",
                "message": str(e),
                "backend_dir": backend_dir,
                "cwd": os.getcwd(),
                "python_path": sys.path[:3]
            }
        )
