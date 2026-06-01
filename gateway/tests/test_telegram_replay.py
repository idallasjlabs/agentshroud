# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for UpdateReplayBuffer (gateway/proxy/telegram_replay.py)."""
from __future__ import annotations

import json
import sqlite3
import time
import unittest.mock

import pytest

from gateway.proxy.telegram_replay import UpdateReplayBuffer


@pytest.fixture
def buf(tmp_path):
    return UpdateReplayBuffer(db_path=str(tmp_path / "replay.sqlite3"))


def _update(update_id: int, text: str = "hi") -> dict:
    return {
        "update_id": update_id,
        "message": {"message_id": update_id, "text": text, "from": {"id": 999}},
    }


# ── core CRUD ─────────────────────────────────────────────────────────────────

def test_record_then_pull_returns_undelivered(buf):
    updates = [_update(1), _update(2)]
    buf.record_inbound("hermes", updates)
    # Need to bypass the 30s grace window for this test
    # Set received_at to well in the past
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert len(result) == 2
    ids = {u["update_id"] for u in result}
    assert ids == {1, 2}


def test_mark_delivered_excludes_from_pull(buf):
    buf.record_inbound("hermes", [_update(1), _update(2), _update(3)])
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    buf.mark_delivered("hermes", 3)  # marks update_id < 3 as delivered
    result = buf.pull_undelivered("hermes", older_than_s=30)
    ids = {u["update_id"] for u in result}
    assert ids == {3}  # only update_id=3 remains undelivered


def test_grace_window_excludes_recent(buf):
    buf.record_inbound("hermes", [_update(10)])
    # Do NOT adjust received_at — it was just inserted (< 30s ago)
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []


def test_cleanup_drops_old_rows(buf):
    buf.record_inbound("hermes", [_update(99)])
    # Back-date received_at beyond retention window (86400s)
    buf._conn.execute("UPDATE replay SET received_at = received_at - 86401")
    buf._conn.commit()
    # Force cleanup on next call
    buf._call_count = 999
    buf.cleanup_if_due()
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []


def test_multibot_isolation(buf):
    buf.record_inbound("hermes", [_update(1)])
    buf.record_inbound("openclaw", [_update(1)])
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    # Mark hermes update as delivered
    buf.mark_delivered("hermes", 2)
    hermes_result = buf.pull_undelivered("hermes", older_than_s=30)
    openclaw_result = buf.pull_undelivered("openclaw", older_than_s=30)
    assert hermes_result == []
    assert len(openclaw_result) == 1


def test_duplicate_record_is_ignored(buf):
    updates = [_update(5)]
    buf.record_inbound("hermes", updates)
    buf.record_inbound("hermes", updates)  # duplicate INSERT OR IGNORE
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert len(result) == 1  # deduplicated


# ── fault tolerance ────────────────────────────────────────────────────────────

def test_sqlite_failure_does_not_raise(tmp_path):
    bad_buf = UpdateReplayBuffer(db_path="/nonexistent/path/replay.sqlite3")
    # All methods must silently noop when DB is unavailable
    bad_buf.record_inbound("hermes", [_update(1)])
    assert bad_buf.pull_undelivered("hermes") == []
    bad_buf.mark_delivered("hermes", 100)
    bad_buf.cleanup_if_due()  # must not raise


def test_cleanup_interval_guard(buf):
    buf.record_inbound("hermes", [_update(1)])
    buf._call_count = 0
    # cleanup_if_due at count=1 should NOT delete (only at multiples of 1000)
    buf.cleanup_if_due()
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert len(result) == 1  # cleanup didn't run


def test_record_inbound_skips_updates_without_update_id(buf):
    updates = [{"message": {"text": "no update_id here"}}]
    buf.record_inbound("hermes", updates)  # must not raise
    buf._conn.execute("UPDATE replay SET received_at = received_at - 60")
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []  # nothing inserted


def test_record_inbound_db_error_swallowed(buf):
    # Force a DB error by closing the connection
    buf._conn.close()
    buf._conn = None
    buf.record_inbound("hermes", [_update(1)])  # must not raise


def test_mark_delivered_db_error_swallowed(buf):
    buf._conn.close()
    buf._conn = None
    buf.mark_delivered("hermes", 100)  # must not raise


def test_pull_undelivered_db_error_swallowed(buf):
    buf._conn.close()
    buf._conn = None
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []


def test_pull_undelivered_handles_corrupt_payload(buf):
    # Insert a row with corrupt JSON payload directly
    buf._conn.execute(
        "INSERT OR IGNORE INTO replay (bot_id,update_id,received_at,payload) VALUES (?,?,?,?)",
        ("hermes", 42, int(time.time()) - 60, "{corrupt"),
    )
    buf._conn.commit()
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []  # corrupt row silently skipped


def test_cleanup_db_error_swallowed(buf):
    buf._conn.close()
    buf._conn = None
    buf._call_count = _cleanup_call_count_for_next_cleanup(buf)
    buf.cleanup_if_due()  # must not raise


def _cleanup_call_count_for_next_cleanup(buf):
    from gateway.proxy.telegram_replay import _CLEANUP_EVERY
    return _CLEANUP_EVERY - 1


# ── exception handlers on live-but-failing DB connections ────────────────────

def test_record_inbound_executemany_exception_swallowed(buf):
    """Exception during executemany (valid conn, SQL error) must be swallowed."""
    mock_conn = unittest.mock.MagicMock()
    mock_conn.executemany.side_effect = sqlite3.OperationalError("fail")
    buf._conn = mock_conn
    buf.record_inbound("hermes", [_update(1)])  # must not raise


def test_mark_delivered_execute_exception_swallowed(buf):
    """Exception during execute in mark_delivered must be swallowed."""
    mock_conn = unittest.mock.MagicMock()
    mock_conn.execute.side_effect = sqlite3.OperationalError("fail")
    buf._conn = mock_conn
    buf.mark_delivered("hermes", 100)  # must not raise


def test_pull_undelivered_execute_exception_swallowed(buf):
    """Exception during execute in pull_undelivered must return empty list."""
    mock_conn = unittest.mock.MagicMock()
    mock_conn.execute.side_effect = sqlite3.OperationalError("fail")
    buf._conn = mock_conn
    result = buf.pull_undelivered("hermes", older_than_s=30)
    assert result == []


def test_cleanup_execute_exception_swallowed(buf):
    """Exception during cleanup execute must be swallowed."""
    mock_conn = unittest.mock.MagicMock()
    mock_conn.execute.side_effect = sqlite3.OperationalError("fail")
    buf._conn = mock_conn
    buf._call_count = 999  # one before threshold
    buf.cleanup_if_due()  # must not raise
