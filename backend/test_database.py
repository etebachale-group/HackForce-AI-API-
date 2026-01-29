"""
Test script to verify database connection and operations
Run this after setting up Supabase to ensure everything works
"""

import sys
from database import test_connection, SessionLocal, create_tables
from models import Bug, Developer, PredictionLog
import crud

def test_database_setup():
    """
    Test complete database setup
    """
    print("=" * 60)
    print("🧪 Testing HackForce AI API Database Setup")
    print("=" * 60)
    print()
    
    # Test 1: Connection
    print("Test 1: Database Connection")
    print("-" * 60)
    if test_connection():
        print("✅ PASS: Database connection successful\n")
    else:
        print("❌ FAIL: Database connection failed")
        print("Check your DATABASE_URL in .env file\n")
        return False
    
    # Test 2: Tables exist
    print("Test 2: Database Tables")
    print("-" * 60)
    try:
        db = SessionLocal()
        
        # Try to query each table
        bug_count = db.query(Bug).count()
        dev_count = db.query(Developer).count()
        pred_count = db.query(PredictionLog).count()
        
        print(f"✅ PASS: bugs table exists ({bug_count} records)")
        print(f"✅ PASS: developers table exists ({dev_count} records)")
        print(f"✅ PASS: predictions_log table exists ({pred_count} records)\n")
        
    except Exception as e:
        print(f"❌ FAIL: Error accessing tables: {e}\n")
        db.close()
        return False
    
    # Test 3: CRUD Operations
    print("Test 3: CRUD Operations")
    print("-" * 60)
    
    try:
        # Create a test bug
        test_bug_data = {
            "title": "Test Bug - Database Connection",
            "description": "This is a test bug to verify database operations are working correctly.",
            "severity": "Low",
            "predicted_severity": "Low",
            "confidence_score": 0.95,
            "status": "Open",
            "source": "Test Script",
            "assigned_developer": "Test Developer"
        }
        
        # CREATE
        new_bug = crud.create_bug(db, test_bug_data)
        print(f"✅ PASS: Created bug with ID: {new_bug.id}")
        
        # READ
        retrieved_bug = crud.get_bug(db, new_bug.id)
        if retrieved_bug and retrieved_bug.title == test_bug_data["title"]:
            print(f"✅ PASS: Retrieved bug successfully")
        else:
            print(f"❌ FAIL: Could not retrieve bug")
            return False
        
        # UPDATE
        updated_bug = crud.update_bug(db, new_bug.id, {"status": "Resolved"})
        if updated_bug and updated_bug.status == "Resolved":
            print(f"✅ PASS: Updated bug successfully")
        else:
            print(f"❌ FAIL: Could not update bug")
            return False
        
        # DELETE
        if crud.delete_bug(db, new_bug.id):
            print(f"✅ PASS: Deleted bug successfully\n")
        else:
            print(f"❌ FAIL: Could not delete bug\n")
            return False
            
    except Exception as e:
        print(f"❌ FAIL: CRUD operations error: {e}\n")
        db.close()
        return False
    
    # Test 4: Statistics
    print("Test 4: Statistics Query")
    print("-" * 60)
    try:
        stats = crud.get_statistics(db)
        print(f"✅ PASS: Statistics retrieved successfully")
        print(f"   Total bugs: {stats['total_bugs']}")
        print(f"   By severity: {stats['severity']}")
        print(f"   By status: {stats['status']}\n")
    except Exception as e:
        print(f"❌ FAIL: Statistics query error: {e}\n")
        db.close()
        return False
    
    # Test 5: Sample Data
    print("Test 5: Sample Data")
    print("-" * 60)
    try:
        bugs = crud.get_bugs(db, limit=5)
        developers = crud.get_developers(db, limit=5)
        
        print(f"✅ PASS: Found {len(bugs)} bugs")
        if bugs:
            print(f"   First bug: {bugs[0].title}")
        
        print(f"✅ PASS: Found {len(developers)} developers")
        if developers:
            print(f"   First developer: {developers[0].name}\n")
            
    except Exception as e:
        print(f"❌ FAIL: Sample data query error: {e}\n")
        db.close()
        return False
    
    db.close()
    
    # Final Summary
    print("=" * 60)
    print("🎉 ALL TESTS PASSED!")
    print("=" * 60)
    print()
    print("Your database is ready to use!")
    print("You can now start the API server with: python app.py")
    print()
    
    return True

if __name__ == "__main__":
    try:
        success = test_database_setup()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
