# Azure Agentic AI Platform

> **Boilerplate foundation.** Production-ready FastAPI skeleton ready for incremental AI feature development via dedicated branches.

[![CI](https://github.com/saurabhthakur-ai/azure-agentic-ai-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/saurabhthakur-ai/azure-agentic-ai-platform/actions/workflows/ci.yml)

---

## Project Overview

A professional, Azure-based Python AI platform demonstrating two forthcoming implementations:

| Branch family | Description |
|---------------|-------------|
| `feature/langchain-*` | RAG-based enterprise chatbot powered by LangChain + Azure AI Search |
| `feature/langgraph-*` | Multi-agent chatbot with orchestrated workflows using LangGraph |

`main` is intentionally kept framework-neutral and boilerplate-only.

---

## Architecture Overview

```
Client (Browser / REST)
        │
        ▼
  FastAPI (Uvicorn)
  ├── GET /health          ← live health probe
  ├── GET /api/v1/health   ← versioned health probe
  └── GET /               ← serves frontend/index.html
```

See [docs/architecture.md](docs/architecture.md) for the full module breakdown.

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Runtime | Python 3.11+ |
| Web framework | FastAPI + Uvicorn |
| Validation | Pydantic v2 |
| Configuration | pydantic-settings + `.env` |
| Testing | pytest + httpx |
| Containerisation | Docker / Docker Compose |
| CI | GitHub Actions |

---

## Repository Structure

```
azure-agentic-ai-platform/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── backend/
│   ├── app.py              # FastAPI application factory
│   ├── config/             # Settings (pydantic-settings)
│   ├── api/v1/             # Versioned routers
│   ├── models/             # Pydantic schemas
│   ├── services/           # Business logic stubs
│   ├── agents/             # LangGraph agent stubs (future)
│   └── tools/              # LangChain/LangGraph tool stubs (future)
├── frontend/
│   └── index.html          # Plain HTML/CSS/JS chatbot placeholder
├── tests/
│   └── test_health.py
├── docs/
│   ├── architecture.md
│   ├── development.md
│   ├── branching-strategy.md
│   └── azure-deployment.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Branching Strategy

```
main                          ← stable boilerplate
├── feature/project-foundation
├── feature/langchain-rag
├── feature/langchain-retrieval
├── feature/langchain-chatbot
├── feature/langgraph-orchestrator
├── feature/langgraph-agents
├── feature/azure-deployment
└── feature/frontend
```

See [docs/branching-strategy.md](docs/branching-strategy.md) for the full rules.

---

## Local Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn backend.app:app --reload --port 8000
```

Open <http://localhost:8000> for the frontend or <http://localhost:8000/health> for the health probe.

---

## Environment Configuration

Copy `.env.example` to `.env` and fill in the Azure OpenAI values when working on AI feature branches.  
The boilerplate works without any Azure credentials.

---

## Docker Usage

```bash
docker compose up --build
```

---

## Testing

```bash
pytest tests/ -v
```

---

## Future: LangChain RAG Implementation

Planned in `feature/langchain-rag` and `feature/langchain-chatbot`:

- Azure OpenAI embeddings + Azure AI Search vector store
- LangChain retrieval chain with chat history
- `/api/v1/chat` streaming endpoint

---

## Future: LangGraph Multi-Agent Implementation

Planned in `feature/langgraph-orchestrator` and `feature/langgraph-agents`:

- Orchestrator node that routes user intent
- Specialist agents (research, code, summarisation)
- LangGraph state graph with streaming

---

## Azure Deployment Roadmap

See [docs/azure-deployment.md](docs/azure-deployment.md).

Target: Azure Container Apps + Azure OpenAI + Azure AI Search + Azure Key Vault.
