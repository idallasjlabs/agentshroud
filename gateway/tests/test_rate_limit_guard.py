# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for RateLimitGuard — SCRUM-68 WS-B.1 deep-hardening module.

Adaptive per-agent / per-tool request throttling with burst detection.
IEC 62443 FR7 (Resource Availability): bounds the request rate an agent can
sustain against any single tool, and detects short-window bursts that indicate
a compromised or runaway agent.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from gateway.security.rate_limit_guard import (
    RateLimitConfig,
    RateLimitGuard,
)


# ---------------------------------------------------------------------------
# Deterministic clock — no real sleeps (CLAUDE.md test-quality rule).
# ---------------------------------------------------------------------------
class FakeClock:
    def __init__(self, start: float = 1000.0):
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


@pytest.fixture
def clock():
    return FakeClock()


# ---------------------------------------------------------------------------
# Sustained-rate limiting
# ---------------------------------------------------------------------------
def test_under_limit_allows(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=5, sustained_window_s=60),
        clock=clock,
    )
    for _ in range(5):
        decision = guard.check("agent-1", "read_file")
        assert decision.allowed is True
        assert decision.blocked is False


def test_sustained_limit_blocks_on_overflow(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=3, sustained_window_s=60),
        clock=clock,
    )
    for _ in range(3):
        assert guard.check("agent-1", "read_file").allowed is True
    decision = guard.check("agent-1", "read_file")
    assert decision.allowed is False
    assert decision.blocked is True
    assert decision.reason_code == "sustained_rate_exceeded"
    assert "read_file" in decision.reason


def test_window_slides_and_allows_again(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=2, sustained_window_s=60),
        clock=clock,
    )
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is False
    # After the window fully passes, the counter resets.
    clock.advance(61)
    assert guard.check("agent-1", "read_file").allowed is True


# ---------------------------------------------------------------------------
# Per-tool and per-agent isolation
# ---------------------------------------------------------------------------
def test_limits_are_per_tool(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=2, sustained_window_s=60),
        clock=clock,
    )
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is False
    # A different tool has its own independent budget.
    assert guard.check("agent-1", "delete_file").allowed is True


def test_limits_are_per_agent(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=1, sustained_window_s=60),
        clock=clock,
    )
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is False
    # A different agent is unaffected.
    assert guard.check("agent-2", "read_file").allowed is True


def test_per_tool_override(clock):
    guard = RateLimitGuard(
        RateLimitConfig(
            enabled=True,
            sustained_limit=100,
            sustained_window_s=60,
            burst_limit=100,
            burst_window_s=1,
            per_tool_sustained_limit={"delete_file": 2},
        ),
        clock=clock,
    )
    assert guard.check("agent-1", "delete_file").allowed is True
    assert guard.check("agent-1", "delete_file").allowed is True
    assert guard.check("agent-1", "delete_file").allowed is False
    # read_file still uses the generous default.
    for _ in range(50):
        assert guard.check("agent-1", "read_file").allowed is True


# ---------------------------------------------------------------------------
# Burst / spike detection (short window)
# ---------------------------------------------------------------------------
def test_burst_detection_blocks(clock):
    guard = RateLimitGuard(
        RateLimitConfig(
            enabled=True,
            sustained_limit=1000,
            sustained_window_s=3600,
            burst_limit=3,
            burst_window_s=1,
        ),
        clock=clock,
    )
    # 3 in the same instant is allowed; the 4th within the burst window blocks.
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    decision = guard.check("agent-1", "read_file")
    assert decision.allowed is False
    assert decision.reason_code == "burst_detected"


def test_burst_clears_after_burst_window(clock):
    guard = RateLimitGuard(
        RateLimitConfig(
            enabled=True,
            sustained_limit=1000,
            sustained_window_s=3600,
            burst_limit=2,
            burst_window_s=1,
        ),
        clock=clock,
    )
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is False  # burst
    clock.advance(1.1)  # burst window passes
    assert guard.check("agent-1", "read_file").allowed is True


# ---------------------------------------------------------------------------
# Config-off = unchanged (default-safe passthrough)
# ---------------------------------------------------------------------------
def test_disabled_never_blocks(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=False, sustained_limit=1, sustained_window_s=60, burst_limit=1),
        clock=clock,
    )
    for _ in range(100):
        decision = guard.check("agent-1", "read_file")
        assert decision.allowed is True
        assert decision.blocked is False
    assert decision.reason_code == "disabled"


# ---------------------------------------------------------------------------
# Fail-closed on malformed internal state
# ---------------------------------------------------------------------------
def test_fail_closed_on_internal_error(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=5, sustained_window_s=60),
        clock=clock,
    )

    # Corrupt the internal store so the counter path raises.
    class Boom(dict):
        def __getitem__(self, k):
            raise RuntimeError("corrupt store")

    guard._windows = Boom()
    decision = guard.check("agent-1", "read_file")
    assert decision.allowed is False
    assert decision.blocked is True
    assert decision.reason_code == "guard_error"


def test_default_clock_is_monotonic():
    """No injected clock: the guard falls back to time.monotonic and still works."""
    guard = RateLimitGuard(RateLimitConfig(enabled=True, sustained_limit=2, sustained_window_s=60))
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is True
    assert guard.check("agent-1", "read_file").allowed is False


def test_stats_counts_blocks(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=1, sustained_window_s=60),
        clock=clock,
    )
    guard.check("agent-1", "read_file")
    guard.check("agent-1", "read_file")  # blocked
    stats = guard.get_stats()
    assert stats["checks_total"] == 2
    assert stats["blocked_total"] == 1


# ---------------------------------------------------------------------------
# Pipeline wiring — a blocked case must actually block (downstream unreached).
# ---------------------------------------------------------------------------
def _make_pipeline(rate_limit_guard, clock):
    """Build a SecurityPipeline with only the guards needed to exercise the
    RateLimitGuard step, plus tracking mocks proving downstream is not reached."""
    from gateway.proxy.pipeline import SecurityPipeline

    pii = MagicMock()
    pii.filter_xml_blocks = MagicMock(return_value=("msg", False))
    pii.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="msg", entity_types_found=[], redactions=[])
    )
    # trust_manager stands in for "downstream" — it must NOT be reached on block.
    trust = MagicMock()
    trust.is_action_allowed = MagicMock(return_value=True)
    trust.get_trust = MagicMock(return_value=(3, "ok"))
    pipeline = SecurityPipeline(
        pii_sanitizer=pii,
        trust_manager=trust,
        rate_limit_guard=rate_limit_guard,
    )
    return pipeline, trust


@pytest.mark.asyncio
async def test_pipeline_blocks_and_downstream_not_reached(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=True, sustained_limit=1, sustained_window_s=60),
        clock=clock,
    )
    pipeline, trust = _make_pipeline(guard, clock)

    first = await pipeline.process_inbound("hi", agent_id="a1", action="read_file")
    assert first.blocked is False
    # trust check reached on the allowed request
    assert trust.is_action_allowed.call_count == 1

    second = await pipeline.process_inbound("hi again", agent_id="a1", action="read_file")
    assert second.blocked is True
    assert second.block_reason.startswith("RateLimitGuard")
    # Downstream (trust_manager) MUST NOT be reached again on the blocked request.
    assert trust.is_action_allowed.call_count == 1


@pytest.mark.asyncio
async def test_pipeline_disabled_guard_passthrough(clock):
    guard = RateLimitGuard(
        RateLimitConfig(enabled=False, sustained_limit=1, sustained_window_s=60),
        clock=clock,
    )
    pipeline, trust = _make_pipeline(guard, clock)
    for _ in range(5):
        res = await pipeline.process_inbound("hi", agent_id="a1", action="read_file")
        assert res.blocked is False
    assert trust.is_action_allowed.call_count == 5


@pytest.mark.asyncio
async def test_pipeline_no_guard_is_unchanged(clock):
    """config-off equivalence: absent guard leaves inbound behaviour identical."""
    from gateway.proxy.pipeline import SecurityPipeline

    pii = MagicMock()
    pii.filter_xml_blocks = MagicMock(return_value=("msg", False))
    pii.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="msg", entity_types_found=[], redactions=[])
    )
    pipeline = SecurityPipeline(pii_sanitizer=pii)  # no rate_limit_guard kwarg
    res = await pipeline.process_inbound("hi", agent_id="a1", action="read_file")
    assert res.blocked is False
