"""Health check router."""
from datetime import datetime, timezone

from fastapi import APIRouter

from backend.config import settings
from backend.models import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health() -> HealthResponse:
    """Return the current health status of the service."""
    return HealthResponse(
        status="ok",
        environment=settings.app_env,
        timestamp=datetime.now(tz=timezone.utc),
    )
