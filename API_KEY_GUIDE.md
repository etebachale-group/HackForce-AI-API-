## 🔑 API Key System - Developer Guide

### Overview

HackForce AI API now supports API key authentication, allowing external developers to integrate our bug classification system into their applications.

## 🚀 Quick Start

### 1. Generate Your API Key

**Option A: Using the Dashboard**
1. Go to https://hack-force-ai-api.vercel.app/
2. Navigate to "API Keys" section
3. Click "Generate New Key"
4. Fill in your details
5. **Save your key immediately** - it's only shown once!

**Option B: Using the API**

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/keys/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My App Integration",
    "email": "developer@example.com",
    "company": "My Company",
    "rate_limit": 1000
  }'
```

**Response:**
```json
{
  "id": 1,
  "name": "My App Integration",
  "email": "developer@example.com",
  "key": "hf_abc123...xyz789",
  "rate_limit": 1000,
  "created_at": "2026-01-30T20:00:00"
}
```

⚠️ **Important:** Save the `key` value immediately! You won't be able to see it again.

### 2. Use Your API Key

Include your API key in the `X-API-Key` header with every request:

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -H "X-API-Key: hf_your_api_key_here" \
  -d '{
    "title": "Bug title",
    "description": "Bug description",
    "source": "My App"
  }'
```

## 📊 API Key Management

### View Your Keys

```bash
curl "https://hack-force-ai-api.vercel.app/api/keys/my-keys?email=developer@example.com"
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "My App Integration",
    "email": "developer@example.com",
    "key_preview": "...xyz789",
    "is_active": true,
    "usage_count": 245,
    "rate_limit": 1000,
    "created_at": "2026-01-30T20:00:00"
  }
]
```

### Check Usage Statistics

```bash
curl https://hack-force-ai-api.vercel.app/api/keys/1/stats
```

**Response:**
```json
{
  "id": 1,
  "name": "My App Integration",
  "total_requests": 245,
  "rate_limit": 1000,
  "remaining_requests": 755,
  "last_used": "2026-01-30T22:30:00",
  "is_active": true
}
```

### Update Your Key

```bash
curl -X PUT https://hack-force-ai-api.vercel.app/api/keys/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Name",
    "rate_limit": 2000
  }'
```

### Deactivate a Key

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/keys/1/deactivate
```

### Delete a Key

```bash
curl -X DELETE https://hack-force-ai-api.vercel.app/api/keys/1
```

## 💻 Integration Examples

### JavaScript/TypeScript

```javascript
const API_BASE = 'https://hack-force-ai-api.vercel.app';
const API_KEY = 'hf_your_api_key_here';

async function createBug(title, description) {
  const response = await fetch(`${API_BASE}/api/bugs`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': API_KEY
    },
    body: JSON.stringify({
      title,
      description,
      source: 'My App'
    })
  });
  
  return response.json();
}

// Usage
const bug = await createBug(
  'Critical bug',
  'Database connection failed'
);

console.log(`Bug created with severity: ${bug.severity}`);
console.log(`Confidence: ${bug.confidence_score}`);
console.log(`Assigned to: ${bug.assigned_developer}`);
```

### Python

```python
import requests

API_BASE = 'https://hack-force-ai-api.vercel.app'
API_KEY = 'hf_your_api_key_here'

def create_bug(title, description):
    response = requests.post(
        f'{API_BASE}/api/bugs',
        headers={
            'Content-Type': 'application/json',
            'X-API-Key': API_KEY
        },
        json={
            'title': title,
            'description': description,
            'source': 'My App'
        }
    )
    return response.json()

# Usage
bug = create_bug(
    'Critical bug',
    'Database connection failed'
)

print(f"Bug created with severity: {bug['severity']}")
print(f"Confidence: {bug['confidence_score']}")
print(f"Assigned to: {bug['assigned_developer']}")
```

### PHP

```php
<?php
$apiBase = 'https://hack-force-ai-api.vercel.app';
$apiKey = 'hf_your_api_key_here';

function createBug($title, $description) {
    global $apiBase, $apiKey;
    
    $ch = curl_init("$apiBase/api/bugs");
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
        'title' => $title,
        'description' => $description,
        'source' => 'My App'
    ]));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        "X-API-Key: $apiKey"
    ]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    $response = curl_exec($ch);
    curl_close($ch);
    
    return json_decode($response, true);
}

// Usage
$bug = createBug('Critical bug', 'Database connection failed');
echo "Bug created with severity: " . $bug['severity'];
?>
```

### cURL

```bash
# Create bug
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -H "X-API-Key: hf_your_api_key_here" \
  -d '{
    "title": "Critical bug",
    "description": "Database connection failed",
    "source": "My App"
  }'

# Predict severity
curl -X POST https://hack-force-ai-api.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -H "X-API-Key: hf_your_api_key_here" \
  -d '{
    "title": "UI bug",
    "description": "Button misaligned"
  }'

# Get statistics
curl -H "X-API-Key: hf_your_api_key_here" \
  https://hack-force-ai-api.vercel.app/api/stats
```

## 🔒 Security Best Practices

### 1. Keep Your Key Secret
- ❌ Never commit API keys to Git
- ❌ Never expose keys in client-side code
- ✅ Store keys in environment variables
- ✅ Use server-side code for API calls

### 2. Environment Variables

**.env file:**
```env
HACKFORCE_API_KEY=hf_your_api_key_here
```

**JavaScript:**
```javascript
const API_KEY = process.env.HACKFORCE_API_KEY;
```

**Python:**
```python
import os
API_KEY = os.getenv('HACKFORCE_API_KEY')
```

### 3. Rotate Keys Regularly
- Generate new keys periodically
- Deactivate old keys after migration
- Monitor usage for suspicious activity

### 4. Use Different Keys for Different Apps
- Create separate keys for each application
- Easier to track usage
- Easier to revoke if compromised

## 📈 Rate Limits

### Default Limits
- **Free Tier:** 1,000 requests per day
- **Custom Tier:** Up to 10,000 requests per day

### Rate Limit Headers
Every response includes rate limit information:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 755
X-RateLimit-Reset: 2026-01-31T00:00:00Z
```

### Handling Rate Limits

```javascript
async function createBugWithRetry(title, description) {
  try {
    const response = await fetch(`${API_BASE}/api/bugs`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY
      },
      body: JSON.stringify({ title, description })
    });
    
    if (response.status === 429) {
      // Rate limit exceeded
      const resetTime = response.headers.get('X-RateLimit-Reset');
      console.log(`Rate limit exceeded. Resets at: ${resetTime}`);
      return null;
    }
    
    return response.json();
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}
```

## ❌ Error Handling

### Common Errors

**401 Unauthorized - Invalid API Key**
```json
{
  "detail": "Invalid API key"
}
```

**401 Unauthorized - Inactive Key**
```json
{
  "detail": "API key is inactive"
}
```

**401 Unauthorized - Expired Key**
```json
{
  "detail": "API key has expired"
}
```

**429 Too Many Requests - Rate Limit Exceeded**
```json
{
  "detail": "Rate limit exceeded (1000 requests per day)"
}
```

### Error Handling Example

```javascript
async function handleApiCall() {
  try {
    const response = await fetch(url, {
      headers: { 'X-API-Key': API_KEY }
    });
    
    if (!response.ok) {
      const error = await response.json();
      
      switch (response.status) {
        case 401:
          console.error('Authentication failed:', error.detail);
          // Regenerate or check your API key
          break;
        case 429:
          console.error('Rate limit exceeded:', error.detail);
          // Wait and retry later
          break;
        default:
          console.error('API error:', error);
      }
      
      return null;
    }
    
    return response.json();
  } catch (error) {
    console.error('Network error:', error);
    return null;
  }
}
```

## 📚 API Endpoints

All endpoints require the `X-API-Key` header:

### Bugs
- `POST /api/bugs` - Create bug with AI classification
- `GET /api/bugs` - List bugs
- `GET /api/bugs/{id}` - Get specific bug
- `PUT /api/bugs/{id}` - Update bug
- `DELETE /api/bugs/{id}` - Delete bug

### Prediction
- `POST /api/predict` - Predict severity (no save)

### Statistics
- `GET /api/stats` - Get statistics

### Developers
- `POST /api/developers` - Create developer
- `GET /api/developers` - List developers

## 🆘 Support

### Need Help?
- 📖 **Documentation:** https://hack-force-ai-api.vercel.app/docs
- 💬 **Issues:** https://github.com/etebachale-group/HackForce-AI-API-/issues
- 📧 **Email:** support@hackforce-ai.com

### Frequently Asked Questions

**Q: Can I use the same key for multiple applications?**
A: Yes, but we recommend creating separate keys for better tracking and security.

**Q: What happens if I lose my API key?**
A: Generate a new key and deactivate the old one. Keys cannot be recovered.

**Q: Can I increase my rate limit?**
A: Yes, update your key with a higher rate limit (up to 10,000/day).

**Q: Is there a cost for API keys?**
A: Currently, API keys are free with a 1,000 requests/day limit.

---

**Version:** 2.0.0  
**