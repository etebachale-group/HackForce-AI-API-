"""
Test script to check if all imports work correctly
"""
import sys
import os

print("Python version:", sys.version)
print("Current directory:", os.getcwd())
print("\n" + "="*60)

# Test 1: Basic imports
print("\n1. Testing basic imports...")
try:
    import fastapi
    print("✅ FastAPI imported successfully")
except Exception as e:
    print(f"❌ FastAPI import failed: {e}")

try:
    from pydantic import BaseModel
    print("✅ Pydantic imported successfully")
except Exception as e:
    print(f"❌ Pydantic import failed: {e}")

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv imported successfully")
except Exception as e:
    print(f"❌ python-dotenv import failed: {e}")

# Test 2: Database imports
print("\n2. Testing database imports...")
try:
    import sqlalchemy
    print("✅ SQLAlchemy imported successfully")
except Exception as e:
    print(f"❌ SQLAlchemy import failed: {e}")

try:
    import psycopg2
    print("✅ psycopg2 imported successfully")
except Exception as e:
    print(f"❌ psycopg2 import failed: {e}")

# Test 3: AI imports
print("\n3. Testing AI imports...")
try:
    import groq
    print("✅ Groq imported successfully")
except Exception as e:
    print(f"❌ Groq import failed: {e}")

# Test 4: Local modules
print("\n4. Testing local modules...")

# Add backend to path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

try:
    import database
    print("✅ database module imported successfully")
except Exception as e:
    print(f"❌ database module import failed: {e}")

try:
    import models
    print("✅ models module imported successfully")
except Exception as e:
    print(f"❌ models module import failed: {e}")

try:
    import crud
    print("✅ crud module imported successfully")
except Exception as e:
    print(f"❌ crud module import failed: {e}")

try:
    from services.groq_service import GroqService
    print("✅ groq_service imported successfully")
except Exception as e:
    print(f"❌ groq_service import failed: {e}")

# Test 5: Try importing app
print("\n5. Testing app import...")
try:
    from app import app
    print("✅ app imported successfully")
    print(f"   App title: {app.title}")
    print(f"   App version: {app.version}")
except Exception as e:
    print(f"❌ app import failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("✅ Import test complete!")
