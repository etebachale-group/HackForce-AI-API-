# 🔐 Vercel Environment Variables - HackForce AI API

## Required Environment Variables for Deployment

When deploying to Vercel, add these environment variables in the dashboard:

---

## Backend Environment Variables

### API Configuration
```
API_SECRET_KEY=hackforce-secret-2026-change-in-production
CORS_ORIGINS=https://hackforce-ai-api.vercel.app
ENVIRONMENT=production
DEBUG=False
```

### Groq API (AI Features)
```
GROQ_API_KEY=your_groq_api_key_here
```

**Note:** Replace with your actual Groq API key from your Groq dashboard.

---

## Frontend Environment Variables

### API Configuration
```
VITE_API_URL=/api
VITE_ENVIRONMENT=production
```

---

## How to Add Environment Variables in Vercel

### Method 1: During Initial Setup

1. When importing the project, click "Environment Variables"
2. Add each variable one by one:
   - Name: `GROQ_API_KEY`
   - Value: `[Your Groq API key from backend/.env file]`
   - Environment: Production, Preview, Development (select all)
3. Click "Add"
4. Repeat for all variables above

### Method 2: After Deployment

1. Go to your project in Vercel Dashboard
2. Click "Settings" → "Environment Variables"
3. Click "Add New"
4. Enter Name and Value
5. Select environments (Production, Preview, Development)
6. Click "Save"
7. Redeploy for changes to take effect

---

## Environment Variables by Priority

### Critical (Required for Basic Functionality)
```
✅ VITE_API_URL=/api
✅ API_SECRET_KEY=hackforce-secret-2026-change-in-production
✅ CORS_ORIGINS=https://hackforce-ai-api.vercel.app
✅ GROQ_API_KEY=your_groq_api_key_here
```

### Optional (For Future Features)
```
⏳ DATABASE_URL (when PostgreSQL is integrated)
⏳ NOTION_API_KEY (when Notion integration is ready)
⏳ NOTION_DATABASE_ID (when Notion integration is ready)
⏳ JIRA_SERVER (when Jira integration is ready)
⏳ JIRA_EMAIL (when Jira integration is ready)
⏳ JIRA_API_TOKEN (when Jira integration is ready)
⏳ JIRA_PROJECT_KEY (when Jira integration is ready)
```

---

## Quick Copy-Paste for Vercel

### For Backend/API
```
API_SECRET_KEY=hackforce-secret-2026-change-in-production
CORS_ORIGINS=https://hackforce-ai-api.vercel.app
ENVIRONMENT=production
DEBUG=False
GROQ_API_KEY=your_groq_api_key_here
```

**Important:** Add your actual Groq API key in Vercel dashboard.

### For Frontend
```
VITE_API_URL=/api
VITE_ENVIRONMENT=production
```

---

## Important Notes

### Security
- ⚠️ **Never commit .env files to Git** (already in .gitignore)
- ⚠️ **Change API_SECRET_KEY in production** to a strong random value
- ⚠️ **Keep Groq API key secure** - don't share publicly
- ✅ Environment variables in Vercel are encrypted and secure

### CORS Configuration
- Update `CORS_ORIGINS` with your actual Vercel URL after deployment
- Format: `https://your-actual-url.vercel.app`
- Can include multiple origins separated by commas

### Groq API Key
- This key enables AI-powered bug classification
- Used for advanced NLP features (future implementation)
- Free tier has rate limits - monitor usage

---

## After Adding Environment Variables

1. **Redeploy** your application
   - Go to Deployments tab
   - Click "Redeploy" on latest deployment
   - Or push a new commit to trigger deployment

2. **Verify** environment variables are working
   - Check application logs
   - Test API endpoints
   - Verify no errors in console

3. **Update** if needed
   - Can change values anytime in Settings
   - Must redeploy after changes

---

## Testing Environment Variables

### Local Testing
```bash
# Backend
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('GROQ_API_KEY:', os.getenv('GROQ_API_KEY')[:20] + '...')"
```

### Production Testing
- Check Vercel function logs
- Look for environment variable errors
- Test API endpoints that use Groq

---

## Troubleshooting

### Issue: "Environment variable not found"
**Solution:** 
1. Verify variable name is correct (case-sensitive)
2. Check it's added to correct environment (Production/Preview/Development)
3. Redeploy after adding variables

### Issue: "CORS error"
**Solution:**
1. Update CORS_ORIGINS with actual Vercel URL
2. Make sure URL doesn't have trailing slash
3. Redeploy after updating

### Issue: "Groq API not working"
**Solution:**
1. Verify API key is correct
2. Check Groq API rate limits
3. Look at function logs for errors

---

## Environment Variables Checklist

Before deploying, ensure:
- [ ] All critical variables added
- [ ] CORS_ORIGINS matches your domain
- [ ] API_SECRET_KEY is strong and unique
- [ ] GROQ_API_KEY is correct
- [ ] Frontend VITE_API_URL is set
- [ ] All variables saved
- [ ] Ready to deploy!

---

## Next Steps

1. ✅ Add all environment variables in Vercel
2. ✅ Deploy your application
3. ✅ Test that everything works
4. ✅ Monitor logs for any issues

---

**Your Groq API key is configured and ready to use! 🚀**

---

*Last Updated: January 29, 2026*  
*Security Level: Production Ready* 🔐
