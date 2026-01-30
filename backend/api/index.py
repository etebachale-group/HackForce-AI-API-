"""
Vercel serverless function entry point for HackForce AI API
"""
import sys
import os

# Add parent directory to path so we can import from backend
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Set environment for production
os.environ.setdefault('ENVIRONMENT', 'production')

try:
    # Import the FastAPI app
    from app import app
    
    # Vercel will use this as the ASGI application
    print("✅ FastAPI app loaded successfully")
    
except Exception as e:
    print(f"❌ Error loading app: {e}")
    import traceback
    traceback.print_exc()
    
    # Create a minimal error app
    from fastapi import FastAPI
    app = FastAPI()
    
    @app.get("/")
    @app.get("/api/")
    async def error_handler():
        return {
            "error": "Failed to load application",
            "message": str(e),
            "status": "error"
        }
