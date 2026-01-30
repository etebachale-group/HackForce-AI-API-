"""
Vercel serverless function entry point for HackForce AI API
"""
import sys
import os

# Add parent directory to path so we can import from backend
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import the FastAPI app
from app import app

# Vercel will use this as the ASGI application
# No need for a handler function with FastAPI
