# Development Guide

## Prerequisites

- Python 3.11+
- pip

## Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/saurabhthakur-ai/azure-agentic-ai-platform.git
cd azure-agentic-ai-platform

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and configure environment variables
cp .env.example .env

# 5. Start the development server
uvicorn backend.app:app --reload
```

The API will be available at <http://localhost:8000>.  
OpenAPI docs are at <http://localhost:8000/docs>.

## Running Tests

```bash
pytest tests/ -v
```

## Project Layout

| Path | Purpose |
|------|---------|
| `backend/app.py` | FastAPI application factory |
| `backend/config/` | Pydantic Settings |
| `backend/api/` | FastAPI routers |
| `backend/models/` | Pydantic request/response models |
| `backend/services/` | Business logic (feature branches) |
| `backend/agents/` | LangGraph / LangChain agents (feature branches) |
| `backend/tools/` | Agent tools (feature branches) |
| `frontend/` | Static HTML/CSS/JS frontend |
| `tests/` | Pytest test suite |
