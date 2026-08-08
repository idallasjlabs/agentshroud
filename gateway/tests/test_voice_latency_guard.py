# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""SCRUM-56 — Hermes voice-turn latency guard.

Covers the two config-gated mitigations added to the voice /forward path:

  (1) MEASURE  — _record_turn_latency: emits a structured latency record and
      flags outliers above a soft threshold; wired into _call_agent_stream
      (success path AND read-timeout path).
  (2) FIX      — _voice_forward_metadata: builds the ephemeral "no_memory" tag,
      DEFAULT OFF (empty metadata → forwarded request unchanged), ON only when
      VG_VOICE_NO_MEMORY is enabled.  _call_agent_stream attaches it to the
      /forward/stream body.

All I/O is mocked — no real network, no sleep, no DB.
"""

from __future__ import annotations

import json
from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import voice_gateway.server as srv
from voice_gateway.server import _call_agent_stream, _record_turn_latency, _voice_forward_metadata


def _sse_body(events: list[dict]) -> list[str]:
    return [f"data: {json.dumps(e)}" for e in events]


def _mock_stream_resp(lines: list[str], status_code: int = 200):
    """Mock httpx.Response usable as the yield value of a mocked
    AsyncClient.stream() async context manager."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.raise_for_status = MagicMock()

    async def _aiter_lines():
        for line in lines:
            yield line

    resp.aiter_lines = _aiter_lines
    return resp


# ── (1) MEASURE: _record_turn_latency ─────────────────────────────────────────


def test_record_turn_latency_normal_not_outlier():
    """A turn under the soft threshold is recorded as a non-outlier."""
    rec = _record_turn_latency("hermes", 5.0, soft_threshold_s=30.0)
    assert rec["event"] == "voice_turn_latency"
    assert rec["agent"] == "hermes"
    assert rec["duration_s"] == 5.0
    assert rec["soft_threshold_s"] == 30.0
    assert rec["outlier"] is False


def test_record_turn_latency_over_threshold_is_outlier():
    """A turn exceeding the soft threshold is flagged as an outlier."""
    rec = _record_turn_latency("hermes", 73.4, soft_threshold_s=30.0)
    assert rec["outlier"] is True
    assert rec["duration_s"] == 73.4


def test_record_turn_latency_boundary_is_not_outlier():
    """Exactly at the threshold is NOT an outlier (strict >, not >=)."""
    rec = _record_turn_latency("hermes", 30.0, soft_threshold_s=30.0)
    assert rec["outlier"] is False


def test_record_turn_latency_outlier_logs_warning():
    """Outliers log at WARNING; normal turns do not."""
    with patch.object(srv.logger, "warning") as warn, patch.object(srv.logger, "info") as info:
        _record_turn_latency("hermes", 99.0, soft_threshold_s=30.0)
    warn.assert_called_once()
    info.assert_not_called()


def test_record_turn_latency_normal_logs_info():
    """Normal (sub-threshold) turns log at INFO, not WARNING."""
    with patch.object(srv.logger, "warning") as warn, patch.object(srv.logger, "info") as info:
        _record_turn_latency("hermes", 2.0, soft_threshold_s=30.0)
    info.assert_called_once()
    warn.assert_not_called()


def test_record_turn_latency_default_threshold_from_module():
    """When soft_threshold_s is omitted it is read from the module config at call time."""
    with patch.object(srv, "_VOICE_TURN_SOFT_LATENCY_S", 10.0):
        rec = _record_turn_latency("hermes", 11.0)
    assert rec["outlier"] is True
    assert rec["soft_threshold_s"] == 10.0


# ── (2) FIX: _voice_forward_metadata gating ───────────────────────────────────


def test_voice_forward_metadata_default_off_is_empty():
    """DEFAULT OFF: no_memory=False → empty metadata (request unchanged)."""
    assert _voice_forward_metadata(no_memory=False) == {}


def test_voice_forward_metadata_on_sets_no_memory_tag():
    """ON: no_memory=True → {"no_memory": True} ephemeral tag."""
    assert _voice_forward_metadata(no_memory=True) == {"no_memory": True}


def test_voice_forward_metadata_module_default_is_off():
    """The module-level default flag is OFF unless VG_VOICE_NO_MEMORY is set."""
    # Guard the shipped default: the flag must evaluate falsey by default.
    assert srv._voice_forward_metadata() == {}
    assert srv._VOICE_NO_MEMORY is False


# ── Integration: _call_agent_stream wiring ────────────────────────────────────


@pytest.mark.asyncio
async def test_call_agent_default_body_has_no_metadata(monkeypatch):
    """DEFAULT OFF: /forward/stream body carries NO metadata key — byte-for-byte legacy."""
    monkeypatch.setattr(srv, "_VOICE_NO_MEMORY", False)
    captured: dict = {}

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        captured["body"] = json or {}
        yield _mock_stream_resp(_sse_body([{"done": True}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        async for _ in _call_agent_stream("test query", "hermes"):
            pass

    assert "metadata" not in captured["body"], "default path must not add metadata"


@pytest.mark.asyncio
async def test_call_agent_no_memory_on_adds_ephemeral_tag(monkeypatch):
    """ON: /forward/stream body carries metadata={"no_memory": True}."""
    monkeypatch.setattr(srv, "_VOICE_NO_MEMORY", True)
    captured: dict = {}

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        captured["body"] = json or {}
        yield _mock_stream_resp(_sse_body([{"done": True}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        async for _ in _call_agent_stream("test query", "hermes"):
            pass

    assert captured["body"].get("metadata") == {"no_memory": True}
    # Core fields untouched.
    assert captured["body"]["content"] == "test query"
    assert captured["body"]["route_to"] == "hermes"


@pytest.mark.asyncio
async def test_call_agent_records_latency_on_success():
    """_call_agent_stream emits a latency record on the success path."""

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(_sse_body([{"sentence": "hi"}, {"done": True}]))

    with (
        patch.object(srv, "_record_turn_latency") as rec,
        patch("httpx.AsyncClient.stream", new=mock_stream),
    ):
        async for _ in _call_agent_stream("q", "hermes"):
            pass
    rec.assert_called_once()
    # Signature: (agent, duration_s)
    args = rec.call_args.args
    assert args[0] == "hermes"
    assert isinstance(args[1], float) and args[1] >= 0.0


@pytest.mark.asyncio
async def test_call_agent_records_latency_on_read_timeout():
    """A read-timeout (worst-case latency) is still recorded, then falls back."""
    import httpx

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        raise httpx.ReadTimeout("boom")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    with (
        patch.object(srv, "_record_turn_latency") as rec,
        patch("httpx.AsyncClient.stream", new=mock_stream),
    ):
        result = [s async for s in _call_agent_stream("q", "hermes")]

    rec.assert_called_once()
    assert rec.call_args.args[0] == "hermes"
    assert len(result) == 1
    assert "trouble connecting" in result[0]
