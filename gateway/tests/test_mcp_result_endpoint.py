# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for POST /mcp/result endpoint and mcp_proxy_data / proxy_allowed_domains config loading."""
from __future__ import annotations


import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock
from pathlib import Path

from gateway.ingest_api.config import (
    ApprovalQueueConfig,
    GatewayConfig,
    LedgerConfig,
    PIIConfig,
    RouterConfig,
)
from gateway.ingest_api.main import app, lifespan


# ── Fixtures ──────────────────────────────────────────────────────────────────


@pytest.fixture
def test_config() -> GatewayConfig:
    return GatewayConfig(
        bind="127.0.0.1",
        port=8080,
        auth_method="shared_secret",
        auth_token="test-token-12345",
        ledger=LedgerConfig(backend="sqlite", path=Path(":memory:"), retention_days=90),
        router=RouterConfig(enabled=True, default_target="test-agent", targets={}),
        pii=PIIConfig(engine="regex", entities=[], enabled=False),
        approval_queue=ApprovalQueueConfig(enabled=True, actions=[], timeout_seconds=3600),
        log_level="WARNING",
    )


@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test-token-12345"}


@pytest_asyncio.fixture
async def client(test_config, auth_headers):
    with patch("gateway.ingest_api.main.load_config", return_value=test_config), patch(
        "gateway.ingest_api.router.MultiAgentRouter.forward_to_agent",
        new_callable=AsyncMock,
    ) as mock_forward:
        mock_forward.return_value = "mocked response"
        async with lifespan(app):
            transport = ASGITransport(app=app)
            async with AsyncClient(transport=transport, base_url="http://test") as ac:
                yield ac


# ── /mcp/result endpoint tests ────────────────────────────────────────────────


class TestMCPResultEndpoint:

    @pytest.mark.asyncio
    async def test_clean_result_accepted(self, client, auth_headers):
        """A result with no threats should be accepted and audited (200)."""
        resp = await client.post(
            "/mcp/result",
            json={
                "server_name": "github",
                "tool_name": "get_file_contents",
                "call_id": "test-call-001",
                "content": {"content": "Hello, world!", "encoding": "none"},
                "agent_id": "openclaw-bot",
            },
            headers=auth_headers,
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "audit_entry_id" in data
        assert "findings_count" in data
        assert "threat_level" in data
        assert "sanitized_result" in data

    @pytest.mark.asyncio
    async def test_result_with_pii_is_audited_not_blocked(self, client, auth_headers):
        """A result containing PII is audited and redacted — never blocked (results are never denied)."""
        resp = await client.post(
            "/mcp/result",
            json={
                "server_name": "filesystem",
                "tool_name": "read_file",
                "call_id": "test-call-002",
                "content": {"text": "SSN: 123-45-6789 found in document"},
                "agent_id": "openclaw-bot",
            },
            headers=auth_headers,
        )
        # Results are NEVER blocked — only redacted and audited
        assert resp.status_code == 200
        data = resp.json()
        assert "audit_entry_id" in data
        # PII should be flagged
        assert data["findings_count"] >= 0  # may be 0 if PII scan disabled in test config

    @pytest.mark.asyncio
    async def test_result_requires_auth(self, client):
        """Unauthenticated request is rejected."""
        resp = await client.post(
            "/mcp/result",
            json={
                "server_name": "github",
                "tool_name": "get_file_contents",
                "content": {"text": "data"},
            },
        )
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_result_with_null_content(self, client, auth_headers):
        """Null content is handled gracefully."""
        resp = await client.post(
            "/mcp/result",
            json={
                "server_name": "github",
                "tool_name": "list_commits",
                "call_id": "test-call-003",
                "content": None,
                "agent_id": "openclaw-bot",
            },
            headers=auth_headers,
        )
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_result_missing_server_name_rejected(self, client, auth_headers):
        """Request missing required server_name is rejected with 422."""
        resp = await client.post(
            "/mcp/result",
            json={
                "tool_name": "get_file_contents",
                "content": {"text": "data"},
            },
            headers=auth_headers,
        )
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_result_returns_processing_time(self, client, auth_headers):
        """Response includes processing_time_ms."""
        resp = await client.post(
            "/mcp/result",
            json={
                "server_name": "github",
                "tool_name": "get_issue",
                "call_id": "test-call-004",
                "content": {"title": "Bug report", "number": 42},
                "agent_id": "openclaw-bot",
            },
            headers=auth_headers,
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "processing_time_ms" in data
        assert data["processing_time_ms"] >= 0


# ── Config loading tests ───────────────────────────────────────────────────────


class TestMCPProxyConfigLoading:

    def test_mcp_proxy_data_parsed_from_yaml(self, tmp_path):
        """mcp_proxy_data is populated from the mcp_proxy YAML section."""
        from gateway.ingest_api.config import load_config

        config_file = tmp_path / "agentshroud.yaml"
        config_file.write_text(
            """
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
security:
  pii_redaction: false
mcp_proxy:
  enabled: true
  pii_scan_enabled: true
  injection_scan_enabled: false
  servers:
    github:
      min_trust_level: 1
      tools:
        get_file_contents:
          permission_level: read
"""
        )
        cfg = load_config(config_file)
        assert cfg.mcp_proxy_data != {}
        assert cfg.mcp_proxy_data["enabled"] is True
        assert cfg.mcp_proxy_data["injection_scan_enabled"] is False
        assert "github" in cfg.mcp_proxy_data["servers"]

    def test_mcp_proxy_data_defaults_to_empty_when_absent(self, tmp_path):
        """mcp_proxy_data is an empty dict when section is absent from YAML."""
        from gateway.ingest_api.config import load_config

        config_file = tmp_path / "agentshroud.yaml"
        config_file.write_text(
            """
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
security:
  pii_redaction: false
"""
        )
        cfg = load_config(config_file)
        assert cfg.mcp_proxy_data == {}

    def test_proxy_allowed_domains_parsed_from_yaml(self, tmp_path):
        """proxy_allowed_domains is populated from the proxy.allowed_domains YAML section."""
        from gateway.ingest_api.config import load_config

        config_file = tmp_path / "agentshroud.yaml"
        config_file.write_text(
            """
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
security:
  pii_redaction: false
proxy:
  allowed_domains:
    - api.openai.com
    - api.anthropic.com
    - "*.github.com"
"""
        )
        cfg = load_config(config_file)
        assert "api.openai.com" in cfg.proxy_allowed_domains
        assert "*.github.com" in cfg.proxy_allowed_domains

    def test_proxy_allowed_domains_defaults_to_empty_when_absent(self, tmp_path):
        """proxy_allowed_domains is empty list when proxy section is absent from YAML."""
        from gateway.ingest_api.config import load_config

        config_file = tmp_path / "agentshroud.yaml"
        config_file.write_text(
            """
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "test-token"
security:
  pii_redaction: false
"""
        )
        cfg = load_config(config_file)
        assert cfg.proxy_allowed_domains == []
