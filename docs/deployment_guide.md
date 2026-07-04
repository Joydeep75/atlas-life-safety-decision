# ATLAS: Deployment & Running Guide

This document outlines the deployment and local execution pathways for the ATLAS Life-Safety Decision Agent.

---

## 1. Judging & Reproducibility Notice
- **Live deployment is completely optional** for competition judging.
- Judges can download, configure, and run ATLAS entirely locally on their machine. All safety tool lookups use local mock/fallback databases by default to ensure offline reproducibility.
- If live deployment is desired, the project contains a Dockerfile and fully reproducible Cloud Run instructions.

---

## 2. Running Locally (Recommended)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/atlas-life-safety-decision.git
   cd atlas-life-safety-decision
   ```
2. **Configure Environment:**
   Create a `.env` file containing your Gemini API key:
   ```text
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```
3. **Install Dependencies:**
   ```bash
   make install
   ```
4. **Run Streamlit Dashboard:**
   ```bash
   make ui
   ```
   Access the dashboard at http://localhost:8501.
5. **Run ADK Playground:**
   ```bash
   make playground
   ```
   Access the playground at http://localhost:18081.

---

## 3. Cloud Run Deployment (Optional)
ATLAS includes a `Dockerfile` and is compatible with Google Cloud Run.
To deploy:
1. Build the container image:
   ```bash
   gcloud builds submit --tag gcr.io/your-project-id/atlas-agent
   ```
2. Deploy to Cloud Run:
   ```bash
   gcloud run deploy atlas-agent \
     --image gcr.io/your-project-id/atlas-agent \
     --platform managed \
     --set-env-vars GOOGLE_API_KEY=your_gemini_api_key_here \
     --allow-unauthenticated
   ```
This deploys the REST API endpoints defined in `app/fast_api_app.py`, allowing integrations to invoke the agent via HTTP.
