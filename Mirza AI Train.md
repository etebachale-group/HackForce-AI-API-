# AI Bug Classification API Workflow

## 1️⃣ Data Preparation
- **Collect sample bug reports**
  - Fields: `title`, `description`, `severity` (Low / Medium / High / Critical), `assigned developer` (optional)
  - Sources: Jira, Notion exports, GitHub issues, or synthetic data for demo
- **Preprocess text**
  - Lowercase, remove punctuation, clean emojis/special characters
  - Tokenization for NLP model
- **Label dataset** for supervised learning

---

## 2️⃣ Feature Engineering
- Convert text into numerical features for the model:
  - TF-IDF vectorization or embeddings (spaCy, Hugging Face)
- Keep feature pipeline simple for **fast prototyping**

---

## 3️⃣ Model Selection
- Lightweight models for MVP:
  - Logistic Regression or Naive Bayes (fast, easy to explain)
  - Optional: small transformer embeddings if time allows
- Focus on: **accuracy, speed, deployability**

---

## 4️⃣ Model Training
- Split dataset: train/test (80/20)
- Train model on bug text → predict severity
- Evaluate metrics: accuracy, precision, recall, F1 score
- Save trained model (`.pkl` / `.joblib`)

---

## 5️⃣ API Development (Python / FastAPI)
- **Endpoint:** `/predict`
  - Input: JSON `{ "title": "...", "description": "..." }`
  - Output: JSON `{ "severity": "...", "suggested_developer": "..." }`
- Include database integration:
  - Store bug reports + predictions in **PostgreSQL**
  - Enable CRUD operations for frontend dashboard
- Include **Notion/Jira integration hooks** (optional, for demo)

---

## 6️⃣ Testing & Validation
- Test API with multiple bug samples
- Check prediction accuracy and response time
- Ensure JSON outputs match frontend expectations

---

## 7️⃣ Deployment
- Host API on **serverless endpoint** compatible with **Vercel** backend functions or small cloud instance
- Ensure accessible for React frontend and dashboard visualizations

---

## 8️⃣ Handoff & Integration
- Provide model file + API code to frontend team
- Connect to React dashboard:
  - Filters: severity, developer, status
  - Charts: severity distribution, timelines, developer workload
- Backend handles persistence with PostgreSQL

---

💡 **Notes:**
- Keep API **stateless** and **fast**
- MVP first, **complex AI improvements** can come later
- Focus: **usable API → demo-ready dashboard → integration with web/app**

