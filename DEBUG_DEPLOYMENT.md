# 🔍 Debug Deployment - Estrategia de Diagnóstico

## 🎯 Estrategia: Deploy Sin Groq Primero

### Problema Actual
La función crashea con `FUNCTION_INVOCATION_FAILED`. Posibles causas:
1. ❌ Groq package no se instala correctamente en Vercel
2. ❌ Problema con imports
3. ❌ Problema con database connection
4. ❌ Problema con environment variables

### Solución: Deploy Incremental

#### Paso 1: Deploy SIN Groq (AHORA)
- ✅ Groq comentado en requirements.txt
- ✅ groq_service.py maneja ImportError gracefully
- ✅ Sistema usa fallback mode automáticamente
- ✅ API funciona con clasificación por keywords

#### Paso 2: Una Vez Funcionando
- Descomentar groq en requirements.txt
- Redeploy
- Verificar que Groq funcione

## 🔧 Cambios Realizados

### 1. `backend/api/index.py`
```python
try:
    from app import app
    handler = app
except Exception as e:
    # Crea app de error que muestra el problema
    # Útil para debugging
```

### 2. `backend/services/groq_service.py`
```python
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    # Usa fallback mode
```

### 3. `backend/api/requirements.txt`
```txt
# groq==0.11.0  ← Comentado temporalmente
```

## 🚀 Deploy Ahora

```bash
git add .
git commit -m "fix: Make Groq optional, add error handling for debugging"
git push origin main
```

## 🧪 Qué Esperar

### Si Funciona (Esperado)
```bash
curl https://hack-force-ai-api.vercel.app/
```
Respuesta:
```json
{
  "message": "Welcome to HackForce AI API",
  "version": "2.0.0",
  "status": "running"
}
```

### Si Aún Falla
```bash
curl https://hack-force-ai-api.vercel.app/
```
Respuesta mostrará el error específico:
```json
{
  "error": "Failed to load application",
  "message": "ModuleNotFoundError: No module named 'xxx'",
  "backend_dir": "/var/task/backend",
  "sys_path": [...]
}
```

## 📊 Diagnóstico por Respuesta

### Error: "No module named 'database'"
**Causa:** Problema con imports relativos
**Solución:** Ajustar sys.path en index.py

### Error: "No module named 'sqlalchemy'"
**Causa:** requirements.txt no se instaló
**Solución:** Verificar ubicación de requirements.txt

### Error: "DATABASE_URL not set"
**Causa:** Variables de entorno no configuradas
**Solución:** Verificar en Vercel Settings

### Error: "Connection refused"
**Causa:** No puede conectar a Supabase
**Solución:** Verificar DATABASE_URL y firewall

### ✅ Sin Error
**Resultado:** API funciona!
**Siguiente:** Descomentar groq y redeploy

## 🎯 Plan de Acción

### Ahora (Deploy 1)
```bash
# Deploy sin Groq
git add .
git commit -m "fix: Make Groq optional for debugging"
git push origin main
```

### Si Funciona (Deploy 2)
```bash
# Descomentar groq en backend/api/requirements.txt
# groq==0.11.0  →  groq==0.11.0

git add backend/api/requirements.txt
git commit -m "feat: Enable Groq AI integration"
git push origin main
```

### Si Falla
Revisar el mensaje de error específico y ajustar.

## 📝 Notas

### Fallback Mode
Cuando Groq no está disponible, el sistema usa:
- Clasificación por keywords
- Confidence scores fijos (0.60-0.85)
- Asignación por workload

### Ventajas de Este Approach
1. ✅ Identificamos el problema exacto
2. ✅ API funciona aunque sea en modo básico
3. ✅ Podemos agregar Groq después
4. ✅ No bloqueamos el deployment

## 🔗 Recursos

- **Vercel Logs:** https://vercel.com/dashboard → Tu proyecto → Function Logs
- **Supabase:** https://supabase.com/dashboard
- **Groq Console:** https://console.groq.com

---

## ⚡ ACCIÓN INMEDIATA

```bash
git add .
git commit -m "fix: Make Groq optional, add error handling"
git push origin main
```

Espera 2 minutos y prueba:
```bash
curl https://hack-force-ai-api.vercel.app/
```

Si funciona → Descomentar groq y redeploy
Si falla → El error message nos dirá exactamente qué está mal

---

**Confianza:** 90% que funcione sin Groq
**Tiempo:** 2 minutos
**Próximo paso:** Deploy y ver qué pasa
