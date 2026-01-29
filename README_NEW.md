# 🐛 AI Bug Classification API

> Automated bug classification and developer assignment system powered by AI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat&logo=react)](https://react.dev/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=flat&logo=postgresql)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python)](https://www.python.org/)

---

## 📋 Overview

The AI Bug Classification API is a web-accessible system that:
- 🤖 **Automatically classifies** bug reports by severity using AI
- 👥 **Suggests developer assignment** based on skills and workload
- 🔄 **Integrates** with Notion and Jira for seamless workflow
- 📊 **Provides analytics** through an interactive dashboard
- 🌐 **Collects bugs** from multiple online sources using Groq

---

## ✨ Features

### Core Features
- ✅ **AI-Powered Classification** - Automatically predicts bug severity (Low, Medium, High, Critical)
- ✅ **Smart Assignment** - Suggests the best developer for each bug
- ✅ **REST API** - Complete CRUD operations with filtering and pagination
- ✅ **Interactive Dashboard** - Real-time bug visualization and management
- ✅ **Multi-Source Collection** - Gather bugs from GitHub, forums, and communities

### Advanced Features
- 🔄 **Notion Integration** - Sync bugs with Notion databases
- 🔄 **Jira Integration** - Sync bugs with Jira projects
- 📊 **Analytics** - Statistics and insights on bug trends
- 🎯 **Confidence Scores** - AI prediction confidence for each classification
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Data Sources                         │
│  GitHub Issues | Forums | Developer Communities        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   Groq API                              │
│              Bug Collection Layer                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              FastAPI Backend + AI Model                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐         │
│  │   API    │→ │ AI Model │→ │  PostgreSQL  │         │
│  │ Endpoints│  │Prediction│  │   Database   │         │
│  └──────────┘  └──────────┘  └──────────────┘         │
└────────┬────────────────────────────────┬──────────────┘
         │                                │
         ▼                                ▼
┌──────────────────┐            ┌──────────────────┐
│ React Dashboard  │            │  Integrations    │
│  • Bug List      │            │  • Notion        │
│  • Filters       │            │  • Jira          │
│  • Charts        │            └──────────────────┘
│  • Stats         │
└──────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL 14+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Bug-Classification-API.git
   cd AI-Bug-Classification-API
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Setup Database**
   ```bash
   createdb bugdb
   psql bugdb < ../database/schema.sql
   ```

4. **Run Backend**
   ```bash
   python app.py
   ```
   Backend will be available at http://localhost:8000

5. **Setup Frontend** (in a new terminal)
   ```bash
   cd frontend
   npm install
   cp .env.example .env
   npm run dev
   ```
   Frontend will be available at http://localhost:3000

### First Steps

1. Open http://localhost:3000 in your browser
2. Create your first bug report
3. Watch the AI classify it automatically!
4. Explore the API docs at http://localhost:8000/docs

---

## 📚 Documentation

- **[Setup Instructions](SETUP_INSTRUCTIONS.md)** - Detailed setup guide
- **[Progress Log](PROGRESS_LOG.md)** - Current project status and tasks
- **[Team Workflow](TEAM_WORKFLOW.md)** - Team organization and responsibilities
- **[Implementation Plan](PLAN_DE_IMPLEMENTACION.md)** - Complete implementation roadmap
- **[Quick Start Guide](QUICK_START_GUIDE.md)** - Get started in 30 minutes

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **PostgreSQL** - Powerful, open-source relational database
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **Vite** - Next generation frontend tooling
- **Chart.js** - Simple yet flexible JavaScript charting
- **Axios** - Promise-based HTTP client

### AI/ML
- **Scikit-learn** - Machine learning library
- **TF-IDF** - Text feature extraction
- **Logistic Regression** - Classification algorithm
- **Optional: BERT/RoBERTa** - Advanced NLP models

### Integrations
- **Groq API** - Bug collection from online sources
- **Notion API** - Workspace integration
- **Jira REST API** - Project management integration

### Deployment
- **Vercel** - Serverless deployment platform
- **Neon/Supabase** - Serverless PostgreSQL
- **GitHub Actions** - CI/CD automation

---

## 📡 API Endpoints

### Bugs
- `POST /api/bugs` - Create a new bug
- `GET /api/bugs` - List all bugs (with filters)
- `GET /api/bugs/{id}` - Get specific bug
- `PUT /api/bugs/{id}` - Update bug
- `DELETE /api/bugs/{id}` - Delete bug

### AI Prediction
- `POST /api/predict` - Predict bug severity

### Statistics
- `GET /api/stats` - Get bug statistics

### Health
- `GET /health` - Health check endpoint

**Full API Documentation:** http://localhost:8000/docs

---

## 🎯 Project Status

**Current Phase:** Phase 1 - Setup & Fundamentals  
**Overall Progress:** 15%

### Completed ✅
- Project structure and setup
- Backend API with 9 endpoints
- Frontend dashboard with bug management
- Database schema design
- Development environment configuration

### In Progress 🔄
- Database integration with SQLAlchemy
- Component refactoring
- Dataset creation for AI model

### Upcoming 📋
- AI model training
- Groq integration
- Notion/Jira integrations
- Advanced visualizations
- Deployment to Vercel

See [PROGRESS_LOG.md](PROGRESS_LOG.md) for detailed status.

---

## 👥 Team

| Name | Role | Responsibilities |
|------|------|------------------|
| **Fernando Chale Eteba** | Full-Stack Lead | Backend API, Database, Integrations, Deployment |
| **Laraib Memon** | Frontend & UI/UX Lead | React Dashboard, Visualizations, Responsive Design |
| **Mirza Yasir Abdullah Baig** | AI/ML Lead | NLP Model, Classification, Developer Assignment |

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Standards
- Follow existing code style
- Add comments for complex logic
- Write tests for new features
- Update documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- React team for the powerful UI library
- Scikit-learn for ML capabilities
- Groq for data collection API
- Notion and Jira for integration support

---

## 📞 Contact

- **Project Repository:** [GitHub](https://github.com/your-username/AI-Bug-Classification-API)
- **Documentation:** [Docs](./docs)
- **Issues:** [GitHub Issues](https://github.com/your-username/AI-Bug-Classification-API/issues)

---

## 🗺️ Roadmap

### Phase 1: MVP (Weeks 1-2) ✅
- [x] Project setup
- [x] Basic API
- [x] Frontend dashboard
- [ ] Database integration
- [ ] Basic AI model

### Phase 2: Core Features (Weeks 3-4)
- [ ] Advanced AI model
- [ ] Groq integration
- [ ] Notion/Jira sync
- [ ] Charts and analytics

### Phase 3: Polish & Deploy (Weeks 5-6)
- [ ] Testing
- [ ] Performance optimization
- [ ] Deployment to Vercel
- [ ] Documentation
- [ ] Demo preparation

---

## 📊 Statistics

- **Lines of Code:** ~2,500+
- **API Endpoints:** 9
- **Database Tables:** 3
- **React Components:** 5+ (growing)
- **Test Coverage:** TBD

---

## 🎉 Demo

Coming soon! We're preparing a live demo for the hackathon.

---

**Built with ❤️ by the AI Bug Classification Team**

*Last Updated: January 29, 2026*
