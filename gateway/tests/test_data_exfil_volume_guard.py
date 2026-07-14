# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for DataExfilVolumeGuard — SCRUM-68 WS-B.1 deep-hardening module.

Cumulative outbound byte-volume anomaly detection per session. Complements the
domain-based EgressFilter (which decides *where* data may go) and the
event-count EgressMonitor (which counts events/channel/hour, monitor-only) with
a *how much* dimension: it blocks a session whose cumulative outbound volume, or
a single response, exceeds an adaptive baseline — the classic slow-and-fast
exfiltration signal.

IEC 62443 FR3 (System Integrity) / FR4 (Data Confidentiality): bounds the volume
of data that can leave the gateway per session before a human is in the loop.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from gateway.security.data_exfil_volume_guard import (
    DataExfilVolumeConfig,
    DataExfilVolumeGuard,
)


# ---------------------------------------------------------------------------
# Single-response hard cap
# ---------------------------------------------------------------------------
def test_under_single_cap_allows():
    guard = DataExfilVolumeGuard(DataExfilVolumeConfig(enabled=True, max_single_response_bytes=100))
    verdict = guard.observe("sess-1", b"x" * 50)
    assert verdict.allowed is True
    assert verdict.blocked is False
    assert verdict.reason_code == "ok"


def test_single_response_over_cap_blocks():
    guard = DataExfilVolumeGuard(DataExfilVolumeConfig(enabled=True, max_single_response_bytes=100))
    verdict = guard.observe("sess-1", b"x" * 250)
    assert verdict.allowed is False
    assert verdict.blocked is True
    assert verdict.reason_code == "single_response_exceeded"
    assert verdict.response_bytes == 250


def test_accepts_str_and_bytes():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(enabled=True, max_single_response_bytes=1000)
    )
    v1 = guard.observe("sess-1", "hello")  # str
    v2 = guard.observe("sess-1", b"hello")  # bytes
    assert v1.response_bytes == 5
    assert v2.response_bytes == 5


# ---------------------------------------------------------------------------
# Cumulative per-session cap
# ---------------------------------------------------------------------------
def test_cumulative_cap_blocks_when_crossed():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000,
            max_session_cumulative_bytes=100,
        )
    )
    assert guard.observe("sess-1", b"x" * 60).allowed is True
    # Second response pushes cumulative over 100.
    verdict = guard.observe("sess-1", b"x" * 60)
    assert verdict.blocked is True
    assert verdict.reason_code == "session_cumulative_exceeded"
    assert verdict.cumulative_bytes == 120


def test_cumulative_is_per_session():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000,
            max_session_cumulative_bytes=100,
        )
    )
    assert guard.observe("sess-1", b"x" * 90).allowed is True
    # Different session has its own budget.
    assert guard.observe("sess-2", b"x" * 90).allowed is True


def test_blocked_response_does_not_add_to_cumulative():
    """A blocked (undelivered) response must not consume the session budget,
    otherwise one oversized attempt would wedge the whole session."""
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=50,
            max_session_cumulative_bytes=1000,
        )
    )
    # This is blocked on the single-response cap; it must not count.
    assert guard.observe("sess-1", b"x" * 200).blocked is True
    # Cumulative is still 0, so a normal response proceeds.
    v = guard.observe("sess-1", b"x" * 40)
    assert v.allowed is True
    assert v.cumulative_bytes == 40


# ---------------------------------------------------------------------------
# Adaptive baseline — spike relative to rolling mean
# ---------------------------------------------------------------------------
def test_adaptive_spike_blocks():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000_000,
            max_session_cumulative_bytes=10_000_000,
            adaptive_enabled=True,
            adaptive_multiplier=3.0,
            adaptive_min_samples=3,
            adaptive_floor_bytes=100,
        )
    )
    # Establish a baseline of ~100-byte responses.
    for _ in range(4):
        assert guard.observe("sess-1", b"x" * 100).allowed is True
    # A 10x spike over the baseline blocks.
    verdict = guard.observe("sess-1", b"x" * 1000)
    assert verdict.blocked is True
    assert verdict.reason_code == "adaptive_spike"


def test_adaptive_needs_min_samples():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000_000,
            max_session_cumulative_bytes=10_000_000,
            adaptive_enabled=True,
            adaptive_multiplier=2.0,
            adaptive_min_samples=5,
            adaptive_floor_bytes=10,
        )
    )
    # Fewer than min_samples: a big response is NOT flagged as a spike yet.
    guard.observe("sess-1", b"x" * 10)
    verdict = guard.observe("sess-1", b"x" * 10_000)
    assert verdict.blocked is False


def test_adaptive_floor_prevents_noise_blocks():
    """Tiny baselines must not turn ordinary small growth into spikes."""
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000_000,
            max_session_cumulative_bytes=10_000_000,
            adaptive_enabled=True,
            adaptive_multiplier=2.0,
            adaptive_min_samples=2,
            adaptive_floor_bytes=5000,
        )
    )
    for _ in range(3):
        guard.observe("sess-1", b"x" * 10)
    # 200 bytes is 20x the 10-byte baseline, but below the 5000-byte floor.
    assert guard.observe("sess-1", b"x" * 200).blocked is False


# ---------------------------------------------------------------------------
# Config-off = unchanged
# ---------------------------------------------------------------------------
def test_disabled_never_blocks():
    guard = DataExfilVolumeGuard(DataExfilVolumeConfig(enabled=False, max_single_response_bytes=1))
    verdict = guard.observe("sess-1", b"x" * 10_000_000)
    assert verdict.allowed is True
    assert verdict.blocked is False
    assert verdict.reason_code == "disabled"


def test_get_stats():
    guard = DataExfilVolumeGuard(DataExfilVolumeConfig(enabled=True, max_single_response_bytes=50))
    guard.observe("sess-1", b"x" * 10)
    guard.observe("sess-1", b"x" * 200)  # blocked
    stats = guard.get_stats()
    assert stats["observations_total"] == 2
    assert stats["blocked_total"] == 1


def test_adaptive_window_bounds_baseline_memory():
    """The rolling baseline deque is trimmed to adaptive_window; old samples drop."""
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000_000,
            max_session_cumulative_bytes=10_000_000,
            adaptive_enabled=True,
            adaptive_min_samples=2,
            adaptive_window=3,
            adaptive_floor_bytes=1,
            adaptive_multiplier=100.0,
        )
    )
    for _ in range(10):
        assert guard.observe("sess-1", b"x" * 100).allowed is True
    # Only the last `adaptive_window` (3) samples are retained.
    assert len(guard._sessions["sess-1"].recent) == 3


def test_reset_session_clears_state():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(
            enabled=True,
            max_single_response_bytes=10_000,
            max_session_cumulative_bytes=100,
        )
    )
    assert guard.observe("sess-1", b"x" * 90).allowed is True
    guard.reset_session("sess-1")
    # Budget is fresh after reset.
    assert guard.observe("sess-1", b"x" * 90).allowed is True


# ---------------------------------------------------------------------------
# Pipeline wiring — a blocked case must actually block (delivery replaced).
# ---------------------------------------------------------------------------
def _make_pipeline(volume_guard):
    from gateway.proxy.pipeline import SecurityPipeline

    pii = MagicMock()
    pii.filter_xml_blocks = MagicMock(return_value=("msg", False))
    pii.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="msg", entity_types_found=[], redactions=[])
    )
    # envelope_signer stands in for the downstream (post-volume) stage; it must
    # NOT be reached when the volume guard blocks.
    envelope = MagicMock()
    envelope.sign = MagicMock(
        return_value=MagicMock(instruction_id="e1", signature="s", timestamp=1.0)
    )
    pipeline = SecurityPipeline(
        pii_sanitizer=pii,
        data_exfil_volume_guard=volume_guard,
        envelope_signer=envelope,
    )
    return pipeline, envelope


@pytest.mark.asyncio
async def test_pipeline_blocks_and_downstream_not_reached():
    guard = DataExfilVolumeGuard(DataExfilVolumeConfig(enabled=True, max_single_response_bytes=2))
    pipeline, envelope = _make_pipeline(guard)
    result = await pipeline.process_outbound(
        "this is a long response", agent_id="a1", metadata={"session_id": "s1"}
    )
    assert result.blocked is True
    assert result.block_reason.startswith("DataExfilVolumeGuard")
    # Downstream envelope signing MUST NOT run on a blocked response.
    envelope.sign.assert_not_called()


@pytest.mark.asyncio
async def test_pipeline_allows_small_response():
    guard = DataExfilVolumeGuard(
        DataExfilVolumeConfig(enabled=True, max_single_response_bytes=10_000)
    )
    # pii returns the message unchanged (len 3)
    pipeline, envelope = _make_pipeline(guard)
    pipeline.pii_sanitizer.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="msg", entity_types_found=[], redactions=[])
    )
    result = await pipeline.process_outbound("msg", agent_id="a1")
    assert result.blocked is False


@pytest.mark.asyncio
async def test_pipeline_fail_closed_for_non_owner_on_error():
    """If the guard raises, non-owner outbound is blocked (fail-closed)."""
    guard = MagicMock()
    guard.observe = MagicMock(side_effect=RuntimeError("boom"))
    pipeline, envelope = _make_pipeline(guard)
    result = await pipeline.process_outbound("msg", agent_id="a1")
    assert result.blocked is True
    assert "DataExfilVolumeGuard" in result.block_reason
    envelope.sign.assert_not_called()


@pytest.mark.asyncio
async def test_pipeline_no_guard_is_unchanged():
    from gateway.proxy.pipeline import SecurityPipeline

    pii = MagicMock()
    pii.filter_xml_blocks = MagicMock(return_value=("msg", False))
    pii.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="msg", entity_types_found=[], redactions=[])
    )
    pipeline = SecurityPipeline(pii_sanitizer=pii)  # no data_exfil_volume_guard
    result = await pipeline.process_outbound("msg", agent_id="a1")
    assert result.blocked is False
