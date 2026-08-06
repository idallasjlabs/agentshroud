"""Tests for chatbot/main.py.

Covers the four SCRUM-109 fixes:
1. Auth enforcement on /chat
2. Async OpenAI (non-blocking)
3. Health check reflects missing credentials
4. Internal errors not disclosed to clients
"""

import importlib
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

# ---------------------------------------------------------------------------
# Helpers to import and configure the app with controlled state
# ---------------------------------------------------------------------------


@pytest.fixture
def app():
    """Import chatbot.main with a fresh module state (no real OpenAI)."""
    import chatbot.main as mod

    # Reset module-level state
    mod._openai_client = None
    mod._persona_prompt = "Test persona"
    mod._rate_buckets.clear()
    return mod.app


@pytest.fixture
def client(app):
    return TestClient(app, raise_server_exceptions=False)


# ---------------------------------------------------------------------------
# 1. Auth enforcement
# ---------------------------------------------------------------------------


class TestAuth:
    def test_chat_requires_auth_when_token_set(self, client, monkeypatch):
        """When CHATBOT_AUTH_TOKEN is set, /chat without a token returns 401."""
        import chatbot.main as mod

        # Mock the OpenAI client so it's "ready"
        mod._openai_client = MagicMock()
        monkeypatch.setenv("CHATBOT_AUTH_TOKEN", "secret-token-123")

        resp = client.post("/chat", json={"content": "hello"})
        assert resp.status_code == 401 or resp.status_code == 403

    def test_chat_allows_valid_token(self, client, monkeypatch):
        """When CHATBOT_AUTH_TOKEN is set and correct token given, request proceeds."""
        import chatbot.main as mod

        monkeypatch.setenv("CHATBOT_AUTH_TOKEN", "secret-token-123")
        # Client not configured -> 503
        mod._openai_client = None
        resp = client.post(
            "/chat",
            json={"content": "hello"},
            headers={"Authorization": "Bearer secret-token-123"},
        )
        # Should get 503 (no client) not 401
        assert resp.status_code == 503

    def test_chat_allows_when_no_token_configured(self, client, monkeypatch):
        """When CHATBOT_AUTH_TOKEN is not set, /chat is open (backward compat)."""
        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._openai_client = None
        resp = client.post("/chat", json={"content": "hello"})
        # Should get 503 (no client) not 401
        assert resp.status_code == 503


# ---------------------------------------------------------------------------
# 2. Rate limiting
# ---------------------------------------------------------------------------


class TestRateLimit:
    def test_rate_limit_enforced(self, client, monkeypatch):
        """Exceeding the rate limit returns 429."""
        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._openai_client = (
            None  # Will hit 503 before OpenAI, but rate limit fires first
        )
        mod._RATE_LIMIT_MAX = 3
        mod._rate_buckets.clear()

        for i in range(3):
            resp = client.post("/chat", json={"content": f"msg {i}"})
            assert resp.status_code in (503, 429)

        # 4th request should be rate-limited
        resp = client.post("/chat", json={"content": "one too many"})
        assert resp.status_code == 429

        # Restore
        mod._RATE_LIMIT_MAX = 20


# ---------------------------------------------------------------------------
# 3. Health check reflects missing credentials
# ---------------------------------------------------------------------------


class TestHealthCheck:
    def test_health_degraded_without_client(self, client):
        """Health endpoint reports degraded when OpenAI client is not available."""
        import chatbot.main as mod

        mod._openai_client = None
        resp = client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "degraded"
        assert data["client_ready"] is False

    def test_health_healthy_with_client(self, client):
        """Health endpoint reports healthy when OpenAI client is available."""
        import chatbot.main as mod

        mod._openai_client = MagicMock()
        resp = client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "healthy"
        assert data["client_ready"] is True


# ---------------------------------------------------------------------------
# 4. Internal errors not disclosed
# ---------------------------------------------------------------------------


class TestErrorSanitization:
    def test_internal_error_not_leaked(self, client, monkeypatch):
        """OpenAI exceptions should not leak internal details to the client."""
        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._rate_buckets.clear()

        # Create a mock async client that raises an unexpected error
        mock_client = MagicMock()
        mock_client.chat = MagicMock()
        mock_client.chat.completions = MagicMock()
        mock_client.chat.completions.create = AsyncMock(
            side_effect=RuntimeError(
                "Internal secret: API key abc123 failed at endpoint xyz"
            )
        )
        mod._openai_client = mock_client

        resp = client.post("/chat", json={"content": "hello"})
        assert resp.status_code == 502
        body = resp.json()
        # Must NOT contain the internal error details
        assert "abc123" not in body.get("detail", "")
        assert "xyz" not in body.get("detail", "")
        assert "internal error" in body.get("detail", "").lower()

    def test_openai_auth_error_returns_503(self, client, monkeypatch):
        """OpenAI AuthenticationError returns 503 without leaking the key."""
        import openai as openai_mod

        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._rate_buckets.clear()

        mock_client = MagicMock()
        mock_client.chat = MagicMock()
        mock_client.chat.completions = MagicMock()
        mock_client.chat.completions.create = AsyncMock(
            side_effect=openai_mod.AuthenticationError(
                message="Invalid API key",
                response=MagicMock(status_code=401),
                body=None,
            )
        )
        mod._openai_client = mock_client

        resp = client.post("/chat", json={"content": "hello"})
        assert resp.status_code == 503
        assert "API key" not in resp.json().get("detail", "")


# ---------------------------------------------------------------------------
# 5. Async client (non-blocking)
# ---------------------------------------------------------------------------


class TestAsyncClient:
    def test_uses_async_openai_client(self):
        """Verify the module uses AsyncOpenAI, not sync OpenAI."""
        import chatbot.main as mod

        # The lifespan creates AsyncOpenAI, not OpenAI
        # We verify by checking the type annotation in the source
        import inspect

        source = inspect.getsource(mod)
        assert "AsyncOpenAI" in source
        assert "openai.AsyncOpenAI" in source or "openai.AsyncOpenAI" in source
