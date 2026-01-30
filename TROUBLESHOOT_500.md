# 🔧 Troubleshooting 500 Errors

## Current Issue

The API is returning 500 Internal Server Error when accessing endpoints like `/api/bugs` or `/api/stats`.

---

## Possible Causes

### 1. Database Connection Issues
**Symptoms:**
- 500 errors on all API endpoints
- Frontend loads but shows "Failed to load data"

**Check:**
```bash
# Test database connection in Supabase
# Go to: https://supabase.com/dashboard
# Project: HackForce AI
# Check if database is running
```

**Fix:**
- Verify `DATABASE_URL` in Vercel environment variables
- Check if Supabase project is active
- Test connection string manually

### 2. Missing Environment Variables
**Required Variables in Vercel:**
- `DATABASE_URL` - PostgreSQL connection string
- `GROQ_API_KEY` - AI classification key
- `API_SECRET_KEY` - Security key
- `ENVIRONMENT` - Set to "production"
- `CORS_ORIGINS` - Frontend URL

**How to Check:**
1. Go to Vercel dashboard
2. Select project "hack-force-ai-api"
3. Settings → Environment Variables
4. Verify all variables are set

### 3. Import Errors
**Symptoms:**
- Function crashes on startup
- Logs show "ModuleNotFoundError"

**Check Vercel Logs:**
1. Go to Vercel dashboard
2. Click on latest deployment
3. Click "Functions" tab
4. Click "api/index.py"
5. Check logs for errors

### 4. API Key Model Issues
**Current Status:** APIKey model is commented out

**If you see errors about APIKey:**
- The model is intentionally disabled
- Routes are disabled with `API_KEYS_ENABLED = False`
- This should not cause errors

---

## Step-by-Step Debugging

### Step 1: Check Vercel Deployment Status
```bash
# Visit Vercel dashboard
https://vercel.com/etebachale-groups-projects/hack-force-ai-api

# Check if deployment succeeded
# Look for green checkmark
```

### Step 2: View Function Logs
1. Click on latest deployment
2. Go to "Functions" tab
3. Click on "api/index.py"
4. Look for error messages in logs

**Common errors to look for:**
- `ModuleNotFoundError` - Missing dependency
- `OperationalError` - Database connection failed
- `ImportError` - Module import failed
- `KeyError` - Missing environment variable

### Step 3: Test Database Connection
```python
# Create a simple test endpoint
# Add to backend/app.py:

@app.get("/test-db")
async def test_db():
    try:
        from database import test_connection
        if test_connection():
            return {"status": "success", "message": "Database connected"}
        else:
            return {"status": "error", "message": "Database connection failed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```

### Step 4: Check Environment Variables
```python
# Add debug endpoint (REMOVE AFTER TESTING):

@app.get("/debug-env")
async def debug_env():
    import os
    return {
        "database_url_set": bool(os.getenv("DATABASE_URL")),
        "groq_key_set": bool(os.getenv("GROQ_API_KEY")),
        "environment": os.getenv("ENVIRONMENT", "not set"),
        "python_version": sys.version
    }
```

---

## Quick Fixes

### Fix 1: Restart Vercel Function
1. Go to Vercel dashboard
2. Click "Redeploy" button
3. Wait for deployment to complete

### Fix 2: Clear Build Cache
1. Go to Vercel dashboard
2. Settings → General
3. Scroll to "Build & Development Settings"
4. Click "Clear Build Cache"
5. Redeploy

### Fix 3: Check Database
1. Go to Supabase dashboard
2. Check if project is paused
3. If paused, click "Resume"
4. Test connection from SQL Editor

### Fix 4: Verify Requirements
Check `backend/requirements.txt`:
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
pydantic==2.5.0
pydantic-settings==2.1.0
python-dotenv==1.0.0
sqlalchemy==2.0.46
psycopg2-binary==2.9.9
groq==0.11.0
```

---

## Common Error Messages

### Error: "FUNCTION_INVOCATION_FAILED"
**Cause:** Function crashed during execution

**Solutions:**
1. Check function logs for specific error
2. Verify all imports work
3. Check database connection
4. Verify environment variables

### Error: "NOT_FOUND"
**Cause:** Route not configured correctly

**Solutions:**
1. Check `vercel.json` routes configuration
2. Verify `backend/api/index.py` exports `handler`
3. Check if function is deployed

### Error: "Internal Server Error"
**Cause:** Unhandled exception in code

**Solutions:**
1. Add try-catch blocks
2. Check logs for stack trace
3. Test locally first

---

## Testing Locally

### Setup Local Environment
```bash
# 1. Create virtual environment
cd backend
python -m venv venv

# 2. Activate (Windows)
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
# Copy from .env.example

# 5. Run server
uvicorn app:app --reload --port 8000

# 6. Test
curl http://localhost:8000/health
curl http://localhost:8000/api/stats
```

---

## Vercel-Specific Issues

### Issue: Python Version Mismatch
**Solution:** Vercel uses Python 3.12 by default

Add to `vercel.json`:
```json
{
  "build": {
    "env": {
      "PYTHON_VERSION": "3.12"
    }
  }
}
```

### Issue: Cold Start Timeout
**Solution:** Increase timeout

Add to `vercel.json`:
```json
{
  "functions": {
    "backend/api/index.py": {
      "maxDuration": 30
    }
  }
}
```

### Issue: Large Dependencies
**Solution:** Already configured with `maxLambdaSize: 50mb`

---

## Emergency Rollback

If nothing works, rollback to previous working version:

```bash
# 1. Find last working commit
git log --oneline

# 2. Rollback
git revert <commit-hash>

# 3. Push
git push origin main

# 4. Wait for Vercel to redeploy
```

---

## Contact Support

If issue persists:

1. **Vercel Support:**
   - Dashboard → Help
   - Include deployment ID
   - Include error logs

2. **Supabase Support:**
   - Dashboard → Support
   - Include project ID
   - Include connection errors

3. **GitHub Issues:**
   - Create issue with:
     - Error message
     - Steps to reproduce
     - Vercel logs
     - Environment details

---

## Next Steps

1. ✅ Check Vercel deployment logs
2. ✅ Verify environment variables
3. ✅ Test database connection
4. ✅ Check function handler
5. ✅ Review recent code changes

**Most likely cause:** Database connection or environment variable issue

**Quick test:** Try accessing `/health` endpoint - if it fails, it's a startup issue
