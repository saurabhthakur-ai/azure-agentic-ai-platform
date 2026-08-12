# Development Guide

## Prerequisites

- Python 3.11+
- pip or a virtual-environment manager (e.g. `venv`, `pyenv`)

## Local Setup

```bash
# Clone the repository
git clone https://github.com/saurabhthakur-ai/azure-agentic-ai-platform.git
cd azure-agentic-ai-platform

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env as needed

# Start the development server
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Type hints on all public functions.
- Docstrings on all public modules, classes, and functions.
- Keep services, models, and routers in separate files.
