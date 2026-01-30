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

# Change to backend directory for relative imports
os.chdir(backend_dir)

# Import the FastAPI app
from app import app

# Vercel handler
handler = app
