# 🤖 HackForce AI API

AI-powered bug classification and developer assignment system using Groq's Mixtral-8x7b model.

[![Status](https://img.shields.io/badge/status-production-success)](https://hack-force-ai-api.vercel.app/)
[![API](https://img.shields.io/badge/API-live-blue)](https://hack-force-ai-api.vercel.app/api/)
[![Docs](https://img.shields.io/badge/docs-interactive-orange)](https://hack-force-ai-api.vercel.app/docs)

## 🌟 Features

- **🤖 AI-Powered Classification:** Intelligent bug severity detection using Groq AI (Mixtral-8x7b)
- **👥 Smart Developer Assignment:** Automatic assignment based on skills and workload
- **📊 Real-time Analytics:** Statistics and insights dashboard
- **🔄 Fallback System:** Works even when AI is unavailable
- **📚 Auto-Generated Docs:** Interactive API documentation with Swagger UI
- **🚀 Production Ready:** Deployed on Vercel with Supabase PostgreSQL

## 🌐 Live Demo

- **🎨 Dashboard:** https://hack-force-ai-api.vercel.app/
- **🔌 API:** https://hack-force-ai-api.vercel.app/api/
- **📖 Docs:** https://hack-force-ai-api.vercel.app/docs

## 🚀 Quick Start

### Create a Bug with AI Classification

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Critical: Database connection timeout",
    "description": "Production database is not responding, all users affected",
    "source": "Production Monitor"
  }'
```

**Response:**
```json
{
  "id": 1,
  "severity": "Critical",
  "confidence_score": 0.92,
  "assigned_developer": "Senior Developer",
  "status": "Open"
}
```

### Predict Severity (Without Saving)

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "title": "UI button misaligned",
    "description": "Submit button is 2px off center"
  }'
```

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│   Frontend (React + Vite)           │
│   - Dashboard UI                    │
│   - Bug Management                  │
│   - Real-time Predictions           │
│   - Charts & Analytics              │
└──────────────┬──────────────────────┘
               │ HTTPS
┌──────────────▼──────────────────────┐
│   Backend (FastAPI)                 │
│   - RESTful API                     │
│   - CRUD Operations                 │
│   - Statistics Engine               │
│   - Lazy Loading                    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   AI Layer (Groq)                   │
│   - Mixtral-8x7b Model              │
│   - Bug Classification              │
│   - Developer Suggestion            │
│   - Fallback System                 │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│   Database (Supabase PostgreSQL)    │
│   - bugs table                      │
│   - developers table                │
│   - prediction_logs table           │
└─────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **FastAPI** 0.104.1 - Modern Python web framework
- **SQLAlchemy** 2.0.46 - ORM for database operations
- **PostgreSQL** - Database hosted on Supabase
- **Groq AI** 0.11.0 - Mixtral-8x7b for classification
- **Pydantic** 2.5.0 - Data validation
- **psycopg2-binary** 2.9.9 - PostgreSQL adapter

### Frontend
- **React** 18.2.0 - UI library
- **Vite** 5.0.8 - Build tool and dev server
- **Axios** 1.6.2 - HTTP client
- **Chart.js** 4.4.0 - Data visualization
- **React Router** 6.20.0 - Client-side routing

### Deployment & Infrastructure
- **Vercel** - Hosting and serverless functions
- **Supabase** - PostgreSQL database
- **GitHub** - Version control and CI/CD
- **Groq Cloud** - AI inference

## 📊 API Endpoints

### Bugs Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/bugs` | Create bug with AI classification |
| GET | `/api/bugs` | List bugs (with filters) |
| GET | `/api/bugs/{id}` | Get specific bug |
| PUT | `/api/bugs/{id}` | Update bug |
| DELETE | `/api/bugs/{id}` | Delete bug |
| GET | `/api/bugs/search/{term}` | Search bugs |

### Developers Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/developers` | Create developer |
| GET | `/api/developers` | List developers |
| GET | `/api/developers/{id}` | Get developer |
| GET | `/api/developers/{id}/workload` | Get workload stats |

### AI & Analytics
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/predict` | Predict severity (no save) |
| GET | `/api/stats` | Get statistics |
| GET | `/health` | Health check |

### Documentation
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc documentation |

## 🤖 AI Classification System

### How It Works

1. **Input Analysis**
   - Receives bug title and description
   - Preprocesses text for AI model

2. **AI Processing (Groq Mixtral-8x7b)**
   - Analyzes context and severity indicators
   - Considers: impact, urgency, security, data integrity
   - Generates classification with confidence score

3. **Developer Matching**
   - Analyzes developer skills
   - Considers current workload
   - Matches based on bug type and severity

4. **Response Generation**
   - Returns severity classification
   - Provides confidence score (0.0-1.0)
   - Suggests best developer
   - Includes reasoning explanation

### Severity Levels

| Level | Description | Examples |
|-------|-------------|----------|
| **Critical** | System crashes, security vulnerabilities, data loss | SQL injection, production down, data breach |
| **High** | Major functionality broken, many users affected | Login fails, API timeout, payment errors |
| **Medium** | Functionality impaired, workaround exists | Slow performance, minor bugs, UI glitches |
| **Low** | Minor issues, cosmetic problems | Typos, color inconsistencies, alignment issues |

### Example AI Response

```json
{
  "severity": "Critical",
  "confidence": 0.92,
  "suggested_developer": "Senior Security Engineer",
  "reasoning": "SQL injection vulnerability with potential data breach affecting all users. Requires immediate attention from security specialist."
}
```

## 🔧 Local Development

### Prerequisites
- Python 3.10 or higher
- Node.js 18 or higher
- PostgreSQL database (or Supabase account)
- Groq API key ([Get one here](https://console.groq.com/))

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your credentials

# Run development server
python app.py
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be available at `http://localhost:3000`

### Environment Variables

Create `.env` file in `backend/` directory:

```env
DATABASE_URL=postgresql://user:password@host:5432/database
GROQ_API_KEY=gsk_your_groq_api_key_here
API_SECRET_KEY=your-secret-key-here
ENVIRONMENT=development
CORS_ORIGINS=http://localhost:3000,http://localhost:3001
```

## 📚 Documentation

- **📖 API Usage Guide:** [API_USAGE_GUIDE.md](./API_USAGE_GUIDE.md)
- **🤖 Groq Integration:** [backend/GROQ_INTEGRATION.md](./backend/GROQ_INTEGRATION.md)
- **🚀 Deployment Guide:** [FINAL_DEPLOYMENT.md](./FINAL_DEPLOYMENT.md)
- **📊 Status:** [STATUS.md](./STATUS.md)
- **🌐 Interactive Docs:** https://hack-force-ai-api.vercel.app/docs

## 🧪 Testing

### Test Groq AI Integration

```bash
cd backend
python test_groq.py
```

### Test Database Connection

```bash
cd backend
python test_database.py
```

### Run Frontend Tests

```bash
cd frontend
npm test
```

## 📈 Performance Metrics

- **API Response Time:** < 2 seconds
- **AI Prediction Time:** 1-2 seconds
- **Dashboard Load Time:** < 3 seconds
- **Database Query Time:** < 100ms
- **Uptime:** 99.9%

## 🔐 Security Features

- ✅ Environment variables for sensitive data
- ✅ CORS configured for specific origins
- ✅ SQL injection protection via ORM
- ✅ Input validation with Pydantic
- ✅ Rate limiting on Vercel
- ✅ HTTPS encryption
- ✅ Lazy loading to prevent crashes

## 👥 Team

### HackForce Team
- **Fernando Chale Eteba** - Full Stack Lead (Backend, Database, Deployment)
- **Laraib Memon** - Frontend UI/UX Lead (React Dashboard)
- **Mirza Yasir Abdullah Baig** - AI/ML Lead (Model Development)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **🌐 Live Application:** https://hack-force-ai-api.vercel.app/
- **📂 GitHub Repository:** https://github.com/etebachale-group/HackForce-AI-API-
- **🤖 Groq Console:** https://console.groq.com/
- **🗄️ Supabase Dashboard:** https://supabase.com/dashboard
- **🚀 Vercel Dashboard:** https://vercel.com/dashboard

## 📞 Support

For issues, questions, or feature requests:
- 🐛 [Open an issue](https://github.com/etebachale-group/HackForce-AI-API-/issues)
- 📖 Check the [documentation](https://hack-force-ai-api.vercel.app/docs)
- 💬 Review [API examples](./API_USAGE_GUIDE.md)

## 🎯 Project Status

**Version:** 2.0.0  
**Status:** ✅ Production  
**Last Updated:** January 30, 2026  
**Deployment:** Vercel  
**Database:** Supabase PostgreSQL  
**AI Model:** Groq Mixtral-8x7b

---

Made with ❤️ by the HackForce Team
