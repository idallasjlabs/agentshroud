# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SQLite-backed audit event store with tamper-evident hash chain.

Similar to ApprovalStore pattern but designed for high-volume audit logs
with cryptographic integrity verification.
"""

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import aiosqlite

logger = logging.getLogger("agentshroud.gateway.security.audit_store")

SCHEMA = """
CREATE TABLE IF NOT EXISTS audit_events (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id     TEXT NOT NULL UNIQUE,
    event_type   TEXT NOT NULL,
    severity     TEXT NOT NULL,
    timestamp    TEXT NOT NULL,
    source_module TEXT NOT NULL,
    details      TEXT NOT NULL,  -- JSON
    prev_hash    TEXT,
    entry_hash   TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_events(timestamp);
CREATE INDEX IF NOT EXISTS idx_audit_type ON audit_events(event_type);
CREATE INDEX IF NOT EXISTS idx_audit_severity ON audit_events(severity);
"""


class AuditEvent:
    """Represents a single audit event."""

    def __init__(
        self,
        event_type: str,
        severity: str,
        details: dict,
        source_module: str,
        event_id: Optional[str] = None,
        timestamp: Optional[str] = None,
    ):
        self.event_id = event_id or self._generate_event_id()
        self.event_type = event_type
        self.severity = severity.upper()
        self.timestamp = timestamp or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        self.source_module = source_module
        self.details = details
        self.prev_hash: Optional[str] = None
        self.entry_hash: Optional[str] = None

    def _generate_event_id(self) -> str:
        """Generate a unique event ID based on timestamp + random."""
        import uuid
        return f"audit_{int(datetime.now().timestamp())}_{str(uuid.uuid4())[24:]}"

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "severity": self.severity,
            "timestamp": self.timestamp,
            "source_module": self.source_module,
            "details": self.details,
            "prev_hash": self.prev_hash,
            "entry_hash": self.entry_hash,
        }

    def compute_content_hash(self) -> str:
        """Compute SHA-256 hash of event content (excluding hashes)."""
        content = {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "severity": self.severity,
            "timestamp": self.timestamp,
            "source_module": self.source_module,
            "details": self.details,
        }
        content_str = json.dumps(content, sort_keys=True)
        return hashlib.sha256(content_str.encode()).hexdigest()

    def compute_entry_hash(self, prev_hash: Optional[str] = None) -> str:
        """Compute entry hash including previous hash (chain)."""
        content_hash = self.compute_content_hash()
        chain_input = f"{prev_hash or ''}:{content_hash}"
        return hashlib.sha256(chain_input.encode()).hexdigest()


class AuditStore:
    """SQLite-backed audit event store with tamper-evident hash chain."""

    def __init__(self, db_path: str | Path = "audit_events.db"):
        self.db_path = str(db_path)
        self._db: Optional[aiosqlite.Connection] = None

    async def initialize(self) -> None:
        """Open the database and create the schema."""
        self._db = await aiosqlite.connect(self.db_path)
        await self._db.executescript(SCHEMA)
        await self._db.commit()
        logger.info(f"Audit store initialized: {self.db_path}")

    async def close(self) -> None:
        """Close the database connection."""
        if self._db:
            await self._db.close()
            self._db = None

    async def log_event(
        self,
        event_type: str,
        severity: str,
        details: dict,
        source_module: str,
        event_id: Optional[str] = None,
    ) -> AuditEvent:
        """Log a new audit event with hash chain integrity."""
        assert self._db is not None

        # Create event
        event = AuditEvent(
            event_type=event_type,
            severity=severity,
            details=details,
            source_module=source_module,
            event_id=event_id,
        )

        # Get previous hash for chain
        prev_hash = await self._get_latest_hash()
        event.prev_hash = prev_hash
        event.entry_hash = event.compute_entry_hash(prev_hash)

        # Insert into database
        await self._db.execute(
            """INSERT INTO audit_events
               (event_id, event_type, severity, timestamp, source_module, details, prev_hash, entry_hash)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                event.event_id,
                event.event_type,
                event.severity,
                event.timestamp,
                event.source_module,
                json.dumps(event.details),
                event.prev_hash,
                event.entry_hash,
            ),
        )
        await self._db.commit()

        logger.debug(f"Audit event logged: {event.event_id} ({event.event_type})")
        return event

    async def query_events(
        self,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        event_type: Optional[str] = None,
        severity_min: Optional[str] = None,
        limit: int = 1000,
    ) -> list[AuditEvent]:
        """Query audit events with optional filters."""
        assert self._db is not None

        # Build WHERE clause
        conditions = []
        params = []

        if start_time:
            conditions.append("timestamp >= ?")
            params.append(start_time)
        if end_time:
            conditions.append("timestamp <= ?")
            params.append(end_time)
        if event_type:
            conditions.append("event_type = ?")
            params.append(event_type)
        if severity_min:
            # Severity ordering: CRITICAL > HIGH > MEDIUM > LOW > INFO
            severity_values = {"CRITICAL": 5, "HIGH": 4, "MEDIUM": 3, "LOW": 2, "INFO": 1}
            min_level = severity_values.get(severity_min.upper(), 0)
            severity_condition = " OR ".join(
                f"severity = '{sev}'" for sev, val in severity_values.items() if val >= min_level
            )
            if severity_condition:
                conditions.append(f"({severity_condition})")

        where_clause = " AND ".join(conditions) if conditions else "1=1"
        query = f"""SELECT event_id, event_type, severity, timestamp, source_module, 
                               details, prev_hash, entry_hash
                        FROM audit_events
                        WHERE {where_clause}
                        ORDER BY timestamp DESC
                        LIMIT ?"""
        params.append(limit)

        cursor = await self._db.execute(query, params)
        rows = await cursor.fetchall()

        events = []
        for row in rows:
            event = AuditEvent(
                event_id=row[0],
                event_type=row[1],
                severity=row[2],
                source_module=row[4],
                details=json.loads(row[5]),
                timestamp=row[3],
            )
            event.prev_hash = row[6]
            event.entry_hash = row[7]
            events.append(event)

        return events

    async def get_recent_entries(self, limit: int = 100) -> list["AuditEvent"]:
        """Return the most recent audit entries (alias for query_events with limit)."""
        return await self.query_events(limit=limit)

    async def verify_hash_chain(self, start_id: Optional[str] = None, limit: int = 1000) -> tuple[bool, str]:
        """Verify the integrity of the hash chain.
        
        Args:
            start_id: Start verification from this event ID (None = from beginning)
            limit: Maximum number of events to verify
            
        Returns:
            Tuple of (is_valid, message)
        """
        assert self._db is not None

        query = """SELECT event_id, event_type, severity, timestamp, source_module, 
                           details, prev_hash, entry_hash
                    FROM audit_events
                    ORDER BY id ASC"""
        params = []

        if start_id:
            query = query.replace("ORDER BY id ASC", """WHERE id >= (SELECT id FROM audit_events WHERE event_id = ?)
                                                            ORDER BY id ASC""")
            params.append(start_id)

        if limit:
            query += f" LIMIT {limit}"

        cursor = await self._db.execute(query, params)
        rows = await cursor.fetchall()

        if not rows:
            return True, "No events to verify"

        expected_prev_hash = None
        verified_count = 0

        for row in rows:
            event = AuditEvent(
                event_id=row[0],
                event_type=row[1],
                severity=row[2],
                source_module=row[4],
                details=json.loads(row[5]),
                timestamp=row[3],
            )
            stored_prev_hash = row[6]
            stored_entry_hash = row[7]

            # Verify previous hash chain
            if stored_prev_hash != expected_prev_hash:
                return False, f"Hash chain broken at event {event.event_id}: expected prev_hash {expected_prev_hash}, got {stored_prev_hash}"

            # Verify entry hash
            computed_hash = event.compute_entry_hash(stored_prev_hash)
            if computed_hash != stored_entry_hash:
                return False, f"Entry hash mismatch at event {event.event_id}: expected {computed_hash}, got {stored_entry_hash}"

            expected_prev_hash = stored_entry_hash
            verified_count += 1

        return True, f"Verified {verified_count} events successfully"

    async def _get_latest_hash(self) -> Optional[str]:
        """Get the entry_hash of the most recent event for chain continuation."""
        assert self._db is not None

        cursor = await self._db.execute(
            "SELECT entry_hash FROM audit_events ORDER BY id DESC LIMIT 1"
        )
        row = await cursor.fetchone()
        return row[0] if row else None

    async def get_stats(self) -> dict:
        """Get audit store statistics."""
        assert self._db is not None

        cursor = await self._db.execute("SELECT COUNT(*) FROM audit_events")
        total_count = (await cursor.fetchone())[0]

        cursor = await self._db.execute(
            "SELECT severity, COUNT(*) FROM audit_events GROUP BY severity"
        )
        severity_counts = dict(await cursor.fetchall())

        cursor = await self._db.execute(
            "SELECT MIN(timestamp), MAX(timestamp) FROM audit_events"
        )
        time_range = await cursor.fetchone()

        return {
            "total_events": total_count,
            "severity_counts": severity_counts,
            "earliest_event": time_range[0],
            "latest_event": time_range[1],
        }