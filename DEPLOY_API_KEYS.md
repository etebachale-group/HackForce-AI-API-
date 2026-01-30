# 🔑 Deploy API Keys System

## ✅ Changes Made

### 1. Database Model
- Added `APIKey` model to `backend/models.py`
- Secure key generation with `secrets` module
- Usage tracking and rate limiting

### 2. CRUD Operations
- Created `backend/crud_api_keys.py`
- Full CRUD for API keys
- Validation and rate limit checking

### 3. Authentication Middleware
- Created `backend/auth.py`
- API key verification
- Automatic usage tracking

### 4. API Endpoints
- Created `backend/routes_api_keys.py`
- 8 endpoints for key management
- Full documentation

### 5. Graceful Degradation
- API keys are optional
- System works without the table
- Will enable automatically when table is created

## 🚀 Deploy Now

```bash
git add .
git commit -m "feat: Add API Key authentication system (optional)"
git push origin main
```

## 📋 After Deploy

### Step 1: Create the Table in Supabase

1. Go to https://supabase.com/dashboard
2. Select your project
3. Click "SQL Editor"
4. Run this SQL:

```sql
CREATE TABLE IF NOT EXISTS api_keys (
    id SERIAL PRIMARY KEY,
    key VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    company VARCHAR(100),
    is_active INTEGER DEFAULT 1,
    usage_count INTEGER DEFAULT 0,
    rate_limit INTEGER DEFAULT 1000,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_used_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE
);

CREATE INDEX IF NOT EXISTS idx_api_keys_key ON api_keys(key);
CREATE INDEX IF NOT EXISTS idx_api_keys_email ON api_keys(email);
CREATE INDEX IF NOT EXISTS idx_api_keys_is_active ON api_keys(is_active);
```

### Step 2: Redeploy (Optional)

After creating the table, the API keys endpoints will be automatically available.

If you want to force a redeploy:
```bash
git commit --allow-empty -m "chore: trigger redeploy for API keys"
git push origin main
```

## 🧪 Test API Keys

### Generate a Key

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/keys/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Key",
    "email": "test@example.com",
    "rate_limit": 1000
  }'
```

### Use the Key

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_KEY_HERE" \
  -d '{
    "title": "Test Bug",
    "description": "Testing API key authentication"
  }'
```

## 📊 Current Status

- ✅ Backend code ready
- ✅ Graceful degradation implemented
- ✅ Frontend unaffected
- ⏳ Waiting for table creation
- ⏳ Waiting for deployment

## 🎯 What Happens

### Before Table Creation
- API works normally
- No API key endpoints
- Console shows: "⚠️  API Keys endpoints disabled"

### After Table Creation
- API keys endpoints available
- `/api/keys/*` routes active
- Console shows: "✅ API Keys endpoints enabled"

---

**Next Action:** Deploy now, create table later (or vice versa)
