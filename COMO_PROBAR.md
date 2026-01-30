# 🧪 Cómo Probar HackForce AI

## Método 1: Navegador (Más Fácil) 🌐

### Paso 1: Abrir el Dashboard
1. Abre tu navegador (Chrome, Firefox, Edge)
2. Ve a: **https://hack-force-ai-api.vercel.app/**
3. Deberías ver un dashboard oscuro con el título "🤖 HackForce AI"

### Paso 2: Verificar que Carga
✅ Ves tarjetas con estadísticas (Total Bugs, Critical, High, etc.)  
✅ Ves un formulario "🐛 Report New Bug"  
✅ Ves una lista de bugs abajo  

❌ Si ves "Failed to load data" o errores 500, hay un problema

### Paso 3: Crear un Bug de Prueba
1. En el formulario, escribe:
   - **Bug Title:** `Login button not working`
   - **Description:** `When I click the login button nothing happens. This is blocking all users from accessing the system.`

2. Click en **"🚀 Submit Bug Report"**

3. Espera 2-3 segundos (la IA está analizando)

4. Deberías ver:
   - ✅ Mensaje "Bug created successfully with AI classification!"
   - ✅ El bug aparece en la lista abajo
   - ✅ Tiene una etiqueta de severidad (Critical/High/Medium/Low)
   - ✅ Tiene un desarrollador asignado
   - ✅ Muestra el porcentaje de confianza de la IA

### Paso 4: Verificar las Estadísticas
- Las tarjetas de arriba deberían actualizarse
- El contador "Total Bugs" debería aumentar
- La tarjeta de severidad correspondiente debería aumentar

### Paso 5: Probar Filtros
1. En los selectores arriba de la lista:
   - Selecciona "Critical" en "All Severities"
   - Solo deberías ver bugs críticos

2. Selecciona "Open" en "All Statuses"
   - Solo deberías ver bugs abiertos

3. Click en "🔄 Refresh" para recargar

### Paso 6: Eliminar un Bug
1. Click en el botón "🗑️ Delete" de cualquier bug
2. Confirma la eliminación
3. El bug desaparece de la lista
4. Las estadísticas se actualizan

---

## Método 2: Probar la API Directamente 🔧

### Opción A: Desde el Navegador

Abre estas URLs en tu navegador:

1. **Health Check:**
   ```
   https://hack-force-ai-api.vercel.app/health
   ```
   Deberías ver: `{"status":"healthy","database":"connected","version":"2.0.0"}`

2. **Ver Bugs:**
   ```
   https://hack-force-ai-api.vercel.app/api/bugs
   ```
   Deberías ver un array JSON con los bugs

3. **Ver Estadísticas:**
   ```
   https://hack-force-ai-api.vercel.app/api/stats
   ```
   Deberías ver estadísticas en JSON

4. **Documentación API:**
   ```
   https://hack-force-ai-api.vercel.app/docs
   ```
   Interfaz interactiva de Swagger

### Opción B: Desde PowerShell (Windows)

Abre PowerShell y ejecuta:

```powershell
# 1. Health Check
Invoke-RestMethod -Uri "https://hack-force-ai-api.vercel.app/health"

# 2. Ver todos los bugs
Invoke-RestMethod -Uri "https://hack-force-ai-api.vercel.app/api/bugs"

# 3. Ver estadísticas
Invoke-RestMethod -Uri "https://hack-force-ai-api.vercel.app/api/stats"

# 4. Crear un bug (con IA)
$body = @{
    title = "Database connection timeout"
    description = "The application cannot connect to the database. Users are seeing error 500. This is affecting production."
    source = "PowerShell Test"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://hack-force-ai-api.vercel.app/api/bugs" -Method Post -Body $body -ContentType "application/json"
```

### Opción C: Desde CMD (Windows)

```cmd
REM Health Check
curl https://hack-force-ai-api.vercel.app/health

REM Ver bugs
curl https://hack-force-ai-api.vercel.app/api/bugs

REM Ver estadísticas
curl https://hack-force-ai-api.vercel.app/api/stats
```

---

## Método 3: Usar Swagger UI (Más Completo) 📚

1. Ve a: **https://hack-force-ai-api.vercel.app/docs**

2. Verás todos los endpoints disponibles

3. Para probar crear un bug:
   - Click en **POST /api/bugs**
   - Click en **"Try it out"**
   - Edita el JSON:
     ```json
     {
       "title": "Payment processing fails",
       "description": "Users cannot complete purchases. The payment gateway returns error 502. This is critical for business.",
       "source": "Swagger Test"
     }
     ```
   - Click en **"Execute"**
   - Verás la respuesta con la clasificación de la IA

4. Prueba otros endpoints:
   - GET /api/bugs - Ver todos los bugs
   - GET /api/stats - Ver estadísticas
   - DELETE /api/bugs/{bug_id} - Eliminar un bug

---

## 🎯 Qué Esperar (Resultados Correctos)

### ✅ Dashboard Funciona Si:
- Carga sin errores 500
- Muestra estadísticas
- Puedes crear bugs
- Los bugs aparecen en la lista
- La IA asigna severidad automáticamente
- Se asigna un desarrollador

### ❌ Hay Problemas Si:
- Ves "Failed to load data"
- Errores 500 en la consola del navegador
- El formulario no envía
- Los bugs no aparecen
- No hay clasificación de IA

---

## 🔍 Cómo Ver Errores (Si Algo Falla)

### En el Navegador:
1. Presiona **F12** para abrir DevTools
2. Ve a la pestaña **Console**
3. Busca mensajes en rojo
4. Copia el error y me lo pasas

### En Vercel:
1. Ve a: https://vercel.com/etebachale-groups-projects/hack-force-ai-api
2. Click en el último deployment
3. Click en **"Functions"**
4. Click en **"api/index.py"**
5. Ve los logs de errores

---

## 📊 Ejemplos de Bugs para Probar

Prueba crear estos bugs para ver cómo la IA los clasifica:

### Bug Crítico (Debería ser "Critical"):
```
Title: Production server is down
Description: The entire production server is not responding. All users are affected. Revenue is being lost. This needs immediate attention.
```

### Bug Alto (Debería ser "High"):
```
Title: Users cannot login
Description: The login functionality is broken. Users get an error message when trying to authenticate. This affects all users.
```

### Bug Medio (Debería ser "Medium"):
```
Title: Search results are slow
Description: When users search for products, it takes 10-15 seconds to load results. This is annoying but the feature still works.
```

### Bug Bajo (Debería ser "Low"):
```
Title: Button color is wrong
Description: The submit button is blue instead of green. This is a minor visual issue that doesn't affect functionality.
```

---

## ✅ Checklist de Prueba Completa

- [ ] Dashboard carga sin errores
- [ ] Estadísticas se muestran correctamente
- [ ] Puedo crear un bug
- [ ] La IA clasifica la severidad
- [ ] Se asigna un desarrollador automáticamente
- [ ] El bug aparece en la lista
- [ ] Puedo filtrar por severidad
- [ ] Puedo filtrar por estado
- [ ] Puedo eliminar un bug
- [ ] Las estadísticas se actualizan
- [ ] El botón refresh funciona
- [ ] La página es responsive (se ve bien en móvil)

---

## 🆘 Si Necesitas Ayuda

1. **Abre el navegador en:** https://hack-force-ai-api.vercel.app/
2. **Presiona F12** para ver la consola
3. **Intenta crear un bug**
4. **Copia cualquier error** que veas en rojo
5. **Pégame el error** y lo arreglo

¡Prueba ahora y me dices qué ves! 🚀
