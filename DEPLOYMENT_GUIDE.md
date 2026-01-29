# 🚀 Deployment Guide - Vercel

## Quick Deploy to Vercel

### Prerequisites
- GitHub account
- Vercel account (free tier is fine)
- Git installed locally

---

## Step 1: Prepare Git Repository

### 1.1 Initialize Git (if not already done)
```bash
git init
git add .
git commit -m "Initial commit - AI Bug Classification API"
```

### 1.2 Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository named `AI-Bug-Classification-API`
3. Don't initialize with README (we already have one)

### 1.3 Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/AI-Bug-Classification-API.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Vercel

### Option A: Using Vercel Dashboard (Easiest)

1. **Go to Vercel**
   - Visit https://vercel.com
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New..." → "Project"
   - Select your GitHub repository
   - Click "Import"

3. **Configure Project**
   
   **Framework Preset:** Other
   
   **Root Directory:** Leave as `.` (root)
   
   **Build Settings:**
   - Build Command: `npm run build` (for frontend)
   - Output Directory: `frontend/dist`
   - Install Command: `npm install`

4. **Environment Variables**
   
   Add these in the Vercel dashboard:
   ```
   CORS_ORIGINS=https://your-app.vercel.app
   API_SECRET_KEY=your-production-secret-key
   ENVIRONMENT=production
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live!

### Option B: Using Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Deploy to Production**
   ```bash
   vercel --prod
   ```

---

## Step 3: Configure Backend API

### 3.1 Separate Backend Deployment (Recommended)

For better performance, deploy backend separately:

1. **Create a new Vercel project for backend**
   - In Vercel dashboard, click "Add New..." → "Project"
   - Import the same repository
   - Set Root Directory to `backend`

2. **Configure Backend**
   - Framework Preset: Other
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   - Install Command: `pip install -r requirements_simple.txt`

3. **Environment Variables for Backend**
   ```
   API_SECRET_KEY=your-secret-key
   CORS_ORIGINS=https://your-frontend.vercel.app
   ENVIRONMENT=production
   ```

### 3.2 Update Frontend API URL

After backend is deployed, update frontend environment:

In Vercel dashboard (Frontend project):
- Go to Settings → Environment Variables
- Add: `VITE_API_URL=https://your-backend.vercel.app`
- Redeploy frontend

---

## Step 4: Verify Deployment

### 4.1 Test Backend
```bash
curl https://your-backend.vercel.app/health
curl https://your-backend.vercel.app/api/stats
```

### 4.2 Test Frontend
1. Visit https://your-frontend.vercel.app
2. Create a test bug
3. Verify it appears in the list
4. Check statistics update

---

## 🎯 Deployment Structure

### Two-Project Setup (Recommended)

```
Project 1: Frontend
├── URL: https://ai-bug-frontend.vercel.app
├── Root: /frontend
└── Env: VITE_API_URL

Project 2: Backend
├── URL: https://ai-bug-backend.vercel.app
├── Root: /backend
└── Env: CORS_ORIGINS, API_SECRET_KEY
```

### Single-Project Setup (Alternative)

```
Project: Full Stack
├── URL: https://ai-bug-app.vercel.app
├── Root: /
├── Frontend: /
└── Backend: /api/*
```

---

## 📝 Important Notes

### CORS Configuration
Make sure to update CORS_ORIGINS in backend to include your Vercel frontend URL:
```python
# In backend/app.py or environment variable
CORS_ORIGINS=https://your-frontend.vercel.app,http://localhost:3000
```

### Environment Variables
- Never commit `.env` files
- Set all environment variables in Vercel dashboard
- Use different secrets for production

### Cold Starts
- Vercel serverless functions may have cold starts
- First request might be slower (1-2 seconds)
- Subsequent requests are fast

### Free Tier Limits
- 100GB bandwidth per month
- Serverless function execution time: 10 seconds
- 100 deployments per day
- More than enough for this project!

---

## 🔧 Troubleshooting

### Issue: "Module not found"
**Solution:** Make sure `requirements_simple.txt` is in the backend directory

### Issue: "CORS error"
**Solution:** Update CORS_ORIGINS environment variable with your frontend URL

### Issue: "Build failed"
**Solution:** Check build logs in Vercel dashboard, ensure all dependencies are listed

### Issue: "API not responding"
**Solution:** Check serverless function logs in Vercel dashboard

---

## 🎉 Post-Deployment

### Custom Domain (Optional)
1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

### Monitoring
- View deployment logs in Vercel dashboard
- Check function logs for errors
- Monitor bandwidth usage

### Continuous Deployment
- Every push to `main` branch auto-deploys
- Preview deployments for pull requests
- Rollback to previous deployments anytime

---

## 📊 Deployment Checklist

### Pre-Deployment
- [ ] Code committed to Git
- [ ] Repository pushed to GitHub
- [ ] Environment variables documented
- [ ] Build tested locally

### Deployment
- [ ] Vercel account created
- [ ] Project imported
- [ ] Environment variables set
- [ ] First deployment successful

### Post-Deployment
- [ ] Backend health check passes
- [ ] Frontend loads correctly
- [ ] Can create bugs
- [ ] Statistics update
- [ ] CORS working

### Optional
- [ ] Custom domain configured
- [ ] Analytics enabled
- [ ] Error monitoring setup

---

## 🚀 Quick Commands

```bash
# Deploy to preview
vercel

# Deploy to production
vercel --prod

# View logs
vercel logs

# List deployments
vercel ls

# Remove deployment
vercel rm deployment-url
```

---

## 📚 Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [Vercel CLI](https://vercel.com/docs/cli)

---

**Ready to deploy?** Follow the steps above and your app will be live in minutes! 🎉

---

*Last Updated: January 29, 2026*
