# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Progressive Lockdown — per-user cumulative risk scoring and escalation.

Tracks the number of blocked/quarantined requests per user across a session.
At defined thresholds, escalates the response:
  3 blocks  → owner alert (silent escalation notice)
  5 blocks  → rate limit window doubled for this user
  10 blocks → session suspended + owner notification

Block counts are in-memory only (reset on gateway restart). For persistent
tracking across restarts, the audit store can be wired in the future.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional

logger = logging.getLogger("agentshroud.security.progressive_lockdown")


class LockdownLevel(str, Enum):
    NORMAL = "normal"        # < 3 blocks — no change
    ALERT = "alert"          # 3–4 blocks — owner alert sent
    ESCALATED = "escalated"  # 5–9 blocks — rate limit doubled
    SUSPENDED = "suspended"  # 10+ blocks — session suspended


@dataclass
class UserLockdownState:
    user_id: str
    block_count: int = 0
    level: LockdownLevel = LockdownLevel.NORMAL
    alert_sent: bool = False       # owner alert at ALERT level
    escalation_sent: bool = False  # owner alert at ESCALATED level
    suspend_sent: bool = False     # owner alert at SUSPENDED level
    first_block_ts: float = 0.0
    last_block_ts: float = 0.0
    suspended_at: Optional[float] = None


@dataclass
class LockdownAction:
    """What the caller should do in response to this block."""
    level: LockdownLevel
    notify_owner: bool           # send escalation notice to owner right now
    notify_text: str             # text of owner notification (empty if no notify)
    rate_limit_multiplier: float # 1.0 = normal, 2.0 = double window
    suspended: bool              # True → drop request immediately, no response


_THRESHOLD_ALERT = 3
_THRESHOLD_ESCALATE = 5
_THRESHOLD_SUSPEND = 10


class ProgressiveLockdown:
    """Tracks per-user block counts and returns escalation actions.

    Thread-safe for single-process async use (no shared mutation across threads).
    """

    def __init__(self) -> None:
        self._states: Dict[str, UserLockdownState] = {}

    def _get_state(self, user_id: str) -> UserLockdownState:
        if user_id not in self._states:
            self._states[user_id] = UserLockdownState(user_id=user_id)
        return self._states[user_id]

    def record_block(
        self,
        user_id: str,
        reason: str = "",
        username: str = "",
    ) -> LockdownAction:
        """Record one blocked request for user_id and return the resulting action.

        Args:
            user_id: The user whose request was blocked.
            reason: Short description of what was blocked (for owner notification).
            username: Display name for owner notification text.

        Returns:
            LockdownAction describing what the call site should do.
        """
        state = self._get_state(user_id)
        now = time.time()

        state.block_count += 1
        if state.first_block_ts == 0.0:
            state.first_block_ts = now
        state.last_block_ts = now

        n = state.block_count
        display = username or user_id

        # Determine level and whether to notify owner
        if n >= _THRESHOLD_SUSPEND:
            state.level = LockdownLevel.SUSPENDED
            state.suspended_at = now
            notify = not state.suspend_sent
            state.suspend_sent = True
            notify_text = (
                f"🔴 *Session Suspended* — {display} has triggered {n} security blocks.\n"
                f"Latest: {reason}\n"
                f"All further messages from this user are silently dropped.\n"
                f"Use /unlock {user_id} to restore access."
            ) if notify else ""
            return LockdownAction(
                level=LockdownLevel.SUSPENDED,
                notify_owner=notify,
                notify_text=notify_text,
                rate_limit_multiplier=4.0,
                suspended=True,
            )

        if n >= _THRESHOLD_ESCALATE:
            state.level = LockdownLevel.ESCALATED
            notify = not state.escalation_sent
            state.escalation_sent = True
            notify_text = (
                f"🟠 *Lockdown Escalated* — {display} has {n} blocks.\n"
                f"Latest: {reason}\n"
                f"Rate limit window doubled. Next suspension at {_THRESHOLD_SUSPEND} blocks."
            ) if notify else ""
            return LockdownAction(
                level=LockdownLevel.ESCALATED,
                notify_owner=notify,
                notify_text=notify_text,
                rate_limit_multiplier=2.0,
                suspended=False,
            )

        if n >= _THRESHOLD_ALERT:
            state.level = LockdownLevel.ALERT
            notify = not state.alert_sent
            state.alert_sent = True
            notify_text = (
                f"🟡 *Lockdown Alert* — {display} has reached {n} security blocks.\n"
                f"Latest: {reason}\n"
                f"Monitoring elevated. Escalation at {_THRESHOLD_ESCALATE} blocks."
            ) if notify else ""
            return LockdownAction(
                level=LockdownLevel.ALERT,
                notify_owner=notify,
                notify_text=notify_text,
                rate_limit_multiplier=1.0,
                suspended=False,
            )

        return LockdownAction(
            level=LockdownLevel.NORMAL,
            notify_owner=False,
            notify_text="",
            rate_limit_multiplier=1.0,
            suspended=False,
        )

    def is_suspended(self, user_id: str) -> bool:
        """Return True if the user's session is currently suspended."""
        state = self._states.get(user_id)
        return state is not None and state.level == LockdownLevel.SUSPENDED

    def get_status(self, user_id: str) -> dict:
        """Return current lockdown state for a user (for /collabs or owner inspection)."""
        state = self._states.get(user_id)
        if not state:
            return {"user_id": user_id, "block_count": 0, "level": LockdownLevel.NORMAL.value}
        return {
            "user_id": state.user_id,
            "block_count": state.block_count,
            "level": state.level.value,
            "first_block_ts": state.first_block_ts,
            "last_block_ts": state.last_block_ts,
            "suspended_at": state.suspended_at,
        }

    def reset(self, user_id: str) -> bool:
        """Owner command: reset lockdown state for a user. Returns True if existed."""
        if user_id in self._states:
            del self._states[user_id]
            logger.info(f"ProgressiveLockdown: reset state for user {user_id}")
            return True
        return False

    def all_statuses(self) -> list[dict]:
        """Return lockdown status for all tracked users."""
        return [self.get_status(uid) for uid in self._states]
