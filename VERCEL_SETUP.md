# 🚀 Vercel Environment Variables Setup

## Variables to Add in Vercel Dashboard

Go to: https://vercel.com/dashboard → Your Project → Settings → Environment Variables

### Required Variables:

```bash
# Database (Supabase)
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres

# Groq API
GROQ_API_KEY=gsk_your_groq_api_key_here

# API Configuration
API_SECRET_KEY=hackforce-secret-2026
ENVIRONMENT=production

# CORS (Update with your actual Vercel URL after first deploy)
CORS_ORIGINS=https://your-app.vercel.app,http://localhost:3001
```

### Steps:

1. Go to Vercel Dashboard
2. Select "hackforce-ai-api" project
3. Click "Settings"
4. Click "Environment Variables"
5. Add each variable above
6. Select: Production, Preview, Development (all three)
7. Click "Save"
8. Redeploy the project

### After First Deploy:

Update CORS_ORIGINS with your actual Vercel URL:
```
CORS_ORIGINS=https://hackforce-ai-api.vercel.app
```
