# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Progressive Trust System — agent earns autonomy over time.

Trust levels from UNTRUSTED to FULL, backed by SQLite persistence.
Actions are gated by minimum trust levels. Trust is earned through
successful operations and decays over time or on violations.
"""


import sqlite3
import time
from dataclasses import dataclass
from enum import IntEnum
from typing import Optional

from gateway.security.progressive_trust_config import (
    ProgressiveTrustConfig,
)
from gateway.security.progressive_trust_config import TrustLevel as ProgressiveTrustLevel
from gateway.security.progressive_trust_config import ViolationType


class TrustLevel(IntEnum):
    UNTRUSTED = 0
    BASIC = 1
    STANDARD = 2
    ELEVATED = 3
    FULL = 4


# Mapping between the score-based manager levels (IntEnum) and the
# progressive-trust ladder levels (str enum). TRUSTED↔ELEVATED and
# VERIFIED↔FULL are the same rung under different names.
_PROGRESSIVE_BY_MANAGER: dict["TrustLevel", ProgressiveTrustLevel] = {
    TrustLevel.UNTRUSTED: ProgressiveTrustLevel.UNTRUSTED,
    TrustLevel.BASIC: ProgressiveTrustLevel.BASIC,
    TrustLevel.STANDARD: ProgressiveTrustLevel.STANDARD,
    TrustLevel.ELEVATED: ProgressiveTrustLevel.TRUSTED,
    TrustLevel.FULL: ProgressiveTrustLevel.VERIFIED,
}
_MANAGER_BY_PROGRESSIVE: dict[ProgressiveTrustLevel, "TrustLevel"] = {
    v: k for k, v in _PROGRESSIVE_BY_MANAGER.items()
}


@dataclass
class TrustConfig:
    initial_level: TrustLevel = TrustLevel.BASIC
    initial_score: float = 100.0
    # Score thresholds for each level
    thresholds: dict[int, float] = None
    # Points
    success_points: float = 5.0
    failure_points: float = -20.0
    violation_points: float = -50.0
    # Rate limiting
    max_successes_per_hour: int = 10
    # Decay: points lost per hour of inactivity
    decay_rate: float = 0.5
    decay_interval_hours: float = 24.0

    def __post_init__(self):
        if self.thresholds is None:
            self.thresholds = {
                TrustLevel.UNTRUSTED: 0,
                TrustLevel.BASIC: 50,
                TrustLevel.STANDARD: 150,
                TrustLevel.ELEVATED: 300,
                TrustLevel.FULL: 500,
            }


# Default action -> minimum trust level mapping
DEFAULT_ACTION_LEVELS: dict[str, TrustLevel] = {
    "read_file": TrustLevel.BASIC,
    "write_file": TrustLevel.STANDARD,
    "execute_command": TrustLevel.ELEVATED,
    "network_request": TrustLevel.STANDARD,
    "install_package": TrustLevel.ELEVATED,
    "modify_config": TrustLevel.ELEVATED,
    "admin_action": TrustLevel.FULL,
    "delete_file": TrustLevel.ELEVATED,
    "send_message": TrustLevel.STANDARD,
    "access_secrets": TrustLevel.FULL,
}


class TrustManager:
    """Manage progressive trust for agents."""

    def __init__(
        self,
        db_path: str = ":memory:",
        config: Optional[TrustConfig] = None,
        action_levels: Optional[dict[str, TrustLevel]] = None,
        progressive_config: Optional[ProgressiveTrustConfig] = None,
    ):
        self.config = config or TrustConfig()
        self.action_levels = action_levels or dict(DEFAULT_ACTION_LEVELS)
        self.db_path = db_path
        # Optional trust ladder: when set, promotions are additionally gated by
        # interaction-count/age/violation thresholds, typed violations carry
        # configured penalties, and per-level tool access can be queried.
        self.progressive_config = progressive_config
        self._vouched_agents: set[str] = set()
        self._conn = sqlite3.connect(db_path)
        if db_path != ":memory:":
            self._conn.execute("PRAGMA journal_mode=WAL")
        self._init_db()

    def _init_db(self):
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS trust_scores (
                agent_id TEXT PRIMARY KEY,
                score REAL NOT NULL,
                level INTEGER NOT NULL,
                last_action_time REAL NOT NULL,
                created_at REAL NOT NULL,
                total_successes INTEGER DEFAULT 0,
                total_failures INTEGER DEFAULT 0,
                total_violations INTEGER DEFAULT 0
            )
        """)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS trust_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                timestamp REAL NOT NULL,
                event_type TEXT NOT NULL,
                score_delta REAL NOT NULL,
                new_score REAL NOT NULL,
                new_level INTEGER NOT NULL,
                details TEXT
            )
        """)
        self._conn.commit()

    def _score_to_level(self, score: float) -> TrustLevel:
        """Convert score to trust level based on thresholds."""
        level = TrustLevel.UNTRUSTED
        for tl in sorted(self.config.thresholds.keys()):
            if score >= self.config.thresholds[tl]:
                level = TrustLevel(tl)
        return level

    def register_agent(self, agent_id: str) -> TrustLevel:
        """Register a new agent with initial trust."""
        now = time.time()
        existing = self._conn.execute(
            "SELECT score FROM trust_scores WHERE agent_id = ?", (agent_id,)
        ).fetchone()
        if existing:
            return self._score_to_level(existing[0])

        self._conn.execute(
            """INSERT INTO trust_scores
               (agent_id, score, level, last_action_time, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (
                agent_id,
                self.config.initial_score,
                int(self.config.initial_level),
                now,
                now,
            ),
        )
        self._conn.commit()
        return self.config.initial_level

    def get_trust(self, agent_id: str) -> Optional[tuple[TrustLevel, float]]:
        """Get current trust level and score for an agent."""
        row = self._conn.execute(
            "SELECT score, level, last_action_time FROM trust_scores WHERE agent_id = ?",
            (agent_id,),
        ).fetchone()
        if not row:
            return None
        score, level, last_time = row
        # Apply decay
        score = self._apply_decay(score, last_time)
        new_level = self._score_to_level(score)
        # With a progressive config, the stored level is the promotion ceiling:
        # score alone cannot raise the effective level past what the gated
        # promotion path (_update_score) has granted. Demotion by decay still
        # applies via min().
        if self.progressive_config is not None:
            new_level = min(new_level, TrustLevel(level))
        return (new_level, score)

    def _apply_decay(self, score: float, last_action_time: float) -> float:
        """Apply time-based decay to score."""
        now = time.time()
        hours_elapsed = (now - last_action_time) / 3600
        decay_periods = hours_elapsed / self.config.decay_interval_hours
        decayed = score - (decay_periods * self.config.decay_rate)
        return max(0.0, decayed)

    def is_action_allowed(self, agent_id: str, action: str) -> bool:
        """Check if an agent's trust level allows a given action."""
        trust = self.get_trust(agent_id)
        if trust is None:
            return False
        current_level, _ = trust
        required = self.action_levels.get(action, TrustLevel.FULL)
        return current_level >= required

    def record_success(self, agent_id: str, details: str = "") -> TrustLevel:
        """Record a successful action, increasing trust."""
        return self._update_score(agent_id, self.config.success_points, "success", details)

    def record_failure(self, agent_id: str, details: str = "") -> TrustLevel:
        """Record a failed/blocked action, decreasing trust."""
        return self._update_score(agent_id, self.config.failure_points, "failure", details)

    def record_violation(
        self,
        agent_id: str,
        details: str = "",
        violation_type: Optional[ViolationType] = None,
    ) -> TrustLevel:
        """Record a security violation, significantly decreasing trust.

        With a progressive config and a typed violation, the penalty comes from
        the config's violation_penalties and severe violations trigger an
        immediate one-level demotion regardless of remaining score.
        """
        if violation_type is not None and self.progressive_config is not None:
            penalty = self.progressive_config.violation_penalties.get(violation_type)
            delta = -float(penalty) if penalty is not None else self.config.violation_points
            new_level = self._update_score(
                agent_id, delta, "violation", details or violation_type.value
            )
            if (
                self.progressive_config.auto_demotion_enabled
                and self.progressive_config.severe_violation_immediate_demotion
                and violation_type in self.progressive_config.severe_violation_types
            ):
                new_level = self._force_demotion(agent_id, violation_type.value)
            return new_level
        return self._update_score(agent_id, self.config.violation_points, "violation", details)

    def _force_demotion(self, agent_id: str, reason: str) -> TrustLevel:
        """Drop an agent one trust level immediately (severe violations)."""
        row = self._conn.execute(
            "SELECT score, level FROM trust_scores WHERE agent_id = ?", (agent_id,)
        ).fetchone()
        if not row:
            return self.config.initial_level
        score, level = row
        current = TrustLevel(level)
        if current == TrustLevel.UNTRUSTED:
            return current
        target = TrustLevel(int(current) - 1)
        # Clamp the score to the target level's threshold so the score-derived
        # level agrees with the demotion.
        new_score = min(float(score), float(self.config.thresholds[target]))
        now = time.time()
        self._conn.execute(
            "UPDATE trust_scores SET score = ?, level = ?, last_action_time = ? WHERE agent_id = ?",
            (new_score, int(target), now, agent_id),
        )
        self._conn.execute(
            """INSERT INTO trust_history
               (agent_id, timestamp, event_type, score_delta, new_score, new_level, details)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                agent_id,
                now,
                "demotion",
                new_score - float(score),
                new_score,
                int(target),
                f"severe violation: {reason}",
            ),
        )
        self._conn.commit()
        return target

    def vouch_for_agent(self, agent_id: str) -> None:
        """Owner vouches for an agent, unlocking VERIFIED/FULL promotion."""
        self._vouched_agents.add(agent_id)

    def is_tool_allowed(self, agent_id: str, tool_name: str) -> Optional[bool]:
        """Per-level tool gate from the progressive trust ladder.

        Tri-state: True/False when the ladder has an opinion; None when it has
        no opinion (no progressive config, unregistered agent, or a tool name
        outside the ladder's vocabulary) so callers fall through to the ACL.
        """
        if self.progressive_config is None:
            return None
        trust = self.get_trust(agent_id)
        if trust is None:
            return None
        known_tools: set[str] = set()
        for tools in self.progressive_config.tool_access.values():
            known_tools |= tools
        known_tools.discard("*")
        if tool_name not in known_tools:
            return None
        progressive_level = _PROGRESSIVE_BY_MANAGER[trust[0]]
        return self.progressive_config.is_tool_allowed(progressive_level, tool_name)

    def _update_score(
        self, agent_id: str, delta: float, event_type: str, details: str
    ) -> TrustLevel:
        now = time.time()
        row = self._conn.execute(
            """SELECT score, last_action_time, level, created_at,
                      total_successes, total_failures, total_violations
               FROM trust_scores WHERE agent_id = ?""",
            (agent_id,),
        ).fetchone()
        if not row:
            self.register_agent(agent_id)
            row = (
                self.config.initial_score,
                now,
                int(self.config.initial_level),
                now,
                0,
                0,
                0,
            )

        current_score = self._apply_decay(row[0], row[1])

        # Rate-limit trust gains to prevent rapid escalation
        if delta > 0:
            one_hour_ago = now - 3600
            recent = self._conn.execute(
                """SELECT COUNT(*) FROM trust_history
                   WHERE agent_id = ? AND event_type = 'success'
                   AND timestamp > ?""",
                (agent_id, one_hour_ago),
            ).fetchone()[0]
            if recent >= self.config.max_successes_per_hour:
                delta = 0  # Cap gains, still record the event

        new_score = max(0.0, current_score + delta)
        new_level = self._score_to_level(new_score)

        # Progressive promotion gating: score alone is not enough to climb the
        # ladder — each rung also requires the configured interaction count,
        # account age, violation ceiling, and (for the top rung) owner vouching.
        if self.progressive_config is not None:
            stored_level = TrustLevel(row[2])
            created_at = row[3]
            interactions = (row[4] or 0) + (row[5] or 0) + (row[6] or 0)
            violations = row[6] or 0
            if new_level > stored_level:
                granted = stored_level
                for candidate in range(int(stored_level) + 1, int(new_level) + 1):
                    if self._promotion_allowed(
                        agent_id, TrustLevel(candidate), created_at, interactions, violations, now
                    ):
                        granted = TrustLevel(candidate)
                    else:
                        break
                new_level = granted

        # Update counters — use safe whitelist, never interpolate user input
        _COUNTER_COLS = {
            "success": "total_successes",
            "failure": "total_failures",
            "violation": "total_violations",
        }
        counter_col = _COUNTER_COLS.get(event_type)

        if counter_col:
            # Safe: counter_col comes from hardcoded dict above, never from user input
            assert counter_col in (
                "total_successes",
                "total_failures",
                "total_violations",
            )
            sql = f"UPDATE trust_scores SET score = ?, level = ?, last_action_time = ?, {counter_col} = {counter_col} + 1 WHERE agent_id = ?"
        else:
            sql = "UPDATE trust_scores SET score = ?, level = ?, last_action_time = ? WHERE agent_id = ?"

        self._conn.execute(sql, (new_score, int(new_level), now, agent_id))
        self._conn.execute(
            """INSERT INTO trust_history
               (agent_id, timestamp, event_type, score_delta, new_score, new_level, details)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (agent_id, now, event_type, delta, new_score, int(new_level), details),
        )
        self._conn.commit()
        return new_level

    def _promotion_allowed(
        self,
        agent_id: str,
        target_level: TrustLevel,
        created_at: float,
        interactions: int,
        violations: int,
        now: float,
    ) -> bool:
        """Check the progressive ladder's threshold for promotion to target_level."""
        if self.progressive_config is None:
            return True
        progressive_level = _PROGRESSIVE_BY_MANAGER[target_level]
        threshold = self.progressive_config.promotion_thresholds.get(progressive_level)
        if threshold is None:
            return True
        if interactions < threshold.min_interactions:
            return False
        if (now - created_at) / 86400.0 < threshold.min_days_since_first:
            return False
        if violations > threshold.max_violations:
            return False
        if threshold.requires_owner_vouching and agent_id not in self._vouched_agents:
            return False
        return True

    def get_history(self, agent_id: str, limit: int = 50) -> list[dict]:
        """Get trust history for an agent."""
        rows = self._conn.execute(
            """SELECT timestamp, event_type, score_delta, new_score, new_level, details
               FROM trust_history WHERE agent_id = ? ORDER BY timestamp DESC LIMIT ?""",
            (agent_id, limit),
        ).fetchall()
        return [
            {
                "timestamp": r[0],
                "event_type": r[1],
                "score_delta": r[2],
                "new_score": r[3],
                "new_level": r[4],
                "details": r[5],
            }
            for r in rows
        ]

    def close(self):
        self._conn.close()
