"""SQLite persistence for the approval queue.

Uses aiosqlite to persist approval items across restarts.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import aiosqlite

from ..ingest_api.models import ApprovalQueueItem

logger = logging.getLogger("agentshroud.gateway.approval_queue.store")

SCHEMA = """
CREATE TABLE IF NOT EXISTS approval_items (
    request_id   TEXT PRIMARY KEY,
    action_type  TEXT NOT NULL,
    description  TEXT NOT NULL,
    details      TEXT NOT NULL,
    agent_id     TEXT NOT NULL,
    submitted_at TEXT NOT NULL,
    expires_at   TEXT NOT NULL,
    status       TEXT NOT NULL DEFAULT 'pending',
    decided_at   TEXT,
    reason       TEXT
);
"""


class ApprovalStore:
    """SQLite-backed persistence for approval queue items."""

    def __init__(self, db_path: str | Path = "approval_queue.db"):
        self.db_path = str(db_path)
        self._db: aiosqlite.Connection | None = None

    async def initialize(self) -> None:
        """Open the database and create the schema."""
        self._db = await aiosqlite.connect(self.db_path)
        await self._db.execute(SCHEMA)
        await self._db.commit()
        logger.info(f"Approval store initialized: {self.db_path}")

    async def close(self) -> None:
        """Close the database connection."""
        if self._db:
            await self._db.close()
            self._db = None

    async def save(self, item: ApprovalQueueItem) -> None:
        """Insert or replace an approval item."""
        assert self._db is not None
        await self._db.execute(
            """INSERT OR REPLACE INTO approval_items
               (request_id, action_type, description, details, agent_id,
                submitted_at, expires_at, status, decided_at, reason)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                item.request_id,
                item.action_type,
                item.description,
                json.dumps(item.details),
                item.agent_id,
                item.submitted_at,
                item.expires_at,
                item.status,
                getattr(item, "decided_at", None),
                getattr(item, "reason", None),
            ),
        )
        await self._db.commit()

    async def update_status(
        self, request_id: str, status: str, reason: str = ""
    ) -> None:
        """Update the status of an existing item."""
        assert self._db is not None
        decided_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        await self._db.execute(
            """UPDATE approval_items
               SET status = ?, decided_at = ?, reason = ?
               WHERE request_id = ?""",
            (status, decided_at, reason, request_id),
        )
        await self._db.commit()

    async def load_pending(self) -> list[ApprovalQueueItem]:
        """Load all pending (non-expired, non-decided) items.

        Items whose expires_at is in the past are marked expired
        in the database and excluded.
        """
        assert self._db is not None
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        # Mark expired items
        await self._db.execute(
            """UPDATE approval_items
               SET status = 'expired'
               WHERE status = 'pending' AND expires_at < ?""",
            (now,),
        )
        await self._db.commit()

        cursor = await self._db.execute(
            """SELECT request_id, action_type, description, details, agent_id,
                      submitted_at, expires_at, status
               FROM approval_items WHERE status = 'pending'"""
        )
        rows = await cursor.fetchall()
        items = []
        for row in rows:
            items.append(
                ApprovalQueueItem(
                    request_id=row[0],
                    action_type=row[1],
                    description=row[2],
                    details=json.loads(row[3]),
                    agent_id=row[4],
                    submitted_at=row[5],
                    expires_at=row[6],
                    status=row[7],
                )
            )
        return items

    async def load_all(self) -> list[ApprovalQueueItem]:
        """Load all items (for audit/debugging)."""
        assert self._db is not None
        cursor = await self._db.execute(
            """SELECT request_id, action_type, description, details, agent_id,
                      submitted_at, expires_at, status
               FROM approval_items"""
        )
        rows = await cursor.fetchall()
        return [
            ApprovalQueueItem(
                request_id=r[0],
                action_type=r[1],
                description=r[2],
                details=json.loads(r[3]),
                agent_id=r[4],
                submitted_at=r[5],
                expires_at=r[6],
                status=r[7],
            )
            for r in rows
        ]
