# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Synthetic /v1/models/<id> response so hermes v0.16.0 preflight succeeds.

The actual hermes-v0.16.0 SDK does `GET /v1/models/<id>` before each
`/v1/messages` call. Our ANTHROPIC_API_KEY is an OAuth token
(sk-ant-oat01-…) which Anthropic accepts for /v1/messages but rejects
on /v1/models/<id> with 400/401. The SDK raises AssertionError on
non-200, which bubbles up and crashes hermes cron jobs.

This shim intercepts the model-metadata GET in the gateway and returns
a synthetic 200 envelope — no round-trip to Anthropic.
"""

from __future__ import annotations

import ipaddress
import json
from contextlib import ExitStack
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from gateway.ingest_api.main import app


@pytest.fixture
def client():
    """TestClient with a stubbed proxy IP that passes the network allowlist."""
    with ExitStack() as stack:
        stack.enter_context(
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                [ipaddress.ip_network("10.254.111.0/24")],
            )
        )
        stack.enter_context(
            patch(
                "gateway.ingest_api.main._ipaddress.ip_address",
                return_value=ipaddress.ip_address("10.254.111.10"),
            )
        )
        mock_state = stack.enter_context(patch("gateway.ingest_api.main.app_state"))
        mock_state.llm_proxy = MagicMock()
        mock_state.llm_proxy.proxy_messages = AsyncMock(
            return_value=(502, {"content-type": "text/plain"}, b"unused upstream")
        )
        with TestClient(app) as c:
            yield c


@pytest.mark.parametrize(
    "model_id",
    [
        "claude-opus-4-6",
        "claude-fable-5",
        "claude-haiku-4-5-20251001",
        "claude-sonnet-4-6",
    ],
)
def test_v1_models_get_returns_synthetic_200(client, model_id):
    resp = client.get(f"/v1/models/{model_id}")
    # Must succeed regardless of upstream Anthropic auth state
    assert resp.status_code == 200
    body = resp.json()
    assert body["type"] == "model"
    assert body["id"] == model_id
    assert "display_name" in body
    assert "created_at" in body


def test_v1_models_post_still_goes_through_proxy(client):
    # POST /v1/models is not a real Anthropic endpoint, but the gateway must
    # NOT intercept it as a synthetic GET — must keep flowing through the
    # llm_proxy path. The proxy will likely return an error; we just verify
    # the request is not intercepted at the metadata shim.
    resp = client.post(
        "/v1/models/claude-opus-4-6",
        content=json.dumps({"hello": "world"}),
        headers={"Content-Type": "application/json"},
    )
    # Anything except the synthetic 200 confirms the shim was skipped.
    # 502/500/400/503 are all fine; the shim must not own POST.
    assert resp.status_code != 200 or resp.json().get("type") != "model"


def test_v1_messages_still_goes_through_proxy(client):
    # POST /v1/messages must hit the proxy — not the metadata shim.
    resp = client.post(
        "/v1/messages",
        content=json.dumps(
            {
                "model": "claude-opus-4-6",
                "messages": [{"role": "user", "content": "hi"}],
                "max_tokens": 10,
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    # Don't care about the body — just that it didn't get short-circuited
    # by the metadata shim (the shim only fires on GET + path "models/…").
    body = resp.text
    assert '"type":"model"' not in body[:120] or '"id":"claude-opus-4-6"' not in body[:120]
