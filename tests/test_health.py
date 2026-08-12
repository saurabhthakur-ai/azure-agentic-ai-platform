"""
Health endpoint tests.
"""

import pytest
from fastapi.testclient import TestClient

from backend.app import app

client = TestClient(app)


def test_health_returns_200() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response_schema() -> None:
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"
    assert "service" in data
    assert "version" in data
    assert "environment" in data


def test_health_service_name() -> None:
    response = client.get("/health")
    data = response.json()
    assert data["service"] == "azure-agentic-ai-platform"
