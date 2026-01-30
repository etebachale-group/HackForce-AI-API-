# 🎨 Deploy Frontend + Backend

## ✅ Cambios Realizados

### 1. Actualizado `vercel.json`
Ahora despliega **AMBOS**:
- ✅ Backend (API Python) en `/api/*`
- ✅ Frontend (React) en `/` (raíz)

### 2. Rutas Configuradas
```
/ → Frontend (Dashboard React)
/api/* → Backend (FastAPI)
/docs → API Documentation
/redoc → API ReDoc
```

### 3. Frontend Build
- ✅ Vite configurado para build
- ✅ API service usa rutas relativas en producción
- ✅ Proxy configurado para desarrollo local

## 🚀 Deploy Ahora

```bash
git add .
git commit -m "feat: Add frontend deployment configuration"
git push origin main
```

## ⏱️ Qué Esperar (3-4 minutos)

Vercel hará:
1. ✅ Build del backend (Python)
2. ✅ Build del frontend (React + Vite)
3. ✅ Configurar rutas
4. ✅ Desplegar todo

## 🧪 Después del Deploy

### Frontend (Dashboard)
```
https://hack-force-ai-api.vercel.app/
```
Verás el dashboard React con:
- Lista de bugs
- Formulario para crear bugs
- Estadísticas
- Gráficos

### Backend (API)
```
https://hack-force-ai-api.vercel.app/api/
```
JSON con info de la API

### Documentación
```
https://hack-force-ai-api.vercel.app/docs
```
Swagger UI interactivo

## 📊 Estructura Final

```
hack-force-ai-api.vercel.app/
├── /                    → React Dashboard (Frontend)
├── /api/bugs           → API Endpoints
├── /api/predict        → AI Prediction
├── /api/stats          → Statistics
├── /docs               → API Documentation
└── /redoc              → Alternative API Docs
```

## 🔧 Cómo Funciona

### En Producción (Vercel)
- Frontend hace requests a `/api/*`
- Vercel rutea `/api/*` al backend Python
- Todo en el mismo dominio (no CORS issues)

### En Desarrollo Local
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- Vite proxy rutea `/api/*` a `localhost:8000`

## ✅ Checklist

- [x] vercel.json actualizado
- [x] vite.config.js configurado
- [x] API service usa rutas relativas
- [x] Rutas configuradas correctamente
- [ ] **HACER COMMIT Y PUSH**
- [ ] Esperar 3-4 minutos
- [ ] Ver dashboard en /
- [ ] Probar crear bugs
- [ ] Verificar AI funciona

## 🎯 Resultado Esperado

Después del deploy, al entrar a:
```
https://hack-force-ai-api.vercel.app/
```

Verás:
- 🎨 Dashboard bonito con React
- 📊 Gráficos y estadísticas
- 🐛 Lista de bugs
- ➕ Botón para crear nuevos bugs
- 🤖 Predicción de severidad con IA

---

**Siguiente Acción:** Ejecuta los comandos de commit arriba ⬆️
