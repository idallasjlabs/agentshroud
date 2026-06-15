# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Claude-model-via-OpenAI-path translation.

Hermes v0.16.0 routes Claude calls through its OpenAI client, sending to
/v1/chat/completions with Authorization: Bearer None (literal). Without
translation that hits OpenAI's API with no key → 401 → AssertionError.
The proxy detects the (path=/v1/chat/completions, model=claude-*) combo
and rewrites to /v1/messages with the gateway's own Anthropic key.
"""

from __future__ import annotations

import builtins
import json
from contextlib import contextmanager
from unittest.mock import mock_open, patch

import pytest

from gateway.proxy.anthropic_openai_translator import (
    anthropic_to_openai_response,
    openai_to_anthropic_request,
)
from gateway.proxy.llm_proxy import LLMProxy


def test_openai_to_anthropic_request_strips_system_role():
    body = {
        "model": "claude-opus-4-6",
        "messages": [
            {"role": "system", "content": "You are Hermes."},
            {"role": "user", "content": "hi"},
        ],
        "max_tokens": 50,
        "temperature": 0.7,
    }
    out = openai_to_anthropic_request(body)
    assert out["model"] == "claude-opus-4-6"
    assert out["max_tokens"] == 50
    assert out["temperature"] == 0.7
    assert out["system"] == "You are Hermes."
    assert out["messages"] == [{"role": "user", "content": "hi"}]


def test_anthropic_to_openai_response_envelope():
    anth = {
        "id": "msg_x",
        "type": "message",
        "content": [{"type": "text", "text": "Hello!"}],
        "model": "claude-opus-4-6",
        "stop_reason": "end_turn",
        "usage": {"input_tokens": 5, "output_tokens": 3},
    }
    out = anthropic_to_openai_response(anth, original_model="claude-opus-4-6")
    assert out["object"] == "chat.completion"
    assert out["model"] == "claude-opus-4-6"
    assert out["choices"][0]["message"]["content"] == "Hello!"
    assert out["choices"][0]["finish_reason"] == "stop"
    assert out["usage"]["total_tokens"] == 8


@pytest.mark.asyncio
async def test_proxy_rewrites_claude_via_openai_path(monkeypatch):
    """The combined path: /v1/chat/completions with model=claude-* must
    end up POSTing to api.anthropic.com /v1/messages with x-api-key, and
    the OpenAI envelope must come back."""
    proxy = LLMProxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    captured: dict = {}

    async def mock_forward(url, body, headers):
        captured["url"] = url
        captured["headers"] = headers
        captured["body"] = json.loads(body)
        # Return an Anthropic-shaped response
        return (
            200,
            {"content-type": "application/json"},
            json.dumps(
                {
                    "id": "msg_real",
                    "type": "message",
                    "content": [{"type": "text", "text": "from upstream"}],
                    "model": "claude-opus-4-6",
                    "stop_reason": "end_turn",
                    "usage": {"input_tokens": 4, "output_tokens": 2},
                }
            ).encode(),
        )

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    # Stub the Anthropic key file
    real_open = builtins.open

    def fake_open(path, *args, **kwargs):
        if str(path) == "/run/secrets/anthropic_oauth_token":
            return mock_open(read_data="sk-ant-test-key\n")()
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", fake_open)

    body = json.dumps(
        {
            "model": "claude-opus-4-6",
            "messages": [
                {"role": "system", "content": "Sys"},
                {"role": "user", "content": "hi"},
            ],
            "max_tokens": 50,
        }
    ).encode()
    headers = {"content-type": "application/json", "Authorization": "Bearer None"}
    status, _, resp_body = await proxy.proxy_messages("/v1/chat/completions", body, headers)

    # Path was rewritten to Anthropic /v1/messages
    assert "/v1/messages" in captured["url"]
    assert "api.anthropic.com" in captured["url"]
    # Real Anthropic key was substituted; Bearer None scrubbed
    assert captured["headers"].get("x-api-key") == "sk-ant-test-key"
    assert "authorization" not in (k.lower() for k in captured["headers"])
    # Body was translated: system at top level, messages stripped of system role
    assert captured["body"]["system"] == "Sys"
    assert captured["body"]["messages"] == [{"role": "user", "content": "hi"}]
    # Response is OpenAI-shaped (hermes expects this)
    assert status == 200
    resp = json.loads(resp_body)
    assert resp["object"] == "chat.completion"
    assert resp["model"] == "claude-opus-4-6"
    assert resp["choices"][0]["message"]["content"] == "from upstream"
