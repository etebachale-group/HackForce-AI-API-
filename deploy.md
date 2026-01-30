# 🚀 Deployment Guide

## Current Status
✅ Groq AI integration complete
✅ All endpoints updated
✅ Code tested and verified

## Deployment Steps

### 1. Commit Changes
```bash
git add .
git commit -m "feat: Add Groq AI integration for bug classification"
git push origin main
```

### 2. Vercel Auto-Deploy
- Vercel will automatically detect the push
- Build process takes ~2-3 minutes
- Check Vercel dashboard for build logs

### 3. Verify Deployment

#### Check Build Status
1. Go to Vercel dashboard
2. Click on your project
3. Check latest deployment status

#### Test API Endpoints
```bash
# Replace YOUR_DOMAIN with your Vercel URL

# Health check
curl https://YOUR_DOMAIN.vercel.app/health

# API info
curl https://YOUR_DOMAIN.vercel.app/

# Test prediction (with Groq AI)
curl -X POST https://YOUR_DOMAIN.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Database connection timeout",
    "description": "Users cannot login, database times out"
  }'
```

### 4. Monitor Logs

#### Vercel Logs
```bash
vercel logs YOUR_DOMAIN.vercel.app
```

#### Check for Groq API Usage
Look for these log messages:
- ✅ `GROQ_API_KEY found` - API key configured
- ⚠️ `Warning: GROQ_API_KEY not found` - Using fallback mode

## Environment Variables Checklist

Make sure these are set in Vercel:

- [ ] `DATABASE_URL` - Supabase connection string
- [ ] `GROQ_API_KEY` - Groq API key (gsk_...)
- [ ] `API_SECRET_KEY` - API security key
- [ ] `ENVIRONMENT` - Set to "production"
- [ ] `CORS_ORIGINS` - Your frontend URL

## Testing After Deployment

### 1. Test Bug Creation with AI
```bash
curl -X POST https://YOUR_DOMAIN.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Critical: Server crash on startup",
    "description": "Production server crashes immediately after deployment",
    "source": "Production Monitor"
  }'
```

Expected response:
```json
{
  "id": 1,
  "severity": "Critical",
  "confidence_score": 0.92,
  "assigned_developer": "Alice Johnson",
  "status": "Open"
}
```

### 2. Test Prediction Endpoint
```bash
curl -X POST https://YOUR_DOMAIN.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "title": "UI button misaligned",
    "description": "Submit button is 2px off center"
  }'
```

Expected response:
```json
{
  "severity": "Low",
  "confidence": 0.78,
  "suggested_developer": "Bob Smith",
  "reasoning": "Minor UI issue with low user impact"
}
```

### 3. Check Database Integration
```bash
# List all bugs
curl https://YOUR_DOMAIN.vercel.app/api/bugs

# Get statistics
curl https://YOUR_DOMAIN.vercel.app/api/stats
```

## Troubleshooting

### Build Fails
1. Check Vercel build logs
2. Verify `requirements.txt` is correct
3. Ensure Python version compatibility

### API Returns 500 Error
1. Check Vercel function logs
2. Verify `DATABASE_URL` is correct
3. Test database connection in Supabase

### Groq AI Not Working
1. Verify `GROQ_API_KEY` in Vercel
2. Check Groq API quota/limits
3. API will fallback to rule-based if Groq fails

### CORS Errors
1. Check `CORS_ORIGINS` includes your frontend URL
2. Ensure URL format is correct (no trailing slash)
3. Redeploy after updating CORS settings

## Rollback Plan

If deployment fails:
```bash
# Revert to previous commit
git revert HEAD
git push origin main

# Or rollback in Vercel dashboard
# Go to Deployments → Previous deployment → Promote to Production
```

## Success Indicators

✅ Build completes without errors
✅ Health check returns `{"status": "healthy"}`
✅ API docs accessible at `/docs`
✅ Bug creation returns AI classification
✅ Prediction endpoint works
✅ Database queries succeed

## Next Steps After Deployment

1. **Monitor Performance**
   - Check response times
   - Monitor Groq API usage
   - Track error rates

2. **Test Frontend Integration**
   - Verify frontend can connect
   - Test bug creation flow
   - Check developer assignment

3. **Add Sample Data**
   - Create test developers
   - Submit test bugs
   - Verify AI classifications

4. **Documentation**
   - Update README with production URL
   - Document API endpoints
   - Share with team

## Support

- **Vercel Issues**: Check Vercel dashboard logs
- **Database Issues**: Check Supabase dashboard
- **Groq API Issues**: Check Groq console
- **Code Issues**: Review GitHub commits
