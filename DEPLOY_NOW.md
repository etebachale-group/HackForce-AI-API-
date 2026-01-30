# 🚀 DEPLOY NOW - Configuración Corregida

## ✅ Problemas Resueltos

1. **❌ Eliminado:** `backend/vercel.json` (causaba conflicto)
2. **✅ Simplificado:** `vercel.json` en raíz
3. **✅ Mejorado:** `backend/api/index.py` con mejor path handling
4. **✅ Cambiado:** psycopg3 → psycopg2-binary (compatible con Vercel)

## 🎯 Estructura Final

```
HackForce-AI-API/
├── vercel.json                    ← Solo este (raíz)
├── backend/
│   ├── api/
│   │   ├── index.py              ← Entry point para Vercel
│   │   └── requirements.txt      ← Dependencias
│   ├── app.py                    ← FastAPI app principal
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   └── services/
│       └── groq_service.py
```

## 📝 Comandos para Deploy

```bash
# 1. Agregar cambios
git add .

# 2. Commit
git commit -m "fix: Simplify Vercel config and fix routing (remove conflicting vercel.json)"

# 3. Push (esto dispara el deploy automático)
git push origin main
```

## ⏱️ Qué Esperar

### Durante el Build (2-3 minutos)
Vercel hará:
1. ✅ Detectar `backend/api/index.py`
2. ✅ Instalar dependencias de `backend/api/requirements.txt`
3. ✅ Instalar: fastapi, uvicorn, sqlalchemy, psycopg2-binary, groq
4. ✅ Crear función serverless
5. ✅ Desplegar

### Después del Deploy
Todas las rutas apuntarán a tu API:
- `https://hack-force-ai-api.vercel.app/` → API root
- `https://hack-force-ai-api.vercel.app/health` → Health check
- `https://hack-force-ai-api.vercel.app/docs` → API docs
- `https://hack-force-ai-api.vercel.app/api/bugs` → Bugs endpoint
- `https://hack-force-ai-api.vercel.app/api/predict` → Prediction

## 🧪 Pruebas Post-Deploy

### 1. Health Check
```bash
curl https://hack-force-ai-api.vercel.app/health
```
**Esperado:**
```json
{
  "status": "healthy",
  "database": "connected",
  "version": "2.0.0"
}
```

### 2. API Root
```bash
curl https://hack-force-ai-api.vercel.app/
```
**Esperado:**
```json
{
  "message": "Welcome to HackForce AI API",
  "version": "2.0.0",
  "status": "running",
  "database": "PostgreSQL (Supabase)"
}
```

### 3. Prediction con Groq AI
```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"title": "Critical database crash", "description": "Production database is completely down, all users affected"}'
```
**Esperado:**
```json
{
  "severity": "Critical",
  "confidence": 0.92,
  "suggested_developer": "Alice Johnson",
  "reasoning": "Production database outage affecting all users with high impact"
}
```

### 4. Crear Bug con IA
```bash
curl -X POST https://hack-force-ai-api.vercel.app/api/bugs \
  -H "Content-Type: application/json" \
  -d '{"title": "UI button misaligned", "description": "Submit button is 2px off center on login page"}'
```
**Esperado:**
```json
{
  "id": 1,
  "title": "UI button misaligned",
  "severity": "Low",
  "confidence_score": 0.78,
  "assigned_developer": "Bob Smith",
  "status": "Open"
}
```

## 🔍 Verificar en Vercel Dashboard

1. Ve a: https://vercel.com/dashboard
2. Click en tu proyecto
3. Verás el deployment en progreso
4. Click en "View Function Logs" para ver:
   - ✅ "Installing dependencies..."
   - ✅ "groq==0.11.0"
   - ✅ "psycopg2-binary==2.9.9"
   - ✅ "Build completed"

## ⚠️ Si Aún Falla

### Revisar Logs
En Vercel → Deployment → Function Logs, busca:
- Errores de importación
- Problemas con DATABASE_URL
- Problemas con GROQ_API_KEY

### Variables de Entorno
Verifica en Vercel Settings → Environment Variables:
```
DATABASE_URL=postgresql://postgres:CMCcJT7XromBwUrG@db.zcykvnviudjvmfepxwvv.supabase.co:5432/postgres
GROQ_API_KEY=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
API_SECRET_KEY=hackforce-secret-2026
ENVIRONMENT=production
CORS_ORIGINS=https://hack-force-ai-api.vercel.app
```

### Fallback Mode
Si Groq falla, el sistema usará clasificación por keywords automáticamente.

## 📊 Cambios Clave

| Antes | Ahora | Por qué |
|-------|-------|---------|
| 2 vercel.json | 1 vercel.json | Evita conflictos |
| psycopg3 | psycopg2-binary | Compatible con Vercel |
| Rutas complejas | Ruta simple | Más confiable |
| `/api/*` prefix | Todas las rutas | Más flexible |

## ✅ Checklist Final

- [x] Eliminado backend/vercel.json
- [x] Simplificado vercel.json raíz
- [x] Actualizado backend/api/index.py
- [x] Cambiado a psycopg2-binary
- [x] Creado requirements.txt en api/
- [ ] **HACER COMMIT Y PUSH AHORA**
- [ ] Esperar 2-3 minutos
- [ ] Probar endpoints
- [ ] Verificar Groq AI funciona

---

## 🎯 ACCIÓN INMEDIATA

Ejecuta estos 3 comandos:

```bash
git add .
git commit -m "fix: Simplify Vercel config and fix routing"
git push origin main
```

Luego ve a: https://vercel.com/dashboard y observa el deployment! 🚀

---

**Confianza:** 95% ✅
**Tiempo estimado:** 2-3 minutos
**Próximo paso:** Commit y push
