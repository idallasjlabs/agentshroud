# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
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


class TrustLevel(IntEnum):
    UNTRUSTED = 0
    BASIC = 1
    STANDARD = 2
    ELEVATED = 3
    FULL = 4


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
    ):
        self.config = config or TrustConfig()
        self.action_levels = action_levels or dict(DEFAULT_ACTION_LEVELS)
        self.db_path = db_path
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
        return self._update_score(
            agent_id, self.config.success_points, "success", details
        )

    def record_failure(self, agent_id: str, details: str = "") -> TrustLevel:
        """Record a failed/blocked action, decreasing trust."""
        return self._update_score(
            agent_id, self.config.failure_points, "failure", details
        )

    def record_violation(self, agent_id: str, details: str = "") -> TrustLevel:
        """Record a security violation, significantly decreasing trust."""
        return self._update_score(
            agent_id, self.config.violation_points, "violation", details
        )

    def _update_score(
        self, agent_id: str, delta: float, event_type: str, details: str
    ) -> TrustLevel:
        now = time.time()
        row = self._conn.execute(
            "SELECT score, last_action_time FROM trust_scores WHERE agent_id = ?",
            (agent_id,),
        ).fetchone()
        if not row:
            self.register_agent(agent_id)
            row = (self.config.initial_score, now)

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
