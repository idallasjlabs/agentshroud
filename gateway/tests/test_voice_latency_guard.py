# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""SCRUM-56 — Hermes voice-turn latency guard.

Covers the two config-gated mitigations added to the voice /forward path:

  (1) MEASURE  — _record_turn_latency: emits a structured latency record and
      flags outliers above a soft threshold; wired into _call_agent (success
      path AND read-timeout path).
  (2) FIX      — _voice_forward_metadata: builds the ephemeral "no_memory" tag,
      DEFAULT OFF (empty metadata → forwarded request unchanged), ON only when
      VG_VOICE_NO_MEMORY is enabled.  _call_agent attaches it to the /forward body.

All I/O is mocked — no real network, no sleep, no DB.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import voice_gateway.server as srv
from voice_gateway.server import _call_agent, _record_turn_latency, _voice_forward_metadata


def _forward_resp(agent_response: str, status: int = 201):
    """Mock httpx response with a ForwardResponse-shape body."""
    mock = MagicMock()
    mock.status_code = status
    mock.json = MagicMock(
        return_value={
            "id": "abc123",
            "sanitized": False,
            "redactions": [],
            "redaction_count": 0,
            "content_hash": "deadbeef",
            "forwarded_to": "hermes",
            "timestamp": "2026-07-14T00:00:00Z",
            "agent_response": agent_response,
        }
    )
    mock.raise_for_status = MagicMock()
    return mock


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


# ── Integration: _call_agent wiring ───────────────────────────────────────────


@pytest.mark.asyncio
async def test_call_agent_default_body_has_no_metadata(monkeypatch):
    """DEFAULT OFF: /forward body carries NO metadata key — byte-for-byte legacy."""
    monkeypatch.setattr(srv, "_VOICE_NO_MEMORY", False)
    captured: dict = {}

    async def _capture(url, json=None, headers=None, **kw):
        captured["body"] = json or {}
        return _forward_resp("ok")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        await _call_agent("test query", "hermes")

    assert "metadata" not in captured["body"], "default path must not add metadata"


@pytest.mark.asyncio
async def test_call_agent_no_memory_on_adds_ephemeral_tag(monkeypatch):
    """ON: /forward body carries metadata={"no_memory": True}."""
    monkeypatch.setattr(srv, "_VOICE_NO_MEMORY", True)
    captured: dict = {}

    async def _capture(url, json=None, headers=None, **kw):
        captured["body"] = json or {}
        return _forward_resp("ok")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        await _call_agent("test query", "hermes")

    assert captured["body"].get("metadata") == {"no_memory": True}
    # Core fields untouched.
    assert captured["body"]["content"] == "test query"
    assert captured["body"]["route_to"] == "hermes"


@pytest.mark.asyncio
async def test_call_agent_records_latency_on_success():
    """_call_agent emits a latency record on the success path."""
    with (
        patch.object(srv, "_record_turn_latency") as rec,
        patch("httpx.AsyncClient.post", new=AsyncMock(return_value=_forward_resp("hi"))),
    ):
        await _call_agent("q", "hermes")
    rec.assert_called_once()
    # Signature: (agent, duration_s)
    args = rec.call_args.args
    assert args[0] == "hermes"
    assert isinstance(args[1], float) and args[1] >= 0.0


@pytest.mark.asyncio
async def test_call_agent_records_latency_on_read_timeout():
    """A read-timeout (worst-case latency) is still recorded, then falls back."""
    import httpx

    with (
        patch.object(srv, "_record_turn_latency") as rec,
        patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=httpx.ReadTimeout("boom"))),
    ):
        result = await _call_agent("q", "hermes")

    rec.assert_called_once()
    assert rec.call_args.args[0] == "hermes"
    assert "trouble connecting" in result
