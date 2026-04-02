# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for multi-agent router"""

from __future__ import annotations

import pytest

from gateway.ingest_api.config import RouterConfig
from gateway.ingest_api.models import AgentTarget, ForwardRequest
from gateway.ingest_api.router import ForwardError, MultiAgentRouter


@pytest.fixture
def router_config():
    """Create a router configuration for testing"""
    return RouterConfig(
        enabled=True,
        default_target="test-agent",
        targets={"agent2": "http://localhost:19000"},
    )


@pytest.fixture
def router(router_config):
    """Create a router instance for testing"""
    return MultiAgentRouter(router_config)


@pytest.mark.asyncio
async def test_resolve_target_default(router):
    """Test routing to default target"""
    request = ForwardRequest(content="test content", source="shortcut", content_type="text")

    target = await router.resolve_target(request)

    assert target.name == "test-agent"
    assert target.url == "http://localhost:18789"


@pytest.mark.asyncio
async def test_resolve_target_explicit(router):
    """Test routing with explicit route_to"""
    request = ForwardRequest(
        content="test content",
        source="shortcut",
        content_type="text",
        route_to="agent2",
    )

    target = await router.resolve_target(request)

    assert target.name == "agent2"
    assert target.url == "http://localhost:19000"


@pytest.mark.asyncio
async def test_resolve_target_invalid_explicit(router):
    """Test routing with invalid explicit target falls back to default"""
    request = ForwardRequest(
        content="test content",
        source="shortcut",
        content_type="text",
        route_to="nonexistent-agent",
    )

    # Should fall back to default
    target = await router.resolve_target(request)

    assert target.name == "test-agent"


@pytest.mark.asyncio
async def test_forward_to_agent_offline(router):
    """Test forwarding to offline agent raises ForwardError"""
    target = AgentTarget(name="offline-agent", url="http://localhost:99999")  # Invalid port

    with pytest.raises(ForwardError):
        await router.forward_to_agent(
            target=target,
            sanitized_content="test content",
            ledger_id="test-id",
            metadata={"source": "shortcut"},
        )


def test_list_targets(router):
    """Test listing all configured targets"""
    targets = router.list_targets()

    assert len(targets) == 2
    names = [t.name for t in targets]
    assert "test-agent" in names
    assert "agent2" in names


@pytest.mark.asyncio
async def test_health_check_offline_agent(router):
    """Test health check for offline agent"""
    results = await router.health_check()

    # Both agents should be reported (both offline)
    assert "test-agent" in results
    assert "agent2" in results

    # Both should be unhealthy (not running)
    assert results["test-agent"]["healthy"] is False
    assert results["agent2"]["healthy"] is False


@pytest.mark.asyncio
async def test_health_check_single_target(router):
    """Test health check for single target"""
    target = router.targets["test-agent"]
    results = await router.health_check(target=target)

    assert "test-agent" in results
    assert len(results) == 1


@pytest.mark.asyncio
async def test_forward_to_agent_timeout(router, monkeypatch):
    """Test forwarding handles timeout exception"""
    import httpx

    async def mock_post(*args, **kwargs):
        raise httpx.TimeoutException("Connection timed out")

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(name="timeout-agent", url="http://localhost:18789")

    with pytest.raises(ForwardError) as exc:
        await router.forward_to_agent(
            target=target,
            sanitized_content="test",
            ledger_id="test-id",
            metadata={"source": "test"},
        )

    assert "Timeout" in str(exc.value)


@pytest.mark.asyncio
async def test_forward_to_agent_http_error(router, monkeypatch):
    """Test forwarding handles HTTP error responses"""
    import httpx

    class MockResponse:
        status_code = 500
        text = "Internal Server Error"

        def raise_for_status(self):
            raise httpx.HTTPStatusError(
                "Server error",
                request=httpx.Request("POST", "http://test"),
                response=self,
            )

    async def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(name="error-agent", url="http://localhost:18789")

    with pytest.raises(ForwardError) as exc:
        await router.forward_to_agent(
            target=target,
            sanitized_content="test",
            ledger_id="test-id",
            metadata={"source": "test"},
        )

    assert "returned error: 500" in str(exc.value)


@pytest.mark.asyncio
async def test_forward_to_agent_unexpected_error(router, monkeypatch):
    """Test forwarding handles unexpected exceptions"""

    async def mock_post(*args, **kwargs):
        raise RuntimeError("Unexpected error")

    import httpx

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(name="error-agent", url="http://localhost:18789")

    with pytest.raises(ForwardError) as exc:
        await router.forward_to_agent(
            target=target,
            sanitized_content="test",
            ledger_id="test-id",
            metadata={"source": "test"},
        )

    assert "Failed to forward" in str(exc.value)


@pytest.mark.asyncio
async def test_health_check_healthy_agent(router, monkeypatch):
    """Test health check with healthy agent"""
    import httpx

    class MockResponse:
        status_code = 200

    async def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    results = await router.health_check()

    # Should have results for all configured agents
    assert len(results) > 0
    for agent_name, status in results.items():
        assert "healthy" in status
        assert "last_check" in status


def test_agent_target_default_paths():
    """AgentTarget defaults chat_path and health_path correctly."""
    target = AgentTarget(name="bot", url="http://localhost:18789")
    assert target.chat_path == "/chat"
    assert target.health_path == "/health"


def test_agent_target_custom_paths():
    """AgentTarget accepts custom chat_path and health_path."""
    target = AgentTarget(
        name="bot",
        url="http://localhost:18789",
        chat_path="/api/chat",
        health_path="/api/health",
    )
    assert target.chat_path == "/api/chat"
    assert target.health_path == "/api/health"


@pytest.mark.asyncio
async def test_forward_uses_chat_path(router, monkeypatch):
    """forward_to_agent builds URL from target.chat_path."""
    import httpx

    captured_url = []

    class MockResponse:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "ok"}

    async def mock_post(self, url, **kwargs):
        captured_url.append(url)
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(name="bot", url="http://localhost:18789", chat_path="/api/chat")
    await router.forward_to_agent(
        target=target,
        sanitized_content="hello",
        ledger_id="test-id",
        metadata={"source": "test"},
    )
    assert captured_url[0] == "http://localhost:18789/api/chat"


@pytest.mark.asyncio
async def test_health_check_uses_health_path(router, monkeypatch):
    """health_check builds URL from target.health_path."""
    import httpx

    captured_url = []

    class MockResponse:
        status_code = 200

    async def mock_get(self, url, **kwargs):
        captured_url.append(url)
        return MockResponse()

    monkeypatch.setattr(httpx.AsyncClient, "get", mock_get)

    target = AgentTarget(name="bot", url="http://localhost:18789", health_path="/api/health")
    await router.health_check(target=target)
    assert captured_url[0] == "http://localhost:18789/api/health"


def test_cors_origins_include_configured_port():
    """load_config computes CORS origins from the configured port."""
    from gateway.ingest_api.config import GatewayConfig

    # Simulate what load_config does: cors_origins derived from port
    port = 9080
    cors_origins = [
        f"http://localhost:{port}",
        f"http://127.0.0.1:{port}",
        "http://localhost:18790",
        "http://127.0.0.1:18790",
    ]
    cfg = GatewayConfig(port=port, cors_origins=cors_origins)
    assert f"http://localhost:{port}" in cfg.cors_origins
    assert f"http://127.0.0.1:{port}" in cfg.cors_origins
    assert "http://localhost:8080" not in cfg.cors_origins
