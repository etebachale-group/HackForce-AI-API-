# 🚀 Vercel Environment Variables Setup

## Quick Import Method

1. Go to: https://vercel.com/dashboard
2. Select your project: **hackforce-ai-api**
3. Go to: **Settings** → **Environment Variables**
4. Click: **Add New** → **Paste .env**
5. Copy ALL content from `.env.production` file (in project root)
6. Paste it in Vercel
7. Select: **Production, Preview, Development** (all three)
8. Click: **Save**

## Manual Method (if paste doesn't work)

Add each variable individually:

### 1. DATABASE_URL
```
postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
```

### 2. GROQ_API_KEY
```
gsk_your_actual_groq_api_key_here
```

### 3. API_SECRET_KEY
```
hackforce-secret-2026
```

### 4. ENVIRONMENT
```
production
```

### 5. CORS_ORIGINS
```
https://hackforce-ai-api.vercel.app
```

## After Adding Variables

1. Go to: **Deployments** tab
2. Click: **...** on latest deployment
3. Click: **Redeploy**
4. Wait for deployment to complete

## Update CORS After First Deploy

After your first successful deploy, you'll get a URL like:
`https://hackforce-ai-api-xxx.vercel.app`

Update CORS_ORIGINS with your actual URL:
1. Go back to Environment Variables
2. Edit CORS_ORIGINS
3. Replace with your actual Vercel URL
4. Save and redeploy
