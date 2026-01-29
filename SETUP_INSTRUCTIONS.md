# 🚀 Setup Instructions - AI Bug Classification API

## Quick Start Guide

This guide will help you set up the development environment for the AI Bug Classification API project.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **PostgreSQL 14+** - [Download](https://www.postgresql.org/download/)
- **Git** - [Download](https://git-scm.com/downloads/)

### Verify Installations

```bash
python --version  # Should be 3.9 or higher
node --version    # Should be 18 or higher
npm --version     # Should be 9 or higher
psql --version    # Should be 14 or higher
git --version     # Any recent version
```

---

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Bug-Classification-API.git
cd AI-Bug-Classification-API
```

---

## 2. Backend Setup

### Step 1: Create Virtual Environment

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env file with your configuration
# Use your favorite text editor (notepad, vim, nano, vscode, etc.)
```

**Required Environment Variables:**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/bugdb
API_SECRET_KEY=your-secret-key-here
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Step 4: Setup PostgreSQL Database

#### Option A: Local PostgreSQL

```bash
# Create database
createdb bugdb

# Run schema
psql bugdb < ../database/schema.sql

# Verify tables were created
psql bugdb -c "\dt"
```

#### Option B: Cloud PostgreSQL (Neon)

1. Go to [Neon](https://neon.tech/)
2. Create a free account
3. Create a new project
4. Copy the connection string
5. Update `DATABASE_URL` in `.env`
6. Run schema using provided connection string:
   ```bash
   psql "your-connection-string" < ../database/schema.sql
   ```

### Step 5: Run Backend Server

```bash
# Make sure you're in the backend directory with venv activated
python app.py
```

The backend should now be running at:
- API: http://localhost:8000
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Verify Backend is Working

Open your browser and go to http://localhost:8000/docs

You should see the Swagger UI with all API endpoints.

---

## 3. Frontend Setup

### Step 1: Install Dependencies

```bash
# Open a new terminal
cd frontend

# Install dependencies
npm install
```

### Step 2: Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env file
```

**Required Environment Variables:**
```env
VITE_API_URL=http://localhost:8000
```

### Step 3: Run Frontend Development Server

```bash
npm run dev
```

The frontend should now be running at:
- Frontend: http://localhost:3000 or http://localhost:5173

### Verify Frontend is Working

Open your browser and go to http://localhost:3000 (or the port shown in terminal)

You should see the AI Bug Classification Dashboard.

---

## 4. AI Model Setup (For Mirza)

### Step 1: Create Virtual Environment

```bash
cd ai_model

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install ML Dependencies

```bash
pip install pandas numpy scikit-learn jupyter matplotlib seaborn joblib
```

### Step 3: Start Jupyter Notebook

```bash
jupyter notebook
```

This will open Jupyter in your browser where you can create notebooks for data exploration and model training.

---

## 5. Testing the Complete Setup

### Test 1: Backend Health Check

```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-01-29T..."
}
```

### Test 2: Create a Bug via API

```bash
curl -X POST http://localhost:8000/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test bug",
    "description": "This is a test bug to verify the API is working"
  }'
```

### Test 3: Frontend Integration

1. Open http://localhost:3000 in your browser
2. Fill out the "Report New Bug" form
3. Click "Submit Bug Report"
4. Verify the bug appears in the list below

---

## 6. Common Issues and Solutions

### Issue: "Module not found" error in Python

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal prompt

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Port already in use"

**Solution:**
```bash
# Find process using the port (example for port 8000)
# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -i :8000
kill -9 <PID>

# Or use a different port
python app.py --port 8001
```

### Issue: "Cannot connect to database"

**Solution:**
1. Verify PostgreSQL is running:
   ```bash
   # On Windows:
   pg_ctl status
   
   # On macOS/Linux:
   sudo service postgresql status
   ```

2. Check DATABASE_URL in `.env` is correct

3. Verify database exists:
   ```bash
   psql -l | grep bugdb
   ```

### Issue: "CORS error" in browser console

**Solution:**
1. Verify backend is running
2. Check CORS_ORIGINS in backend `.env` includes your frontend URL
3. Restart backend server after changing `.env`

### Issue: npm install fails

**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

---

## 7. Development Workflow

### Daily Workflow

1. **Start Backend:**
   ```bash
   cd backend
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   python app.py
   ```

2. **Start Frontend (in new terminal):**
   ```bash
   cd frontend
   npm run dev
   ```

3. **Start Coding!**

### Before Committing

```bash
# Backend
cd backend
pytest  # Run tests (when available)

# Frontend
cd frontend
npm run lint  # Check for linting errors
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "feat: description of your changes"

# Push to remote
git push origin feature/your-feature-name

# Create Pull Request on GitHub
```

---

## 8. Useful Commands

### Backend

```bash
# Run server
python app.py

# Run with auto-reload
uvicorn app:app --reload

# Run tests
pytest

# Check code style
black .
flake8 .
```

### Frontend

```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

### Database

```bash
# Connect to database
psql bugdb

# List tables
\dt

# Describe table
\d bugs

# Run query
SELECT * FROM bugs;

# Exit
\q
```

---

## 9. IDE Setup Recommendations

### VS Code Extensions

- Python
- Pylance
- ESLint
- Prettier
- PostgreSQL
- GitLens
- Thunder Client (for API testing)

### VS Code Settings

Create `.vscode/settings.json`:
```json
{
  "python.defaultInterpreterPath": "./backend/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

---

## 10. Next Steps

After completing the setup:

1. ✅ Verify all services are running
2. ✅ Test creating and viewing bugs
3. ✅ Read the PROGRESS_LOG.md for current status
4. ✅ Check your assigned tasks in TEAM_WORKFLOW.md
5. ✅ Join the team communication channel
6. ✅ Start coding!

---

## 11. Getting Help

### Documentation
- Check the `/docs` folder for detailed documentation
- Read API documentation at http://localhost:8000/docs
- Review code comments

### Team Communication
- Daily standup at 9:00 AM
- Slack/Discord channel: #ai-bug-classification
- GitHub Issues for bug reports
- Pull Requests for code review

### External Resources
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [React Documentation](https://react.dev/learn)
- [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

---

## 12. Troubleshooting Checklist

Before asking for help, verify:

- [ ] Virtual environment is activated (you see `(venv)` in terminal)
- [ ] All dependencies are installed (`pip list` or `npm list`)
- [ ] Environment variables are set correctly (check `.env` files)
- [ ] PostgreSQL is running and accessible
- [ ] Ports 8000 and 3000 are not in use by other applications
- [ ] You're in the correct directory
- [ ] You've pulled the latest changes from Git

---

**Setup Complete! 🎉**

You're now ready to start developing. Good luck!

---

*Last Updated: January 29, 2026*
