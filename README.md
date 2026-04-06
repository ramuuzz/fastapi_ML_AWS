# Insurance Prediction Premium

Small Streamlit + prediction service for insurance premium estimation.

## What this repo contains
- `app.py` — backend API (prediction logic)
- `frontend.py` — Streamlit UI
- `model/` — saved model artifact (ignored by .gitignore)
- `config/`, `schema/` — helper modules and data schemas

## Requirements
- Python 3.8+
- Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run locally

1. Activate your virtualenv (example):

```bash
source .venv/Scripts/activate
```

2. Run the Streamlit UI:

```bash
streamlit run frontend.py --server.port 8501
```

3. Or run the API directly:

```bash
python app.py
```
