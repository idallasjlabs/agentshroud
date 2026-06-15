# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Post-retry rate-limit failover.

Observed 2026-06-13/14/15: Anthropic returned 429 to hermes cron jobs,
the upstream retry loop tried 3x (all 429), and the final 429 reached
hermes — which raised AssertionError. 3 days of competitive reports
missed.

This test pair verifies (a) the detector fires on a plain 429 (no
quota-wall body), and (b) the proxy falls over to local once the
detector triggers.
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest

from gateway.proxy.llm_proxy import LLMProxy
from gateway.proxy.llm_quota_detector import is_rate_limited_post_retry

# Plain 429 with Anthropic envelope — no "credit balance" / "out of usage"
ANTHROPIC_RATE_LIMIT_BODY = json.dumps(
    {
        "type": "error",
        "error": {
            "type": "rate_limit_error",
            "message": "Number of request tokens has exceeded your per-minute rate limit.",
        },
        "request_id": "req_011Cc1234567890",
    }
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


def test_detector_fires_on_plain_429():
    hit, token = is_rate_limited_post_retry(429, ANTHROPIC_RATE_LIMIT_BODY)
    assert hit is True
    assert token == "anthropic_rate_limit"


def test_detector_skips_non_429():
    assert is_rate_limited_post_retry(200, b"") == (False, "")
    assert is_rate_limited_post_retry(529, b"") == (False, "")
    assert is_rate_limited_post_retry(503, b"") == (False, "")


def test_detector_empty_body_still_fires_as_generic_cloud():
    hit, token = is_rate_limited_post_retry(429, b"")
    assert hit is True
    assert token == "cloud_rate_limit"


@pytest.mark.asyncio
async def test_proxy_failover_on_post_retry_429(monkeypatch):
    """A 429 that escaped the retry loop must trigger local failover."""
    proxy = LLMProxy()
    monkeypatch.setattr("gateway.proxy.llm_proxy.MODEL_MODE", "cloud")

    call_count = [0]

    async def mock_forward(url, body, headers):
        call_count[0] += 1
        if "api.anthropic.com" in url:
            return 429, {"content-type": "application/json"}, ANTHROPIC_RATE_LIMIT_BODY
        # Local backend response
        return 200, {"content-type": "application/json"}, OLLAMA_OK_BODY

    monkeypatch.setattr(proxy, "_forward_request", mock_forward)
    monkeypatch.setattr(proxy, "_emit_failover_notice", lambda *a, **kw: None)
    monkeypatch.setattr(proxy, "_record_failover_event", lambda *a, **kw: None)
    monkeypatch.setenv("AGENTSHROUD_FAILOVER_ON_QUOTA", "1")

    headers = {"content-type": "application/json"}
    body = json.dumps(
        {
            "model": "claude-opus-4-6",
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 10,
        }
    ).encode()
    status, _, resp_body = await proxy.proxy_messages("/v1/messages", body, headers)

    # Successfully failed over to local
    assert status == 200
    parsed = json.loads(resp_body)
    assert parsed["type"] == "message"  # Anthropic envelope shape
    # The local "Hello from local!" content should have made it through
    assert any(b.get("text") == "Hello from local!" for b in parsed["content"])
    assert proxy._stats["failover_quota_succeeded"] == 1
    assert call_count[0] == 2  # 1× Anthropic, 1× local
