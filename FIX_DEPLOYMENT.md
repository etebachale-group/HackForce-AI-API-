# 🔧 Fix Deployment - Vercel Compatibility

## Cambios Realizados

### 1. Actualizado `backend/api/index.py`
- ✅ Mejor manejo de errores
- ✅ Mensajes de debug más claros
- ✅ Fallback si falla la carga de la app

### 2. Cambiado `psycopg` → `psycopg2-binary`
- ✅ `backend/requirements.txt` actualizado
- ✅ `backend/api/requirements.txt` creado
- ✅ `backend/database.py` actualizado
- **Razón:** `psycopg2-binary` es más compatible con Vercel

### 3. Actualizado `vercel.json`
- ✅ Agregado `maxLambdaSize: 50mb`
- ✅ Configurado `PYTHONPATH`
- **Razón:** Groq y otras dependencias necesitan más espacio

## 🚀 Próximos Pasos

### 1. Commit y Push
```bash
git add .
git commit -m "fix: Update dependencies for Vercel compatibility (psycopg2-binary)"
git push origin main
```

### 2. Esperar Deployment (2-3 minutos)
Ve a: https://vercel.com/dashboard

### 3. Verificar Build Logs
Busca estos mensajes:
- ✅ `Installing dependencies from requirements.txt`
- ✅ `groq==0.11.0` instalado
- ✅ `psycopg2-binary==2.9.9` instalado
- ✅ `Build completed`

### 4. Probar API
```bash
# Health check
curl https://hack-force-ai-api.vercel.app/api/

# Prediction con IA
curl -X POST https://hack-force-ai-api.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"title": "Database crash", "description": "Production DB down"}'
```

## 🐛 Si Aún Falla

### Opción A: Revisar Logs en Vercel
1. Dashboard → Tu proyecto
2. Click en el deployment
3. Ver "Function Logs"
4. Buscar el error específico

### Opción B: Simplificar Requirements
Si `groq` causa problemas, temporalmente:
```txt
# Comentar groq temporalmente
# groq==0.11.0
```
El sistema usará el fallback mode (clasificación por keywords)

### Opción C: Verificar Variables de Entorno
En Vercel Settings → Environment Variables:
- `DATABASE_URL` ✅
- `GROQ_API_KEY` ✅
- `API_SECRET_KEY` ✅
- `ENVIRONMENT=production` ✅
- `CORS_ORIGINS` ✅

## 📊 Diferencias Clave

### Antes (psycopg3)
```python
DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")
```
- ❌ No compatible con Vercel
- ❌ Requiere compilación

### Ahora (psycopg2-binary)
```python
DATABASE_URL  # Usa psycopg2 por defecto
```
- ✅ Compatible con Vercel
- ✅ Pre-compilado (binary)
- ✅ Más rápido de instalar

## ✅ Checklist

- [x] Cambiar a psycopg2-binary
- [x] Crear requirements.txt en api/
- [x] Actualizar database.py
- [x] Mejorar error handling
- [x] Actualizar vercel.json
- [ ] **Hacer commit y push**
- [ ] Verificar deployment
- [ ] Probar endpoints

---

**Siguiente Acción:** Ejecuta los comandos de commit arriba ⬆️
