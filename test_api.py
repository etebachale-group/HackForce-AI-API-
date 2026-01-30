"""
Simple test script to check API endpoints
"""
import requests
import json

BASE_URL = "https://hack-force-ai-api.vercel.app"

def test_endpoint(endpoint, method="GET", data=None):
    """Test an API endpoint"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n{'='*60}")
    print(f"Testing: {method} {endpoint}")
    print(f"{'='*60}")
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=10)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ SUCCESS")
            try:
                print(json.dumps(response.json(), indent=2))
            except:
                print(response.text[:500])
        else:
            print("❌ FAILED")
            print(f"Response: {response.text[:500]}")
            
    except Exception as e:
        print(f"❌ ERROR: {e}")

# Test endpoints
print("🧪 Testing HackForce AI API")
print(f"Base URL: {BASE_URL}")

# Test 1: Root endpoint
test_endpoint("/")

# Test 2: Health check
test_endpoint("/health")

# Test 3: API Stats
test_endpoint("/api/stats")

# Test 4: List bugs
test_endpoint("/api/bugs")

# Test 5: Create bug
test_endpoint("/api/bugs", method="POST", data={
    "title": "Test bug from Python script",
    "description": "This is a test bug to verify the API is working correctly. It should be classified by AI.",
    "source": "Python Test Script"
})

print("\n" + "="*60)
print("✅ Testing complete!")
print("="*60)
