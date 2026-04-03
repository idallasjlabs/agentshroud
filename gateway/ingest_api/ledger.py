# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Data Ledger for AgentShroud Gateway

SQLite-based audit trail of all forwarded content.
CRITICAL: Stores only SHA-256 hashes, never raw content.
"""


import hashlib
import json
import logging
import uuid
from datetime import datetime, timedelta
from typing import Any, Optional

import aiosqlite

from .config import LedgerConfig
from .models import LedgerEntry, LedgerQueryResponse

logger = logging.getLogger("agentshroud.gateway.ledger")


# Database schema
CREATE_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS ledger (
    id TEXT PRIMARY KEY,
    timestamp TEXT NOT NULL,
    source TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    original_content_hash TEXT NOT NULL,
    sanitized INTEGER NOT NULL DEFAULT 0,
    size INTEGER NOT NULL,
    redaction_count INTEGER NOT NULL DEFAULT 0,
    redaction_types TEXT NOT NULL DEFAULT '[]',
    forwarded_to TEXT NOT NULL DEFAULT '',
    content_type TEXT NOT NULL DEFAULT 'text',
    metadata TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL,
    expires_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_ledger_timestamp ON ledger(timestamp);
CREATE INDEX IF NOT EXISTS idx_ledger_source ON ledger(source);
CREATE INDEX IF NOT EXISTS idx_ledger_content_hash ON ledger(content_hash);
CREATE INDEX IF NOT EXISTS idx_ledger_forwarded_to ON ledger(forwarded_to);
CREATE INDEX IF NOT EXISTS idx_ledger_expires_at ON ledger(expires_at);
CREATE INDEX IF NOT EXISTS idx_ledger_content_type ON ledger(content_type);
"""

CREATE_VERSION_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
);
INSERT OR IGNORE INTO schema_version (version, applied_at)
VALUES (1, datetime('now'));
"""


class DataLedger:
    """Async SQLite-backed data ledger

    Records all content forwarded through the gateway.
    Stores only SHA-256 hashes, never raw content.
    """

    def __init__(self, config: LedgerConfig):
        """Store configuration

        Actual database connection created in initialize().

        Args:
            config: Ledger configuration
        """
        self.config = config
        self.db: aiosqlite.Connection | None = None

    async def initialize(self) -> None:
        """Create database, tables, and run initial cleanup

        Must be called before using the ledger.
        """
        # Ensure parent directory exists
        self.config.path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Initializing ledger database at {self.config.path}")

        # Connect to database
        self.db = await aiosqlite.connect(str(self.config.path))

        # Enable foreign keys and WAL mode for better concurrency
        await self.db.execute("PRAGMA foreign_keys = ON")
        await self.db.execute("PRAGMA journal_mode = WAL")

        # Create schema
        await self.db.executescript(CREATE_SCHEMA_SQL)
        await self.db.executescript(CREATE_VERSION_TABLE_SQL)
        await self.db.commit()

        # Run retention cleanup
        deleted = await self.enforce_retention()
        if deleted > 0:
            logger.info(f"Deleted {deleted} expired entries during initialization")

    async def record(
        self,
        source: str,
        content: str,
        original_content: str,
        sanitized: bool,
        redaction_count: int,
        redaction_types: list[str],
        forwarded_to: str,
        content_type: str = "text",
        metadata: Optional[dict] = None,
    ) -> LedgerEntry:
        """Create a new ledger entry

        Args:
            source: Source identifier (shortcut, browser_extension, etc.)
            content: Sanitized content (will be hashed, not stored)
            original_content: Original content (will be hashed, not stored)
            sanitized: Whether PII was redacted
            redaction_count: Number of redactions made
            redaction_types: List of entity types redacted
            forwarded_to: Target agent name
            content_type: Type of content (text, url, photo, file)
            metadata: Optional metadata dictionary

        Returns:
            LedgerEntry with the created entry details
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized. Call initialize() first.")

        # Generate ID and timestamps
        from datetime import timezone

        entry_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc)
        timestamp_iso = now.isoformat().replace("+00:00", "Z")
        expires_at = now + timedelta(days=self.config.retention_days)
        expires_iso = expires_at.isoformat().replace("+00:00", "Z")

        # Hash content (never store raw)
        content_hash = self._hash_content(content)
        original_hash = self._hash_content(original_content)

        # Serialize JSON fields
        redaction_types_json = json.dumps(redaction_types)
        metadata_json = json.dumps(metadata or {})

        # Insert
        await self.db.execute(
            """
            INSERT INTO ledger (
                id, timestamp, source, content_hash, original_content_hash,
                sanitized, size, redaction_count, redaction_types,
                forwarded_to, content_type, metadata, created_at, expires_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                entry_id,
                timestamp_iso,
                source,
                content_hash,
                original_hash,
                1 if sanitized else 0,
                len(content),
                redaction_count,
                redaction_types_json,
                forwarded_to,
                content_type,
                metadata_json,
                timestamp_iso,
                expires_iso,
            ),
        )
        await self.db.commit()

        logger.info(
            f"Ledger entry created: {entry_id} (source={source}, "
            f"sanitized={sanitized}, size={len(content)})"
        )

        return LedgerEntry(
            id=entry_id,
            timestamp=timestamp_iso,
            source=source,
            content_hash=content_hash,
            sanitized=sanitized,
            size=len(content),
            redaction_count=redaction_count,
            forwarded_to=forwarded_to,
        )

    async def query(
        self,
        page: int = 1,
        page_size: int = 50,
        source: Optional[str] = None,
        since: Optional[str] = None,
        until: Optional[str] = None,
        forwarded_to: Optional[str] = None,
    ) -> LedgerQueryResponse:
        """Query ledger entries with pagination and filters

        Args:
            page: Page number (1-indexed)
            page_size: Entries per page
            source: Filter by source
            since: Filter by timestamp >= this ISO 8601 date
            until: Filter by timestamp <= this ISO 8601 date
            forwarded_to: Filter by target agent

        Returns:
            LedgerQueryResponse with entries and pagination metadata
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized")

        # Build WHERE clause
        conditions = []
        params: list[Any] = []

        if source:
            conditions.append("source = ?")
            params.append(source)

        if since:
            conditions.append("timestamp >= ?")
            params.append(since)

        if until:
            conditions.append("timestamp <= ?")
            params.append(until)

        if forwarded_to:
            conditions.append("forwarded_to = ?")
            params.append(forwarded_to)

        where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""

        # Count total
        count_sql = f"SELECT COUNT(*) FROM ledger{where_clause}"
        async with self.db.execute(count_sql, params) as cursor:
            row = await cursor.fetchone()
            total = row[0] if row else 0

        # Fetch page
        offset = (page - 1) * page_size
        query_sql = f"""
            SELECT id, timestamp, source, content_hash, sanitized, size,
                   redaction_count, forwarded_to
            FROM ledger
            {where_clause}
            ORDER BY timestamp DESC
            LIMIT ? OFFSET ?
        """
        params.extend([page_size, offset])

        entries = []
        async with self.db.execute(query_sql, params) as cursor:
            async for row in cursor:
                entries.append(
                    LedgerEntry(
                        id=row[0],
                        timestamp=row[1],
                        source=row[2],
                        content_hash=row[3],
                        sanitized=bool(row[4]),
                        size=row[5],
                        redaction_count=row[6],
                        forwarded_to=row[7],
                    )
                )

        return LedgerQueryResponse(entries=entries, total=total, page=page, page_size=page_size)

    async def get_entry(self, entry_id: str) -> LedgerEntry | None:
        """Fetch a single ledger entry by ID

        Args:
            entry_id: Entry UUID

        Returns:
            LedgerEntry if found, None otherwise
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized")

        async with self.db.execute(
            """
            SELECT id, timestamp, source, content_hash, sanitized, size,
                   redaction_count, forwarded_to
            FROM ledger
            WHERE id = ?
            """,
            (entry_id,),
        ) as cursor:
            row = await cursor.fetchone()
            if not row:
                return None

            return LedgerEntry(
                id=row[0],
                timestamp=row[1],
                source=row[2],
                content_hash=row[3],
                sanitized=bool(row[4]),
                size=row[5],
                redaction_count=row[6],
                forwarded_to=row[7],
            )

    async def delete_entry(self, entry_id: str) -> bool:
        """'Forget this' - permanently delete a ledger entry

        Implements right to erasure.

        Args:
            entry_id: Entry UUID

        Returns:
            True if entry existed and was deleted, False if not found
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized")

        cursor = await self.db.execute("DELETE FROM ledger WHERE id = ?", (entry_id,))
        await self.db.commit()

        deleted = cursor.rowcount > 0
        if deleted:
            logger.info(f"Ledger entry deleted: {entry_id}")
        return deleted

    async def get_stats(self) -> dict[str, Any]:
        """Get aggregate statistics

        Returns:
            Dictionary with total entries, by source, etc.
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized")

        stats = {}

        # Total entries
        async with self.db.execute("SELECT COUNT(*) FROM ledger") as cursor:
            row = await cursor.fetchone()
            stats["total_entries"] = row[0] if row else 0

        # By source
        async with self.db.execute("SELECT source, COUNT(*) FROM ledger GROUP BY source") as cursor:
            stats["by_source"] = {row[0]: row[1] async for row in cursor}

        # Sanitized vs not
        async with self.db.execute(
            "SELECT sanitized, COUNT(*) FROM ledger GROUP BY sanitized"
        ) as cursor:
            async for row in cursor:
                key = "sanitized" if row[0] else "not_sanitized"
                stats[key] = row[1]

        return stats

    async def enforce_retention(self) -> int:
        """Delete entries older than retention_days

        Returns:
            Number of entries deleted
        """
        if not self.db:
            raise RuntimeError("Ledger not initialized")

        from datetime import timezone

        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        cursor = await self.db.execute(
            "DELETE FROM ledger WHERE expires_at IS NOT NULL AND expires_at < ?", (now,)
        )
        await self.db.commit()

        deleted = cursor.rowcount
        if deleted > 0:
            logger.info(f"Retention enforcement: deleted {deleted} expired entries")

        return deleted

    async def close(self) -> None:
        """Close database connection"""
        if self.db:
            await self.db.close()
            self.db = None
            logger.info("Ledger database closed")

    @staticmethod
    def _hash_content(content: str) -> str:
        """SHA-256 hash of content string

        Args:
            content: Text to hash

        Returns:
            Hexadecimal SHA-256 hash
        """
        return hashlib.sha256(content.encode("utf-8")).hexdigest()
