# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Retention archival for the audit_events hash-chained log.

audit_events grows unbounded (it is a tamper-evident log — see audit_store.py).
This module moves events older than a cutoff into a separate on-disk archive
database, verbatim (including prev_hash/entry_hash), then deletes them from
the live database and VACUUMs it.

Chain safety: the live table's forward-going chain only ever depends on the
*latest* row's entry_hash (see AuditStore._get_latest_hash) — new events are
unaffected by removing older rows. Historical verifiability is preserved
because archived rows are retained byte-for-byte in the archive database, not
discarded.
"""

import logging
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger("agentshroud.gateway.security.audit_archive")

_ARCHIVE_SCHEMA = """
CREATE TABLE IF NOT EXISTS audit_events (
    id           INTEGER PRIMARY KEY,
    event_id     TEXT NOT NULL UNIQUE,
    event_type   TEXT NOT NULL,
    severity     TEXT NOT NULL,
    timestamp    TEXT NOT NULL,
    source_module TEXT NOT NULL,
    details      TEXT NOT NULL,
    prev_hash    TEXT,
    entry_hash   TEXT NOT NULL,
    bot_id       TEXT NOT NULL DEFAULT 'openclaw'
);
CREATE INDEX IF NOT EXISTS idx_archive_timestamp ON audit_events(timestamp);
"""


def archive_old_events(
    db_path: str | Path,
    archive_path: str | Path,
    cutoff_days: int = 90,
    now: Optional[datetime] = None,
    vacuum: bool = True,
) -> dict:
    """Move audit_events older than cutoff_days into archive_path, then delete + VACUUM the live db.

    Args:
        db_path: Path to the live audit.db.
        archive_path: Path to the archive database (created if missing).
        cutoff_days: Events with timestamp older than this many days are archived.
        now: Reference time for the cutoff (defaults to real UTC now).
        vacuum: Whether to VACUUM the live db after deletion (reclaims disk space).

    Returns:
        dict with archived_count, remaining_count, cutoff (ISO string).
    """
    db_path = Path(db_path)
    archive_path = Path(archive_path)
    if not db_path.exists():
        return {"archived_count": 0, "remaining_count": 0, "cutoff": None, "skipped": "db_missing"}

    reference = now or datetime.now(timezone.utc)
    cutoff = (reference - timedelta(days=cutoff_days)).isoformat()

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    # audit.db uses SQLite's default DELETE journal mode (not WAL), which
    # requires an exclusive lock for writes — the live gateway process holds
    # it periodically while logging new events. A busy_timeout makes this
    # connection wait for that lock instead of raising "database is locked"
    # immediately, matching how a live production run actually behaves.
    archive_conn = sqlite3.connect(archive_path, timeout=60)
    try:
        archive_conn.executescript(_ARCHIVE_SCHEMA)

        live_conn = sqlite3.connect(db_path, timeout=60)
        try:
            live_conn.row_factory = sqlite3.Row
            rows = live_conn.execute(
                "SELECT id, event_id, event_type, severity, timestamp, source_module, "
                "details, prev_hash, entry_hash, bot_id FROM audit_events "
                "WHERE timestamp < ? ORDER BY id ASC",
                (cutoff,),
            ).fetchall()

            if not rows:
                return {
                    "archived_count": 0,
                    "remaining_count": live_conn.execute(
                        "SELECT COUNT(*) FROM audit_events"
                    ).fetchone()[0],
                    "cutoff": cutoff,
                }

            archive_conn.executemany(
                "INSERT OR IGNORE INTO audit_events "
                "(id, event_id, event_type, severity, timestamp, source_module, "
                "details, prev_hash, entry_hash, bot_id) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [tuple(row) for row in rows],
            )
            archive_conn.commit()

            ids = [row["id"] for row in rows]
            live_conn.executemany(
                "DELETE FROM audit_events WHERE id = ?", [(i,) for i in ids]
            )
            live_conn.commit()

            # VACUUM needs roughly the live db's own size again in scratch
            # space on the *same filesystem*. On a genuinely full volume this
            # can fail even though the archive+delete above already
            # succeeded and committed — that data-safety work must not be
            # thrown away just because the disk-reclaim nicety couldn't run.
            # It will succeed on a later run once headroom exists (idempotent).
            vacuum_succeeded = None
            if vacuum:
                try:
                    live_conn.execute("VACUUM")
                    vacuum_succeeded = True
                except sqlite3.OperationalError as exc:
                    vacuum_succeeded = False
                    logger.warning(
                        f"VACUUM failed after successful archive+delete of {len(ids)} "
                        f"events (data safely archived, disk space not yet reclaimed): {exc}"
                    )

            remaining = live_conn.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0]
            logger.info(
                f"Archived {len(ids)} audit events older than {cutoff} "
                f"to {archive_path} ({remaining} remain live)"
            )
            return {
                "archived_count": len(ids),
                "remaining_count": remaining,
                "cutoff": cutoff,
                "vacuum_succeeded": vacuum_succeeded,
            }
        finally:
            live_conn.close()
    finally:
        archive_conn.close()


def purge_low_value_events(
    db_path: str | Path,
    archive_path: str | Path,
    event_type: str,
    severity: str,
    batch_size: int = 50_000,
    vacuum: bool = True,
    progress_every: int = 20,
) -> dict:
    """Archive+delete ALL rows matching (event_type, severity), regardless of age.

    For one-time cleanup of a bug's accumulated output (e.g. a module that
    persisted every routine decision instead of only notable ones) — not for
    routine retention, which should use archive_old_events. Processes in
    batches so this is safe against tables with tens of millions of matching
    rows: each batch is its own committed transaction, so an interruption
    partway through loses no work and a re-run simply continues.

    Args:
        event_type: exact event_type to match (e.g. "egress_filter").
        severity: exact severity to match (e.g. "INFO").
        batch_size: rows archived+deleted per transaction.
        progress_every: log a progress line every N batches.

    Returns:
        dict with archived_count, remaining_count (matching this filter,
        should be 0), batches.
    """
    db_path = Path(db_path)
    archive_path = Path(archive_path)
    if not db_path.exists():
        return {"archived_count": 0, "remaining_count": 0, "skipped": "db_missing"}

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_conn = sqlite3.connect(archive_path, timeout=60)
    try:
        archive_conn.executescript(_ARCHIVE_SCHEMA)

        live_conn = sqlite3.connect(db_path, timeout=60)
        try:
            live_conn.row_factory = sqlite3.Row
            total_archived = 0
            batches = 0

            while True:
                rows = live_conn.execute(
                    "SELECT id, event_id, event_type, severity, timestamp, source_module, "
                    "details, prev_hash, entry_hash, bot_id FROM audit_events "
                    "WHERE event_type = ? AND severity = ? ORDER BY id ASC LIMIT ?",
                    (event_type, severity, batch_size),
                ).fetchall()
                if not rows:
                    break

                archive_conn.executemany(
                    "INSERT OR IGNORE INTO audit_events "
                    "(id, event_id, event_type, severity, timestamp, source_module, "
                    "details, prev_hash, entry_hash, bot_id) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    [tuple(row) for row in rows],
                )
                archive_conn.commit()

                ids = [row["id"] for row in rows]
                live_conn.executemany(
                    "DELETE FROM audit_events WHERE id = ?", [(i,) for i in ids]
                )
                live_conn.commit()

                total_archived += len(ids)
                batches += 1
                if batches % progress_every == 0:
                    logger.info(
                        f"purge_low_value_events: {total_archived} rows archived so far "
                        f"({event_type}/{severity})"
                    )

            vacuum_succeeded = None
            if vacuum and total_archived:
                try:
                    live_conn.execute("VACUUM")
                    vacuum_succeeded = True
                except sqlite3.OperationalError as exc:
                    vacuum_succeeded = False
                    logger.warning(
                        f"VACUUM failed after successful purge of {total_archived} "
                        f"{event_type}/{severity} events: {exc}"
                    )

            remaining = live_conn.execute(
                "SELECT COUNT(*) FROM audit_events WHERE event_type = ? AND severity = ?",
                (event_type, severity),
            ).fetchone()[0]
            logger.info(
                f"purge_low_value_events: archived {total_archived} {event_type}/{severity} "
                f"events in {batches} batch(es) to {archive_path}"
            )
            return {
                "archived_count": total_archived,
                "remaining_count": remaining,
                "batches": batches,
                "vacuum_succeeded": vacuum_succeeded,
            }
        finally:
            live_conn.close()
    finally:
        archive_conn.close()


def _cli() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Archive audit_events rows")
    sub = parser.add_subparsers(dest="command", required=True)

    age = sub.add_parser("age", help="Archive events older than a cutoff (routine retention)")
    age.add_argument("--db", default="/app/data/audit.db")
    age.add_argument("--archive", default="/app/data/audit_archive.db")
    age.add_argument("--cutoff-days", type=int, default=90)
    age.add_argument("--no-vacuum", action="store_true")

    filt = sub.add_parser(
        "filter", help="Archive ALL events matching an event_type+severity (one-time cleanup)"
    )
    filt.add_argument("--db", default="/app/data/audit.db")
    filt.add_argument("--archive", default="/app/data/audit_archive.db")
    filt.add_argument("--event-type", required=True)
    filt.add_argument("--severity", required=True)
    filt.add_argument("--batch-size", type=int, default=50_000)
    filt.add_argument("--no-vacuum", action="store_true")

    args = parser.parse_args()

    if args.command == "age":
        result = archive_old_events(
            args.db, args.archive, cutoff_days=args.cutoff_days, vacuum=not args.no_vacuum
        )
    else:
        result = purge_low_value_events(
            args.db,
            args.archive,
            event_type=args.event_type,
            severity=args.severity,
            batch_size=args.batch_size,
            vacuum=not args.no_vacuum,
        )
    print(result)


if __name__ == "__main__":
    _cli()
