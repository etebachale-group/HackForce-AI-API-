"""
Test script for Groq AI integration
Run this to verify Groq API is working
"""

import os
from dotenv import load_dotenv
from services.groq_service import groq_service

# Load environment variables
load_dotenv()

def test_classification():
    """Test bug classification"""
    print("🧪 Testing Groq AI Bug Classification\n")
    
    # Test cases
    test_bugs = [
        {
            "title": "Critical: Database connection failing",
            "description": "Production database is down, all users affected. Cannot connect to PostgreSQL server."
        },
        {
            "title": "UI button alignment issue",
            "description": "The submit button on the login page is slightly misaligned by 2px"
        },
        {
            "title": "API timeout on large requests",
            "description": "When uploading files larger than 10MB, the API times out after 30 seconds"
        }
    ]
    
    for i, bug in enumerate(test_bugs, 1):
        print(f"Test {i}: {bug['title']}")
        print("-" * 60)
        
        result = groq_service.classify_bug_severity(
            title=bug['title'],
            description=bug['description']
        )
        
        print(f"Severity: {result['severity']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Reasoning: {result['reasoning']}")
        print(f"Impact Areas: {', '.join(result.get('impact_areas', []))}")
        print()

def test_developer_suggestion():
    """Test developer suggestion"""
    print("🧪 Testing Developer Suggestion\n")
    
    developers = [
        {
            "id": 1,
            "name": "Alice Johnson",
            "skills": ["Python", "FastAPI", "PostgreSQL"],
            "workload": 3
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "skills": ["React", "JavaScript", "CSS"],
            "workload": 5
        },
        {
            "id": 3,
            "name": "Carol Davis",
            "skills": ["Python", "Machine Learning", "AI"],
            "workload": 2
        }
    ]
    
    bug_description = "Critical: AI model prediction endpoint returning 500 errors"
    severity = "Critical"
    
    print(f"Bug: {bug_description}")
    print(f"Severity: {severity}")
    print("-" * 60)
    
    result = groq_service.suggest_developer(
        bug_description=bug_description,
        severity=severity,
        developers=developers
    )
    
    print(f"Suggested Developer: {result['developer_name']}")
    print(f"Confidence: {result['confidence']:.2f}")
    print(f"Reasoning: {result['reasoning']}")
    print()

if __name__ == "__main__":
    print("=" * 60)
    print("HackForce AI - Groq Integration Test")
    print("=" * 60)
    print()
    
    # Check if API key is set
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        print(f"✅ GROQ_API_KEY found: {api_key[:20]}...")
    else:
        print("⚠️  GROQ_API_KEY not found - will use fallback mode")
    print()
    
    try:
        test_classification()
        test_developer_suggestion()
        print("✅ All tests completed successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")
