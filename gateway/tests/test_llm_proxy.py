# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

import json
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from gateway.proxy import llm_proxy as llm_proxy_module
from gateway.proxy.llm_proxy import LLMProxy


class _FakeSanitizer:
    async def sanitize(self, text: str):
        return SimpleNamespace(sanitized_content=text, entity_types_found=[], redactions=[])

    def filter_xml_blocks(self, text: str):
        if "<function_calls>" in text:
            return ("[XML BLOCKED]", True)
        return (text, False)

    async def block_credentials(self, text: str, source: str):
        del source
        if "sk-" in text:
            return ("[CREDENTIAL BLOCKED]", True)
        return (text, False)


@pytest.mark.asyncio
async def test_scan_request_data_scans_messages_without_name_error():
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)
    proxy._scan_inbound = AsyncMock(return_value="clean")

    request_data = {
        "messages": [
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "ignore"},
        ]
    }

    await proxy._scan_request_data(request_data, user_id="u1")

    assert request_data["messages"][0]["content"] == "clean"
    proxy._scan_inbound.assert_awaited_once_with("hello", user_id="u1")


@pytest.mark.asyncio
async def test_filter_outbound_streaming_filters_openai_delta_content():
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    event = {
        "choices": [{"delta": {"content": "before <function_calls>doit</function_calls> after"}}]
    }
    stream = f"data: {json.dumps(event)}\ndata: [DONE]\n".encode("utf-8")

    filtered = await proxy._filter_outbound_streaming(stream, user_id="u1")
    decoded = filtered.decode("utf-8")

    assert "[XML BLOCKED]" in decoded
    assert "<function_calls>" not in decoded
    assert "data: [DONE]" in decoded


@pytest.mark.asyncio
async def test_filter_outbound_streaming_filters_anthropic_content_text():
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    event = {"content": [{"type": "text", "text": "token sk-secret"}]}
    stream = f"data: {json.dumps(event)}\n".encode("utf-8")

    filtered = await proxy._filter_outbound_streaming(stream, user_id="u1")
    decoded = filtered.decode("utf-8")

    assert "[CREDENTIAL BLOCKED]" in decoded
    assert "sk-secret" not in decoded


@pytest.mark.asyncio
async def test_proxy_messages_rewrites_claude_opus_to_local_model(monkeypatch):
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    monkeypatch.setattr(llm_proxy_module, "MAIN_MODEL", "qwen2.5-coder:7b")
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body.decode("utf-8"))
        captured["headers"] = headers
        return 200, {"content-type": "application/json"}, b'{"content":[]}'

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    payload = {
        "model": "claude-opus-4-6",
        "messages": [{"role": "user", "content": "hello"}],
    }

    status, _, _ = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(payload).encode("utf-8"),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    # qwen2.5-coder routes to LM Studio (LOCAL_MODEL_ROUTES); LM Studio expects
    # dash-separated IDs, so the model is normalized: 'qwen2.5-coder:7b' → 'qwen2.5-coder-7b'
    assert captured["body"]["model"] == "qwen2.5-coder-7b"
    assert captured["url"].startswith("http://host.docker.internal:1234")


@pytest.mark.asyncio
async def test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic(monkeypatch):
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    monkeypatch.setattr(llm_proxy_module, "MAIN_MODEL", "qwen2.5-coder:7b")
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    captured = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body.decode("utf-8"))
        captured["headers"] = headers
        return 200, {"content-type": "application/json"}, b'{"content":[]}'

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    payload = {
        "model": "claude-opus-4-6",
        "messages": [{"role": "user", "content": "hello"}],
    }

    status, _, _ = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(payload).encode("utf-8"),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    assert captured["body"]["model"] == "claude-opus-4-6"
    assert captured["url"].startswith("https://api.anthropic.com")


@pytest.mark.asyncio
async def test_proxy_messages_strips_ollama_prefix_for_openai_compat(monkeypatch):
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body.decode("utf-8"))
        captured["headers"] = headers
        return 200, {"content-type": "application/json"}, b'{"choices":[]}'

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    payload = {
        "model": "ollama/qwen2.5-coder:7b",
        "messages": [{"role": "user", "content": "hello"}],
    }

    status, _, _ = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(payload).encode("utf-8"),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    # ollama/qwen2.5-coder:7b → strip prefix → qwen2.5-coder:7b → LM Studio dash normalize → qwen2.5-coder-7b
    assert captured["body"]["model"] == "qwen2.5-coder-7b"
    # qwen2.5-coder is routed to LM Studio (LOCAL_MODEL_ROUTES), not Ollama
    assert captured["url"].startswith("http://host.docker.internal:1234")


@pytest.mark.asyncio
async def test_proxy_messages_timeout_returns_openai_compatible_fallback():
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)

    async def _fake_forward(*_args, **_kwargs):
        raise TimeoutError("timed out")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    payload = {
        "model": "ollama/llama3.1:8b",
        "messages": [{"role": "user", "content": "hello"}],
    }

    status, headers, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(payload).encode("utf-8"),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    assert headers.get("content-type") == "application/json"
    parsed = json.loads(body.decode("utf-8"))
    assert parsed["object"] == "chat.completion"
    assert "choices" in parsed
    assert "timed out before completion" in parsed["choices"][0]["message"]["content"].lower()


@pytest.mark.asyncio
async def test_proxy_messages_timeout_returns_anthropic_compatible_fallback(monkeypatch):
    sanitizer = _FakeSanitizer()
    proxy = LLMProxy(sanitizer=sanitizer)
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    async def _fake_forward(*_args, **_kwargs):
        raise TimeoutError("timed out")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    payload = {
        "model": "claude-opus-4-6",
        "messages": [{"role": "user", "content": "hello"}],
    }

    status, headers, body = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(payload).encode("utf-8"),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    assert headers.get("content-type") == "application/json"
    parsed = json.loads(body.decode("utf-8"))
    assert parsed["type"] == "message"
    assert parsed["role"] == "assistant"
    assert "timed out before completion" in parsed["content"][0]["text"].lower()


# ---------------------------------------------------------------------------
# Credential injector integration — gateway-side OAuth translation
# ---------------------------------------------------------------------------

import urllib.request as _urllib_request  # noqa: E402 (after existing imports)
from unittest.mock import MagicMock  # noqa: E402


class _TrackingInjector:
    """Fake CredentialInjector that records inject_headers calls and applies Anthropic translation."""

    def __init__(self):
        self.calls: list = []

    def inject_headers(self, domain: str, headers: dict) -> dict:
        self.calls.append((domain, dict(headers)))
        if domain == "api.anthropic.com":
            existing_auth = headers.get("Authorization", "")
            if not existing_auth.startswith("Bearer "):
                # Strip x-api-key (any case) and inject Bearer + beta
                for k in list(headers):
                    if k.lower() == "x-api-key":
                        del headers[k]
                headers["Authorization"] = "Bearer injected-gateway-token"
                existing_beta = headers.get("anthropic-beta", "")
                if "oauth-2025-04-20" not in existing_beta:
                    headers["anthropic-beta"] = (
                        f"{existing_beta},oauth-2025-04-20" if existing_beta else "oauth-2025-04-20"
                    )
        return headers


def _make_fake_urlopen(status: int = 200, body: bytes = b'{"content":[]}'):
    """Return a monkeypatched urlopen that captures the Request headers."""
    captured: dict = {}

    def fake_urlopen(req, timeout=None, context=None):
        captured["request_headers"] = dict(req.headers)
        resp = MagicMock()
        resp.read.return_value = body
        resp.headers = {"content-type": "application/json"}
        resp.status = status
        return resp

    return fake_urlopen, captured


@pytest.mark.asyncio
async def test_credential_injector_injects_bearer_for_anthropic_x_api_key(monkeypatch):
    """Anthropic-bound request with x-api-key: injector injects Bearer + beta, strips x-api-key."""
    sanitizer = _FakeSanitizer()
    injector = _TrackingInjector()
    proxy = LLMProxy(sanitizer=sanitizer, credential_injector=injector)
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    fake_urlopen, captured = _make_fake_urlopen()
    monkeypatch.setattr(_urllib_request, "urlopen", fake_urlopen)

    await proxy._forward_request(
        f"{llm_proxy_module.ANTHROPIC_API_BASE}/v1/messages",
        b'{"model":"claude-opus-4-6","messages":[]}',
        {"x-api-key": "sk-ant-oat01-hermes-token", "anthropic-version": "2023-06-01"},
    )

    # Injector must have been called for the Anthropic domain
    assert any(d == "api.anthropic.com" for d, _ in injector.calls), "inject_headers not called"
    # Headers forwarded to the upstream must have Bearer and no x-api-key
    fwd = captured["request_headers"]
    assert "Authorization" in fwd or "authorization" in fwd
    auth_val = fwd.get("Authorization") or fwd.get("authorization", "")
    assert auth_val.startswith("Bearer "), f"Expected Bearer token, got: {auth_val}"
    assert "x-api-key" not in fwd and "X-Api-Key" not in fwd


@pytest.mark.asyncio
async def test_credential_injector_does_not_overwrite_existing_bearer(monkeypatch):
    """OpenClaw already sends Authorization: Bearer — injector must leave it untouched."""
    sanitizer = _FakeSanitizer()
    injector = _TrackingInjector()
    proxy = LLMProxy(sanitizer=sanitizer, credential_injector=injector)
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    fake_urlopen, captured = _make_fake_urlopen()
    monkeypatch.setattr(_urllib_request, "urlopen", fake_urlopen)

    openclaw_token = "Bearer sk-ant-oat01-openclaw-runtime-token"
    await proxy._forward_request(
        f"{llm_proxy_module.ANTHROPIC_API_BASE}/v1/messages",
        b'{"model":"claude-opus-4-6","messages":[]}',
        {"Authorization": openclaw_token},
    )

    # Injector was called but must not have overwritten Bearer
    fwd = captured["request_headers"]
    auth_val = fwd.get("Authorization") or fwd.get("authorization", "")
    assert auth_val == openclaw_token, f"Bearer was overwritten: {auth_val!r}"


@pytest.mark.asyncio
async def test_credential_injector_not_applied_for_non_anthropic_dest(monkeypatch):
    """Local/non-Anthropic destination: injector must NOT be called."""
    sanitizer = _FakeSanitizer()
    injector = _TrackingInjector()
    proxy = LLMProxy(sanitizer=sanitizer, credential_injector=injector)
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    fake_urlopen, _ = _make_fake_urlopen(body=b'{"choices":[]}')
    monkeypatch.setattr(_urllib_request, "urlopen", fake_urlopen)

    # Use a non-Anthropic URL (LM Studio local endpoint)
    await proxy._forward_request(
        "http://host.docker.internal:1234/v1/chat/completions",
        b'{"model":"qwen2.5-coder:7b","messages":[]}',
        {"content-type": "application/json"},
    )

    assert (
        injector.calls == []
    ), f"inject_headers must not be called for local dest; got: {injector.calls}"


@pytest.mark.asyncio
async def test_credential_injector_called_in_streaming_path(monkeypatch):
    """Streaming Anthropic request triggers inject_headers before httpx connects."""
    sanitizer = _FakeSanitizer()
    injector = _TrackingInjector()
    proxy = LLMProxy(sanitizer=sanitizer, credential_injector=injector)
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    payload = json.dumps(
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hello"}],
            "stream": True,
        }
    ).encode()

    # Injection happens before _stream() — it occurs as part of proxy_messages_streaming() setup
    stream = await proxy.proxy_messages_streaming(
        "/v1/messages", payload, {"x-api-key": "sk-ant-oat01-hermes"}, user_id="u1"
    )

    # Injection already happened at this point (before the generator is iterated)
    assert any(
        d == "api.anthropic.com" for d, _ in injector.calls
    ), "inject_headers must be called before streaming starts"

    # Drain one chunk (httpx will fail gracefully → error chunk; we don't care about content)
    async for _ in stream:
        break


# ---------------------------------------------------------------------------
# CVE-2026-9367: ToolACL enforcement in streaming path
# ---------------------------------------------------------------------------


class _FakeToolACL:
    """Minimal ToolACLEnforcer stub that denies a named tool."""

    def __init__(self, deny_tool: str):
        self._deny = deny_tool

    def can_use_tool(self, user_id: str, tool_name: str):
        if tool_name == self._deny:
            return False, f"{tool_name} is PRIVATE"
        return True, "allowed"


@pytest.mark.asyncio
async def test_streaming_tool_acl_blocks_terminal_tool():
    """content_block_start with terminal_tool must be replaced with a text error block."""
    sanitizer = _FakeSanitizer()
    acl = _FakeToolACL(deny_tool="terminal_tool")
    proxy = LLMProxy(sanitizer=sanitizer, tool_acl_enforcer=acl)

    event = {
        "type": "content_block_start",
        "index": 0,
        "content_block": {"type": "tool_use", "id": "tu_1", "name": "terminal_tool", "input": {}},
    }
    result = await proxy._filter_streaming_event(event, user_id="collab-123")

    assert result is not event
    assert result["type"] == "content_block_start"
    assert result["content_block"]["type"] == "text"
    assert "terminal_tool" in result["content_block"]["text"]
    assert "not permitted" in result["content_block"]["text"]


@pytest.mark.asyncio
async def test_streaming_tool_acl_allows_permitted_tool():
    """Allowed tool blocks must pass through unchanged."""
    sanitizer = _FakeSanitizer()
    acl = _FakeToolACL(deny_tool="terminal_tool")
    proxy = LLMProxy(sanitizer=sanitizer, tool_acl_enforcer=acl)

    event = {
        "type": "content_block_start",
        "index": 0,
        "content_block": {"type": "tool_use", "id": "tu_2", "name": "web_search", "input": {}},
    }
    result = await proxy._filter_streaming_event(event, user_id="collab-123")
    # Should be the same object (no modification)
    assert result is event


@pytest.mark.asyncio
async def test_streaming_tool_acl_skips_unknown_user():
    """Events from 'unknown' user_id must not be blocked (not authenticated)."""
    sanitizer = _FakeSanitizer()
    acl = _FakeToolACL(deny_tool="terminal_tool")
    proxy = LLMProxy(sanitizer=sanitizer, tool_acl_enforcer=acl)

    event = {
        "type": "content_block_start",
        "index": 0,
        "content_block": {"type": "tool_use", "id": "tu_3", "name": "terminal_tool", "input": {}},
    }
    result = await proxy._filter_streaming_event(event, user_id="unknown")
    # unknown user_id bypasses ACL enforcement
    assert result is event


# ---------------------------------------------------------------------------
# CVE-2026-9352: secret value scrubbing in _filter_outbound_streaming
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_streaming_secret_value_redacted():
    """A known secret value echoed in a streaming delta must be scrubbed."""

    class _SecretSanitizer(_FakeSanitizer):
        async def block_credentials(self, text: str, source: str):
            if "supersecrettoken12345" in text:
                return ("<REDACTED:secret>", True)
            return (text, False)

    proxy = LLMProxy(sanitizer=_SecretSanitizer())
    sse_body = (
        'data: {"choices":[{"delta":{"content":"your token is supersecrettoken12345"}}]}\n'
        "data: [DONE]\n"
    ).encode()

    result = await proxy._filter_outbound_streaming(sse_body, user_id="u1")
    assert b"supersecrettoken12345" not in result
    assert b"REDACTED" in result


# ---------------------------------------------------------------------------
# Local backend graceful degradation: structured 503 on connect failure
# ---------------------------------------------------------------------------


async def _proxy_with_connect_refused(monkeypatch, model: str):
    proxy = LLMProxy()

    async def mock_forward(url, body, headers):
        raise ConnectionRefusedError(f"[Errno 61] Connection refused: {url}")

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    status, headers, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps({"model": model, "messages": [{"role": "user", "content": "hi"}]}).encode(),
        {"content-type": "application/json"},
    )
    return proxy, status, headers, body


@pytest.mark.asyncio
async def test_mlxlm_connect_failure_returns_structured_503(monkeypatch):
    """mlx_lm down (connection refused) → 503 backend_unavailable with start hint."""
    _, status, headers, body = await _proxy_with_connect_refused(monkeypatch, "deepseek-r1")
    assert status == 503
    assert headers["content-type"] == "application/json"
    data = json.loads(body)
    assert data["error"]["type"] == "backend_unavailable"
    assert "mlx_lm.server --port 8234" in data["error"]["message"]


@pytest.mark.asyncio
async def test_ollama_connect_failure_returns_structured_503(monkeypatch):
    """Ollama down → 503 backend_unavailable with ollama serve hint."""
    _, status, _, body = await _proxy_with_connect_refused(monkeypatch, "llama3.2")
    assert status == 503
    data = json.loads(body)
    assert data["error"]["type"] == "backend_unavailable"
    assert "ollama serve" in data["error"]["message"]


@pytest.mark.asyncio
async def test_lmstudio_connect_failure_returns_structured_503(monkeypatch):
    """LM Studio down → 503 backend_unavailable with LM Studio hint."""
    _, status, _, body = await _proxy_with_connect_refused(monkeypatch, "qwen3:14b")
    assert status == 503
    data = json.loads(body)
    assert data["error"]["type"] == "backend_unavailable"
    assert "LM Studio" in data["error"]["message"]


@pytest.mark.asyncio
async def test_backend_unavailable_warning_rate_limited(monkeypatch, caplog):
    """Repeated connect failures log one WARNING per window, not per request."""
    import logging

    proxy = LLMProxy()

    async def mock_forward(url, body, headers):
        raise ConnectionRefusedError("Connection refused")

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    caplog.set_level(logging.WARNING, logger="agentshroud.proxy.llm_api")

    req = json.dumps(
        {"model": "deepseek-r1", "messages": [{"role": "user", "content": "hi"}]}
    ).encode()
    for _ in range(3):
        status, _, _ = await proxy.proxy_messages(
            "/v1/chat/completions", req, {"content-type": "application/json"}
        )
        assert status == 503

    warnings = [
        r
        for r in caplog.records
        if r.levelno == logging.WARNING and "backend unreachable" in r.getMessage()
    ]
    assert len(warnings) == 1


@pytest.mark.asyncio
async def test_cloud_backend_connect_failure_still_returns_502(monkeypatch):
    """Connect failures to cloud providers keep the existing 502 behavior."""
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")
    proxy = LLMProxy()

    async def mock_forward(url, body, headers):
        raise ConnectionRefusedError("Connection refused")

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    status, _, body = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(
            {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
    )
    assert status == 502
    assert json.loads(body)["error"]["type"] == "api_error"


def test_is_connect_error_classification():
    """_is_connect_error matches connection-level failures only."""
    import urllib.error

    class ConnectError(Exception):  # mimics httpx.ConnectError by name
        pass

    assert LLMProxy._is_connect_error(ConnectError("refused"))
    assert LLMProxy._is_connect_error(ConnectionRefusedError())
    assert LLMProxy._is_connect_error(ConnectionResetError())
    assert LLMProxy._is_connect_error(urllib.error.URLError(ConnectionRefusedError()))
    assert not LLMProxy._is_connect_error(ValueError("nope"))
    # HTTPError wraps a file object — close it or its GC finalizer trips the
    # ResourceWarning gate in pytest.ini
    http_err = urllib.error.HTTPError("http://x", 500, "err", {}, None)
    try:
        assert not LLMProxy._is_connect_error(http_err)
    finally:
        http_err.close()


def test_llm_connect_timeout_clears_observed_dns_latency():
    """Connect timeout must exceed this host's measured DNS-resolution latency
    (~4.0-4.1s to api.anthropic.com/api.openai.com under the current VPN/resolver
    setup) or every proxied streaming call intermittently fails at connect time —
    the failure surfaces upstream as an OpenClaw cron "model idle timeout", not as
    a visible connect error, which made it hard to root-cause.
    """
    assert llm_proxy_module.LLM_CONNECT_TIMEOUT_SECONDS >= 15.0


def test_all_streaming_clients_use_the_shared_connect_timeout_constant():
    """No streaming call site may hardcode its own connect timeout literal.

    Guards against a regression where a new/edited call site (primary request,
    local quota-failover, or cloud quota-failover) reintroduces a tight literal
    like httpx.Timeout(5.0, ...) instead of referencing the shared constant.
    """
    import inspect
    import re

    source = inspect.getsource(llm_proxy_module)
    timeout_calls = re.findall(r"_httpx\.Timeout\(\s*([^,]+),", source)
    assert timeout_calls, "expected at least one httpx.Timeout(...) call site"
    for connect_arg in timeout_calls:
        assert connect_arg.strip() == "LLM_CONNECT_TIMEOUT_SECONDS", (
            f"found a hardcoded connect timeout literal: {connect_arg.strip()!r}"
        )
