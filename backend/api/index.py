"""
Vercel serverless function entry point for HackForce AI API
"""
import sys
import os

print("🚀 Starting HackForce AI API...")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")

# Get the backend directory (parent of api/)
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Backend directory: {backend_dir}")

# Add to Python path
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)
    print(f"✅ Added {backend_dir} to Python path")

# Change working directory
os.chdir(backend_dir)
print(f"✅ Changed working directory to {os.getcwd()}")

# Check environment variables
print("\n📋 Environment variables:")
print(f"DATABASE_URL: {'✅ Set' if os.getenv('DATABASE_URL') else '❌ Not set'}")
print(f"GROQ_API_KEY: {'✅ Set' if os.getenv('GROQ_API_KEY') else '❌ Not set'}")
print(f"ENVIRONMENT: {os.getenv('ENVIRONMENT', 'not set')}")

# Import the FastAPI app
try:
    print("\n📦 Importing FastAPI app...")
    from app import app
    print("✅ FastAPI app imported successfully")
    print(f"   App title: {app.title}")
    print(f"   App version: {app.version}")
except Exception as e:
    print(f"❌ Failed to import app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Vercel handler
handler = app
print("✅ Handler configured")
print("="*60)
