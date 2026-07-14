# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""DataExfilVolumeGuard — cumulative outbound data-volume anomaly guard (SCRUM-68 WS-B.1).

Existing coverage and the gap this fills:
    * ``egress_filter`` is *domain-based*: it decides **where** data may go, not
      **how much**.
    * ``egress_monitor`` counts *events per channel per hour* in monitor mode and
      flags individually large events, but keeps no cumulative per-session byte
      budget and is not wired into the outbound response pipeline.

DataExfilVolumeGuard adds the missing volume dimension to the outbound pipeline:

    1. **Single-response cap** — hard ceiling on the size of any one response.
    2. **Cumulative session cap** — total bytes a session may emit before a human
       is in the loop (defeats slow-drip exfiltration that stays under any single
       cap but adds up).
    3. **Adaptive spike detection** — a response far above the session's own
       rolling baseline (mean of recent responses) is flagged, catching a sudden
       fast-exfiltration burst even when the absolute caps are generous. A byte
       floor prevents tiny baselines from turning ordinary growth into noise.

Design constraints (CLAUDE.md):
    * Config-gated, **default-safe**: ``enabled=False`` is a pure passthrough.
    * **Blocked responses do not consume the cumulative budget** — an oversized
      attempt is rejected, not counted, so one bad response cannot wedge a session.
    * The caller (pipeline) is responsible for fail-closed handling when
      ``observe`` raises; this module surfaces structured verdicts only.

IEC 62443 alignment: FR3 (System Integrity) / FR4 (Data Confidentiality) — bounds
the volume of data that can leave the gateway per session.
"""

import logging
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Deque, Optional, Union

logger = logging.getLogger("agentshroud.security.data_exfil_volume_guard")


@dataclass
class DataExfilVolumeConfig:
    """Configuration for :class:`DataExfilVolumeGuard`."""

    enabled: bool = False
    # Hard ceiling on a single outbound response.
    max_single_response_bytes: int = 5_000_000  # 5 MB
    # Cumulative ceiling per session before blocking.
    max_session_cumulative_bytes: int = 50_000_000  # 50 MB
    # Adaptive spike detection.
    adaptive_enabled: bool = True
    adaptive_multiplier: float = 8.0
    adaptive_min_samples: int = 5
    adaptive_window: int = 20  # rolling window size for the baseline mean
    adaptive_floor_bytes: int = 8192  # baselines below this never trigger a spike


@dataclass
class VolumeVerdict:
    """Structured verdict returned by :meth:`DataExfilVolumeGuard.observe`."""

    allowed: bool
    blocked: bool
    reason_code: str  # "ok" | "single_response_exceeded" | "session_cumulative_exceeded" | "adaptive_spike" | "disabled"  # noqa: E501
    reason: str = ""
    session_id: str = ""
    response_bytes: int = 0
    cumulative_bytes: int = 0
    baseline_bytes: float = 0.0


@dataclass
class _SessionState:
    cumulative: int = 0
    recent: Deque[int] = field(default_factory=deque)


class DataExfilVolumeGuard:
    """Cumulative + adaptive outbound-volume anomaly detector, per session."""

    def __init__(self, config: Optional[DataExfilVolumeConfig] = None):
        self.config = config or DataExfilVolumeConfig()
        self._sessions: dict[str, _SessionState] = defaultdict(_SessionState)
        self._stats: dict[str, int] = defaultdict(int)

    # ------------------------------------------------------------------
    @staticmethod
    def _size(payload: Union[str, bytes]) -> int:
        if isinstance(payload, bytes):
            return len(payload)
        return len(payload.encode("utf-8", errors="ignore"))

    # ------------------------------------------------------------------
    def observe(self, session_id: str, payload: Union[str, bytes]) -> VolumeVerdict:
        """Observe one outbound response and decide allow/block.

        A blocked response is NOT added to the cumulative budget or the adaptive
        baseline, so a single oversized attempt cannot wedge or skew the session.
        """
        self._stats["observations_total"] += 1
        n = self._size(payload)

        if not self.config.enabled:
            return VolumeVerdict(
                allowed=True,
                blocked=False,
                reason_code="disabled",
                session_id=session_id,
                response_bytes=n,
            )

        state = self._sessions[session_id]

        # 1. Single-response hard cap.
        if n > self.config.max_single_response_bytes:
            self._stats["blocked_total"] += 1
            self._stats["single_blocks"] += 1
            logger.warning(
                "DataExfilVolumeGuard: single response %dB exceeds cap %dB (session=%s)",
                n,
                self.config.max_single_response_bytes,
                session_id,
            )
            return VolumeVerdict(
                allowed=False,
                blocked=True,
                reason_code="single_response_exceeded",
                reason=(
                    f"Single response {n}B exceeds cap " f"{self.config.max_single_response_bytes}B"
                ),
                session_id=session_id,
                response_bytes=n,
                cumulative_bytes=state.cumulative,
            )

        # 2. Cumulative session cap.
        projected = state.cumulative + n
        if projected > self.config.max_session_cumulative_bytes:
            self._stats["blocked_total"] += 1
            self._stats["cumulative_blocks"] += 1
            logger.warning(
                "DataExfilVolumeGuard: session %s cumulative %dB would exceed cap %dB",
                session_id,
                projected,
                self.config.max_session_cumulative_bytes,
            )
            return VolumeVerdict(
                allowed=False,
                blocked=True,
                reason_code="session_cumulative_exceeded",
                reason=(
                    f"Session cumulative {projected}B would exceed cap "
                    f"{self.config.max_session_cumulative_bytes}B"
                ),
                session_id=session_id,
                response_bytes=n,
                cumulative_bytes=projected,
            )

        # 3. Adaptive spike detection against the session's rolling baseline.
        baseline = 0.0
        if self.config.adaptive_enabled and len(state.recent) >= self.config.adaptive_min_samples:
            baseline = sum(state.recent) / len(state.recent)
            threshold = max(
                baseline * self.config.adaptive_multiplier,
                float(self.config.adaptive_floor_bytes),
            )
            if n > threshold:
                self._stats["blocked_total"] += 1
                self._stats["adaptive_blocks"] += 1
                logger.warning(
                    "DataExfilVolumeGuard: adaptive spike %dB > threshold %.0fB "
                    "(baseline=%.0fB, session=%s)",
                    n,
                    threshold,
                    baseline,
                    session_id,
                )
                return VolumeVerdict(
                    allowed=False,
                    blocked=True,
                    reason_code="adaptive_spike",
                    reason=(
                        f"Response {n}B exceeds adaptive threshold {threshold:.0f}B "
                        f"(baseline {baseline:.0f}B x{self.config.adaptive_multiplier:g})"
                    ),
                    session_id=session_id,
                    response_bytes=n,
                    cumulative_bytes=state.cumulative,
                    baseline_bytes=baseline,
                )

        # Allowed — commit to cumulative + rolling baseline.
        state.cumulative = projected
        state.recent.append(n)
        while len(state.recent) > self.config.adaptive_window:
            state.recent.popleft()

        return VolumeVerdict(
            allowed=True,
            blocked=False,
            reason_code="ok",
            session_id=session_id,
            response_bytes=n,
            cumulative_bytes=state.cumulative,
            baseline_bytes=baseline,
        )

    # ------------------------------------------------------------------
    def reset_session(self, session_id: str) -> None:
        """Clear cumulative + baseline state for a session (e.g. on new session)."""
        self._sessions.pop(session_id, None)

    def get_stats(self) -> dict[str, int]:
        return dict(self._stats)
