# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""RateLimitGuard — adaptive per-agent / per-tool request throttling (SCRUM-68 WS-B.1).

Existing coverage and the gap this fills:
    * ``resource_guard.check_resource("requests")`` is a coarse *per-agent* total
      request counter with a single fixed limit, no tool granularity, and no
      spike detection; it is not wired into the inbound message pipeline.
    * ``egress_monitor`` counts *outbound egress events per channel per hour* in
      monitor mode; it is not a request-side (inbound) rate limiter and does not
      block.

RateLimitGuard closes the request-side gap: it bounds how fast a single agent may
invoke a *specific tool/action* using two independent sliding windows —

    1. a **sustained** window (e.g. N calls / 60 s) that caps steady-state rate, and
    2. a short **burst** window (e.g. B calls / 1 s) that catches spikes indicative
       of a compromised or runaway agent hammering one tool.

Design constraints (CLAUDE.md):
    * Config-gated, **default-safe**: ``enabled=False`` is a pure passthrough that
      never blocks and leaves the pipeline behaviour identical.
    * **Fail-closed**: any internal error yields a BLOCK decision, never a silent
      allow — an availability guard that fails open is theater.
    * Deterministic: a ``clock`` callable is injectable so tests need no real sleeps.

IEC 62443 alignment: FR7 (Resource Availability, SL2) — bounds the request rate
an agent can sustain against any single control, limiting denial-of-service and
runaway-loop blast radius.
"""

import logging
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Callable, Deque, Optional

logger = logging.getLogger("agentshroud.security.rate_limit_guard")


@dataclass
class RateLimitConfig:
    """Configuration for :class:`RateLimitGuard`.

    All windows are per (agent_id, tool) pair. ``per_tool_sustained_limit`` and
    ``per_tool_burst_limit`` override the defaults for named tools, so
    high-risk actions (e.g. ``delete_file``) can be throttled harder.
    """

    enabled: bool = False
    # Sustained sliding window.
    sustained_limit: int = 60
    sustained_window_s: float = 60.0
    # Short burst/spike window.
    burst_limit: int = 15
    burst_window_s: float = 1.0
    # Per-tool overrides.
    per_tool_sustained_limit: dict[str, int] = field(default_factory=dict)
    per_tool_burst_limit: dict[str, int] = field(default_factory=dict)


@dataclass
class RateLimitDecision:
    """Structured verdict returned by :meth:`RateLimitGuard.check`."""

    allowed: bool
    blocked: bool
    reason_code: str  # "allowed" | "sustained_rate_exceeded" | "burst_detected" | "disabled" | "guard_error"  # noqa: E501
    reason: str = ""
    agent_id: str = ""
    tool: str = ""
    sustained_count: int = 0
    burst_count: int = 0


class RateLimitGuard:
    """Adaptive per-agent / per-tool sliding-window rate limiter with burst detection."""

    def __init__(
        self,
        config: Optional[RateLimitConfig] = None,
        clock: Callable[[], float] | None = None,
    ):
        self.config = config or RateLimitConfig()
        # Injectable monotonic-ish clock for deterministic tests.
        if clock is not None:
            self._now = clock
        else:
            import time

            self._now = time.monotonic
        # (agent_id, tool) -> deque[timestamp]; a single deque serves both
        # windows since the burst window is a subset of the sustained window.
        self._windows: dict[tuple[str, str], Deque[float]] = defaultdict(deque)
        self._stats: dict[str, int] = defaultdict(int)

    # ------------------------------------------------------------------
    def _sustained_limit(self, tool: str) -> int:
        return self.config.per_tool_sustained_limit.get(tool, self.config.sustained_limit)

    def _burst_limit(self, tool: str) -> int:
        return self.config.per_tool_burst_limit.get(tool, self.config.burst_limit)

    # ------------------------------------------------------------------
    def check(self, agent_id: str, tool: str) -> RateLimitDecision:
        """Record one request for (agent_id, tool) and decide allow/block.

        Fail-closed: on any unexpected error the request is BLOCKED.
        """
        self._stats["checks_total"] += 1

        if not self.config.enabled:
            return RateLimitDecision(
                allowed=True,
                blocked=False,
                reason_code="disabled",
                agent_id=agent_id,
                tool=tool,
            )

        try:
            now = self._now()
            key = (agent_id, tool)
            window = self._windows[key]

            sustained_window_s = self.config.sustained_window_s
            burst_window_s = self.config.burst_window_s

            # Evict timestamps older than the (larger) sustained window.
            cutoff = now - sustained_window_s
            while window and window[0] <= cutoff:
                window.popleft()

            sustained_count = len(window)
            burst_cutoff = now - burst_window_s
            burst_count = sum(1 for ts in window if ts > burst_cutoff)

            # Burst check first — a spike is the more urgent signal.
            burst_limit = self._burst_limit(tool)
            if burst_count >= burst_limit:
                self._stats["blocked_total"] += 1
                self._stats["burst_blocks"] += 1
                logger.warning(
                    "RateLimitGuard: burst detected agent=%s tool=%s (%d in %.2gs, limit=%d)",
                    agent_id,
                    tool,
                    burst_count,
                    burst_window_s,
                    burst_limit,
                )
                return RateLimitDecision(
                    allowed=False,
                    blocked=True,
                    reason_code="burst_detected",
                    reason=(
                        f"Burst detected for tool '{tool}': {burst_count} calls in "
                        f"{burst_window_s:g}s (limit {burst_limit})"
                    ),
                    agent_id=agent_id,
                    tool=tool,
                    sustained_count=sustained_count,
                    burst_count=burst_count,
                )

            sustained_limit = self._sustained_limit(tool)
            if sustained_count >= sustained_limit:
                self._stats["blocked_total"] += 1
                self._stats["sustained_blocks"] += 1
                logger.warning(
                    "RateLimitGuard: sustained rate exceeded agent=%s tool=%s (%d in %.4gs, limit=%d)",  # noqa: E501
                    agent_id,
                    tool,
                    sustained_count,
                    sustained_window_s,
                    sustained_limit,
                )
                return RateLimitDecision(
                    allowed=False,
                    blocked=True,
                    reason_code="sustained_rate_exceeded",
                    reason=(
                        f"Sustained rate exceeded for tool '{tool}': {sustained_count} calls in "
                        f"{sustained_window_s:g}s (limit {sustained_limit})"
                    ),
                    agent_id=agent_id,
                    tool=tool,
                    sustained_count=sustained_count,
                    burst_count=burst_count,
                )

            # Allowed — record this request.
            window.append(now)
            return RateLimitDecision(
                allowed=True,
                blocked=False,
                reason_code="allowed",
                agent_id=agent_id,
                tool=tool,
                sustained_count=sustained_count + 1,
                burst_count=burst_count + 1,
            )
        except Exception as exc:  # fail-closed — never silently allow on error
            self._stats["errors"] += 1
            logger.error("RateLimitGuard internal error (failing closed): %s", exc)
            return RateLimitDecision(
                allowed=False,
                blocked=True,
                reason_code="guard_error",
                reason=f"RateLimitGuard internal error: {exc}",
                agent_id=agent_id,
                tool=tool,
            )

    # ------------------------------------------------------------------
    def get_stats(self) -> dict[str, int]:
        return dict(self._stats)
