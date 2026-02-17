"""Integration tests for gateway endpoints using httpx AsyncClient.

Tests the full pipeline: auth -> sanitize -> route -> ledger -> respond.
"""

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock

from gateway.ingest_api.main import app, app_state, lifespan
from gateway.ingest_api.config import (
    GatewayConfig, LedgerConfig, PIIConfig, RouterConfig, ApprovalQueueConfig
)

import tempfile
from pathlib import Path




@pytest_asyncio.fixture
async def client(test_config, auth_headers):
    with patch('gateway.ingest_api.main.load_config', return_value=test_config), \
         patch('gateway.ingest_api.router.MultiAgentRouter.forward_to_agent', new_callable=AsyncMock) as mock_forward:
        mock_forward.return_value = "mocked response"
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


@pytest.mark.asyncio
async def test_status_no_auth_required(client):
    """GET /status should work without authentication."""
    resp = await client.get("/status")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"
    assert data["version"] == "0.1.0"
    assert data["config_loaded"] is True
    assert "pii_engine" in data


@pytest.mark.asyncio
async def test_forward_requires_auth(client):
    """POST /forward without auth should return 401."""
    resp = await client.post("/forward", json={
        "content": "test content",
        "source": "api",
    })
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_forward_with_auth_creates_ledger_entry(client, auth_headers):
    """POST /forward with auth should sanitize, log, and respond."""
    resp = await client.post("/forward", json={
        "content": "Hello world, no PII here",
        "source": "api",
        "content_type": "text",
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.json()
    assert data["sanitized"] is False
    assert data["redaction_count"] == 0
    assert data["id"] is not None
    assert data["content_hash"] is not None
    assert "forwarded_to" in data


@pytest.mark.asyncio
async def test_forward_redacts_pii(client, auth_headers):
    """POST /forward with PII should redact and report."""
    resp = await client.post("/forward", json={
        "content": "My SSN is 123-45-6789 and email is test@example.com",
        "source": "api",
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.json()
    assert data["sanitized"] is True
    assert data["redaction_count"] >= 2
    assert "US_SSN" in data["redactions"]
    assert "EMAIL_ADDRESS" in data["redactions"]


@pytest.mark.asyncio
async def test_forward_empty_content_rejected(client, auth_headers):
    """POST /forward with empty content should return 422."""
    resp = await client.post("/forward", json={
        "content": "   ",
        "source": "api",
    }, headers=auth_headers)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_forward_invalid_source_rejected(client, auth_headers):
    """POST /forward with invalid source should return 422."""
    resp = await client.post("/forward", json={
        "content": "test",
        "source": "invalid_source",
    }, headers=auth_headers)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_ledger_query_requires_auth(client):
    """GET /ledger without auth should return 401."""
    resp = await client.get("/ledger")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_ledger_query_with_auth(client, auth_headers):
    """GET /ledger with auth should return paginated results."""
    # First create an entry
    await client.post("/forward", json={
        "content": "ledger test content",
        "source": "api",
    }, headers=auth_headers)

    resp = await client.get("/ledger", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "entries" in data
    assert "total" in data
    assert data["total"] >= 1


@pytest.mark.asyncio
async def test_ledger_delete(client, auth_headers):
    """DELETE /ledger/{id} should remove the entry."""
    # Create
    resp = await client.post("/forward", json={
        "content": "to be deleted",
        "source": "api",
    }, headers=auth_headers)
    entry_id = resp.json()["id"]

    # Delete
    resp = await client.delete(f"/ledger/{entry_id}", headers=auth_headers)
    assert resp.status_code == 200

    # Verify gone
    resp = await client.get(f"/ledger/{entry_id}", headers=auth_headers)
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_agents_endpoint(client, auth_headers):
    """GET /agents should list configured targets."""
    resp = await client.get("/agents", headers=auth_headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "agents" in data
    assert len(data["agents"]) >= 1


@pytest.mark.asyncio
async def test_approval_workflow(client, auth_headers):
    """Full approval submit -> decide workflow."""
    # Submit
    resp = await client.post("/approve", json={
        "action_type": "email_sending",
        "description": "Send test email",
        "details": {"to": "test@example.com"},
        "agent_id": "test-agent",
    }, headers=auth_headers)
    assert resp.status_code == 200
    request_id = resp.json()["request_id"]
    assert resp.json()["status"] == "pending"

    # List pending
    resp = await client.get("/approve/pending", headers=auth_headers)
    assert resp.status_code == 200
    assert any(item["request_id"] == request_id for item in resp.json())

    # Decide
    resp = await client.post(f"/approve/{request_id}/decide", json={
        "request_id": request_id,
        "approved": True,
        "reason": "Looks good",
    }, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["status"] == "approved"


@pytest.mark.asyncio
async def test_wrong_token_rejected(client):
    """Request with wrong token should return 401."""
    resp = await client.get("/ledger", headers={"Authorization": "Bearer wrong-token"})
    assert resp.status_code == 401
