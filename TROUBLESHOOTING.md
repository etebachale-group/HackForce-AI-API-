# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. Error 500 - Internal Server Error

**Symptoms:**
- Frontend shows "API Error: Internal Server Error"
- `/api/bugs` and `/api/stats` return 500

**Possible Causes:**

#### A. Import Errors
**Solution:** Check Vercel function logs
1. Go to Vercel Dashboard
2. Click on your deployment
3. View "Function Logs"
4. Look for Python import errors

#### B. Database Connection Issues
**Solution:** Verify DATABASE_URL
```bash
# Check if DATABASE_URL is set in Vercel
# Settings → Environment Variables → DATABASE_URL
```

#### C. Missing Dependencies
**Solution:** Check requirements.txt
```bash
# Ensure all packages are listed
cat backend/requirements.txt
```

### 2. CORS Errors

**Symptoms:**
- "Access-Control-Allow-Origin" error in browser console

**Solution:**
Update CORS_ORIGINS in Vercel:
```
CORS_ORIGINS=https://hack-force-ai-api.vercel.app,http://localhost:3000
```

### 3. API Keys Not Working

**Symptoms:**
- `/api/keys/` returns 404
- "API Keys endpoints disabled" in logs

**Solution:**
Create the api_keys table in Supabase:
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
```

### 4. Groq AI Not Working

**Symptoms:**
- Bugs created with "fallback mode" reasoning
- Low confidence scores (0.60-0.75)

**Solution:**
Check GROQ_API_KEY in Vercel:
```bash
# Verify key is set correctly
# Should start with: gsk_
```

### 5. Database Connection Failed

**Symptoms:**
- "Database connection failed" in logs
- Can't create or retrieve bugs

**Solution:**
1. Check DATABASE_URL format:
```
postgresql://user:password@host:5432/database
```

2. Test connection in Supabase:
   - Go to Supabase Dashboard
   - Database → Connection Info
   - Copy connection string

3. Update in Vercel:
   - Settings → Environment Variables
   - Update DATABASE_URL
   - Redeploy

### 6. Frontend Not Loading

**Symptoms:**
- Blank page
- "Failed to load data" message

**Solution:**

#### A. Check API URL
Frontend should use relative paths in production:
```javascript
// In frontend/src/services/api.js
const API_URL = import.meta.env.PROD ? '' : 'http://localhost:8000';
```

#### B. Rebuild Frontend
```bash
cd frontend
npm run build
git add dist/
git commit -m "chore: rebuild frontend"
git push
```

### 7. Rate Limit Exceeded

**Symptoms:**
- 429 Too Many Requests
- "Rate limit exceeded" message

**Solution:**
1. Check your API key usage:
```bash
curl https://hack-force-ai-api.vercel.app/api/keys/YOUR_KEY_ID/stats
```

2. Increase rate limit:
```bash
curl -X PUT https://hack-force-ai-api.vercel.app/api/keys/YOUR_KEY_ID \
  -H "Content-Type: application/json" \
  -d '{"rate_limit": 5000}'
```

### 8. Vercel Build Fails

**Symptoms:**
- Build fails in Vercel dashboard
- "Build Error" message

**Common Causes:**

#### A. Python Version Mismatch
**Solution:** Check runtime
```json
// vercel.json
{
  "functions": {
    "backend/api/index.py": {
      "runtime": "python3.9"
    }
  }
}
```

#### B. Missing Dependencies
**Solution:** Update requirements.txt
```bash
pip freeze > backend/requirements.txt
```

#### C. Import Errors
**Solution:** Check all imports are correct
```python
# Make sure all imports are at module level
# Not inside functions or try/except blocks
```

### 9. Slow API Response

**Symptoms:**
- Requests take > 5 seconds
- Timeout errors

**Solutions:**

#### A. Database Query Optimization
```sql
-- Add indexes
CREATE INDEX idx_bugs_severity ON bugs(severity);
CREATE INDEX idx_bugs_status ON bugs(status);
CREATE INDEX idx_bugs_created_at ON bugs(created_at);
```

#### B. Groq API Timeout
```python
# Increase timeout in groq_service.py
response = self.client.chat.completions.create(
    ...,
    timeout=30  # Increase from default
)
```

### 10. Environment Variables Not Working

**Symptoms:**
- "Environment variable not set" errors
- Features not working in production

**Solution:**

1. **Check Vercel Settings:**
   - Go to Settings → Environment Variables
   - Ensure all variables are set for "Production"

2. **Redeploy After Changes:**
```bash
git commit --allow-empty -m "chore: trigger redeploy"
git push origin main
```

3. **Verify in Code:**
```python
import os
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')[:20]}...")
```

## Debugging Tools

### 1. Check Vercel Logs
```bash
vercel logs https://hack-force-ai-api.vercel.app
```

### 2. Test API Locally
```bash
cd backend
python app.py
# Visit http://localhost:8000/docs
```

### 3. Test Database Connection
```bash
cd backend
python test_database.py
```

### 4. Test Groq Integration
```bash
cd backend
python test_groq.py
```

### 5. Check API Health
```bash
curl https://hack-force-ai-api.vercel.app/health
```

## Getting Help

### 1. Check Documentation
- API Docs: https://hack-force-ai-api.vercel.app/docs
- GitHub: https://github.com/etebachale-group/HackForce-AI-API-

### 2. Review Logs
- Vercel Dashboard → Deployments → Function Logs
- Look for error messages and stack traces

### 3. Test Endpoints
Use the interactive docs to test endpoints:
https://hack-force-ai-api.vercel.app/docs

### 4. Common Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| `ModuleNotFoundError` | Missing dependency | Add to requirements.txt |
| `OperationalError` | Database issue | Check DATABASE_URL |
| `401 Unauthorized` | Invalid API key | Check X-API-Key header |
| `429 Too Many Requests` | Rate limit hit | Wait or increase limit |
| `500 Internal Server Error` | Server crash | Check function logs |

## Prevention Tips

### 1. Always Test Locally First
```bash
# Test before deploying
cd backend
python app.py
# Visit http://localhost:8000/docs
```

### 2. Use Environment Variables
Never hardcode:
- API keys
- Database URLs
- Passwords
- Secrets

### 3. Monitor Deployments
- Watch Vercel dashboard during deploys
- Check function logs after deployment
- Test critical endpoints immediately

### 4. Keep Dependencies Updated
```bash
pip list --outdated
pip install --upgrade package_name
```

### 5. Use Version Control
```bash
# Always commit before major changes
git commit -m "checkpoint: before adding feature X"
```

---

**Last Updated:** January 30, 2026
**Version:** 2.0.0
