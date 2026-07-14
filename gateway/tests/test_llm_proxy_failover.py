# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the cloud→local quota failover orchestrator in LLMProxy."""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest

from gateway.proxy.llm_proxy import LLMProxy

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ANTHROPIC_QUOTA_BODY = json.dumps(
    {"error": {"type": "rate_limit_error", "message": "Your credit balance is too low."}}
).encode()

OPENAI_QUOTA_BODY = json.dumps(
    {"error": {"code": "insufficient_quota", "message": "You exceeded your current quota."}}
).encode()

OLLAMA_OK_BODY = json.dumps(
    {
        "id": "chatcmpl-test",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "Hello from local!"},
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
    }
).encode()


def make_proxy() -> LLMProxy:
    return LLMProxy()


async def _call_proxy(proxy, path, body_dict, extra_headers=None):
    headers = {"content-type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    return await proxy.proxy_messages(path, json.dumps(body_dict).encode(), headers)


# ---------------------------------------------------------------------------
# T10 — Anthropic quota → successful Ollama failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_anthropic_quota_success(monkeypatch):
    proxy = make_proxy()
    call_count = [0]
    # MODEL_MODE is a module-level constant; patch to "cloud" so the claude-opus
    # intercept at llm_proxy.py:277 doesn't rewrite the model before we can test failover.
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    async def mock_forward(url, body, headers):
        call_count[0] += 1
        if "api.anthropic.com" in url:
            return 429, {}, ANTHROPIC_QUOTA_BODY
        # Ollama response
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, body = await _call_proxy(
        proxy,
        "/v1/messages",
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hello"}],
            "max_tokens": 10,
        },
    )
    assert status == 200
    resp = json.loads(body)
    assert resp["type"] == "message"  # Anthropic shape
    assert resp["model"] == "claude-opus-4-6"  # original model echoed
    assert any(b.get("text") == "Hello from local!" for b in resp["content"])
    assert proxy._stats["failover_quota_succeeded"] == 1
    assert call_count[0] == 2  # first Anthropic, then Ollama


# ---------------------------------------------------------------------------
# Interactive flag — voice callers skip the 429 retry preamble entirely
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_forward_request_interactive_header_skips_retries(monkeypatch):
    """x-agentshroud-interactive: 1 → the first 429 returns immediately (no
    2s/4s/8s backoff), letting quota failover answer in ~seconds.  Voice
    callers set this; cron jobs keep the full retry loop (they prefer waiting
    for Anthropic over local-model output)."""
    import io
    import urllib.error

    proxy = make_proxy()
    attempts = [0]

    def fake_urlopen(req, timeout=None, context=None):
        attempts[0] += 1
        raise urllib.error.HTTPError(
            "https://api.anthropic.com/v1/messages",
            429,
            "rate limited",
            {},
            io.BytesIO(b'{"error":{"type":"rate_limit_error"}}'),
        )

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    status, _, _ = await proxy._forward_request(
        "https://api.anthropic.com/v1/messages",
        b"{}",
        {"x-agentshroud-interactive": "1"},
    )
    assert status == 429
    assert attempts[0] == 1, (
        f"interactive caller must not retry a 429; upstream was called " f"{attempts[0]} times"
    )


@pytest.mark.asyncio
async def test_forward_request_default_still_retries_429(monkeypatch):
    """Without the interactive flag the 3-retry loop is unchanged (guards the
    hermes-cron robustness behaviour added 2026-06-15)."""
    import io
    import urllib.error

    proxy = make_proxy()
    attempts = [0]

    def fake_urlopen(req, timeout=None, context=None):
        attempts[0] += 1
        raise urllib.error.HTTPError(
            "https://api.anthropic.com/v1/messages",
            429,
            "rate limited",
            {},
            io.BytesIO(b'{"error":{"type":"rate_limit_error"}}'),
        )

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    async def _no_sleep(_s):
        return None

    monkeypatch.setattr("gateway.proxy.llm_proxy.asyncio.sleep", _no_sleep)

    status, _, _ = await proxy._forward_request(
        "https://api.anthropic.com/v1/messages",
        b"{}",
        {},
    )
    assert status == 429
    assert attempts[0] == 4  # initial + 3 retries


# ---------------------------------------------------------------------------
# T11 — OpenAI quota → drop-in Ollama failover (no translation)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_openai_quota_dropin(monkeypatch):
    proxy = make_proxy()

    async def mock_forward(url, body, headers):
        if "api.openai.com" in url:
            return 429, {}, OPENAI_QUOTA_BODY
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, body = await _call_proxy(
        proxy,
        "/v1/chat/completions",
        {"model": "gpt-4o", "messages": [{"role": "user", "content": "hi"}]},
    )
    assert status == 200
    resp = json.loads(body)
    # OpenAI path returns Ollama's OpenAI-format response unchanged
    assert "choices" in resp


# ---------------------------------------------------------------------------
# T12 — Ollama unreachable → returns original 429
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_ollama_unreachable_returns_original_429(monkeypatch):
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    async def mock_forward(url, body, headers):
        if "api.anthropic.com" in url:
            return 429, {}, ANTHROPIC_QUOTA_BODY
        raise ConnectionRefusedError("Ollama not running")

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, body = await _call_proxy(
        proxy,
        "/v1/messages",
        {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]},
    )
    assert status == 429
    assert b"credit balance" in body
    assert proxy._stats["failover_quota_failed"] == 1


# ---------------------------------------------------------------------------
# T13 — Flag off → no failover, returns 429 directly
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_flag_off_returns_429(monkeypatch):
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    ollama_called = [False]

    async def mock_forward(url, body, headers):
        if "host.docker.internal" in url:
            ollama_called[0] = True
        return 429, {}, ANTHROPIC_QUOTA_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "0")

    status, _, _ = await _call_proxy(
        proxy,
        "/v1/messages",
        {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]},
    )
    assert status == 429
    assert not ollama_called[0]


# ---------------------------------------------------------------------------
# T14 — Non-quota 429 (request rate limit) → no failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_post_retry_429_now_failovers(monkeypatch):
    """Updated 2026-06-15: a plain 429 that escaped the upstream retry loop
    NOW triggers failover (see is_rate_limited_post_retry). Pre-fix
    behavior was to propagate the 429 to the caller, which broke hermes
    cron jobs (3 days of competitive reports missed) because hermes's SDK
    treated the final 429 as AssertionError."""
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    rate_limit_body = json.dumps(
        {"error": {"type": "rate_limit_error", "message": "Too many requests, slow down."}}
    ).encode()
    ollama_called = [False]

    async def mock_forward(url, body, headers):
        if "host.docker.internal" in url or "localhost" in url:
            ollama_called[0] = True
            return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY
        return 429, {}, rate_limit_body

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, _ = await _call_proxy(
        proxy,
        "/v1/messages",
        {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]},
    )
    # Failover succeeded → 200, local was hit
    assert status == 200
    assert ollama_called[0]


# ---------------------------------------------------------------------------
# T15 — Already-local request never triggers failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_already_local_request_does_not_failover(monkeypatch):
    proxy = make_proxy()
    forward_urls: list[str] = []

    async def mock_forward(url, body, headers):
        forward_urls.append(url)
        return 429, {}, ANTHROPIC_QUOTA_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    await _call_proxy(
        proxy,
        "/v1/chat/completions",
        {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]},
    )
    # All calls should be to local (host.docker.internal), never back to Ollama for failover
    assert len(forward_urls) == 1
    assert "host.docker.internal" in forward_urls[0]


# ---------------------------------------------------------------------------
# T16 — Per-request opt-out header skips failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_per_request_opt_out_header_skips_failover(monkeypatch):
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    ollama_called = [False]

    async def mock_forward(url, body, headers):
        if "host.docker.internal" in url:
            ollama_called[0] = True
        return 429, {}, ANTHROPIC_QUOTA_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, _ = await _call_proxy(
        proxy,
        "/v1/messages",
        {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]},
        extra_headers={"x-agentshroud-no-failover": "1"},
    )
    assert status == 429
    assert not ollama_called[0]


# ---------------------------------------------------------------------------
# T17 — Telegram notification cooldown (one notice per window)
# ---------------------------------------------------------------------------


def test_failover_notification_cooldown(tmp_path, monkeypatch):
    proxy = make_proxy()
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test_token")
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "auth")

    stamp_file = str(tmp_path / "failover-stamp")
    monkeypatch.setattr("gateway.proxy.llm_proxy._FAILOVER_NOTIFY_STAMP", stamp_file)

    send_calls: list[str] = []

    def mock_urlopen(req, timeout=None):
        send_calls.append("sent")
        resp = MagicMock()
        resp.read.return_value = b"{}"
        return resp

    monkeypatch.setattr("urllib.request.urlopen", mock_urlopen)

    proxy._emit_failover_notice("anthropic_credit_balance", translated=True)
    proxy._emit_failover_notice("anthropic_credit_balance", translated=True)  # should be suppressed

    assert len(send_calls) == 1  # cooldown suppressed second notice


# ---------------------------------------------------------------------------
# T18 — Google quota → "no translator" message
# ---------------------------------------------------------------------------


def test_failover_notification_distinguishes_translated_vs_not(tmp_path, monkeypatch):
    proxy = make_proxy()
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test_token")
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "auth")

    stamp_file = str(tmp_path / "failover-stamp-google")
    monkeypatch.setattr("gateway.proxy.llm_proxy._FAILOVER_NOTIFY_STAMP", stamp_file)

    sent_messages: list[str] = []

    def mock_urlopen(req, timeout=None):
        body = json.loads(req.data)
        sent_messages.append(body.get("text", ""))
        resp = MagicMock()
        resp.read.return_value = b"{}"
        return resp

    monkeypatch.setattr("urllib.request.urlopen", mock_urlopen)

    proxy._emit_failover_notice("google_quota", translated=False)

    assert sent_messages
    assert "no translator" in sent_messages[0].lower() or "will fail" in sent_messages[0].lower()


# ---------------------------------------------------------------------------
# T19 — Gemini quota → translated Ollama failover (non-streaming text)
# ---------------------------------------------------------------------------

GOOGLE_QUOTA_BODY = json.dumps(
    {
        "error": {
            "code": 429,
            "message": "Quota exceeded for quota metric 'GenerateContent requests'.",
            "status": "RESOURCE_EXHAUSTED",
        }
    }
).encode()

GEMINI_PATH = "/v1beta/models/gemini-2.0-flash:generateContent"


@pytest.mark.asyncio
async def test_proxy_failover_gemini_quota_success(monkeypatch):
    proxy = make_proxy()
    ollama_requests: list[dict] = []

    async def mock_forward(url, body, headers):
        if "generativelanguage.googleapis.com" in url:
            return 429, {}, GOOGLE_QUOTA_BODY
        ollama_requests.append(json.loads(body))
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, body = await _call_proxy(
        proxy,
        GEMINI_PATH,
        {
            "systemInstruction": {"parts": [{"text": "Be brief."}]},
            "contents": [{"role": "user", "parts": [{"text": "hello"}]}],
        },
    )
    assert status == 200
    resp = json.loads(body)
    # Gemini candidates shape returned to the client
    assert resp["candidates"][0]["content"]["parts"][0]["text"] == "Hello from local!"
    assert resp["candidates"][0]["content"]["role"] == "model"
    assert resp["candidates"][0]["finishReason"] == "STOP"
    assert proxy._stats["failover_quota_succeeded"] == 1
    # Translated OpenAI-format request was sent to Ollama
    assert len(ollama_requests) == 1
    sent = ollama_requests[0]
    assert sent["messages"][0] == {"role": "system", "content": "Be brief."}
    assert sent["messages"][1] == {"role": "user", "content": "hello"}


# ---------------------------------------------------------------------------
# T20 — Gemini streaming request → passthrough 429 + warning, no failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_gemini_streaming_passthrough(monkeypatch, caplog):
    import logging

    proxy = make_proxy()
    ollama_called = [False]

    async def mock_forward(url, body, headers):
        if "host.docker.internal" in url:
            ollama_called[0] = True
        return 429, {}, GOOGLE_QUOTA_BODY

    notices: list[dict] = []
    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(
        proxy,
        "_emit_failover_notice",
        lambda token, translated: notices.append({"token": token, "translated": translated}),
    )
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    caplog.set_level(logging.WARNING, logger="agentshroud.proxy.llm_api")
    status, _, body = await _call_proxy(
        proxy,
        "/v1beta/models/gemini-2.0-flash:streamGenerateContent?alt=sse",
        {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]},
    )
    assert status == 429
    assert b"RESOURCE_EXHAUSTED" in body
    assert not ollama_called[0]
    assert proxy._stats["failover_quota_failed"] == 1
    assert any(
        "Gemini failover" in r.getMessage() and "unsupported" in r.getMessage()
        for r in caplog.records
    )
    # Genuinely untranslatable → "no translator" notice fires
    assert notices == [{"token": "google_quota", "translated": False}]


# ---------------------------------------------------------------------------
# T21 — Gemini tool request → passthrough 429, no failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_gemini_tools_passthrough(monkeypatch):
    proxy = make_proxy()
    ollama_called = [False]

    async def mock_forward(url, body, headers):
        if "host.docker.internal" in url:
            ollama_called[0] = True
        return 429, {}, GOOGLE_QUOTA_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, _ = await _call_proxy(
        proxy,
        GEMINI_PATH,
        {
            "contents": [{"role": "user", "parts": [{"text": "weather?"}]}],
            "tools": [{"functionDeclarations": [{"name": "get_weather"}]}],
        },
    )
    assert status == 429
    assert not ollama_called[0]
    assert proxy._stats["failover_quota_failed"] == 1


# ---------------------------------------------------------------------------
# T22 — Gemini translatable but Ollama down → original 429, no false
#       "no translator" notice (translator DOES exist for this request)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_proxy_failover_gemini_ollama_down_no_false_notice(monkeypatch):
    proxy = make_proxy()
    notices: list = []

    async def mock_forward(url, body, headers):
        if "generativelanguage.googleapis.com" in url:
            return 429, {}, GOOGLE_QUOTA_BODY
        raise ConnectionRefusedError("Ollama not running")

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: notices.append(a))
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, body = await _call_proxy(
        proxy,
        GEMINI_PATH,
        {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]},
    )
    assert status == 429
    assert b"RESOURCE_EXHAUSTED" in body
    assert proxy._stats["failover_quota_failed"] == 1
    assert notices == []  # translator exists — no "no translator" notice


# ---------------------------------------------------------------------------
# Overloaded failover — Anthropic HTTP-200 / 529 "overloaded_error" envelopes
# (the 2026-06-11 silent hermes cron-death failure mode)
# ---------------------------------------------------------------------------

ANTHROPIC_OVERLOADED_BODY = json.dumps(
    {
        "type": "error",
        "error": {"details": None, "type": "overloaded_error", "message": "Overloaded"},
        "request_id": "req_test_overloaded",
    }
).encode()


@pytest.mark.asyncio
async def test_proxy_failover_anthropic_overloaded_http200(monkeypatch):
    """HTTP 200 with an overloaded_error body must trigger local failover."""
    proxy = make_proxy()
    call_count = [0]
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    async def mock_forward(url, body, headers):
        call_count[0] += 1
        if "api.anthropic.com" in url:
            return 200, {"content-type": "application/json"}, ANTHROPIC_OVERLOADED_BODY
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, resp_body = await _call_proxy(
        proxy,
        "/v1/messages",
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hello"}],
            "max_tokens": 10,
        },
    )
    assert status == 200
    resp = json.loads(resp_body)
    assert resp["type"] == "message"
    assert any(b.get("text") == "Hello from local!" for b in resp["content"])
    assert proxy._stats["failover_quota_succeeded"] == 1
    assert call_count[0] == 2


@pytest.mark.asyncio
async def test_proxy_failover_anthropic_overloaded_529(monkeypatch):
    """HTTP 529 with an overloaded_error body must trigger local failover."""
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    async def mock_forward(url, body, headers):
        if "api.anthropic.com" in url:
            return 529, {"content-type": "application/json"}, ANTHROPIC_OVERLOADED_BODY
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, resp_body = await _call_proxy(
        proxy,
        "/v1/messages",
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hello"}],
            "max_tokens": 10,
        },
    )
    assert status == 200
    assert json.loads(resp_body)["type"] == "message"
    assert proxy._stats["failover_quota_succeeded"] == 1


@pytest.mark.asyncio
async def test_proxy_normal_200_passthrough_untouched(monkeypatch):
    """A healthy 200 message body must NOT be failed over."""
    proxy = make_proxy()
    ok_body = json.dumps(
        {"type": "message", "model": "claude-opus-4-6", "content": [{"type": "text", "text": "hi"}]}
    ).encode()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    calls = [0]

    async def mock_forward(url, body, headers):
        calls[0] += 1
        return 200, {"content-type": "application/json"}, ok_body

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, resp_body = await _call_proxy(
        proxy,
        "/v1/messages",
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 5,
        },
    )
    assert status == 200
    assert calls[0] == 1  # no second (failover) dispatch
    assert json.loads(resp_body)["type"] == "message"


@pytest.mark.asyncio
async def test_failover_routes_qwen3_to_lm_studio_with_normalized_model(monkeypatch):
    """Failover for a qwen3 local ref must dispatch to LM Studio (not Ollama,
    which has no models installed) and normalize ollama-style 'qwen3:14b' to
    the LM Studio identifier 'qwen3-14b'."""
    proxy = make_proxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    captured = {}

    async def mock_forward(url, body, headers):
        if "api.anthropic.com" in url:
            return 200, {"content-type": "application/json"}, ANTHROPIC_OVERLOADED_BODY
        captured["url"] = url
        captured["model"] = json.loads(body).get("model")
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    status, _, _ = await _call_proxy(
        proxy,
        "/v1/messages",
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hello"}],
            "max_tokens": 10,
        },
    )
    assert status == 200
    from gateway.proxy.llm_proxy import LMSTUDIO_API_BASE

    assert captured["url"].startswith(LMSTUDIO_API_BASE)
    assert captured["model"] == "qwen3-14b"
