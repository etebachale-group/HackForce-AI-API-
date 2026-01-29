# 🗄️ Supabase Database Setup Guide

**HackForce AI API - PostgreSQL Database Configuration**

---

## 📋 What is Supabase?

Supabase is an open-source Firebase alternative that provides:
- PostgreSQL database (serverless)
- Auto-generated APIs
- Real-time subscriptions
- Authentication (optional)
- Storage (optional)

**Why Supabase for this project?**
- ✅ Free tier with generous limits
- ✅ PostgreSQL compatible
- ✅ Works perfectly with Vercel
- ✅ Easy to setup
- ✅ Built-in dashboard

---

## 🚀 Step-by-Step Setup

### Step 1: Create Supabase Account (5 minutes)

1. Go to: https://supabase.com
2. Click "Start your project"
3. Sign up with GitHub (recommended) or email
4. Verify your email if needed

### Step 2: Create New Project (2 minutes)

1. Click "New Project"
2. Fill in the details:
   ```
   Name: hackforce-db
   Database Password: [Create a strong password - SAVE THIS!]
   Region: Choose closest to you (e.g., US East, EU West)
   Pricing Plan: Free
   ```
3. Click "Create new project"
4. Wait 2-3 minutes for project to be ready

### Step 3: Get Database Connection String (2 minutes)

1. In your project dashboard, click "Settings" (gear icon)
2. Click "Database" in the left sidebar
3. Scroll down to "Connection string"
4. Select "URI" tab
5. Copy the connection string - it looks like:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres
   ```
6. Replace `[YOUR-PASSWORD]` with the password you created in Step 2

**Example:**
```
postgresql://postgres:MyStr0ngP@ssw0rd@db.abcdefghijk.supabase.co:5432/postgres
```

### Step 4: Run Database Schema (5 minutes)

You have two options:

#### Option A: Using Supabase SQL Editor (Recommended)

1. In Supabase dashboard, click "SQL Editor" in left sidebar
2. Click "New query"
3. Open the file `database/schema.sql` from your project
4. Copy ALL the content
5. Paste it into the Supabase SQL Editor
6. Click "Run" button
7. You should see: "Success. No rows returned"

#### Option B: Using psql Command Line

```bash
# Make sure you have psql installed
# On Windows: Install PostgreSQL from postgresql.org
# On Mac: brew install postgresql
# On Linux: sudo apt-get install postgresql-client

# Connect to your database
psql "postgresql://postgres:YOUR-PASSWORD@db.xxxxx.supabase.co:5432/postgres"

# Run the schema file
\i database/schema.sql

# Verify tables were created
\dt

# You should see: bugs, developers, predictions_log

# Exit
\q
```

### Step 5: Verify Tables Created (2 minutes)

1. In Supabase dashboard, click "Table Editor"
2. You should see three tables:
   - `bugs`
   - `developers`
   - `predictions_log`
3. Click on each table to see the columns
4. You should also see sample data (4 developers, 5 bugs)

### Step 6: Add Connection String to Local Environment (1 minute)

1. Open `backend/.env` file (create if it doesn't exist)
2. Add your connection string:
   ```bash
   DATABASE_URL=postgresql://postgres:YOUR-PASSWORD@db.xxxxx.supabase.co:5432/postgres
   ```
3. Save the file

**Your `backend/.env` should look like:**
```bash
# Database Configuration
DATABASE_URL=postgresql://postgres:MyStr0ngP@ssw0rd@db.abcdefghijk.supabase.co:5432/postgres

# Groq API
GROQ_API_KEY=gsk_... (your existing key)

# API Configuration
API_SECRET_KEY=hackforce-secret-2026
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
ENVIRONMENT=development
```

### Step 7: Test Local Connection (2 minutes)

```bash
# Navigate to backend directory
cd backend

# Install new dependencies
pip install sqlalchemy psycopg2-binary

# Test database connection
python -c "from database import test_connection; test_connection()"

# You should see: ✅ Database connection successful!
```

### Step 8: Start Backend with Database (1 minute)

```bash
# Make sure you're in backend directory
cd backend

# Start the server
python app.py

# You should see:
# 🚀 Starting HackForce AI API...
# ✅ Database connection successful
# ✅ Database tables ready
# INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 9: Test API with Database (2 minutes)

1. Open browser: http://localhost:8000/docs
2. Try the `/health` endpoint - should show database: "connected"
3. Try `GET /api/bugs` - should return the 5 sample bugs
4. Try `POST /api/bugs` - create a new bug
5. Try `GET /api/bugs` again - should now show 6 bugs

**Success!** Your database is working! 🎉

---

## 🔐 Add to Vercel (For Deployment)

### Step 1: Go to Vercel Dashboard

1. Go to: https://vercel.com/dashboard
2. Select your project: `hackforce-ai-api`
3. Click "Settings"
4. Click "Environment Variables"

### Step 2: Add DATABASE_URL

1. Click "Add New"
2. Fill in:
   ```
   Name: DATABASE_URL
   Value: postgresql://postgres:YOUR-PASSWORD@db.xxxxx.supabase.co:5432/postgres
   Environment: Production, Preview, Development (select all)
   ```
3. Click "Save"

### Step 3: Redeploy

1. Go to "Deployments" tab
2. Click "..." on latest deployment
3. Click "Redeploy"
4. Wait for deployment to complete

---

## 📊 Supabase Dashboard Features

### Table Editor
- View and edit data directly
- Add/delete rows
- Filter and search
- Export data

### SQL Editor
- Run custom SQL queries
- Save queries for later
- View query history

### Database
- View connection details
- Monitor database size
- See connection pooling stats

### Logs
- View database logs
- Monitor queries
- Debug issues

---

## 🎯 Verify Everything Works

### Checklist

- [ ] Supabase project created
- [ ] Database password saved securely
- [ ] Connection string copied
- [ ] Schema.sql executed successfully
- [ ] Tables visible in Supabase dashboard
- [ ] Sample data loaded (4 developers, 5 bugs)
- [ ] DATABASE_URL added to backend/.env
- [ ] Local backend connects successfully
- [ ] API endpoints return data from database
- [ ] DATABASE_URL added to Vercel
- [ ] Vercel deployment successful

---

## 🆘 Troubleshooting

### Issue: "Connection refused"
**Solution:** 
- Check your connection string is correct
- Verify password has no special characters that need escaping
- Make sure you're using the correct host (db.xxxxx.supabase.co)

### Issue: "Password authentication failed"
**Solution:**
- Double-check your password
- Reset password in Supabase Settings > Database
- Update connection string with new password

### Issue: "Tables not found"
**Solution:**
- Run schema.sql again in SQL Editor
- Check for errors in SQL execution
- Verify you're connected to the right database

### Issue: "SSL connection required"
**Solution:**
- Add `?sslmode=require` to end of connection string:
  ```
  postgresql://postgres:pass@host:5432/postgres?sslmode=require
  ```

### Issue: "Too many connections"
**Solution:**
- Supabase free tier has connection limits
- Use connection pooling (already configured in database.py)
- Close unused connections

---

## 💡 Pro Tips

1. **Save Your Password:** Store it in a password manager
2. **Use Environment Variables:** Never commit DATABASE_URL to Git
3. **Monitor Usage:** Check Supabase dashboard for database size
4. **Backup Data:** Export data regularly from Table Editor
5. **Use SQL Editor:** Great for testing queries before adding to code

---

## 📚 Useful Links

- **Supabase Dashboard:** https://supabase.com/dashboard
- **Supabase Docs:** https://supabase.com/docs
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **SQLAlchemy Docs:** https://docs.sqlalchemy.org/

---

## 🎉 Next Steps

After database is setup:

1. ✅ Database working locally
2. 🔄 Integrate Groq AI for classification
3. 🔄 Refactor frontend components
4. 🔄 Add charts and visualizations
5. 🔄 Deploy to Vercel with database

---

**Status:** Database Setup Complete ✅  
**Time Taken:** ~20 minutes  
**Next:** Groq AI Integration

---

*Created: January 29, 2026*  
*For: HackForce AI API - Fernando's Tasks*
