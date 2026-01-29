# 🛠️ Comandos Útiles y Referencias - AI Bug Classification API

## 📦 Instalación y Setup

### Backend (Python/FastAPI)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencia específica
pip install fastapi==0.104.1

# Generar requirements.txt
pip freeze > requirements.txt

# Ejecutar servidor de desarrollo
uvicorn app:app --reload

# Ejecutar en puerto específico
uvicorn app:app --reload --port 8001

# Ejecutar con logs detallados
uvicorn app:app --reload --log-level debug
```

### Frontend (React/Vite)

```bash
# Crear proyecto React con Vite
npm create vite@latest frontend -- --template react

# Instalar dependencias
npm install

# Instalar dependencias específicas
npm install axios react-router-dom chart.js react-chartjs-2

# Ejecutar servidor de desarrollo
npm run dev

# Ejecutar en puerto específico
npm run dev -- --port 3001

# Build para producción
npm run build

# Preview del build
npm run preview

# Limpiar node_modules y reinstalar
rm -rf node_modules package-lock.json
npm install
```

### Base de Datos (PostgreSQL)

```bash
# Instalar PostgreSQL (Ubuntu/Debian)
sudo apt-get install postgresql postgresql-contrib

# Instalar PostgreSQL (Mac con Homebrew)
brew install postgresql

# Iniciar servicio PostgreSQL
# Linux
sudo service postgresql start
# Mac
brew services start postgresql

# Conectar a PostgreSQL
psql -U postgres

# Crear base de datos
createdb bugdb

# Ejecutar script SQL
psql -U postgres -d bugdb -f database/schema.sql

# Backup de base de datos
pg_dump bugdb > backup.sql

# Restaurar backup
psql bugdb < backup.sql

# Ver tablas
\dt

# Describir tabla
\d bugs

# Salir de psql
\q
```

---

## 🔧 Comandos de Desarrollo

### Git Workflow

```bash
# Clonar repositorio
git clone https://github.com/usuario/AI-Bug-Classification-API.git

# Ver estado
git status

# Crear nueva rama
git checkout -b feature/nombre-feature

# Ver ramas
git branch

# Cambiar de rama
git checkout main

# Agregar cambios
git add .
git add archivo.py

# Commit
git commit -m "feat: agregar endpoint de predicción"

# Push
git push origin feature/nombre-feature

# Pull últimos cambios
git pull origin main

# Merge rama
git checkout main
git merge feature/nombre-feature

# Ver historial
git log --oneline

# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer cambios en archivo
git checkout -- archivo.py

# Ver diferencias
git diff

# Stash cambios temporalmente
git stash
git stash pop
```

### Testing

```bash
# Backend - Pytest
pytest
pytest -v  # verbose
pytest tests/test_api.py  # archivo específico
pytest -k "test_create"  # tests que contengan "create"
pytest --cov  # con coverage

# Frontend - Vitest/Jest
npm test
npm test -- --coverage
npm test -- --watch

# E2E - Cypress
npx cypress open
npx cypress run
```

### Linting y Formatting

```bash
# Python - Black
black .
black --check .

# Python - Flake8
flake8 .

# Python - isort (ordenar imports)
isort .

# JavaScript - ESLint
npm run lint
npm run lint -- --fix

# JavaScript - Prettier
npx prettier --write .
```

---

## 🚀 Deployment

### Vercel

```bash
# Instalar Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy a producción
vercel --prod

# Ver logs
vercel logs

# Ver deployments
vercel ls

# Configurar variables de entorno
vercel env add DATABASE_URL
vercel env add GROQ_API_KEY

# Pull variables de entorno
vercel env pull
```

### Docker (Opcional)

```bash
# Build imagen
docker build -t ai-bug-api .

# Ejecutar contenedor
docker run -p 8000:8000 ai-bug-api

# Ver contenedores corriendo
docker ps

# Ver logs
docker logs container_id

# Detener contenedor
docker stop container_id

# Docker Compose
docker-compose up
docker-compose down
docker-compose logs -f
```

---

## 🤖 AI/ML Comandos

### Jupyter Notebook

```bash
# Instalar Jupyter
pip install jupyter

# Iniciar Jupyter
jupyter notebook

# Iniciar JupyterLab
jupyter lab

# Convertir notebook a script
jupyter nbconvert --to script notebook.ipynb
```

### Entrenamiento de Modelos

```bash
# Entrenar modelo
python ai_model/train_model.py

# Evaluar modelo
python ai_model/evaluate.py

# Hacer predicción
python ai_model/predict.py --text "Bug description"

# Ver métricas
python ai_model/metrics.py
```

### Scikit-learn

```python
# Guardar modelo
import joblib
joblib.dump(model, 'model.pkl')

# Cargar modelo
model = joblib.load('model.pkl')

# Ver feature importance
print(model.feature_importances_)
```

---

## 🔍 Debugging

### Backend Debugging

```python
# Agregar breakpoint
import pdb; pdb.set_trace()

# Logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")

# Print con formato
from pprint import pprint
pprint(data)

# Timing
import time
start = time.time()
# ... código ...
print(f"Tiempo: {time.time() - start}s")
```

### Frontend Debugging

```javascript
// Console logs
console.log('Variable:', variable);
console.table(array);
console.error('Error:', error);
console.warn('Warning:', warning);

// Debugger
debugger;

// React DevTools
// Instalar extensión en Chrome/Firefox

// Network debugging
// Abrir DevTools → Network tab
```

### Database Debugging

```sql
-- Ver queries lentas
SELECT * FROM pg_stat_activity WHERE state = 'active';

-- Explain query
EXPLAIN ANALYZE SELECT * FROM bugs WHERE severity = 'High';

-- Ver tamaño de tablas
SELECT 
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Ver índices
SELECT * FROM pg_indexes WHERE tablename = 'bugs';
```

---

## 📊 Monitoreo y Performance

### Backend Performance

```python
# Profiling
import cProfile
cProfile.run('function_to_profile()')

# Memory profiling
from memory_profiler import profile
@profile
def my_function():
    pass

# Timing decorator
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start}s")
        return result
    return wrapper
```

### Frontend Performance

```javascript
// React Profiler
import { Profiler } from 'react';

function onRenderCallback(
  id, phase, actualDuration, baseDuration, startTime, commitTime
) {
  console.log(`${id} took ${actualDuration}ms`);
}

<Profiler id="App" onRender={onRenderCallback}>
  <App />
</Profiler>

// Performance API
const start = performance.now();
// ... código ...
const end = performance.now();
console.log(`Tiempo: ${end - start}ms`);

// Lighthouse
// Chrome DevTools → Lighthouse tab
```

---

## 🔐 Seguridad

### Variables de Entorno

```bash
# Nunca commitear .env
echo ".env" >> .gitignore

# Usar .env.example como template
cp .env.example .env

# Validar variables requeridas
python -c "import os; assert os.getenv('DATABASE_URL'), 'DATABASE_URL not set'"
```

### API Keys

```python
# Backend - Validar API key
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != os.getenv("API_SECRET_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key
```

---

## 📚 Referencias Rápidas

### FastAPI Endpoints

```python
# GET
@app.get("/items")
async def read_items():
    return {"items": []}

# POST
@app.post("/items")
async def create_item(item: Item):
    return item

# PUT
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted": item_id}

# Query parameters
@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return items[skip:skip+limit]

# Path parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Request body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return item
```

### React Hooks

```javascript
// useState
const [count, setCount] = useState(0);

// useEffect
useEffect(() => {
  // código
  return () => {
    // cleanup
  };
}, [dependencies]);

// useContext
const value = useContext(MyContext);

// useRef
const inputRef = useRef(null);

// useMemo
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);

// useCallback
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);

// Custom hook
function useAPI(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      });
  }, [url]);
  
  return { data, loading };
}
```

### SQL Queries Comunes

```sql
-- Crear tabla
CREATE TABLE bugs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    severity VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar
INSERT INTO bugs (title, description, severity)
VALUES ('Bug title', 'Description', 'High');

-- Seleccionar
SELECT * FROM bugs WHERE severity = 'High';

-- Actualizar
UPDATE bugs SET status = 'Closed' WHERE id = 1;

-- Eliminar
DELETE FROM bugs WHERE id = 1;

-- Join
SELECT b.*, d.name as developer_name
FROM bugs b
LEFT JOIN developers d ON b.assigned_developer = d.id;

-- Agregación
SELECT severity, COUNT(*) as count
FROM bugs
GROUP BY severity;

-- Ordenar
SELECT * FROM bugs ORDER BY created_at DESC LIMIT 10;

-- Búsqueda de texto
SELECT * FROM bugs WHERE description ILIKE '%error%';
```

---

## 🐛 Troubleshooting Común

### Error: "Module not found"
```bash
# Backend
pip install -r requirements.txt
pip install nombre-modulo

# Frontend
npm install
npm install nombre-paquete
```

### Error: "Port already in use"
```bash
# Ver qué está usando el puerto
# Linux/Mac
lsof -i :8000
# Windows
netstat -ano | findstr :8000

# Matar proceso
# Linux/Mac
kill -9 PID
# Windows
taskkill /PID PID /F

# O usar otro puerto
uvicorn app:app --port 8001
npm run dev -- --port 3001
```

### Error: "CORS policy"
```python
# Backend - Agregar CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Error: "Database connection failed"
```bash
# Verificar que PostgreSQL esté corriendo
sudo service postgresql status

# Verificar credenciales en .env
echo $DATABASE_URL

# Probar conexión
psql $DATABASE_URL

# Verificar que la base de datos existe
psql -U postgres -l
```

### Error: "Model file not found"
```python
# Verificar ruta del modelo
import os
print(os.path.exists('models/model.pkl'))

# Usar ruta absoluta
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'models', 'model.pkl')
```

### Error: "Out of memory"
```python
# Reducir batch size
# Liberar memoria
import gc
gc.collect()

# Usar generadores en lugar de listas
def data_generator():
    for item in large_dataset:
        yield process(item)
```

---

## 📖 Recursos Externos

### Documentación Oficial
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Scikit-learn](https://scikit-learn.org/)
- [Vercel](https://vercel.com/docs)

### Tutoriales
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [React Tutorial](https://react.dev/learn)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Git Tutorial](https://www.atlassian.com/git/tutorials)

### Comunidades
- [Stack Overflow](https://stackoverflow.com/)
- [Reddit r/FastAPI](https://www.reddit.com/r/FastAPI/)
- [Reddit r/reactjs](https://www.reddit.com/r/reactjs/)
- [Discord - FastAPI](https://discord.gg/fastapi)

### Herramientas
- [Postman](https://www.postman.com/) - Testing de APIs
- [DBeaver](https://dbeaver.io/) - Cliente de base de datos
- [VS Code](https://code.visualstudio.com/) - Editor de código
- [GitHub Desktop](https://desktop.github.com/) - Git GUI

---

## 🎯 Comandos de Emergencia

### Resetear todo y empezar de nuevo

```bash
# Backend
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
rm -rf node_modules package-lock.json
npm install

# Database
dropdb bugdb
createdb bugdb
psql bugdb < database/schema.sql

# Git
git reset --hard HEAD
git clean -fd
```

### Backup rápido antes de cambios grandes

```bash
# Crear branch de backup
git checkout -b backup-$(date +%Y%m%d)
git add .
git commit -m "Backup before major changes"
git checkout main

# Backup de base de datos
pg_dump bugdb > backup_$(date +%Y%m%d).sql

# Backup de archivos
tar -czf backup_$(date +%Y%m%d).tar.gz backend/ frontend/ ai_model/
```

---

¡Guarda este documento como referencia rápida! 📚
