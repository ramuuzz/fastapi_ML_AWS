# Insurance Premium Prediction

A machine learning application that predicts insurance premium categories based on user inputs.
Built with a **FastAPI** backend and a **Streamlit** frontend.

## 🚀 Live Deployments

| Service | URL |
|---|---|
| 🟠 **API (AWS EC2)** | http://16.171.238.145:8000 |
| 🔵 **API (Render)** | https://insuarance-latest.onrender.com |
| 🟢 **Frontend (Streamlit Cloud)** | https://fastapimlaws-zvuhezwd8tbcu4y6hfxhtr.streamlit.app/ |

## What this repo contains

- `app.py` — FastAPI backend (prediction logic)
- `frontend.py` — Streamlit UI (calls the API)
- `model/` — saved model artifact (`.pkl` file)
- `config/`, `schema/` — helper modules and data schemas
- `requirements.txt` — frontend dependencies (Streamlit Cloud)
- `requirements_backend.txt` — backend dependencies (Docker/Render)
- `Dockerfile` — containerises the FastAPI backend

## Run locally

### Prerequisites

- Python 3.12+
- Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 1. Run the FastAPI backend

```bash
pip install -r requirements_backend.txt
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

API will be available at: **http://localhost:8000**
Interactive docs at: **http://localhost:8000/docs**

### 2. Run the Streamlit frontend

In a **separate terminal**, update `API_URL` in `frontend.py` to point to your local backend:

```python
API_URL = "http://localhost:8000/predict"
```

Then run:

```bash
pip install -r requirements.txt
streamlit run frontend.py
```

Frontend will be available at: **http://localhost:8501**

### 3. Run with Docker (backend only)

```bash
docker build -t insuarance .
docker run -p 8000:8000 insuarance
```
