# HackForce AI - Backend API

FastAPI backend with PostgreSQL database and Groq AI integration for intelligent bug classification.

## 🚀 Quick Start

### Local Development

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. **Run Server**
   ```bash
   python app.py
   # Or with uvicorn:
   uvicorn app:app --reload --port 8000
   ```

4. **Access API**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 📁 Project Structure

```
backend/
├── api/
│   └── index.py          # Vercel serverless entry point
├── services/
│   ├── __init__.py
│   └── groq_service.py   # Groq AI integration
├── app.py                # Main FastAPI application
├── database.py           # Database connection
├── models.py             # SQLAlchemy models
├── crud.py               # Database operations
├── requirements.txt      # Python dependencies
├── test_database.py      # Database test script
├── test_groq.py          # Groq AI test script
└── vercel.json           # Vercel configuration
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```bash
# Database
DATABASE_URL=postgresql://user:password@host:5432/database

# Groq AI
GROQ_API_KEY=gsk_your_api_key_here

# API Security
API_SECRET_KEY=your-secret-key
ENVIRONMENT=development

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
```

## 🤖 Groq AI Integration

The API uses Groq's Mixtral-8x7b model for:
- Bug severity classification
- Developer assignment suggestions

See [GROQ_INTEGRATION.md](./GROQ_INTEGRATION.md) for details.

## 📊 Database

### Models
- **Bug**: Bug reports with severity and assignment
- **Developer**: Developer profiles with skills and workload
- **PredictionLog**: AI prediction history

### Schema
See [../database/schema.sql](../database/schema.sql)

## 🔌 API Endpoints

### System
- `GET /` - API information
- `GET /health` - Health check
- `GET /api/stats` - Statistics

### Bugs
- `POST /api/bugs` - Create bug (with AI)
- `GET /api/bugs` - List bugs
- `GET /api/bugs/{id}` - Get bug
- `PUT /api/bugs/{id}` - Update bug
- `DELETE /api/bugs/{id}` - Delete bug
- `GET /api/bugs/search/{term}` - Search bugs

### Developers
- `POST /api/developers` - Create developer
- `GET /api/developers` - List developers
- `GET /api/developers/{id}` - Get developer
- `GET /api/developers/{id}/workload` - Get workload

### AI Prediction
- `POST /api/predict` - Predict severity (no save)

## 🧪 Testing

### Test Database Connection
```bash
python test_database.py
```

### Test Groq AI
```bash
python test_groq.py
```

### Run All Tests
```bash
pytest
```

## 🚀 Deployment

### Vercel

1. **Configure Environment Variables** in Vercel dashboard
2. **Push to GitHub** - auto-deploys
3. **Verify** at your Vercel URL

### Manual Deploy
```bash
vercel --prod
```

## 📝 Development Notes

### Python Version
- Requires Python 3.10+
- Tested with Python 3.14

### Database
- PostgreSQL 14+
- Hosted on Supabase

### AI Model
- Groq Mixtral-8x7b-32768
- Fallback to rule-based if unavailable

## 🐛 Troubleshooting

### Database Connection Issues
```bash
# Test connection
python test_database.py

# Check DATABASE_URL format
postgresql://user:password@host:5432/database
```

### Groq API Issues
```bash
# Test Groq integration
python test_groq.py

# Check API key
echo $GROQ_API_KEY
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📚 Documentation

- [Groq Integration](./GROQ_INTEGRATION.md)
- [API Documentation](http://localhost:8000/docs)
- [Database Schema](../database/schema.sql)

## 🔗 Links

- **GitHub**: https://github.com/etebachale-group/HackForce-AI-API-
- **Groq Docs**: https://console.groq.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
