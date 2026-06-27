# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for §2.2 OpenAI-compatible target translation in MultiAgentRouter.

Verifies that route_to:"hermes" (chat_path=/v1/chat/completions) receives an
OpenAI messages[] payload and returns choices[0].message.content as a string,
while OpenClaw (/chat) keeps the generic payload and passes response.json() through.
"""

from __future__ import annotations

from unittest.mock import MagicMock

import httpx
import pytest

from gateway.ingest_api.config import RouterConfig
from gateway.ingest_api.models import AgentTarget
from gateway.ingest_api.router import ForwardError, MultiAgentRouter


@pytest.fixture
def router():
    config = RouterConfig(enabled=True, default_target="openclaw", targets={})
    return MultiAgentRouter(config)


def _mock_response(body, status_code: int = 200) -> MagicMock:
    """Build a fake httpx.Response whose .json() returns *body*."""
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.json = MagicMock(return_value=body)
    resp.raise_for_status = MagicMock()
    return resp


# ── OpenAI-compatible target (Hermes) ────────────────────────────────────────


@pytest.mark.asyncio
async def test_openai_target_sends_messages_body(router, monkeypatch):
    """forward_to_agent sends {model, messages[]} when chat_path ends /v1/chat/completions.

    The messages array MUST start with a system message that includes a date/time
    string (injected so the model can answer time-aware queries), followed by the
    user message containing the sanitized content.
    """
    import re

    captured = {}

    async def mock_post(self, url, json=None, **kwargs):
        captured["url"] = url
        captured["json"] = json
        return _mock_response(
            {"choices": [{"message": {"content": "Hello from Hermes"}}]}
        )

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    await router.forward_to_agent(
        target=target,
        sanitized_content="what time is it?",
        ledger_id="test-id",
        metadata={"source": "api"},
    )

    assert captured["url"] == "http://agentshroud-hermes:8642/v1/chat/completions"
    body = captured["json"]
    assert "messages" in body
    messages = body["messages"]

    # First message must be a system message with a date/time string
    assert len(messages) == 2, f"Expected [system, user], got {messages}"
    sys_msg = messages[0]
    assert sys_msg["role"] == "system"
    # The content should contain a date pattern (e.g. "Monday, June 23, 2026")
    assert re.search(r"\w+, \w+ \d{1,2}, \d{4}", sys_msg["content"]), (
        f"System message should contain a date: {sys_msg['content']}"
    )
    assert "current date and time" in sys_msg["content"].lower()

    # Second message must be the user content
    user_msg = messages[1]
    assert user_msg["role"] == "user"
    assert user_msg["content"] == "what time is it?"

    assert "model" in body
    assert "content" not in body  # generic field must NOT be sent
    assert "ledger_id" not in body  # generic field must NOT be sent


@pytest.mark.asyncio
async def test_openai_target_returns_content_string(router, monkeypatch):
    """forward_to_agent extracts choices[0].message.content and returns a string."""

    async def mock_post(self, url, json=None, **kwargs):
        return _mock_response(
            {"choices": [{"message": {"content": "Hello from Hermes"}}]}
        )

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    result = await router.forward_to_agent(
        target=target,
        sanitized_content="test",
        ledger_id="lid",
        metadata={"source": "api"},
    )

    assert isinstance(result, str)
    assert result == "Hello from Hermes"


@pytest.mark.asyncio
async def test_openai_malformed_response_raises_forward_error(router, monkeypatch):
    """Malformed OpenAI response (missing choices) raises ForwardError, not KeyError."""

    async def mock_post(self, url, json=None, **kwargs):
        return _mock_response({"error": "something went wrong"})

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    with pytest.raises(ForwardError, match="Malformed OpenAI response"):
        await router.forward_to_agent(
            target=target,
            sanitized_content="test",
            ledger_id="lid",
            metadata={"source": "api"},
        )


@pytest.mark.asyncio
async def test_openai_empty_choices_raises_forward_error(router, monkeypatch):
    """Empty choices list raises ForwardError."""

    async def mock_post(self, url, json=None, **kwargs):
        return _mock_response({"choices": []})

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    with pytest.raises(ForwardError, match="Malformed OpenAI response"):
        await router.forward_to_agent(
            target=target,
            sanitized_content="test",
            ledger_id="lid",
            metadata={"source": "api"},
        )


# ── Generic (non-OpenAI) target — OpenClaw /chat ─────────────────────────────


@pytest.mark.asyncio
async def test_generic_target_sends_content_body(router, monkeypatch):
    """forward_to_agent sends the generic {content, ledger_id, ...} body for /chat targets."""
    captured = {}

    async def mock_post(self, url, json=None, **kwargs):
        captured["json"] = json
        return _mock_response("Hello from OpenClaw")

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="openclaw",
        url="http://agentshroud:18789",
        chat_path="/chat",
    )

    await router.forward_to_agent(
        target=target,
        sanitized_content="test message",
        ledger_id="lid-123",
        metadata={"source": "api", "content_type": "text"},
    )

    body = captured["json"]
    assert body["content"] == "test message"
    assert body["ledger_id"] == "lid-123"
    assert "messages" not in body


@pytest.mark.asyncio
async def test_generic_target_returns_json_as_is(router, monkeypatch):
    """forward_to_agent passes response.json() through unchanged for /chat targets."""

    async def mock_post(self, url, json=None, **kwargs):
        return _mock_response("Hello from OpenClaw")

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="openclaw",
        url="http://agentshroud:18789",
        chat_path="/chat",
    )

    result = await router.forward_to_agent(
        target=target,
        sanitized_content="test",
        ledger_id="lid",
        metadata={"source": "api"},
    )

    assert result == "Hello from OpenClaw"


# ── Model field in OpenAI payload ────────────────────────────────────────────


@pytest.mark.asyncio
async def test_openai_payload_includes_model(router, monkeypatch):
    """The OpenAI payload must include a non-empty model field."""
    captured = {}

    async def mock_post(self, url, json=None, **kwargs):
        captured["json"] = json
        return _mock_response(
            {"choices": [{"message": {"content": "ok"}}]}
        )

    monkeypatch.setattr(httpx.AsyncClient, "post", mock_post)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    await router.forward_to_agent(
        target=target,
        sanitized_content="hello",
        ledger_id="lid",
        metadata={"source": "api"},
    )

    model = captured["json"].get("model", "")
    assert isinstance(model, str) and len(model) > 0
