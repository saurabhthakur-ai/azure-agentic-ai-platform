# Azure Agentic AI Platform

A professional, Azure-based Python AI platform demonstrating two implementation paths:

| Branch | Purpose |
|--------|---------|
| `feature/langchain-rag` | RAG-based enterprise chatbot (LangChain + Azure Cognitive Search) |
| `feature/langgraph-*` | Multi-agent chatbot with orchestrated agentic workflows (LangGraph) |

`main` contains only the clean boilerplate foundation.

---

## Architecture Overview

```
Client (Browser) → FastAPI Backend → Azure Services (future)
```

See [docs/architecture.md](docs/architecture.md) for the full diagram.

## Technology Stack

- **Python 3.11+**
- **FastAPI** — REST API framework
- **Pydantic / Pydantic Settings** — data validation & config
- **Uvicorn** — ASGI server

## Branching Strategy

See [docs/branching-strategy.md](docs/branching-strategy.md).

```
main
├── feature/project-foundation
├── feature/langchain-rag
├── feature/langchain-retrieval
├── feature/langchain-chatbot
├── feature/langgraph-orchestrator
├── feature/langgraph-agents
├── feature/azure-deployment
└── feature/frontend
```

## Local Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn backend.app:app --reload
```

API: <http://localhost:8000>  
Docs: <http://localhost:8000/docs>  
Health: <http://localhost:8000/health>

## Environment Configuration

Copy `.env.example` to `.env` and fill in Azure credentials when needed.

## Docker

```bash
docker compose up --build
```

## Testing

```bash
pytest tests/ -v
```

## Future: LangChain RAG

- `feature/langchain-rag` — Azure Cognitive Search vector index + RAG chain.
- `feature/langchain-chatbot` — conversational memory, prompt templates.

## Future: LangGraph Multi-Agent

- `feature/langgraph-orchestrator` — graph-based agent orchestration.
- `feature/langgraph-agents` — specialist agents (search, code, summarise).

## Azure Deployment Roadmap

See [docs/azure-deployment.md](docs/azure-deployment.md).

