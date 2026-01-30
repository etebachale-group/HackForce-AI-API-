# � HackForce AI API - Guía de Uso Completa

## 🌐 URLs de Producción

- **Dashboard:** https://hack-force-ai-api.vercel.app/
- **API Base:** https://hack-force-ai-api.vercel.app/api/
- **Documentación:** https://hack-force-ai-api.vercel.app/docs
- **ReDoc:** https://hack-force-ai-api.vercel.app/redoc

## � Inicio Rápido

### 1. Crear un Bug con IA

**Endpoint:** `POST /api/bugs`

**Request:**
```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Critical: Database connection timeout",
    "description": "Production database is not responding, all users are affected. Connection times out after 30 seconds.",
    "source": "Production Monitor"
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Critical: Database connection timeout",
  "description": "Production database is not responding...",
  "severity": "Critical",
  "predicted_severity": "Critical",
  "confidence_score": 0.92,
  "assigned_developer": "Senior Developer",
  "status": "Open",
  "source": "Production Monitor",
  "created_at": "2026-01-30T19:45:00",
  "updated_at": null
}
```

**Lo que hace la IA:**
- ✅ Analiza el título y descripción
- ✅ Clasifica la severidad (Critical/High/Medium/Low)
- ✅ Calcula confidence score (0.0-1.0)
- ✅ Sugiere desarrollador basado en skills y workload
- ✅ Proporciona reasoning del análisis

### 2. Predecir Severidad (Sin Guardar)

**Endpoint:** `POST /api/predict`

**Request:**
```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "title": "UI button misaligned",
    "description": "The submit button on the login page is 2px off center"
  }'
```

**Response:**
```json
{
  "severity": "Low",
  "confidence": 0.78,
  "suggested_developer": "Junior Developer",
  "reasoning": "Minor UI issue with low user impact, cosmetic fix required"
}
```

### 3. Listar Bugs

**Endpoint:** `GET /api/bugs`

**Con Filtros:**
```bash
# Todos los bugs críticos
curl "https://hack-force-ai-api.vercel.app/api/bugs?severity=Critical"

# Bugs abiertos
curl "https://hack-force-ai-api.vercel.app/api/bugs?status=Open"

# Paginación
curl "https://hack-force-ai-api.vercel.app/api/bugs?skip=0&limit=10"

# Múltiples filtros
curl "https://hack-force-ai-api.vercel.app/api/bugs?severity=High&status=Open&limit=20"
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Bug title",
    "severity": "High",
    "status": "Open",
    "assigned_developer": "Alice",
    "created_at": "2026-01-30T19:45:00"
  }
]
```

### 4. Obtener Bug Específico

**Endpoint:** `GET /api/bugs/{id}`

```bash
curl https://hack-force-ai-api.vercel.app/api/bugs/1
```

### 5. Actualizar Bug

**Endpoint:** `PUT /api/bugs/{id}`

```bash
curl -X PUT https://hack-force-ai-api.vercel.app/api/bugs/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress",
    "assigned_developer": "Alice Johnson"
  }'
```

### 6. Eliminar Bug

**Endpoint:** `DELETE /api/bugs/{id}`

```bash
curl -X DELETE https://hack-force-ai-api.vercel.app/api/bugs/1
```

### 7. Buscar Bugs

**Endpoint:** `GET /api/bugs/search/{term}`

```bash
curl https://hack-force-ai-api.vercel.app/api/bugs/search/database
```

### 8. Estadísticas

**Endpoint:** `GET /api/stats`

```bash
curl https://hack-force-ai-api.vercel.app/api/stats
```

**Response:**
```json
{
  "total_bugs": 25,
  "by_severity": {
    "Critical": 3,
    "High": 8,
    "Medium": 10,
    "Low": 4
  },
  "by_status": {
    "Open": 12,
    "In Progress": 8,
    "Resolved": 5
  },
  "recent_bugs": [...]
}
```

## � Gestión de Desarrolladores

### Crear Desarrollador

**Endpoint:** `POST /api/developers`

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/developers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "skills": ["Python", "FastAPI", "PostgreSQL", "AI"],
    "status": "Active"
  }'
```

### Listar Desarrolladores

**Endpoint:** `GET /api/developers`

```bash
curl https://hack-force-ai-api.vercel.app/api/developers
```

### Ver Workload de Desarrollador

**Endpoint:** `GET /api/developers/{id}/workload`

```bash
curl https://hack-force-ai-api.vercel.app/api/developers/1/workload
```

**Response:**
```json
{
  "developer_id": 1,
  "name": "Alice Johnson",
  "total_bugs": 5,
  "by_severity": {
    "Critical": 1,
    "High": 2,
    "Medium": 2
  },
  "by_status": {
    "Open": 2,
    "In Progress": 3
  }
}
```

## 🤖 Cómo Funciona la IA

### Groq AI (Mixtral-8x7b)

**Modelo:** Mixtral-8x7b-32768
**Provider:** Groq (ultra-fast inference)

**Proceso de Clasificación:**

1. **Análisis del Texto**
   - Lee título y descripción
   - Identifica keywords críticos
   - Analiza contexto y urgencia

2. **Factores Considerados**
   - Impacto en usuarios
   - Estabilidad del sistema
   - Implicaciones de seguridad
   - Integridad de datos
   - Urgencia de resolución

3. **Clasificación**
   - **Critical:** Crashes, vulnerabilidades, pérdida de datos
   - **High:** Funcionalidad rota, muchos usuarios afectados
   - **Medium:** Funcionalidad afectada, workaround existe
   - **Low:** Problemas menores, cosméticos

4. **Asignación de Desarrollador**
   - Analiza skills del desarrollador
   - Considera workload actual
   - Prioriza por severidad
   - Sugiere mejor match

### Sistema de Fallback

Si Groq AI no está disponible:
- ✅ Usa clasificación por keywords
- ✅ Confidence scores más bajos (0.60-0.75)
- ✅ Asignación por workload
- ✅ Sistema sigue funcionando

## 📊 Ejemplos de Uso Real

### Ejemplo 1: Bug Crítico de Seguridad

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "SQL Injection vulnerability in login form",
    "description": "User input is not sanitized in the login endpoint, allowing SQL injection attacks. This could lead to unauthorized access and data breach.",
    "source": "Security Audit"
  }'
```

**IA Detecta:**
- Severity: **Critical**
- Confidence: **0.95**
- Reasoning: "Security vulnerability with potential data breach"
- Developer: "Senior Security Engineer"

### Ejemplo 2: Bug de UI

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Button color inconsistent",
    "description": "The primary button on the settings page uses #FF0000 instead of the brand color #0066CC",
    "source": "Design Review"
  }'
```

**IA Detecta:**
- Severity: **Low**
- Confidence: **0.82**
- Reasoning: "Cosmetic issue, no functional impact"
- Developer: "Frontend Developer"

### Ejemplo 3: Bug de Performance

```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "API endpoint timeout on large datasets",
    "description": "The /api/reports endpoint times out when generating reports with more than 10,000 records. Users cannot access their data.",
    "source": "User Report"
  }'
```

**IA Detecta:**
- Severity: **High**
- Confidence: **0.88**
- Reasoning: "Performance issue affecting user access to data"
- Developer: "Backend Performance Engineer"

## 🔧 Integración con tu Aplicación

### JavaScript/TypeScript

```javascript
// api.js
const API_BASE = 'https://hack-force-ai-api.vercel.app';

async function createBug(bugData) {
  const response = await fetch(`${API_BASE}/api/bugs`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(bugData)
  });
  return response.json();
}

async function predictSeverity(title, description) {
  const response = await fetch(`${API_BASE}/api/predict`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title, description })
  });
  return response.json();
}

// Uso
const bug = await createBug({
  title: "Database error",
  description: "Connection timeout",
  source: "Monitoring"
});

console.log(`Bug created with severity: ${bug.severity}`);
```

### Python

```python
import requests

API_BASE = 'https://hack-force-ai-api.vercel.app'

def create_bug(title, description, source="Manual"):
    response = requests.post(
        f'{API_BASE}/api/bugs',
        json={
            'title': title,
            'description': description,
            'source': source
        }
    )
    return response.json()

def predict_severity(title, description):
    response = requests.post(
        f'{API_BASE}/api/predict',
        json={
            'title': title,
            'description': description
        }
    )
    return response.json()

# Uso
bug = create_bug(
    title="Database error",
    description="Connection timeout",
    source="Monitoring"
)

print(f"Bug created with severity: {bug['severity']}")
print(f"Confidence: {bug['confidence_score']}")
```

## 📈 Monitoreo y Logs

### Ver Prediction Logs

Los logs de predicción se guardan automáticamente en la base de datos:

```sql
SELECT * FROM prediction_logs 
WHERE model_version = 'groq-mixtral-8x7b'
ORDER BY created_at DESC
LIMIT 10;
```

### Métricas de IA

```sql
-- Accuracy promedio
SELECT AVG(confidence) as avg_confidence
FROM prediction_logs
WHERE model_version = 'groq-mixtral-8x7b';

-- Distribución de severidades
SELECT predicted_severity, COUNT(*) as count
FROM prediction_logs
GROUP BY predicted_severity;
```

## 🔐 Seguridad

### Rate Limiting
- Implementado a nivel de Vercel
- 100 requests por minuto por IP

### CORS
- Configurado para tu dominio
- Actualiza `CORS_ORIGINS` en Vercel si cambias de dominio

### API Keys
- No requeridas actualmente
- Puedes agregar autenticación JWT si necesitas

## 🐛 Troubleshooting

### Error: 500 Internal Server Error
- Verifica que DATABASE_URL esté configurada
- Revisa logs en Vercel dashboard

### Error: AI prediction returns fallback mode
- Verifica que GROQ_API_KEY esté configurada
- Revisa quota en Groq console

### Error: CORS
- Actualiza CORS_ORIGINS en Vercel
- Incluye tu dominio frontend

## 📞 Soporte

- **Documentación:** https://hack-force-ai-api.vercel.app/docs
- **GitHub:** https://github.com/etebachale-group/HackForce-AI-API-
- **Groq Docs:** https://console.groq.com/docs

---

**Versión:** 2.0.0  
**Última Actualización:** Enero 30, 2026  
**Status:** ✅ Producción
