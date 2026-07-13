# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Live per-module enforcement counters (SCRUM-80).

Feeds the SOC dashboard's per-module enforcement heat-map — auditors see, per
security module, how many decisions it allowed / blocked / sanitized in real
time.  This is deliberately REAL counting: the old dashboard's hardcoded
"24/30 active" was flagged as security theater, so this module only ever
reports what enforcement points actually recorded.  A module with no
instrumentation shows genuine zeros (surfaced as ``instrumented: false`` by the
API), never fabricated activity.

Scope + honesty:
- process-lifetime, in-memory counters (reset on gateway restart — documented;
  durable history is the audit ledger's job, not this heat-map)
- thread-safe: enforcement runs across the async loop + worker threads, so
  ``record`` takes a lock and must never raise into a caller's decision path
- an invalid decision value is dropped silently rather than propagated — a
  telemetry bug must not break enforcement
"""

from __future__ import annotations

import threading
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allowed"
    BLOCK = "blocked"
    SANITIZE = "sanitized"


_COUNT_KEYS = ("allowed", "blocked", "sanitized")


class ModuleStatsCollector:
    """Thread-safe per-module allow/block/sanitize counters."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._counts: dict[str, dict[str, int]] = {}

    def record(self, module: str, decision: Decision) -> None:
        """Record one enforcement decision for ``module``.

        Never raises: an unknown/invalid decision is dropped (telemetry must
        not break the enforcement path that called it).
        """
        try:
            key = Decision(decision).value
        except (ValueError, TypeError):
            return
        with self._lock:
            bucket = self._counts.setdefault(str(module), {k: 0 for k in _COUNT_KEYS})
            bucket[key] += 1

    def snapshot(self) -> dict[str, dict[str, float]]:
        """Return a per-module stats snapshot with totals and block rate."""
        with self._lock:
            out: dict[str, dict[str, float]] = {}
            for module, bucket in self._counts.items():
                total = sum(bucket[k] for k in _COUNT_KEYS)
                out[module] = {
                    **{k: bucket[k] for k in _COUNT_KEYS},
                    "total": total,
                    "block_rate": (bucket["blocked"] / total) if total else 0.0,
                }
            return out

    def reset(self) -> None:
        with self._lock:
            self._counts.clear()


# Process-global collector — enforcement points record here, the SOC API reads
# here.  A singleton (not per-request) so counts accumulate across the process.
_COLLECTOR = ModuleStatsCollector()


def get_collector() -> ModuleStatsCollector:
    return _COLLECTOR


def record_decision(module: str, allowed: bool, sanitized: bool = False) -> None:
    """Ergonomic recorder for enforcement points — never raises.

    ``sanitized=True`` (regardless of ``allowed``) counts a sanitize; else
    allow/block from the boolean.  Wrapped in a bare except so a telemetry
    fault can never propagate into a live enforcement decision.
    """
    try:
        if sanitized:
            decision = Decision.SANITIZE
        else:
            decision = Decision.ALLOW if allowed else Decision.BLOCK
        _COLLECTOR.record(module, decision)
    except Exception:  # pragma: no cover - defensive
        pass
