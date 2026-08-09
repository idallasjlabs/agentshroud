# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for audit_archive.py retention archival."""

import sqlite3
import threading
import time
from datetime import datetime, timedelta, timezone

import pytest

from gateway.security.audit_archive import archive_old_events, purge_low_value_events

_LIVE_SCHEMA = """
CREATE TABLE audit_events (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
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
"""


def _make_live_db(path, events):
    """events: list of (event_id, timestamp, prev_hash, entry_hash)."""
    conn = sqlite3.connect(path)
    conn.executescript(_LIVE_SCHEMA)
    for event_id, ts, prev_hash, entry_hash in events:
        conn.execute(
            "INSERT INTO audit_events "
            "(event_id, event_type, severity, timestamp, source_module, details, "
            "prev_hash, entry_hash, bot_id) VALUES (?, 'test', 'LOW', ?, 'test', '{}', ?, ?, 'openclaw')",
            (event_id, ts, prev_hash, entry_hash),
        )
    conn.commit()
    conn.close()


@pytest.fixture
def now():
    return datetime(2026, 8, 8, 12, 0, 0, tzinfo=timezone.utc)


def _chain_events(n, start, spacing_days=1):
    """Build n chained events, oldest first, spaced spacing_days apart ending at `start`."""
    events = []
    prev_hash = None
    for i in range(n):
        ts = (start - timedelta(days=(n - 1 - i) * spacing_days)).isoformat()
        entry_hash = f"hash_{i}"
        events.append((f"evt_{i}", ts, prev_hash, entry_hash))
        prev_hash = entry_hash
    return events


class TestArchiveOldEvents:
    def test_archives_only_events_older_than_cutoff(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        # 10 events, 1 per day, oldest 9 days ago, newest = now.
        events = _chain_events(10, now)
        _make_live_db(db, events)

        result = archive_old_events(db, archive, cutoff_days=5, now=now)

        # Events older than 5 days: days 6,7,8,9 ago -> 4 events archived.
        assert result["archived_count"] == 4
        assert result["remaining_count"] == 6

        live = sqlite3.connect(db)
        remaining_ids = {r[0] for r in live.execute("SELECT event_id FROM audit_events")}
        live.close()
        assert remaining_ids == {"evt_4", "evt_5", "evt_6", "evt_7", "evt_8", "evt_9"}

    def test_archived_rows_preserved_verbatim(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(5, now)
        _make_live_db(db, events)

        archive_old_events(db, archive, cutoff_days=2, now=now)

        arch = sqlite3.connect(archive)
        arch.row_factory = sqlite3.Row
        rows = {r["event_id"]: r for r in arch.execute("SELECT * FROM audit_events")}
        arch.close()

        # evt_0..evt_2 are older than cutoff (2 days) given daily spacing ending at `now`.
        assert "evt_0" in rows
        assert rows["evt_0"]["prev_hash"] is None
        assert rows["evt_1"]["prev_hash"] == "hash_0"
        assert rows["evt_1"]["entry_hash"] == "hash_1"

    def test_no_events_to_archive_is_a_noop(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(3, now)
        _make_live_db(db, events)

        result = archive_old_events(db, archive, cutoff_days=365, now=now)

        assert result["archived_count"] == 0
        assert result["remaining_count"] == 3
        # Archive db should not even need to exist meaningfully populated.

    def test_missing_db_is_reported_not_raised(self, tmp_path, now):
        db = tmp_path / "does_not_exist.db"
        archive = tmp_path / "archive.db"

        result = archive_old_events(db, archive, cutoff_days=90, now=now)

        assert result["archived_count"] == 0
        assert result["skipped"] == "db_missing"

    def test_live_forward_chain_still_valid_after_archival(self, tmp_path, now):
        """The remaining live rows' own internal chain (row N's prev_hash ==
        row N-1's entry_hash, for rows that remain adjacent) is untouched by
        archival — only the oldest remaining row's prev_hash now points to an
        archived (not live) hash, which is expected and handled by consulting
        the archive, not a corruption of the live data itself."""
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(6, now)
        _make_live_db(db, events)

        archive_old_events(db, archive, cutoff_days=3, now=now)

        live = sqlite3.connect(db)
        live.row_factory = sqlite3.Row
        rows = live.execute("SELECT * FROM audit_events ORDER BY id ASC").fetchall()
        live.close()

        # Adjacent live rows still chain correctly among themselves.
        for prev_row, row in zip(rows, rows[1:]):
            assert row["prev_hash"] == prev_row["entry_hash"]

    def test_running_twice_is_idempotent(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(10, now)
        _make_live_db(db, events)

        first = archive_old_events(db, archive, cutoff_days=5, now=now)
        second = archive_old_events(db, archive, cutoff_days=5, now=now)

        assert first["archived_count"] == 4
        assert second["archived_count"] == 0
        assert second["remaining_count"] == first["remaining_count"]

        arch = sqlite3.connect(archive)
        count = arch.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0]
        arch.close()
        assert count == 4  # no duplicate inserts on re-run

    def test_vacuum_reduces_file_size_after_bulk_delete(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        # Enough rows with padding to make VACUUM's effect measurable.
        events = []
        prev_hash = None
        for i in range(500):
            ts = (now - timedelta(days=499 - i)).isoformat()
            entry_hash = f"hash_{i}"
            events.append((f"evt_{i}", ts, prev_hash, entry_hash))
            prev_hash = entry_hash
        conn = sqlite3.connect(db)
        conn.executescript(_LIVE_SCHEMA)
        for event_id, ts, ph, eh in events:
            conn.execute(
                "INSERT INTO audit_events "
                "(event_id, event_type, severity, timestamp, source_module, details, "
                "prev_hash, entry_hash, bot_id) VALUES (?, 'test', 'LOW', ?, 'test', ?, ?, ?, 'openclaw')",
                (event_id, ts, "x" * 2000, ph, eh),
            )
        conn.commit()
        conn.close()

        size_before = db.stat().st_size
        result = archive_old_events(db, archive, cutoff_days=100, now=now)
        size_after = db.stat().st_size

        assert result["archived_count"] == 399
        assert size_after < size_before

    def test_waits_out_a_concurrent_writer_lock_instead_of_failing(self, tmp_path, now):
        """audit.db uses SQLite's default DELETE journal mode, which requires
        an exclusive lock for writes. The live gateway process holds that
        lock briefly while logging events; archive_old_events must wait it
        out (busy_timeout) rather than immediately raising 'database is
        locked' — this reproduces exactly that collision."""
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(10, now)
        _make_live_db(db, events)

        release_lock = threading.Event()
        lock_acquired = threading.Event()

        def hold_write_lock():
            conn = sqlite3.connect(db, timeout=1)
            conn.execute("BEGIN IMMEDIATE")
            conn.execute(
                "UPDATE audit_events SET severity = severity WHERE id = 1"
            )
            lock_acquired.set()
            release_lock.wait(timeout=5)
            conn.commit()
            conn.close()

        holder = threading.Thread(target=hold_write_lock)
        holder.start()
        lock_acquired.wait(timeout=2)

        def release_after_delay():
            time.sleep(0.3)
            release_lock.set()

        releaser = threading.Thread(target=release_after_delay)
        releaser.start()

        result = archive_old_events(db, archive, cutoff_days=5, now=now)

        holder.join(timeout=5)
        releaser.join(timeout=5)

        assert result["archived_count"] == 4

    def test_vacuum_failure_does_not_discard_a_successful_archive(self, tmp_path, now, monkeypatch):
        """A full disk (or any VACUUM-specific OperationalError) must not
        raise past a successful, already-committed archive+delete — that
        data-safety work already happened and must be reported as such."""
        import sqlite3 as sqlite3_module

        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(10, now)
        _make_live_db(db, events)

        class VacuumFailsConnection(sqlite3_module.Connection):
            def execute(self, sql, *a, **kw):
                if sql.strip().upper() == "VACUUM":
                    raise sqlite3_module.OperationalError("database or disk is full")
                return super().execute(sql, *a, **kw)

        real_connect = sqlite3_module.connect

        def failing_vacuum_connect(*args, **kwargs):
            kwargs["factory"] = VacuumFailsConnection
            return real_connect(*args, **kwargs)

        monkeypatch.setattr(
            "gateway.security.audit_archive.sqlite3.connect", failing_vacuum_connect
        )

        result = archive_old_events(db, archive, cutoff_days=5, now=now)

        assert result["archived_count"] == 4
        assert result["vacuum_succeeded"] is False

        live = sqlite3.connect(db)
        remaining_ids = {r[0] for r in live.execute("SELECT event_id FROM audit_events")}
        live.close()
        assert remaining_ids == {"evt_4", "evt_5", "evt_6", "evt_7", "evt_8", "evt_9"}

    def test_no_vacuum_flag_skips_vacuum(self, tmp_path, now):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        events = _chain_events(10, now)
        _make_live_db(db, events)

        # Should not raise even with vacuum disabled.
        result = archive_old_events(db, archive, cutoff_days=5, now=now, vacuum=False)
        assert result["archived_count"] == 4


def _make_mixed_live_db(path, n_noisy, n_denies, n_other_type):
    """n_noisy events of (egress_filter, INFO); n_denies of (egress_filter, HIGH);
    n_other_type of (gateway_startup, INFO). All independently chained (test
    doesn't care about chain correctness here, only about filter selectivity)."""
    conn = sqlite3.connect(path)
    conn.executescript(_LIVE_SCHEMA)
    i = 0
    for _ in range(n_noisy):
        conn.execute(
            "INSERT INTO audit_events (event_id, event_type, severity, timestamp, "
            "source_module, details, prev_hash, entry_hash, bot_id) "
            "VALUES (?, 'egress_filter', 'INFO', '2026-01-01T00:00:00Z', 'egress_filter', "
            "'{}', NULL, ?, 'openclaw')",
            (f"noisy_{i}", f"hash_{i}"),
        )
        i += 1
    for _ in range(n_denies):
        conn.execute(
            "INSERT INTO audit_events (event_id, event_type, severity, timestamp, "
            "source_module, details, prev_hash, entry_hash, bot_id) "
            "VALUES (?, 'egress_filter', 'HIGH', '2026-01-01T00:00:00Z', 'egress_filter', "
            "'{}', NULL, ?, 'openclaw')",
            (f"deny_{i}", f"hash_{i}"),
        )
        i += 1
    for _ in range(n_other_type):
        conn.execute(
            "INSERT INTO audit_events (event_id, event_type, severity, timestamp, "
            "source_module, details, prev_hash, entry_hash, bot_id) "
            "VALUES (?, 'gateway_startup', 'INFO', '2026-01-01T00:00:00Z', 'gateway', "
            "'{}', NULL, ?, 'openclaw')",
            (f"other_{i}", f"hash_{i}"),
        )
        i += 1
    conn.commit()
    conn.close()


class TestPurgeLowValueEvents:
    def test_purges_only_matching_event_type_and_severity(self, tmp_path):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        _make_mixed_live_db(db, n_noisy=25, n_denies=5, n_other_type=7)

        result = purge_low_value_events(
            db, archive, event_type="egress_filter", severity="INFO", batch_size=100
        )

        assert result["archived_count"] == 25
        assert result["remaining_count"] == 0  # none of this exact filter remain

        live = sqlite3.connect(db)
        remaining_total = live.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0]
        remaining_denies = live.execute(
            "SELECT COUNT(*) FROM audit_events WHERE event_type='egress_filter' AND severity='HIGH'"
        ).fetchone()[0]
        remaining_other = live.execute(
            "SELECT COUNT(*) FROM audit_events WHERE event_type='gateway_startup'"
        ).fetchone()[0]
        live.close()

        assert remaining_total == 12  # 5 denies + 7 other, untouched
        assert remaining_denies == 5
        assert remaining_other == 7

    def test_processes_in_multiple_batches(self, tmp_path):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        _make_mixed_live_db(db, n_noisy=25, n_denies=0, n_other_type=0)

        result = purge_low_value_events(
            db, archive, event_type="egress_filter", severity="INFO", batch_size=7
        )

        assert result["archived_count"] == 25
        assert result["batches"] == 4  # 7+7+7+4

        arch = sqlite3.connect(archive)
        count = arch.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0]
        arch.close()
        assert count == 25

    def test_idempotent_rerun_finds_nothing_left(self, tmp_path):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        _make_mixed_live_db(db, n_noisy=10, n_denies=2, n_other_type=1)

        first = purge_low_value_events(db, archive, "egress_filter", "INFO", batch_size=100)
        second = purge_low_value_events(db, archive, "egress_filter", "INFO", batch_size=100)

        assert first["archived_count"] == 10
        assert second["archived_count"] == 0
        assert second["batches"] == 0

        arch = sqlite3.connect(archive)
        count = arch.execute("SELECT COUNT(*) FROM audit_events").fetchone()[0]
        arch.close()
        assert count == 10  # no duplicate inserts

    def test_missing_db_reported_not_raised(self, tmp_path):
        db = tmp_path / "does_not_exist.db"
        archive = tmp_path / "archive.db"

        result = purge_low_value_events(db, archive, "egress_filter", "INFO")

        assert result["archived_count"] == 0
        assert result["skipped"] == "db_missing"

    def test_no_matching_rows_is_a_clean_noop(self, tmp_path):
        db = tmp_path / "audit.db"
        archive = tmp_path / "archive.db"
        _make_mixed_live_db(db, n_noisy=0, n_denies=3, n_other_type=2)

        result = purge_low_value_events(db, archive, "egress_filter", "INFO", batch_size=100)

        assert result["archived_count"] == 0
        assert result["batches"] == 0
        assert result["remaining_count"] == 0
