# 🚀 Guía de Inicio Rápido - AI Bug Classification API

## ⚡ Setup en 30 Minutos

### Paso 1: Clonar y Configurar Estructura (5 min)

```bash
# Crear estructura de proyecto
mkdir AI-Bug-Classification-API
cd AI-Bug-Classification-API

# Crear carpetas principales
mkdir -p backend/routes backend/models backend/integrations
mkdir -p frontend/src/components frontend/src/pages frontend/src/services
mkdir -p ai_model/models ai_model/data
mkdir -p groq_integration
mkdir -p database
mkdir -p docs

# Inicializar Git
git init
echo "node_modules/\n__pycache__/\n.env\n*.pkl\nvenv/" > .gitignore
```

### Paso 2: Backend Setup (10 min)

```bash
cd backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Crear requirements.txt
cat > requirements.txt << EOF
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0
python-dotenv==1.0.0
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
joblib==1.3.2
groq==0.4.0
notion-client==2.2.1
jira==3.5.2
pytest==7.4.3
python-multipart==0.0.6
EOF

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
cat > .env << EOF
DATABASE_URL=postgresql://user:password@localhost:5432/bugdb
GROQ_API_KEY=your_groq_key_here
NOTION_API_KEY=your_notion_key_here
NOTION_DATABASE_ID=your_database_id
JIRA_SERVER=https://your-domain.atlassian.net
JIRA_EMAIL=your@email.com
JIRA_API_TOKEN=your_jira_token
JIRA_PROJECT_KEY=PROJECT
API_SECRET_KEY=your_secret_key_here
CORS_ORIGINS=http://localhost:3000
EOF
```

### Paso 3: Crear Backend Básico (10 min)

```python
# backend/app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Bug Classification API",
    description="API for bug classification and developer assignment",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class BugCreate(BaseModel):
    title: str
    description: str
    source: str = "Manual"

class BugResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    predicted_severity: Optional[str]
    confidence_score: Optional[float]
    assigned_developer: Optional[str]
    status: str
    source: str

class PredictionRequest(BaseModel):
    title: str
    description: str

class PredictionResponse(BaseModel):
    severity: str
    confidence: float
    suggested_developer: Optional[str]

# In-memory storage (temporal, reemplazar con DB)
bugs_db = []
bug_id_counter = 1

# Endpoints
@app.get("/")
async def root():
    return {"message": "AI Bug Classification API", "status": "running"}

@app.post("/api/bugs", response_model=BugResponse)
async def create_bug(bug: BugCreate):
    global bug_id_counter
    
    # TODO: Integrar predicción del modelo AI
    predicted_severity = "Medium"  # Placeholder
    confidence = 0.75  # Placeholder
    
    new_bug = {
        "id": bug_id_counter,
        "title": bug.title,
        "description": bug.description,
        "severity": predicted_severity,
        "predicted_severity": predicted_severity,
        "confidence_score": confidence,
        "assigned_developer": None,
        "status": "Open",
        "source": bug.source
    }
    
    bugs_db.append(new_bug)
    bug_id_counter += 1
    
    return new_bug

@app.get("/api/bugs", response_model=List[BugResponse])
async def list_bugs(
    severity: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 100
):
    filtered_bugs = bugs_db
    
    if severity:
        filtered_bugs = [b for b in filtered_bugs if b["severity"] == severity]
    if status:
        filtered_bugs = [b for b in filtered_bugs if b["status"] == status]
    
    return filtered_bugs[:limit]

@app.get("/api/bugs/{bug_id}", response_model=BugResponse)
async def get_bug(bug_id: int):
    bug = next((b for b in bugs_db if b["id"] == bug_id), None)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return bug

@app.post("/api/predict", response_model=PredictionResponse)
async def predict_severity(request: PredictionRequest):
    # TODO: Integrar modelo AI real
    # Por ahora, lógica simple basada en keywords
    text = f"{request.title} {request.description}".lower()
    
    if any(word in text for word in ["critical", "crash", "security", "data loss"]):
        severity = "Critical"
        confidence = 0.9
    elif any(word in text for word in ["error", "bug", "broken", "not working"]):
        severity = "High"
        confidence = 0.8
    elif any(word in text for word in ["issue", "problem", "slow"]):
        severity = "Medium"
        confidence = 0.7
    else:
        severity = "Low"
        confidence = 0.6
    
    return {
        "severity": severity,
        "confidence": confidence,
        "suggested_developer": "John Doe"  # Placeholder
    }

@app.get("/api/stats")
async def get_stats():
    total = len(bugs_db)
    by_severity = {
        "Low": len([b for b in bugs_db if b["severity"] == "Low"]),
        "Medium": len([b for b in bugs_db if b["severity"] == "Medium"]),
        "High": len([b for b in bugs_db if b["severity"] == "High"]),
        "Critical": len([b for b in bugs_db if b["severity"] == "Critical"]),
    }
    
    return {
        "total_bugs": total,
        "by_severity": by_severity,
        "open_bugs": len([b for b in bugs_db if b["status"] == "Open"]),
        "closed_bugs": len([b for b in bugs_db if b["status"] == "Closed"])
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Paso 4: Frontend Setup (5 min)

```bash
cd ../frontend

# Crear proyecto React con Vite
npm create vite@latest . -- --template react
npm install

# Instalar dependencias adicionales
npm install axios react-router-dom chart.js react-chartjs-2

# Crear archivo .env
cat > .env << EOF
VITE_API_URL=http://localhost:8000
EOF
```

### Paso 5: Crear Frontend Básico

```jsx
// frontend/src/services/api.js
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = {
  getBugs: (params) => axios.get(`${API_URL}/api/bugs`, { params }),
  getBug: (id) => axios.get(`${API_URL}/api/bugs/${id}`),
  createBug: (data) => axios.post(`${API_URL}/api/bugs`, data),
  predictSeverity: (data) => axios.post(`${API_URL}/api/predict`, data),
  getStats: () => axios.get(`${API_URL}/api/stats`),
};

// frontend/src/App.jsx
import { useState, useEffect } from 'react';
import { api } from './services/api';
import './App.css';

function App() {
  const [bugs, setBugs] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [bugsRes, statsRes] = await Promise.all([
        api.getBugs(),
        api.getStats()
      ]);
      setBugs(bugsRes.data);
      setStats(statsRes.data);
    } catch (error) {
      console.error('Error loading data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateBug = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    
    try {
      await api.createBug({
        title: formData.get('title'),
        description: formData.get('description'),
        source: 'Manual'
      });
      loadData();
      e.target.reset();
    } catch (error) {
      console.error('Error creating bug:', error);
    }
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div className="App">
      <header>
        <h1>🐛 AI Bug Classification Dashboard</h1>
      </header>

      <div className="stats">
        <div className="stat-card">
          <h3>Total Bugs</h3>
          <p>{stats?.total_bugs || 0}</p>
        </div>
        <div className="stat-card critical">
          <h3>Critical</h3>
          <p>{stats?.by_severity?.Critical || 0}</p>
        </div>
        <div className="stat-card high">
          <h3>High</h3>
          <p>{stats?.by_severity?.High || 0}</p>
        </div>
        <div className="stat-card medium">
          <h3>Medium</h3>
          <p>{stats?.by_severity?.Medium || 0}</p>
        </div>
        <div className="stat-card low">
          <h3>Low</h3>
          <p>{stats?.by_severity?.Low || 0}</p>
        </div>
      </div>

      <div className="content">
        <div className="create-bug">
          <h2>Report New Bug</h2>
          <form onSubmit={handleCreateBug}>
            <input
              type="text"
              name="title"
              placeholder="Bug title"
              required
            />
            <textarea
              name="description"
              placeholder="Bug description"
              rows="4"
              required
            />
            <button type="submit">Submit Bug</button>
          </form>
        </div>

        <div className="bug-list">
          <h2>Recent Bugs</h2>
          {bugs.length === 0 ? (
            <p>No bugs reported yet</p>
          ) : (
            bugs.map(bug => (
              <div key={bug.id} className={`bug-card ${bug.severity.toLowerCase()}`}>
                <div className="bug-header">
                  <h3>{bug.title}</h3>
                  <span className="severity-badge">{bug.severity}</span>
                </div>
                <p>{bug.description}</p>
                <div className="bug-meta">
                  <span>ID: {bug.id}</span>
                  <span>Status: {bug.status}</span>
                  <span>Source: {bug.source}</span>
                  {bug.confidence_score && (
                    <span>Confidence: {(bug.confidence_score * 100).toFixed(0)}%</span>
                  )}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
```

```css
/* frontend/src/App.css */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  background: #f5f5f5;
}

.App {
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 30px;
  border-radius: 10px;
  margin-bottom: 30px;
  text-align: center;
}

.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.stat-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  text-align: center;
}

.stat-card h3 {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.stat-card p {
  font-size: 32px;
  font-weight: bold;
  color: #333;
}

.stat-card.critical p { color: #7c3aed; }
.stat-card.high p { color: #ef4444; }
.stat-card.medium p { color: #f59e0b; }
.stat-card.low p { color: #10b981; }

.content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 30px;
}

.create-bug, .bug-list {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.create-bug h2, .bug-list h2 {
  margin-bottom: 20px;
  color: #333;
}

.create-bug form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.create-bug input,
.create-bug textarea {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 14px;
}

.create-bug button {
  padding: 12px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
}

.create-bug button:hover {
  background: #5568d3;
}

.bug-card {
  border-left: 4px solid #ddd;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 6px;
  background: #fafafa;
}

.bug-card.critical { border-left-color: #7c3aed; }
.bug-card.high { border-left-color: #ef4444; }
.bug-card.medium { border-left-color: #f59e0b; }
.bug-card.low { border-left-color: #10b981; }

.bug-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.bug-header h3 {
  font-size: 16px;
  color: #333;
}

.severity-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: bold;
  color: white;
}

.bug-card.critical .severity-badge { background: #7c3aed; }
.bug-card.high .severity-badge { background: #ef4444; }
.bug-card.medium .severity-badge { background: #f59e0b; }
.bug-card.low .severity-badge { background: #10b981; }

.bug-card p {
  color: #666;
  margin-bottom: 10px;
  font-size: 14px;
}

.bug-meta {
  display: flex;
  gap: 15px;
  font-size: 12px;
  color: #999;
}

@media (max-width: 768px) {
  .content {
    grid-template-columns: 1fr;
  }
  
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

### Paso 6: Ejecutar el Proyecto

```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Abre tu navegador en:
- Backend API: http://localhost:8000
- Frontend: http://localhost:5173
- API Docs: http://localhost:8000/docs

---

## 🎯 Próximos Pasos

### Inmediatos (Hoy)
1. ✅ Verificar que backend y frontend funcionan
2. ✅ Crear algunos bugs de prueba
3. ✅ Familiarizarse con la estructura

### Corto Plazo (Esta Semana)
1. Configurar PostgreSQL
2. Implementar modelo AI básico
3. Integrar Groq para recolección de datos
4. Mejorar UI con gráficos

### Mediano Plazo (Próximas 2 Semanas)
1. Entrenar modelo AI con datos reales
2. Implementar integraciones Notion/Jira
3. Agregar autenticación
4. Deploy a Vercel

---

## 🐛 Troubleshooting

### Error: "Module not found"
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

### Error: "Port already in use"
```bash
# Cambiar puerto en backend
uvicorn app:app --port 8001

# Cambiar puerto en frontend
npm run dev -- --port 3001
```

### Error: "CORS policy"
Verifica que `CORS_ORIGINS` en `.env` incluya la URL del frontend.

---

## 📚 Recursos Útiles

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [React Docs](https://react.dev/learn)
- [Vite Guide](https://vitejs.dev/guide/)
- [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html)

---

¡Listo para empezar! 🚀
