# F1 Predictor

An Angular frontend, a FastAPI backend for race results, and notebooks for exploring F1 data.

## Repository layout

| Location | Purpose |
| --- | --- |
| `frontend/src/app/pages/` | Angular page components, with their templates, styles, and tests |
| `frontend/src/app/services/` | Angular services and their tests |
| `frontend/public/` | Static browser assets |
| `api/main.py` | FastAPI application and HTTP endpoints |
| `notebooks/` | Exploratory analysis; reusable Python code belongs in `src/f1app/` |
| `tests/` | Python tests as backend functionality grows |
| `data/` | Local datasets and exports (ignored by Git) |
| `cache/` | Downloaded FastF1 cache (ignored by Git) |
| `pyproject.toml` | Python package and build configuration |
| `requirements.txt` | Pinned Python environment, including analysis tools |

Add Python ingestion, feature, model, and database modules inside `src/f1app/` when they are needed. Keep Angular CLI and TypeScript configuration in `frontend/`; those files support the frontend build.

Generated dependencies, caches, and build output are hidden by the root VS Code settings. They remain on disk. To inspect them, temporarily disable the corresponding `files.exclude` entry in `.vscode/settings.json`.

## Python setup

Run from the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The requirements file installs this checkout in editable mode, so changes under `src/` are available without reinstalling.

## Start the API

From the repository root, with the virtual environment activated:

```powershell
python -m uvicorn api.main:app --reload
```

API documentation: http://127.0.0.1:8000/docs

Race results: `GET /api/races/{year}/{round_number}/results`

## Frontend

In another terminal:

```powershell
cd frontend
npm ci
npm start
```

Open http://localhost:4200/. Run `npm run build` to build and `npm test -- --watch=false` to run frontend tests.

## Notebooks and data

Launch Jupyter from `notebooks/` with the virtual environment activated:

```powershell
cd notebooks
python -m jupyter lab
```

The first-look notebook uses `../cache`, so keep the cache at the repository root. Preserve downloaded data locally; do not commit caches, virtual environments, or Node dependencies.
