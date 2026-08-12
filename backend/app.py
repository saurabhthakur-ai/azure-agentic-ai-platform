"""FastAPI application entry point."""
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.api import router
from backend.config import settings

logging.basicConfig(level=settings.log_level.upper())
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Manage application startup and shutdown lifecycle."""
    logger.info(
        "Starting %s in %s environment", settings.app_name, settings.app_env
    )
    yield
    logger.info("Shutting down %s", settings.app_name)


app = FastAPI(
    title=settings.app_name,
    description=(
        "Azure Agentic AI Platform — boilerplate foundation. "
        "LangChain RAG and LangGraph multi-agent features are implemented "
        "in dedicated feature branches."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(router)

# Serve frontend static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/", include_in_schema=False)
async def serve_frontend() -> FileResponse:
    """Serve the frontend index page."""
    return FileResponse("frontend/index.html")


# Convenience top-level /health redirect (keeps backward compat)
@app.get("/health", include_in_schema=False)
async def health_shortcut():  # type: ignore[return]
    """Shortcut that delegates to the versioned health endpoint."""
    from backend.api.v1.health import health

    return await health()
