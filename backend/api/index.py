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
os.chdir(backend_dir)

# Import the FastAPI app
from app import app
