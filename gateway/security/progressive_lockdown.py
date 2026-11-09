# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Progressive Lockdown — per-principal cumulative risk scoring and escalation.

Tracks the number of blocked/quarantined requests per principal. A principal is
any opaque string key: a Telegram user id, a Falco container name, or a future
``edge:<vendor>:<client>`` identity. At defined thresholds, escalates the response:
  3 blocks  → owner alert (silent escalation notice)
  5 blocks  → rate limit window doubled for this principal
  10 blocks → session suspended + owner notification

``escalate_to()`` lets a high-confidence signal (e.g. a Falco CRITICAL alert)
jump a principal straight to a level. Escalation never lowers a level; only
``reset()`` (owner /unlock) clears it.

Optional time-window decay (``decay_window_seconds``) ages old blocks out of the
threshold count. It is OFF by default, which preserves the original behaviour
exactly (blocks accumulate for the gateway's lifetime). Suspension is sticky
under decay — only ``reset()`` lifts it.

ONE instance is created per gateway process in ``gateway/ingest_api/lifespan.py``
and stored on ``app_state.progressive_lockdown``; the Telegram proxy and the
FalcoAlertWatcher share it (SCRUM-203). State is in-memory only (reset on
gateway restart).

IEC 62443: FR3 (system integrity — Falco-driven enforcement), FR7 (resource
availability — rate-limit escalation / suspension of abusive principals).
"""

from __future__ import annotations

import logging
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Deque, Dict, Optional, Union

logger = logging.getLogger("agentshroud.security.progressive_lockdown")


class LockdownLevel(str, Enum):
    NORMAL = "normal"  # < 3 blocks — no change
    ALERT = "alert"  # 3–4 blocks — owner alert sent
    ESCALATED = "escalated"  # 5–9 blocks — rate limit doubled
    SUSPENDED = "suspended"  # 10+ blocks — session suspended


_RANK: Dict[LockdownLevel, int] = {
    LockdownLevel.NORMAL: 0,
    LockdownLevel.ALERT: 1,
    LockdownLevel.ESCALATED: 2,
    LockdownLevel.SUSPENDED: 3,
}


@dataclass
class UserLockdownState:
    user_id: str
    block_count: int = 0
    level: LockdownLevel = LockdownLevel.NORMAL
    alert_sent: bool = False  # owner alert at ALERT level
    escalation_sent: bool = False  # owner alert at ESCALATED level
    suspend_sent: bool = False  # owner alert at SUSPENDED level
    first_block_ts: float = 0.0
    last_block_ts: float = 0.0
    suspended_at: Optional[float] = None
    # Minimum level set by escalate_to(); cleared only by reset().
    floor_level: LockdownLevel = LockdownLevel.NORMAL
    # Block timestamps inside the decay window (only populated when decay is on).
    block_times: Deque[float] = field(default_factory=deque)


@dataclass
class LockdownAction:
    """What the caller should do in response to this block."""

    level: LockdownLevel
    notify_owner: bool  # send escalation notice to owner right now
    notify_text: str  # text of owner notification (empty if no notify)
    rate_limit_multiplier: float  # 1.0 = normal, 2.0 = double window
    suspended: bool  # True → drop request immediately, no response


_THRESHOLD_ALERT = 3
_THRESHOLD_ESCALATE = 5
_THRESHOLD_SUSPEND = 10

_MULTIPLIER: Dict[LockdownLevel, float] = {
    LockdownLevel.NORMAL: 1.0,
    LockdownLevel.ALERT: 1.0,
    LockdownLevel.ESCALATED: 2.0,
    LockdownLevel.SUSPENDED: 4.0,
}


def _level_for_count(n: int) -> LockdownLevel:
    if n >= _THRESHOLD_SUSPEND:
        return LockdownLevel.SUSPENDED
    if n >= _THRESHOLD_ESCALATE:
        return LockdownLevel.ESCALATED
    if n >= _THRESHOLD_ALERT:
        return LockdownLevel.ALERT
    return LockdownLevel.NORMAL


def _max_level(a: LockdownLevel, b: LockdownLevel) -> LockdownLevel:
    return a if _RANK[a] >= _RANK[b] else b


class ProgressiveLockdown:
    """Tracks per-principal block counts and returns escalation actions.

    Thread-safe: every read/modify of principal state happens under one
    ``threading.RLock``. Callers are synchronous methods invoked from the
    asyncio event loop and from executor threads; the critical sections never
    await or do I/O, so holding the lock cannot stall the loop.
    """

    def __init__(
        self,
        decay_window_seconds: Optional[float] = None,
        clock: Callable[[], float] = time.time,
    ) -> None:
        """
        Args:
            decay_window_seconds: When set, only blocks recorded within this many
                seconds count toward thresholds. ``None`` (default) disables decay
                and keeps the original accumulate-forever behaviour.
            clock: Time source (injectable for tests).
        """
        if decay_window_seconds is not None and decay_window_seconds <= 0:
            raise ValueError("decay_window_seconds must be > 0 or None")
        self._states: Dict[str, UserLockdownState] = {}
        self._decay_window = decay_window_seconds
        self._clock = clock
        self._lock = threading.RLock()

    # ── internal helpers (caller must hold self._lock) ──────────────────────

    def _get_state(self, user_id: str) -> UserLockdownState:
        if user_id not in self._states:
            self._states[user_id] = UserLockdownState(user_id=user_id)
        return self._states[user_id]

    @staticmethod
    def _effective_level(state: UserLockdownState) -> LockdownLevel:
        if state.suspended_at is not None:
            return LockdownLevel.SUSPENDED  # sticky until reset()
        return _max_level(state.floor_level, _level_for_count(state.block_count))

    def _refresh(self, state: UserLockdownState, now: float) -> None:
        """Apply decay (if enabled) and recompute the principal's level."""
        if self._decay_window is None:
            return
        cutoff = now - self._decay_window
        while state.block_times and state.block_times[0] <= cutoff:
            state.block_times.popleft()
        state.block_count = len(state.block_times)
        state.level = self._effective_level(state)
        # Re-arm owner notifications for levels the principal has decayed below,
        # so a fresh climb is reported again.
        rank = _RANK[state.level]
        if rank < _RANK[LockdownLevel.ALERT]:
            state.alert_sent = False
        if rank < _RANK[LockdownLevel.ESCALATED]:
            state.escalation_sent = False

    @staticmethod
    def _claim_notify(state: UserLockdownState, level: LockdownLevel) -> bool:
        """Return True the first time `level` is reached; mark it as notified."""
        if level == LockdownLevel.SUSPENDED:
            notify, state.suspend_sent = not state.suspend_sent, True
        elif level == LockdownLevel.ESCALATED:
            notify, state.escalation_sent = not state.escalation_sent, True
        elif level == LockdownLevel.ALERT:
            notify, state.alert_sent = not state.alert_sent, True
        else:
            notify = False
        return notify

    @staticmethod
    def _action(level: LockdownLevel, notify: bool, notify_text: str) -> LockdownAction:
        return LockdownAction(
            level=level,
            notify_owner=notify,
            notify_text=notify_text if notify else "",
            rate_limit_multiplier=_MULTIPLIER[level],
            suspended=level == LockdownLevel.SUSPENDED,
        )

    # ── public API ───────────────────────────────────────────────────────────

    def record_block(
        self,
        user_id: str,
        reason: str = "",
        username: str = "",
    ) -> LockdownAction:
        """Record one blocked request for a principal and return the resulting action.

        Args:
            user_id: Principal key whose request was blocked (any string).
            reason: Short description of what was blocked (for owner notification).
            username: Display name for owner notification text.

        Returns:
            LockdownAction describing what the call site should do.
        """
        with self._lock:
            state = self._get_state(user_id)
            now = self._clock()
            self._refresh(state, now)

            state.block_count += 1
            if self._decay_window is not None:
                state.block_times.append(now)
            if state.first_block_ts == 0.0:
                state.first_block_ts = now
            state.last_block_ts = now

            n = state.block_count
            display = username or user_id
            level = _max_level(state.floor_level, _level_for_count(n))
            if state.suspended_at is not None:
                level = LockdownLevel.SUSPENDED
            state.level = level

            if level == LockdownLevel.SUSPENDED:
                state.suspended_at = now
                notify = self._claim_notify(state, level)
                return self._action(
                    level,
                    notify,
                    f"🔴 *Session Suspended* — {display} has triggered {n} security blocks.\n"
                    f"Latest: {reason}\n"
                    f"All further messages from this user are silently dropped.\n"
                    f"Use /unlock {user_id} to restore access.",
                )

            if level == LockdownLevel.ESCALATED:
                notify = self._claim_notify(state, level)
                return self._action(
                    level,
                    notify,
                    f"🟠 *Lockdown Escalated* — {display} has {n} blocks.\n"
                    f"Latest: {reason}\n"
                    f"Rate limit window doubled. Next suspension at {_THRESHOLD_SUSPEND} blocks.",
                )

            if level == LockdownLevel.ALERT:
                notify = self._claim_notify(state, level)
                return self._action(
                    level,
                    notify,
                    f"🟡 *Lockdown Alert* — {display} has reached {n} security blocks.\n"
                    f"Latest: {reason}\n"
                    f"Monitoring elevated. Escalation at {_THRESHOLD_ESCALATE} blocks.",
                )

            return self._action(LockdownLevel.NORMAL, False, "")

    def escalate_to(
        self,
        principal: str,
        level: Union[LockdownLevel, str],
        reason: str = "",
        username: str = "",
    ) -> LockdownAction:
        """Jump a principal directly to `level` (never lowers its current level).

        The level becomes a floor that holds regardless of block count or decay
        until ``reset()`` is called. The owner is notified the first time a level
        is reached, exactly as with ``record_block``.

        Raises:
            ValueError: if `level` is not a valid LockdownLevel.
        """
        target_req = LockdownLevel(level)
        with self._lock:
            state = self._get_state(principal)
            now = self._clock()
            self._refresh(state, now)
            state.floor_level = _max_level(state.floor_level, target_req)
            new_level = self._effective_level(state)
            if new_level == LockdownLevel.SUSPENDED and state.suspended_at is None:
                state.suspended_at = now
            state.level = new_level

            notify = self._claim_notify(state, new_level)
            display = username or principal
            texts = {
                LockdownLevel.SUSPENDED: (
                    f"🔴 *Session Suspended* — {display} was escalated directly.\n"
                    f"Reason: {reason}\n"
                    f"All further requests from this principal are dropped.\n"
                    f"Use /unlock {principal} to restore access."
                ),
                LockdownLevel.ESCALATED: (
                    f"🟠 *Lockdown Escalated* — {display} was escalated directly.\n"
                    f"Reason: {reason}\n"
                    f"Rate limit window doubled."
                ),
                LockdownLevel.ALERT: (
                    f"🟡 *Lockdown Alert* — {display} was escalated directly.\n"
                    f"Reason: {reason}\n"
                    f"Monitoring elevated."
                ),
                LockdownLevel.NORMAL: "",
            }
            if _RANK[target_req] > _RANK[LockdownLevel.NORMAL]:
                logger.warning(
                    "ProgressiveLockdown: escalate_to %s requested=%s effective=%s reason=%s",
                    principal,
                    target_req.value,
                    new_level.value,
                    reason,
                )
            return self._action(new_level, notify, texts[new_level])

    def level_of(self, principal: str) -> LockdownLevel:
        """Return the principal's current level (decay applied); NORMAL if unknown."""
        with self._lock:
            state = self._states.get(principal)
            if state is None:
                return LockdownLevel.NORMAL
            self._refresh(state, self._clock())
            return state.level

    def is_suspended(self, user_id: str) -> bool:
        """Return True if the principal's session is currently suspended."""
        return self.level_of(user_id) == LockdownLevel.SUSPENDED

    def get_status(self, user_id: str) -> dict:
        """Return current lockdown state for a principal (for /collabs or owner inspection)."""
        with self._lock:
            state = self._states.get(user_id)
            if not state:
                return {"user_id": user_id, "block_count": 0, "level": LockdownLevel.NORMAL.value}
            self._refresh(state, self._clock())
            return {
                "user_id": state.user_id,
                "block_count": state.block_count,
                "level": state.level.value,
                "first_block_ts": state.first_block_ts,
                "last_block_ts": state.last_block_ts,
                "suspended_at": state.suspended_at,
            }

    def reset(self, user_id: str) -> bool:
        """Owner command: reset lockdown state for a principal. Returns True if existed."""
        with self._lock:
            if user_id in self._states:
                del self._states[user_id]
                logger.info(f"ProgressiveLockdown: reset state for user {user_id}")
                return True
            return False

    def all_statuses(self) -> list[dict]:
        """Return lockdown status for all tracked principals."""
        with self._lock:
            return [self.get_status(uid) for uid in list(self._states)]
