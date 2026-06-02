# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Telegram update replay buffer — SQLite WAL, bot-agnostic.

Records every getUpdates response so that crash-recovered bots can receive
messages that arrived while they were offline. Best-effort: all DB calls are
wrapped in try/except to guarantee the proxy hot-path never breaks.
"""

from __future__ import annotations

import json
import logging
import os
import sqlite3
import time
from typing import Any

logger = logging.getLogger("agentshroud.proxy.telegram_replay")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS replay (
    bot_id        TEXT    NOT NULL,
    update_id     INTEGER NOT NULL,
    received_at   INTEGER NOT NULL,
    delivered_at  INTEGER,
    payload       TEXT    NOT NULL,
    PRIMARY KEY (bot_id, update_id)
);
CREATE INDEX IF NOT EXISTS idx_undelivered
    ON replay(bot_id, delivered_at)
    WHERE delivered_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_age ON replay(received_at);
"""

_CLEANUP_EVERY = 1000  # calls between periodic cleanup sweeps
_RETENTION_SECONDS = 86400  # 24 h


class UpdateReplayBuffer:
    """SQLite-backed Telegram update store, safe for concurrent asyncio callers."""

    def __init__(self, db_path: str) -> None:
        self._db_path = db_path
        self._call_count = 0
        self._conn: sqlite3.Connection | None = None
        self._init_db()

    # ── internal ──────────────────────────────────────────────────────────────

    def _init_db(self) -> None:
        try:
            os.makedirs(os.path.dirname(self._db_path), exist_ok=True)
            conn = sqlite3.connect(self._db_path, check_same_thread=False)
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.executescript(_SCHEMA)
            conn.commit()
            self._conn = conn
            logger.info("Telegram replay buffer ready at %s", self._db_path)
        except Exception as exc:
            logger.warning("Replay buffer init failed (%s) — replay disabled", exc)
            self._conn = None

    def _conn_ok(self) -> bool:
        return self._conn is not None

    # ── public API ────────────────────────────────────────────────────────────

    def record_inbound(self, bot_id: str, updates: list[dict[str, Any]]) -> None:
        """Persist inbound updates so they can be replayed after a crash."""
        if not self._conn_ok() or not updates:
            return
        try:
            now = int(time.time())
            rows = [
                (bot_id, u["update_id"], now, json.dumps(u))
                for u in updates
                if isinstance(u, dict) and "update_id" in u
            ]
            if rows:
                self._conn.executemany(  # type: ignore[union-attr]
                    "INSERT OR IGNORE INTO replay (bot_id,update_id,received_at,payload) VALUES (?,?,?,?)",
                    rows,
                )
                self._conn.commit()  # type: ignore[union-attr]
        except Exception as exc:
            logger.warning("replay.record_inbound failed: %s", exc)

    def mark_delivered(self, bot_id: str, offset: int) -> None:
        """Mark all updates with update_id < offset as delivered (normal getUpdates ack)."""
        if not self._conn_ok():
            return
        try:
            now = int(time.time())
            self._conn.execute(  # type: ignore[union-attr]
                "UPDATE replay SET delivered_at=? WHERE bot_id=? AND update_id<? AND delivered_at IS NULL",
                (now, bot_id, offset),
            )
            self._conn.commit()  # type: ignore[union-attr]
        except Exception as exc:
            logger.warning("replay.mark_delivered failed: %s", exc)

    def pull_undelivered(
        self, bot_id: str, older_than_s: int = 30, limit: int = 10
    ) -> list[dict[str, Any]]:
        """Return undelivered updates older than grace window (avoids replay storms)."""
        if not self._conn_ok():
            return []
        try:
            cutoff = int(time.time()) - older_than_s
            rows = self._conn.execute(  # type: ignore[union-attr]
                "SELECT payload FROM replay WHERE bot_id=? AND delivered_at IS NULL AND received_at<? ORDER BY update_id LIMIT ?",
                (bot_id, cutoff, limit),
            ).fetchall()
            updates = []
            for (payload,) in rows:
                try:
                    updates.append(json.loads(payload))
                except Exception:
                    pass
            return updates
        except Exception as exc:
            logger.warning("replay.pull_undelivered failed: %s", exc)
            return []

    def cleanup_if_due(self) -> None:
        """Periodically prune rows older than retention window."""
        self._call_count += 1
        if self._call_count % _CLEANUP_EVERY != 0:
            return
        if not self._conn_ok():
            return
        try:
            cutoff = int(time.time()) - _RETENTION_SECONDS
            deleted = self._conn.execute(  # type: ignore[union-attr]
                "DELETE FROM replay WHERE received_at<?", (cutoff,)
            ).rowcount
            self._conn.commit()  # type: ignore[union-attr]
            if deleted:
                logger.debug("Replay buffer cleanup: pruned %d expired rows", deleted)
        except Exception as exc:
            logger.warning("replay.cleanup_if_due failed: %s", exc)
