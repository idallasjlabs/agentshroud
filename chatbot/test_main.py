"""Tests for chatbot/main.py.

Covers the four SCRUM-109 fixes:
1. Auth enforcement on /chat
2. Async OpenAI (non-blocking)
3. Health check reflects missing credentials
4. Internal errors not disclosed to clients
"""

from unittest.mock import AsyncMock, MagicMock

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
        mod._openai_client = None  # Will hit 503 before OpenAI, but rate limit fires first
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
            side_effect=RuntimeError("Internal secret: API key abc123 failed at endpoint xyz")
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
        import inspect

        import chatbot.main as mod

        # The lifespan creates AsyncOpenAI, not OpenAI
        # We verify by checking the type annotation in the source
        source = inspect.getsource(mod)
        assert "AsyncOpenAI" in source
        assert "openai.AsyncOpenAI" in source or "openai.AsyncOpenAI" in source

    def test_chat_success_returns_parsed_response(self, client, monkeypatch):
        """A successful OpenAI completion returns 200 with the parsed fields
        via the awaited async client (SCRUM-109: non-blocking chat path)."""
        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._rate_buckets.clear()

        mock_message = MagicMock()
        mock_message.content = "Hello there."
        mock_choice = MagicMock()
        mock_choice.message = mock_message
        mock_usage = MagicMock()
        mock_usage.prompt_tokens = 10
        mock_usage.completion_tokens = 5
        mock_completion = MagicMock()
        mock_completion.choices = [mock_choice]
        mock_completion.model = "gpt-4-turbo"
        mock_completion.usage = mock_usage

        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(return_value=mock_completion)
        mod._openai_client = mock_client

        resp = client.post("/chat", json={"content": "hi"})
        assert resp.status_code == 200
        body = resp.json()
        assert body["response"] == "Hello there."
        assert body["model"] == "gpt-4-turbo"
        assert body["tokens_used"] == 15

    def test_openai_rate_limit_error_returns_429(self, client, monkeypatch):
        """OpenAI's own RateLimitError is translated to a 429 for the caller."""
        import openai as openai_mod

        import chatbot.main as mod

        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._rate_buckets.clear()

        mock_client = MagicMock()
        mock_client.chat.completions.create = AsyncMock(
            side_effect=openai_mod.RateLimitError(
                message="Rate limit exceeded",
                response=MagicMock(status_code=429),
                body=None,
            )
        )
        mod._openai_client = mock_client

        resp = client.post("/chat", json={"content": "hi"})
        assert resp.status_code == 429
        assert "temporarily rate-limited" in resp.json().get("detail", "").lower()


# ---------------------------------------------------------------------------
# 6. Auth token source (secret file vs env var)
# ---------------------------------------------------------------------------


class TestAuthTokenSource:
    def test_get_auth_token_reads_secret_file_over_env(self, monkeypatch):
        """When the Docker secret file exists, it wins over the env var."""
        from pathlib import Path

        import chatbot.main as mod

        real_exists = Path.exists
        real_read_text = Path.read_text

        def fake_exists(self, *a, **kw):
            if str(self) == "/run/secrets/chatbot_auth_token":
                return True
            return real_exists(self, *a, **kw)

        def fake_read_text(self, *a, **kw):
            if str(self) == "/run/secrets/chatbot_auth_token":
                return "file-secret-token\n"
            return real_read_text(self, *a, **kw)

        monkeypatch.setattr(Path, "exists", fake_exists)
        monkeypatch.setattr(Path, "read_text", fake_read_text)
        monkeypatch.setenv("CHATBOT_AUTH_TOKEN", "env-token-should-be-ignored")

        assert mod._get_auth_token() == "file-secret-token"

    def test_get_auth_token_falls_back_to_env_when_no_secret_file(self, monkeypatch):
        import chatbot.main as mod

        monkeypatch.setattr(mod.Path, "exists", lambda self: False)
        monkeypatch.setenv("CHATBOT_AUTH_TOKEN", "env-token-123")

        assert mod._get_auth_token() == "env-token-123"


# ---------------------------------------------------------------------------
# 7. Lifespan startup (persona load + client/auth configuration logging)
# ---------------------------------------------------------------------------


class TestLifespan:
    async def test_lifespan_without_api_key_leaves_client_none(self, monkeypatch, caplog):
        import logging

        import chatbot.main as mod

        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        monkeypatch.setattr(mod.Path, "exists", lambda self: False)
        mod._openai_client = None

        with caplog.at_level(logging.WARNING, logger="chatbot"):
            async with mod.lifespan(mod.app):
                pass

        assert mod._openai_client is None
        assert any("No OpenAI API key found" in r.message for r in caplog.records)
        assert any("unauthenticated" in r.message for r in caplog.records)

    async def test_lifespan_with_api_key_initializes_async_client(self, monkeypatch):
        import chatbot.main as mod

        monkeypatch.setenv("OPENAI_API_KEY", "sk-test-123")
        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        monkeypatch.setattr(mod.Path, "exists", lambda self: False)
        mod._openai_client = None

        async with mod.lifespan(mod.app):
            assert isinstance(mod._openai_client, mod.openai.AsyncOpenAI)

        mod._openai_client = None

    async def test_lifespan_reads_api_key_from_secret_file(self, monkeypatch):
        """When the Docker secret file for the OpenAI key exists, it wins
        over the env var (mirrors the auth-token secret-file precedence)."""
        from pathlib import Path

        import chatbot.main as mod

        real_exists = Path.exists
        real_read_text = Path.read_text

        def fake_exists(self, *a, **kw):
            if str(self) == "/run/secrets/openai_api_key":
                return True
            return real_exists(self, *a, **kw)

        def fake_read_text(self, *a, **kw):
            if str(self) == "/run/secrets/openai_api_key":
                return "sk-from-secret-file\n"
            return real_read_text(self, *a, **kw)

        monkeypatch.setattr(Path, "exists", fake_exists)
        monkeypatch.setattr(Path, "read_text", fake_read_text)
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("CHATBOT_AUTH_TOKEN", raising=False)
        mod._openai_client = None

        async with mod.lifespan(mod.app):
            assert isinstance(mod._openai_client, mod.openai.AsyncOpenAI)

        mod._openai_client = None

    async def test_lifespan_logs_when_auth_token_configured(self, monkeypatch, caplog):
        import logging

        import chatbot.main as mod

        monkeypatch.setenv("CHATBOT_AUTH_TOKEN", "secret")
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.setattr(mod.Path, "exists", lambda self: False)

        with caplog.at_level(logging.INFO, logger="chatbot"):
            async with mod.lifespan(mod.app):
                pass

        assert any("Auth token configured" in r.message for r in caplog.records)
