# Architecture Overview

## High-Level Design

```
┌─────────────────────────────────────────────────────────┐
│                     Client (Browser)                    │
│                  frontend/index.html                    │
└────────────────────────┬────────────────────────────────┘
                         │ HTTP / REST
┌────────────────────────▼────────────────────────────────┐
│                  FastAPI Backend                         │
│  backend/app.py                                         │
│  ├── /health         — health check                     │
│  ├── /docs           — OpenAPI documentation            │
│  └── (future routes added in feature branches)          │
│                                                         │
│  backend/config/     — Pydantic Settings                │
│  backend/models/     — Pydantic response models         │
│  backend/api/        — FastAPI routers                  │
│  backend/services/   — Business logic (future)          │
│  backend/agents/     — LangGraph agents (future)        │
│  backend/tools/      — Agent tools (future)             │
└────────────────────────┬────────────────────────────────┘
                         │
           ┌─────────────▼─────────────┐
           │  Azure Services (future)   │
           │  • Azure OpenAI            │
           │  • Azure Cognitive Search  │
           └───────────────────────────┘
```

## Key Design Decisions

- **Framework-neutral main branch** — no LangChain or LangGraph code in `main`.
- **Pydantic Settings** — all configuration through environment variables.
- **Modular routers** — each feature area has its own FastAPI `APIRouter`.
- **Placeholder packages** — `services/`, `agents/`, `tools/` are empty stubs ready for feature branches.
