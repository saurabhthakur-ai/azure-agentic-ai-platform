# Architecture Overview

## High-Level Design

```
┌─────────────────────────────────────────────────────────────┐
│                        Clients                              │
│              (Browser / REST client / CLI)                  │
└───────────────────────┬─────────────────────────────────────┘
                        │  HTTP/REST
┌───────────────────────▼─────────────────────────────────────┐
│                   FastAPI Application                       │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  /health     │  │  future RAG  │  │  future agents    │  │
│  │  (boilerplate│  │  endpoints   │  │  endpoints        │  │
│  │   only)      │  │  (LangChain) │  │  (LangGraph)      │  │
│  └──────────────┘  └──────────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Module Breakdown

| Directory | Purpose |
|-----------|---------|
| `backend/config/` | Settings loaded from environment variables via Pydantic |
| `backend/api/` | FastAPI routers; versioned under `/api/v1/` |
| `backend/models/` | Pydantic request/response schemas |
| `backend/services/` | Business logic (AI service stubs for future use) |
| `backend/agents/` | LangGraph agent definitions (future feature branches) |
| `backend/tools/` | LangChain/LangGraph tool definitions (future) |
| `frontend/` | Plain HTML/CSS/JS chatbot placeholder UI |
| `tests/` | Pytest test suite |

## Future Architecture (Feature Branches)

- **LangChain RAG branch**: Vector store integration, retriever, RAG chain, chat history.
- **LangGraph multi-agent branch**: Orchestrator node, specialist agents, state graph, streaming.
