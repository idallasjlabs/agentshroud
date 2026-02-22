"""Tests for Version Manager API Routes."""

import os
import tempfile

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from gateway.ingest_api.version_routes import router


@pytest.fixture
def app():
    """Create a test FastAPI app with version routes."""
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture
def client(app):
    return TestClient(app)


@pytest.fixture(autouse=True)
def tmp_version_db(monkeypatch):
    """Use a temporary DB for all tests."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        path = f.name
    monkeypatch.setenv("VERSION_DB_PATH", path)
    # Also patch the module-level variable
    import gateway.tools.agentshroud_manager as mgr

    monkeypatch.setattr(mgr, "VERSION_DB_PATH", path)
    yield path
    os.unlink(path)


class TestVersionRoutes:
    def test_get_current_version(self, client):
        resp = client.get("/api/v1/versions/current")
        assert resp.status_code == 200
        assert "current_version" in resp.json()

    def test_get_history_empty(self, client):
        resp = client.get("/api/v1/versions/history")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_get_available(self, client):
        resp = client.get("/api/v1/versions/available")
        assert resp.status_code == 200
        assert "1.0.0" in resp.json()

    def test_review_version(self, client):
        resp = client.post(
            "/api/v1/versions/review",
            json={"target_version": "1.0.0"},
        )
        assert resp.status_code == 200
        assert resp.json()["passed"] is True

    def test_upgrade_dry_run(self, client):
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "1.0.0", "dry_run": True},
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "dry_run"

    def test_upgrade_requires_approval(self, client):
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "1.0.0"},
        )
        assert resp.status_code == 400
        assert "approval_id" in resp.json()["detail"]

    def test_upgrade_with_approval(self, client):
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "1.0.0", "approval_id": "APR-001"},
        )
        assert resp.status_code == 200
        assert resp.json()["status"] == "completed"

    def test_downgrade_requires_approval(self, client):
        resp = client.post(
            "/api/v1/versions/downgrade",
            json={"target_version": "0.9.0"},
        )
        assert resp.status_code == 400

    def test_downgrade_with_approval(self, client):
        resp = client.post(
            "/api/v1/versions/downgrade",
            json={"target_version": "0.9.0", "approval_id": "APR-002"},
        )
        assert resp.status_code == 200

    def test_rollback_requires_approval(self, client):
        resp = client.post(
            "/api/v1/versions/rollback",
            json={},
        )
        assert resp.status_code == 400

    def test_rollback_no_history(self, client):
        resp = client.post(
            "/api/v1/versions/rollback",
            json={"approval_id": "APR-003"},
        )
        assert resp.status_code == 422

    def test_upgrade_invalid_version(self, client):
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "not-valid", "approval_id": "APR-004"},
        )
        assert resp.status_code == 422

    def test_full_workflow(self, client):
        # Upgrade
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "0.9.0", "approval_id": "APR-010"},
        )
        assert resp.status_code == 200

        # Check current
        resp = client.get("/api/v1/versions/current")
        assert resp.json()["current_version"] == "0.9.0"

        # Upgrade again
        resp = client.post(
            "/api/v1/versions/upgrade",
            json={"target_version": "1.0.0", "approval_id": "APR-011"},
        )
        assert resp.status_code == 200

        # History should have 2 entries
        resp = client.get("/api/v1/versions/history")
        assert len(resp.json()) == 2

        # Rollback
        resp = client.post(
            "/api/v1/versions/rollback",
            json={"approval_id": "APR-012"},
        )
        assert resp.status_code == 200
        assert resp.json()["new_version"] == "0.9.0"
