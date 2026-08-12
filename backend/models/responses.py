"""Response models for the API."""
from datetime import datetime
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response schema."""

    status: str
    environment: str
    timestamp: datetime


class ErrorResponse(BaseModel):
    """Generic error response schema."""

    detail: str
