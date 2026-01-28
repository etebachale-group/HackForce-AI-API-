# AI Bug Classification API - Full Workflow with Groq

## 1️⃣ Objective

Develop a **web-accessible API** that collects bug reports online, classifies them by severity, suggests developer assignment, and integrates with platforms like **Notion** and **Jira**. The API will serve both **web applications** and software clients.

---

## 2️⃣ Team & Roles

- **Fernando Chale Eteba** – Full-Stack Lead
  *Focus:* Backend API implementation, PostgreSQL management, Vercel deployment, AI integration.

- **Laraib Memon** – Frontend & UI/UX Lead
  *Focus:* React dashboard for API data visualization, interactive UI, bug severity, developer assignments, integration indicators.

- **Mirza Yasir Abdullah Baig** – AI/ML Lead
  *Focus:* Build NLP model for bug classification, expose prediction endpoints, optimize model performance for API consumption.

---

## 3️⃣ Workflow Steps

### **Step 1: Planning & Data Definition (All)**

- Define bug data schema: title, description, severity, developer, status, source.
- Define API endpoints, request/response formats, and success criteria.
- Decide how Groq will fetch online bug data.

---

### **Step 2: Data Collection (Groq + Team)**

- **Groq Integration:**
  - Configure queries to fetch bug reports from online sources (GitHub Issues, forums, developer communities).
  - Store raw bug data in PostgreSQL for preprocessing.
- Ensure collected data includes fields needed for AI training and API output.

---

### **Step 3: AI Model Development (Mirza)**

- Preprocess data: clean text, tokenize, remove duplicates/noise.
- Train NLP model to classify bug severity.
- Develop algorithm to suggest developer assignments based on historical data and skill tags.
- Test and optimize model for accuracy and low latency.
- Package model for API usage via FastAPI endpoint.

---

### **Step 4: Backend API Development (Fernando)**

- Implement FastAPI server for bug CRUD operations, AI integration, and Groq-fetched data.
- Connect backend to PostgreSQL.
- Build endpoints:
  - `/bugs` – submit bug
  - `/bugs/{id}` – fetch bug info
  - `/predict` – send bug description, get severity & assignment
  - `/fetch-online` – trigger Groq data collection
- Ensure API can handle multiple requests efficiently.
- Prepare backend for Vercel deployment.

---

### **Step 5: Frontend / Dashboard (Laraib)**

- Build React dashboard to visualize API data:
  - Bug list with title, description, severity, developer, status, source.
  - Filters by severity, developer, status, source.
  - Charts for severity distribution, developer workload, timelines.
  - Integration status indicators (Notion/Jira).
- Connect frontend to backend endpoints and AI predictions.
- Ensure responsive design and intuitive UX.

---

### **Step 6: Integrations & Testing (All)**

- Connect API with external apps: Notion & Jira.
- Test full flow: Groq fetch → AI classification → backend storage → dashboard visualization → integration sync.
- Perform unit testing, API testing, and end-to-end testing.
- Validate model predictions against collected sample bugs.

---

### **Step 7: Deployment & Hackathon Demo (Fernando & All)**

- Deploy backend API on Vercel serverless functions.
- Deploy React frontend on Vercel.
- Verify API accessibility from web and software clients.
- Prepare live demo for hackathon presentation.

---

## 4️⃣ Deliverables

- **AI Model:** Trained NLP model integrated with API.
- **Backend API:** REST endpoints with PostgreSQL, including Groq integration.
- **Frontend Dashboard:** React app displaying bug reports, severity, developer assignments, visualizations.
- **Integrations:** Working Notion/Jira sync.
- **Documentation:** API usage, endpoints, AI model explanation, Groq integration, deployment steps.
- **Hackathon Demo:** Live demonstration.

---

## 5️⃣ Suggested Folder Structure

```
AI-Bug-Classification-API/
├─ backend/
│  ├─ app.py
│  ├─ models.py
│  ├─ routes/
│  └─ requirements.txt
├─ frontend/
│  ├─ public/
│  ├─ src/
│  │  ├─ components/
│  │  ├─ pages/
│  │  ├─ App.js
│  │  └─ index.js
│  └─ package.json
├─ ai_model/
│  ├─ train_model.py
│  ├─ predict.py
│  └─ requirements.txt
├─ groq_integration/
│  ├─ fetch_bugs.py
│  └─ requirements.txt
├─ database/
│  └─ schema.sql
├─ docs/
│  └─ architecture.md
└─ README.md
```

---

This workflow ensures **Groq fetches online bugs**, your **AI model classifies them and makes suggestions**, and your **API + frontend** delivers a real-time dashboard for users and software integrations.

