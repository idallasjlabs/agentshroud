# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Alias for hermes v0.16.0's OpenAI client.

POST /chat/completions (no /v1 prefix) used to return 404 → hermes SDK
raised AssertionError → 3 days of competitive cron jobs missed
(2026-06-13/14/15). The alias forwards to the canonical /v1/chat/completions
handler so the security pipeline runs unchanged.
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
            return_value=(
                200,
                {"content-type": "application/json"},
                json.dumps({"id": "chatcmpl-1", "choices": []}).encode(),
            )
        )
        yield TestClient(app)


def test_chat_completions_alias_routes_to_v1_path(client):
    resp = client.post(
        "/chat/completions",
        content=json.dumps(
            {
                "model": "claude-opus-4-6",
                "messages": [{"role": "user", "content": "hi"}],
                "max_tokens": 10,
            }
        ),
        headers={"Content-Type": "application/json"},
    )
    # Reaches the v1 proxy → 200 from the mocked llm_proxy
    assert resp.status_code == 200


def test_chat_completions_alias_passes_correct_path_to_proxy(client):
    # Inspect what path the alias forwarded to llm_proxy.proxy_messages
    from gateway.ingest_api.main import app_state

    app_state.llm_proxy.proxy_messages.reset_mock()
    client.post(
        "/chat/completions",
        content=json.dumps({"model": "claude-opus-4-6", "messages": []}),
        headers={"Content-Type": "application/json"},
    )
    call_args = app_state.llm_proxy.proxy_messages.call_args
    assert call_args is not None
    # First positional arg is the path string
    path = call_args[0][0] if call_args[0] else call_args[1].get("path", "")
    assert "/v1/chat/completions" in path


def test_get_chat_completions_alias_also_routes(client):
    resp = client.get("/chat/completions")
    # The alias should accept GET as well (some OpenAI-compat clients probe)
    # but the v1 handler may return non-200; we just verify it's not 404.
    assert resp.status_code != 404


def test_root_v1_messages_still_works_unchanged(client):
    """Regression: don't break the existing /v1/messages path."""
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
    assert resp.status_code == 200
