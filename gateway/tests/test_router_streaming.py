# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for MultiAgentRouter.forward_to_agent_stream — SSE relay to an
OpenAI-compatible agent (Hermes), used by the voice streaming pipeline.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
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


def _sse_lines(chunks: list[dict]) -> list[str]:
    import json

    lines = [f"data: {json.dumps(c)}" for c in chunks]
    lines.append("data: [DONE]")
    return lines


def _mock_stream_response(lines: list[str], status_code: int = 200) -> MagicMock:
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.raise_for_status = MagicMock()

    async def _aiter_lines():
        for line in lines:
            yield line

    resp.aiter_lines = _aiter_lines
    return resp


@pytest.mark.asyncio
async def test_stream_yields_content_deltas_in_order(router, monkeypatch):
    lines = _sse_lines(
        [
            {"choices": [{"delta": {"role": "assistant"}, "finish_reason": None}]},
            {"choices": [{"delta": {"content": "One"}, "finish_reason": None}]},
            {"choices": [{"delta": {"content": "."}, "finish_reason": None}]},
            {"choices": [{"delta": {"content": " Two."}, "finish_reason": None}]},
            {"choices": [{"delta": {}, "finish_reason": "stop"}]},
        ]
    )

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        yield _mock_stream_response(lines)

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    deltas = [
        d
        async for d in router.forward_to_agent_stream(
            target=target,
            sanitized_content="count to two",
            ledger_id="test-id",
            metadata={"source": "api"},
        )
    ]

    assert deltas == ["One", ".", " Two."]


@pytest.mark.asyncio
async def test_stream_payload_sets_stream_true(router, monkeypatch):
    captured = {}

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        captured["json"] = json
        yield _mock_stream_response(_sse_lines([]))

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    async for _ in router.forward_to_agent_stream(
        target=target,
        sanitized_content="hi",
        ledger_id="test-id",
        metadata={"source": "api"},
    ):
        pass

    assert captured["json"]["stream"] is True


@pytest.mark.asyncio
async def test_stream_rejects_non_openai_compat_target(router):
    target = AgentTarget(
        name="openclaw",
        url="http://agentshroud-openclaw:18789",
        chat_path="/chat",
    )

    with pytest.raises(ForwardError, match="no streaming-compatible chat_path"):
        async for _ in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        ):
            pass


@pytest.mark.asyncio
async def test_stream_raises_forward_error_on_connect_failure(router, monkeypatch):
    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        raise httpx.ConnectError("refused")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    with pytest.raises(ForwardError, match="offline"):
        async for _ in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        ):
            pass


@pytest.mark.asyncio
async def test_stream_raises_forward_error_on_malformed_json(router, monkeypatch):
    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        yield _mock_stream_response(["data: {not valid json", "data: [DONE]"])

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    with pytest.raises(ForwardError, match="Malformed SSE chunk"):
        async for _ in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        ):
            pass


@pytest.mark.asyncio
async def test_stream_skips_chunk_missing_choices_key_and_continues(router, monkeypatch):
    """Live regression 2026-08-07: Hermes's own internal LLM failover
    (Anthropic credit-balance exhaustion → local model unavailable → OpenAI
    fallback) injects a non-content status chunk mid-stream with no
    'choices' key. Treating that as fatal killed the ENTIRE reply ("second
    request no response") even though real content followed it in the same
    stream. A malformed-SHAPE chunk (valid JSON, wrong shape) must be
    skipped, not fatal — unlike genuinely invalid JSON, which stays fatal."""
    import json

    lines = [
        f"data: {json.dumps({'choices': [{'delta': {'content': 'Before.'}}]})}",
        f"data: {json.dumps({'status': 'failover'})}",  # no 'choices' key
        f"data: {json.dumps({'choices': [{'delta': {'content': ' After.'}}]})}",
        "data: [DONE]",
    ]

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        yield _mock_stream_response(lines)

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    received = [
        chunk
        async for chunk in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        )
    ]

    assert received == ["Before.", " After."], (
        "malformed-shape chunk must be skipped, not abort the stream: "
        f"{received!r}"
    )


@pytest.mark.asyncio
async def test_stream_raises_forward_error_on_http_status_error(router, monkeypatch):
    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        resp = _mock_stream_response([], status_code=401)
        resp.raise_for_status = MagicMock(
            side_effect=httpx.HTTPStatusError(
                "401", request=MagicMock(), response=MagicMock(status_code=401, text="bad key")
            )
        )
        yield resp

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    with pytest.raises(ForwardError, match="returned error"):
        async for _ in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        ):
            pass


@pytest.mark.asyncio
async def test_stream_ignores_lines_without_data_prefix(router, monkeypatch):
    lines = [
        "",
        ": comment",
        'data: {"choices": [{"delta": {"content": "Hi"}, "finish_reason": null}]}',
        "data: [DONE]",
    ]

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kwargs):
        yield _mock_stream_response(lines)

    monkeypatch.setattr(httpx.AsyncClient, "stream", mock_stream)

    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
    )

    deltas = [
        d
        async for d in router.forward_to_agent_stream(
            target=target,
            sanitized_content="hi",
            ledger_id="test-id",
            metadata={"source": "api"},
        )
    ]
    assert deltas == ["Hi"]
