"""
Health check router.
"""

from fastapi import APIRouter

from backend.config import settings
from backend.models import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return the current health status of the service."""
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        version="0.1.0",
        environment=settings.app_env,
    )
