"""
Database configuration and connection setup for HackForce AI API
Uses SQLAlchemy with PostgreSQL (Supabase)
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create SQLAlchemy engine
# Note: Supabase uses connection pooling, so we configure accordingly
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=10,  # Number of connections to maintain
    max_overflow=20,  # Maximum number of connections to create beyond pool_size
    echo=False  # Set to True for SQL query logging (useful for debugging)
)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Dependency function to get database session
    Usage in FastAPI endpoints:
        @app.get("/endpoint")
        def endpoint(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to test database connection
def test_connection():
    """
    Test database connection
    Returns True if connection is successful, False otherwise
    """
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

# Function to create all tables
def create_tables():
    """
    Create all tables defined in models
    Should be called after importing all models
    """
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

# Function to drop all tables (use with caution!)
def drop_tables():
    """
    Drop all tables - USE WITH CAUTION!
    Only use in development/testing
    """
    Base.metadata.drop_all(bind=engine)
    print("⚠️  All database tables dropped!")
