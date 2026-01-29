# ⚡ Quick Commands Reference

Quick reference for common commands used in the AI Bug Classification API project.

---

## 🚀 Starting the Application

### Backend
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py
```

### Frontend
```bash
cd frontend
npm run dev
```

### Both (in separate terminals)
```bash
# Terminal 1
cd backend && source venv/bin/activate && python app.py

# Terminal 2
cd frontend && npm run dev
```

---

## 📦 Installation

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend
```bash
cd frontend
npm install
```

---

## 🗄️ Database

### Create Database
```bash
createdb bugdb
```

### Run Schema
```bash
psql bugdb < database/schema.sql
```

### Connect to Database
```bash
psql bugdb
```

### Common SQL Commands
```sql
-- List tables
\dt

-- Describe table
\d bugs

-- View all bugs
SELECT * FROM bugs;

-- Count bugs by severity
SELECT severity, COUNT(*) FROM bugs GROUP BY severity;

-- Exit
\q
```

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
pytest -v  # verbose
pytest --cov  # with coverage
```

### Frontend Tests
```bash
cd frontend
npm test
```

---

## 🔍 Code Quality

### Python
```bash
# Format code
black .

# Lint code
flake8 .

# Sort imports
isort .
```

### JavaScript
```bash
# Lint
npm run lint

# Format
npx prettier --write .
```

---

## 🌿 Git Commands

### Daily Workflow
```bash
# Pull latest changes
git pull origin main

# Create feature branch
git checkout -b feature/your-feature

# Check status
git status

# Add changes
git add .

# Commit
git commit -m "feat: your message"

# Push
git push origin feature/your-feature
```

### Useful Git Commands
```bash
# View branches
git branch

# Switch branch
git checkout main

# Delete branch
git branch -d feature/old-feature

# View log
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard changes
git checkout -- filename
```

---

## 🐛 Debugging

### Check if Port is in Use
```bash
# Windows
netstat -ano | findstr :8000

# macOS/Linux
lsof -i :8000
```

### Kill Process on Port
```bash
# Windows
taskkill /PID <PID> /F

# macOS/Linux
kill -9 <PID>
```

### View Logs
```bash
# Backend logs (if running in background)
tail -f backend/logs/app.log

# Frontend logs
# Check browser console (F12)
```

---

## 📊 API Testing

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Get all bugs
curl http://localhost:8000/api/bugs

# Get stats
curl http://localhost:8000/api/stats

# Create bug
curl -X POST http://localhost:8000/api/bugs \
  -H "Content-Type: application/json" \
  -d '{"title":"Test bug","description":"This is a test"}'

# Predict severity
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"title":"Critical error","description":"System crash"}'
```

### Using httpie (if installed)
```bash
# Get bugs
http GET localhost:8000/api/bugs

# Create bug
http POST localhost:8000/api/bugs title="Test" description="Test bug"
```

---

## 🔧 Environment Management

### Python Virtual Environment
```bash
# Create
python -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Deactivate
deactivate

# List installed packages
pip list

# Freeze requirements
pip freeze > requirements.txt
```

### Node Modules
```bash
# Install
npm install

# Clean install
rm -rf node_modules package-lock.json
npm install

# Update packages
npm update

# Check outdated
npm outdated
```

---

## 📝 File Operations

### Create Files
```bash
# Create directory
mkdir new_folder

# Create file
touch new_file.py

# Create multiple files
touch file1.py file2.py file3.py
```

### View Files
```bash
# View file content
cat filename

# View with pagination
less filename

# View first 10 lines
head filename

# View last 10 lines
tail filename

# View with line numbers
cat -n filename
```

### Search
```bash
# Find files
find . -name "*.py"

# Search in files
grep -r "search_term" .

# Search with line numbers
grep -rn "search_term" .
```

---

## 🚀 Deployment

### Vercel
```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

### Docker (if using)
```bash
# Build image
docker build -t ai-bug-api .

# Run container
docker run -p 8000:8000 ai-bug-api

# View running containers
docker ps

# Stop container
docker stop <container_id>
```

---

## 💾 Backup

### Database Backup
```bash
# Backup
pg_dump bugdb > backup_$(date +%Y%m%d).sql

# Restore
psql bugdb < backup_20260129.sql
```

### Code Backup
```bash
# Create archive
tar -czf backup_$(date +%Y%m%d).tar.gz backend/ frontend/ ai_model/

# Extract archive
tar -xzf backup_20260129.tar.gz
```

---

## 🔄 Update Dependencies

### Python
```bash
# Update pip
pip install --upgrade pip

# Update specific package
pip install --upgrade fastapi

# Update all packages
pip list --outdated
pip install --upgrade package_name
```

### Node
```bash
# Update npm
npm install -g npm@latest

# Update specific package
npm update axios

# Update all packages
npm update
```

---

## 📊 Performance Monitoring

### Check System Resources
```bash
# CPU and Memory
top  # Linux/macOS
htop  # If installed

# Disk usage
df -h

# Directory size
du -sh *
```

### Python Profiling
```python
# In your code
import cProfile
cProfile.run('your_function()')
```

---

## 🎯 Shortcuts

### VS Code
- `Ctrl+P` - Quick file open
- `Ctrl+Shift+P` - Command palette
- `Ctrl+`` - Toggle terminal
- `Ctrl+B` - Toggle sidebar
- `Ctrl+/` - Toggle comment

### Terminal
- `Ctrl+C` - Stop process
- `Ctrl+Z` - Suspend process
- `Ctrl+L` - Clear screen
- `Ctrl+R` - Search history
- `Tab` - Auto-complete

---

## 🆘 Emergency Commands

### Reset Everything
```bash
# Backend
cd backend
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
rm -rf node_modules package-lock.json
npm install

# Database
dropdb bugdb
createdb bugdb
psql bugdb < database/schema.sql
```

### Git Reset
```bash
# Discard all local changes
git reset --hard HEAD
git clean -fd

# Reset to specific commit
git reset --hard <commit_hash>
```

---

## 📚 Help Commands

```bash
# Python help
python --help
pip --help

# Node help
node --help
npm --help

# Git help
git --help
git <command> --help

# PostgreSQL help
psql --help
```

---

**Keep this file handy for quick reference!** 📌

*Last Updated: January 29, 2026*
