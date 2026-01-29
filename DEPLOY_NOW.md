# 🚀 Deploy to Vercel - Quick Guide

## ✅ Pre-Deployment Checklist

- [x] Code committed to Git
- [x] Pushed to GitHub: https://github.com/etebachale-group/HackForce-AI-API-
- [x] Vercel CLI installed (v48.2.0)
- [x] Deployment files created
- [x] Backend and Frontend ready

---

## 🎯 Deployment Options

### Option 1: Deploy via Vercel Dashboard (Recommended for First Time)

This is the easiest way and gives you full control:

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/new
   - Sign in with GitHub

2. **Import Your Repository**
   - Click "Import Git Repository"
   - Select: `etebachale-group/HackForce-AI-API-`
   - Click "Import"

3. **Configure the Project**
   
   **Project Name:** `ai-bug-classification` (or your choice)
   
   **Framework Preset:** Other
   
   **Root Directory:** Leave as `.` (root)
   
   **Build & Development Settings:**
   - Build Command: `cd frontend && npm run build`
   - Output Directory: `frontend/dist`
   - Install Command: `cd frontend && npm install`

4. **Environment Variables**
   
   Click "Environment Variables" and add:
   ```
   Name: VITE_API_URL
   Value: /api
   
   Name: API_SECRET_KEY
   Value: your-secret-key-here-change-this
   
   Name: CORS_ORIGINS
   Value: https://your-app.vercel.app
   ```

5. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live! 🎉

---

### Option 2: Deploy via CLI (Quick)

Run these commands in your terminal:

```bash
# Make sure you're in the project root
cd c:\xampp\htdocs\HackForce-AI-API-

# Login to Vercel (if not already logged in)
vercel login

# Deploy to preview
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? ai-bug-classification
# - Directory? ./
# - Override settings? No

# Once preview is successful, deploy to production
vercel --prod
```

---

## 🎯 Two-Project Setup (Better Performance)

For optimal performance, deploy backend and frontend separately:

### Deploy Backend First

```bash
# Navigate to backend
cd backend

# Deploy backend
vercel

# Set environment variables in Vercel dashboard:
# - API_SECRET_KEY
# - CORS_ORIGINS (will be your frontend URL)

# Deploy to production
vercel --prod
```

**Note the backend URL:** `https://your-backend.vercel.app`

### Deploy Frontend Second

```bash
# Navigate to frontend
cd ../frontend

# Deploy frontend
vercel

# Set environment variables in Vercel dashboard:
# - VITE_API_URL (your backend URL from above)

# Deploy to production
vercel --prod
```

---

## 📝 After Deployment

### 1. Get Your URLs

After deployment, you'll get URLs like:
- **Frontend:** `https://ai-bug-classification.vercel.app`
- **Backend:** `https://ai-bug-classification-backend.vercel.app`

### 2. Update CORS

Go to Vercel dashboard → Backend project → Settings → Environment Variables

Update `CORS_ORIGINS` to include your frontend URL:
```
https://ai-bug-classification.vercel.app
```

Redeploy backend for changes to take effect.

### 3. Test Your Deployment

Visit your frontend URL and:
- ✅ Create a test bug
- ✅ Verify it appears in the list
- ✅ Check statistics update
- ✅ Test filters

---

## 🐛 Troubleshooting

### Issue: Build Failed

**Check:**
- Build logs in Vercel dashboard
- Make sure all dependencies are in `package.json`
- Verify build command is correct

**Solution:**
```bash
# Test build locally first
cd frontend
npm run build
```

### Issue: API Not Working

**Check:**
- CORS_ORIGINS includes your frontend URL
- API_SECRET_KEY is set
- Backend is deployed and running

**Solution:**
- Check function logs in Vercel dashboard
- Test backend directly: `https://your-backend.vercel.app/health`

### Issue: "Module not found"

**Solution:**
- Make sure `requirements_simple.txt` exists in backend
- Verify all imports are correct
- Check Python version compatibility

---

## 🎉 Success Indicators

You'll know it's working when:
- ✅ Frontend loads without errors
- ✅ You can create bugs
- ✅ Bugs appear in the list
- ✅ Statistics update
- ✅ No CORS errors in console

---

## 📊 Vercel Dashboard Features

After deployment, explore:
- **Deployments:** See all your deployments
- **Analytics:** View traffic and performance
- **Logs:** Debug issues
- **Domains:** Add custom domain
- **Environment Variables:** Manage secrets

---

## 🚀 Continuous Deployment

Now that it's set up:
- Every push to `main` → Auto-deploys to production
- Pull requests → Get preview deployments
- Instant rollbacks if needed

---

## 📞 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Support:** https://vercel.com/support
- **Project Docs:** See DEPLOYMENT_GUIDE.md

---

## ⚡ Quick Deploy Command

If you just want to deploy NOW:

```bash
vercel --prod
```

That's it! Follow the prompts and you're live in 3 minutes! 🚀

---

**Your GitHub Repo:** https://github.com/etebachale-group/HackForce-AI-API-

**Ready?** Choose Option 1 (Dashboard) or Option 2 (CLI) above and deploy! 🎉

---

*Last Updated: January 29, 2026*
