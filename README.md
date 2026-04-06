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

## Git / push safety notes
- This repo includes a `.gitignore` that excludes virtualenvs, logs, and model artifacts.
- Do not commit secrets or `.env` files. If a secret is accidentally committed, rotate it immediately and remove it from history (use `git filter-repo` or BFG).
- If a model file (e.g. `model/model.pkl`) is large or sensitive, keep it out of git and store in an artifact store (S3, DVC, or similar).

Quick commands to add & push safely:

```bash
# create a branch
git checkout -b feature/prepare-repo

# stage only intended files, inspect staged diff
git add -p
git diff --staged
git commit -m "chore: add .gitignore and README"
git push -u origin feature/prepare-repo
```

## Tests & linting
- Run tests if present: `pytest -q`
- Lint with `flake8` / `mypy` where applicable.

## License
Include your license here.
