# 🚀 Start Phase 2 - Quick Guide

**Date:** January 29, 2026  
**Phase:** Database Integration & AI Development  
**Duration:** 1-2 weeks

---

## 📋 What You Need to Know

### Phase 1 Status: ✅ COMPLETE
- Backend API with 9 endpoints running
- Frontend dashboard functional
- Vercel deployment configured
- Groq API key ready
- All code committed to GitHub

### Phase 2 Goals: 🎯
1. Replace in-memory storage with PostgreSQL
2. Integrate Groq AI for bug classification
3. Refactor frontend into reusable components
4. Add charts and visualizations

---

## 🏃 Quick Start for Each Team Member

### 👨‍💻 Backend Developer - Start Here

#### Step 1: Setup PostgreSQL (30 minutes)
```bash
# 1. Go to https://neon.tech
# 2. Sign up (free tier is enough)
# 3. Create new project: "hackforce-db"
# 4. Copy the connection string
# 5. It looks like: postgresql://user:pass@host/db
```

#### Step 2: Run Database Schema (5 minutes)
```bash
# Connect to your database
psql "your-connection-string-here"

# Run the schema
\i database/schema.sql

# Verify tables
\dt

# You should see: bugs, developers, predictions_log
```

#### Step 3: Create Database Files (2 hours)
```bash
cd backend

# Create these files (templates in NEXT_STEPS.md):
# 1. database.py - Connection setup
# 2. models.py - SQLAlchemy models
# 3. crud.py - Database operations

# Test connection
python -c "from database import engine; print('Connected!' if engine else 'Failed')"
```

#### Step 4: Update API (2 hours)
```bash
# Modify app.py to use database instead of in-memory storage
# See NEXT_STEPS.md for complete code examples

# Test locally
python app.py

# Visit http://localhost:8000/docs
# Test all endpoints
```

#### Step 5: Deploy (15 minutes)
```bash
# Add DATABASE_URL to Vercel
# Go to: https://vercel.com/your-project/settings/environment-variables
# Add: DATABASE_URL = your-connection-string

# Commit and push
git add .
git commit -m "feat: Add PostgreSQL database integration"
git push origin main

# Vercel will auto-deploy
```

**Total Time:** ~5 hours  
**Documentation:** NEXT_STEPS.md (Backend section)

---

### 🤖 AI/ML Developer - Start Here

#### Step 1: Install Groq Package (5 minutes)
```bash
cd backend

# Install groq
pip install groq

# Test it works
python -c "from groq import Groq; print('Groq installed!')"
```

#### Step 2: Create Groq Service (3 hours)
```bash
# Create backend/services/ directory
mkdir backend/services

# Create groq_service.py
# Copy template from NEXT_STEPS.md

# Key features to implement:
# 1. classify_bug_severity() - Main classification
# 2. _fallback_classification() - Backup when API fails
# 3. suggest_developer() - Developer assignment
```

#### Step 3: Test Groq Integration (1 hour)
```python
# Create test file: backend/test_groq.py
from services.groq_service import GroqService

groq = GroqService()

# Test classification
result = groq.classify_bug_severity(
    title="Login button not working",
    description="Users cannot login, getting 500 error"
)

print(result)
# Should output: {"severity": "High", "confidence": 0.85, ...}
```

#### Step 4: Integrate with API (2 hours)
```bash
# Update backend/app.py
# Import GroqService
# Update POST /api/bugs endpoint
# Update POST /api/predict endpoint

# See NEXT_STEPS.md for complete code
```

#### Step 5: Deploy (15 minutes)
```bash
# Update requirements.txt
pip freeze > requirements.txt

# Commit and push
git add .
git commit -m "feat: Add Groq AI classification"
git push origin main
```

**Total Time:** ~6 hours  
**Documentation:** NEXT_STEPS.md (AI section)

---

### 🎨 Frontend Developer - Start Here

#### Step 1: Install Chart.js (5 minutes)
```bash
cd frontend

# Install dependencies
npm install chart.js react-chartjs-2

# Verify installation
npm list chart.js
```

#### Step 2: Create Component Files (3 hours)
```bash
# Create these components (templates in NEXT_STEPS.md):
# 1. src/components/BugCard.jsx
# 2. src/components/StatsCard.jsx
# 3. src/components/FilterPanel.jsx
# 4. src/components/BugForm.jsx

# Each component should be:
# - Reusable
# - Well-styled
# - Properly typed (PropTypes)
```

#### Step 3: Create Chart Components (2 hours)
```bash
# Create charts directory
mkdir src/components/Charts

# Create chart components:
# 1. Charts/SeverityChart.jsx - Pie chart
# 2. Charts/TrendChart.jsx - Line chart

# See NEXT_STEPS.md for complete code examples
```

#### Step 4: Refactor App.jsx (1 hour)
```jsx
// Import new components
import BugCard from './components/BugCard';
import StatsCard from './components/StatsCard';
import SeverityChart from './components/Charts/SeverityChart';

// Replace inline code with components
// Clean up and organize
```

#### Step 5: Test & Deploy (30 minutes)
```bash
# Test locally
npm run dev

# Check on mobile (responsive)
# Test all features

# Commit and push
git add .
git commit -m "feat: Refactor frontend with reusable components"
git push origin main
```

**Total Time:** ~6 hours  
**Documentation:** NEXT_STEPS.md (Frontend section)

---

## 📚 Key Documentation Files

### Must Read Before Starting
1. **NEXT_STEPS.md** ⭐ - Complete implementation guide with code templates
2. **TEAM_TASKS.md** ⭐ - Your specific tasks and timeline
3. **PROGRESS_LOG.md** - Current project status

### Reference When Needed
4. **SETUP_INSTRUCTIONS.md** - Environment setup
5. **QUICK_COMMANDS.md** - Common commands
6. **GROQ_API_SETUP.md** - Groq API details

---

## 🎯 Success Criteria

### Week 1 Goals (By February 5)
- [ ] PostgreSQL database connected and working
- [ ] All bugs persist across server restarts
- [ ] Groq AI classification working
- [ ] Frontend components created
- [ ] Charts displaying data

### How to Know You're Done
1. **Backend:** Create a bug, restart server, bug still exists
2. **AI:** Create bug with "critical security issue" → classified as Critical
3. **Frontend:** Dashboard shows pie chart of bug severity distribution

---

## 🔧 Environment Variables Needed

### Add to Vercel Dashboard
```bash
# Already added:
GROQ_API_KEY=gsk_... (your Groq API key from backend/.env)
CORS_ORIGINS=https://your-vercel-url.vercel.app
API_SECRET_KEY=hackforce-secret-2026

# Need to add:
DATABASE_URL=postgresql://user:pass@host/db
```

### Add to Local .env Files
```bash
# backend/.env
DATABASE_URL=postgresql://user:pass@host/db
GROQ_API_KEY=gsk_... (copy from existing backend/.env)

# frontend/.env
VITE_API_URL=http://localhost:8000
```

---

## 🚨 Common Issues & Solutions

### Issue: Can't connect to PostgreSQL
**Solution:** 
- Check connection string format
- Verify database exists
- Check firewall/network settings
- Try from psql command line first

### Issue: Groq API not responding
**Solution:**
- Verify API key is correct
- Check internet connection
- Fallback classification should work
- Check Groq console for rate limits

### Issue: Charts not displaying
**Solution:**
- Verify chart.js installed correctly
- Check browser console for errors
- Ensure data format is correct
- Try simple example first

### Issue: Vercel deployment fails
**Solution:**
- Check build logs
- Verify all dependencies in requirements.txt
- Test build locally first
- Check environment variables

---

## 💡 Pro Tips

### Backend
- Test database connection before writing code
- Use SQLAlchemy's `create_all()` to verify models
- Add print statements to debug
- Test each endpoint individually

### AI/ML
- Start with simple prompts, optimize later
- Always have fallback logic
- Log all API calls for debugging
- Test with various bug descriptions

### Frontend
- Build one component at a time
- Test each component in isolation
- Use React DevTools for debugging
- Keep components small and focused

---

## 📞 Getting Help

### If You're Stuck
1. Check the documentation (NEXT_STEPS.md has code templates)
2. Search the error message online
3. Ask in team chat
4. Create GitHub issue with details
5. Schedule pair programming session

### Useful Resources
- **Neon Docs:** https://neon.tech/docs
- **Groq Docs:** https://console.groq.com/docs
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Chart.js Docs:** https://www.chartjs.org/docs/

---

## ✅ Daily Checklist

### Every Morning
- [ ] Pull latest changes: `git pull origin main`
- [ ] Check PROGRESS_LOG.md for updates
- [ ] Review your tasks in TEAM_TASKS.md
- [ ] Start local development environment

### Every Evening
- [ ] Commit your changes with descriptive message
- [ ] Push to GitHub
- [ ] Update PROGRESS_LOG.md with your progress
- [ ] Note any blockers for tomorrow

---

## 🎉 Let's Do This!

Phase 1 is complete. You have:
- ✅ Working backend API
- ✅ Functional frontend
- ✅ Clear documentation
- ✅ Code templates ready
- ✅ Timeline established

Now it's time to add the advanced features that will make HackForce AI API truly impressive!

**Choose your role above and start coding! 🚀**

---

## 📊 Progress Tracking

Update this section as you complete tasks:

### Backend Progress
- [ ] PostgreSQL setup
- [ ] Database files created
- [ ] API updated
- [ ] Tests passing
- [ ] Deployed

### AI Progress
- [ ] Groq service created
- [ ] Classification working
- [ ] Developer assignment
- [ ] Tests passing
- [ ] Deployed

### Frontend Progress
- [ ] Components created
- [ ] Charts added
- [ ] App.jsx refactored
- [ ] Mobile tested
- [ ] Deployed

---

**Current Status:** Ready to Start Phase 2  
**Target Completion:** February 5, 2026  
**Let's build something amazing! 🚀**

---

*Created: January 29, 2026*  
*Phase: 2 - Database & AI Integration*  
*Team: Fernando, Laraib, Mirza*
