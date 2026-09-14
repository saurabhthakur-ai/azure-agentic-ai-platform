"""Tests for the /health endpoint."""
import pytest
from fastapi.testclient import TestClient

from backend.app import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    """Return a synchronous test client."""
    return TestClient(app)


def test_health_returns_200(client: TestClient) -> None:
    """GET /health should return HTTP 200."""
    response = client.get("/health")
    assert response.status_code == 200


def test_health_status_ok(client: TestClient) -> None:
    """GET /health body should contain status=ok."""
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"


def test_health_has_environment(client: TestClient) -> None:
    """GET /health body should include an environment field."""
    response = client.get("/health")
    data = response.json()
    assert "environment" in data


def test_health_has_timestamp(client: TestClient) -> None:
    """GET /health body should include a timestamp field."""
    response = client.get("/health")
    data = response.json()
    assert "timestamp" in data


def test_versioned_health_endpoint(client: TestClient) -> None:
    """GET /api/v1/health should also return HTTP 200 with status=ok."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
