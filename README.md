# HackForce-AI-API-
HackForce AI API

🚀 Objective

Develop a web-accessible API that collects bug reports online, classifies them by severity, suggests developer assignment, and integrates with platforms like Notion and Jira. The API will serve both web applications and software clients. The system will use Groq to fetch bug reports from online sources and a trained AI model for classification and recommendation.


---

📝 Problem Statement

Software projects often accumulate a large number of bug reports across multiple platforms. Manually triaging bugs is time-consuming and error-prone. This project aims to build a centralized AI-powered API that:

Automatically collects bug reports from online sources (GitHub Issues, forums, developer communities).

Classifies bugs by severity.

Suggests the right developer to handle the bug based on historical data and skills.

Provides an interactive dashboard for monitoring, filtering, and visualizing bug data.

Integrates with productivity tools like Notion and Jira to synchronize bug information.



---

👥 Team & Roles

FernandoChaleEteba – FullStackLead
Responsibilities: Backend API development, PostgreSQL database management, Vercel deployment, AI integration.

LaraibMemon – FrontendUIUXLead
Responsibilities: Build React dashboard for visualization, filters, charts, integration indicators, and responsive UI.

MirzaYasirAbdullahBaig – AIMLLead
Responsibilities: Build and train NLP/ML model for bug classification, expose prediction endpoints, optimize model for API usage.



---

🛠 Tech Stack

Backend: Python, FastAPI

Frontend: React, JavaScript, CSS

Database: PostgreSQL

AI/ML: Python, NLP libraries (TensorFlow, PyTorch, HuggingFace, scikit-learn)

Online Data Fetching: Groq

Deployment: Vercel

Integrations: Notion, Jira APIs



---

⚡ Workflow Steps

Step1 PlanningAndDataDefinition (All)

Define bug schema: title, description, severity, developer, status, source.

Define API endpoints and request/response formats.

Decide how Groq will fetch online bug data.


Step2 DataCollection (Groq + Team)

Configure Groq queries to fetch bug reports from sources (GitHub, forums, dev communities).

Store raw data in PostgreSQL for preprocessing.

Ensure collected data includes all fields required for AI training and API output.


Step3 AIModelDevelopment (MirzaYasirAbdullahBaig)

Preprocess data: clean text, tokenize, remove noise.

Train NLP model to classify bug severity.

Develop algorithm to suggest developer assignments based on historical data and skill tags.

Test and optimize for accuracy and low latency.

Package model for API usage via FastAPI endpoints.


Step4 BackendAPIDevelopment (FernandoChaleEteba)

Implement FastAPI server for CRUD operations and AI integration.

Connect backend to PostgreSQL database.

Build endpoints:

/bugs – submit bug

/bugs/{id} – fetch bug info

/predict – send bug description, get severity & assignment

/fetchOnline – trigger Groq data collection


Prepare backend for deployment on Vercel.


Step5 FrontendDashboard (LaraibMemon)

Build React dashboard to visualize API data:

Bug list: title, description, severity, developer, status, source.

Filters by severity, developer, status, source.

Charts: severity distribution, developer workload, timelines.

Integration status indicators (Notion/Jira).


Connect frontend to backend endpoints and AI predictions.

Ensure responsive design and intuitive UX.


Step6 IntegrationsAndTesting (All)

Connect API with Notion and Jira.

Test full flow: Groq fetch → AI classification → backend storage → dashboard visualization → integration sync.

Perform unit testing, API testing, end-to-end testing.

Validate AI predictions against collected bug samples.


Step7 DeploymentAndHackathonDemo (FernandoChaleEteba & All)

Deploy backend API on Vercel serverless functions.

Deploy React frontend on Vercel.

Verify API accessibility from web and software clients.

Prepare live demo for hackathon presentation.



---

📦 Deliverables

AIModel: Trained and integrated NLP model.

BackendAPI: Fully functional REST endpoints with PostgreSQL, Groq integration.

FrontendDashboard: React app showing bug reports, severity, developer assignments, visualizations.

Integrations: Notion/Jira sync.

Documentation: API usage, endpoints, AI model explanation, Groq integration, deployment steps.

HackathonDemo: Live demonstration of the system.



---

📂 Suggested Folder Structure

AiBugClassificationAPI/
├─ Backend/
│  ├─ App.py
│  ├─ Models.py
│  ├─ Routes/
│  └─ Requirements.txt
├─ Frontend/
│  ├─ Public/
│  ├─ Src/
│  │  ├─ Components/
│  │  ├─ Pages/
│  │  ├─ App.js
│  │  └─ Index.js
│  └─ Package.json
├─ AiModel/
│  ├─ TrainModel.py
│  ├─ Predict.py
│  └─ Requirements.txt
├─ GroqIntegration/
│  ├─ FetchBugs.py
│  └─ Requirements.txt
├─ Database/
│  └─ Schema.sql
├─ Docs/
│  └─ Architecture.md
└─ README.md
