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
        "choices": [
            {"delta": {"content": "before <function_calls>doit</function_calls> after"}}
        ]
    }
    stream = f"data: {json.dumps(event)}\ndata: [DONE]\n".encode("utf-8")

    filtered = await proxy._filter_outbound_streaming(stream, user_id="u1")
    decoded = filtered.decode("utf-8")

    assert "[XML BLOCKED]" in decoded
    assert "<function_calls>" not in decoded
    assert 'data: [DONE]' in decoded


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
    assert captured["body"]["model"] == "qwen2.5-coder:7b"
    assert captured["url"].startswith("http://host.docker.internal:11434")


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
    assert captured["body"]["model"] == "qwen2.5-coder:7b"
    assert captured["url"].startswith("http://host.docker.internal:11434")
