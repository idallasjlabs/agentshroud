# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Gemini-model-via-OpenAI-path translation.

Mirrors test_claude_via_openai_path.py: voice_gateway's "use Gemini" fast
path (voice_gateway/server.py's _call_llm) POSTs OpenAI-shaped chat bodies
to /v1/chat/completions with model="gemini-*". Without translation that
hits OpenAI's API with an unrecognized model name. The proxy detects the
(path=/v1/chat/completions, model=gemini-*) combo and rewrites to Gemini's
generateContent endpoint with the gateway's own Google API key.
"""

from __future__ import annotations

import builtins
import json
from unittest.mock import mock_open

import pytest

from gateway.proxy.llm_proxy import LLMProxy


@pytest.mark.asyncio
async def test_proxy_rewrites_gemini_via_openai_path(monkeypatch):
    """The combined path: /v1/chat/completions with model=gemini-* must end
    up POSTing to generativelanguage.googleapis.com's generateContent
    endpoint with x-goog-api-key, and the OpenAI envelope must come back."""
    proxy = LLMProxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")
    captured: dict = {}

    async def mock_forward(url, body, headers):
        captured["url"] = url
        captured["headers"] = headers
        captured["body"] = json.loads(body)
        # Return a Gemini-shaped response
        return (
            200,
            {"content-type": "application/json"},
            json.dumps(
                {
                    "candidates": [
                        {
                            "content": {
                                "parts": [{"text": "from upstream"}],
                                "role": "model",
                            },
                            "finishReason": "STOP",
                            "index": 0,
                        }
                    ],
                    "usageMetadata": {
                        "promptTokenCount": 4,
                        "candidatesTokenCount": 2,
                    },
                }
            ).encode(),
        )

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    # Stub the Google API key file
    real_open = builtins.open

    def fake_open(path, *args, **kwargs):
        if str(path) == "/run/secrets/google_api_key":
            return mock_open(read_data="AIza-test-key\n")()
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", fake_open)

    body = json.dumps(
        {
            "model": "gemini-2.5-flash",
            "messages": [
                {"role": "system", "content": "Sys"},
                {"role": "user", "content": "hi"},
            ],
            "max_tokens": 50,
        }
    ).encode()
    headers = {"content-type": "application/json", "Authorization": "Bearer None"}
    status, _, resp_body = await proxy.proxy_messages("/v1/chat/completions", body, headers)

    # Path was rewritten to Gemini's generateContent endpoint
    assert "gemini-2.5-flash:generateContent" in captured["url"]
    assert "generativelanguage.googleapis.com" in captured["url"]
    # Real Google key was substituted; Bearer None scrubbed
    assert captured["headers"].get("x-goog-api-key") == "AIza-test-key"
    assert "authorization" not in (k.lower() for k in captured["headers"])
    # Body was translated: system -> systemInstruction, messages -> contents
    assert captured["body"]["systemInstruction"] == {"parts": [{"text": "Sys"}]}
    assert captured["body"]["contents"] == [{"role": "user", "parts": [{"text": "hi"}]}]
    # Response is OpenAI-shaped (voice_gateway._call_llm expects this)
    assert status == 200
    resp = json.loads(resp_body)
    assert resp["object"] == "chat.completion"
    assert resp["model"] == "gemini-2.5-flash"
    assert resp["choices"][0]["message"]["content"] == "from upstream"


@pytest.mark.asyncio
async def test_proxy_gemini_translation_failure_falls_through_gracefully(monkeypatch):
    """If openai_to_gemini_request raises, the request must still be
    forwarded (unmodified) rather than crash the proxy — same resilience
    contract as the existing Claude-translation branch."""
    proxy = LLMProxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    def _broken_translator(*args, **kwargs):
        raise ValueError("boom")

    monkeypatch.setattr("gateway.proxy.llm_proxy.openai_to_gemini_request", _broken_translator)

    captured: dict = {}

    async def mock_forward(url, body, headers):
        captured["url"] = url
        return (200, {"content-type": "application/json"}, b'{"choices": []}')

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)

    body = json.dumps(
        {"model": "gemini-2.5-flash", "messages": [{"role": "user", "content": "hi"}]}
    ).encode()
    headers = {"content-type": "application/json"}
    status, _, _ = await proxy.proxy_messages("/v1/chat/completions", body, headers)

    assert status == 200
    # Translation failed → original OpenAI path/host used, not Gemini's.
    assert "generativelanguage.googleapis.com" not in captured["url"]
