# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Unit tests for CollaboratorActivityTracker."""

import json
import time
from pathlib import Path

import pytest

from gateway.security.collaborator_tracker import CollaboratorActivityTracker


@pytest.fixture
def log_file(tmp_path):
    return tmp_path / "collab.jsonl"


@pytest.fixture
def tracker(log_file, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_TRACK_ALL_NON_OWNER_ACTIVITY", "false")
    contributor_dir = log_file.parent / "contributors"
    mirror_dir = log_file.parent / "contributors-mirror"
    monkeypatch.setenv(
        "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS",
        f"{contributor_dir},{mirror_dir}",
    )
    return CollaboratorActivityTracker(
        log_path=log_file,
        owner_user_id="1111111",
        collaborator_ids=["7614658040", "9999999"],
        contributor_log_dir=contributor_dir,
    )


# ── record_activity ───────────────────────────────────────────────────────────

def test_records_known_collaborator(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "Hello there!", "telegram")
    lines = log_file.read_text().strip().split("\n")
    assert len(lines) == 1
    entry = json.loads(lines[0])
    assert entry["user_id"] == "7614658040"
    assert entry["username"] == "Alice"
    assert entry["message_preview"] == "Hello there!"
    assert entry["source"] == "telegram"
    assert "timestamp" in entry


def test_owner_is_never_recorded(tracker, log_file):
    tracker.record_activity("1111111", "Owner", "secret command", "telegram")
    assert not log_file.exists() or log_file.read_text().strip() == ""


def test_unknown_user_is_skipped(tracker, log_file):
    tracker.record_activity("0000000", "Stranger", "who am i", "telegram")
    assert not log_file.exists() or log_file.read_text().strip() == ""


def test_unknown_user_recorded_when_dynamic_tracking_enabled(log_file, monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_TRACK_ALL_NON_OWNER_ACTIVITY", "true")
    contributor_dir = log_file.parent / "contributors"
    mirror_dir = log_file.parent / "contributors-mirror"
    monkeypatch.setenv(
        "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS",
        f"{contributor_dir},{mirror_dir}",
    )
    tracker = CollaboratorActivityTracker(
        log_path=log_file,
        owner_user_id="1111111",
        collaborator_ids=[],
        contributor_log_dir=contributor_dir,
    )
    tracker.record_activity("0000000", "Stranger", "who am i", "telegram")
    assert log_file.exists()
    lines = log_file.read_text().strip().split("\n")
    assert len(lines) == 1
    entry = json.loads(lines[0])
    assert entry["user_id"] == "0000000"


def test_message_preview_truncated(tracker, log_file):
    long_msg = "a" * 200
    tracker.record_activity("7614658040", "Alice", long_msg, "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert len(entry["message_preview"]) == 80


def test_message_preview_newlines_normalized(tracker, log_file):
    msg = "line1\nline2\tline3\rline4"
    tracker.record_activity("7614658040", "Alice", msg, "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert entry["message_preview"] == "line1 line2 line3 line4"


def test_multiple_entries_appended(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "msg1", "telegram")
    tracker.record_activity("9999999", "Bob", "msg2", "telegram")
    lines = log_file.read_text().strip().split("\n")
    assert len(lines) == 2


# ── get_activity ──────────────────────────────────────────────────────────────

def test_get_activity_returns_empty_when_no_file(tracker, log_file):
    assert tracker.get_activity() == []


def test_get_activity_returns_entries_newest_first(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "first", "telegram")
    time.sleep(0.01)
    tracker.record_activity("9999999", "Bob", "second", "telegram")
    results = tracker.get_activity()
    assert len(results) == 2
    assert results[0]["message_preview"] == "second"
    assert results[1]["message_preview"] == "first"


def test_get_activity_respects_since(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "old", "telegram")
    boundary = time.time()
    time.sleep(0.01)
    tracker.record_activity("9999999", "Bob", "new", "telegram")
    results = tracker.get_activity(since=boundary)
    assert len(results) == 1
    assert results[0]["message_preview"] == "new"


def test_get_activity_respects_limit(tracker, log_file):
    for i in range(10):
        tracker.record_activity("7614658040", "Alice", f"msg{i}", "telegram")
    results = tracker.get_activity(limit=3)
    assert len(results) == 3


# ── get_activity_summary ──────────────────────────────────────────────────────

def test_summary_empty_when_no_file(tracker):
    s = tracker.get_activity_summary()
    assert s["total_messages"] == 0
    assert s["unique_users"] == 0
    assert s["last_activity"] is None
    assert s["by_user"] == {}


def test_summary_counts(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "hi", "telegram")
    tracker.record_activity("7614658040", "Alice", "again", "telegram")
    tracker.record_activity("9999999", "Bob", "hello", "telegram")
    s = tracker.get_activity_summary()
    assert s["total_messages"] == 3
    assert s["unique_users"] == 2
    assert s["last_activity"] is not None
    assert s["by_user"]["7614658040"]["message_count"] == 2
    assert s["by_user"]["9999999"]["message_count"] == 1


def test_summary_last_activity_is_latest_timestamp(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "first", "telegram")
    time.sleep(0.01)
    tracker.record_activity("9999999", "Bob", "last", "telegram")
    s = tracker.get_activity_summary()
    assert s["by_user"]["9999999"]["last_active"] > s["by_user"]["7614658040"]["last_active"]
    assert s["last_activity"] == pytest.approx(s["by_user"]["9999999"]["last_active"], abs=1)


def test_record_activity_mirrors_to_contributor_daily_log(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "Need weather update", "telegram")
    contributor_dir = log_file.parent / "contributors"
    mirror_dir = log_file.parent / "contributors-mirror"
    primary_files = list(contributor_dir.glob("*-7614658040.md"))
    mirror_files = list(mirror_dir.glob("*-7614658040.md"))
    assert len(primary_files) == 1
    assert len(mirror_files) == 1
    for content in (primary_files[0].read_text(), mirror_files[0].read_text()):
        assert "Alice (7614658040)" in content
        assert "Need weather update" in content


def test_record_activity_mirror_is_single_line_for_multiline_message(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "Need\nweather\tupdate", "telegram")
    contributor_dir = log_file.parent / "contributors"
    file_path = next(iter(contributor_dir.glob("*-7614658040.md")))
    content = file_path.read_text()
    assert "Need weather update" in content
    # one markdown log line + trailing newline
    assert content.count("\n") == 1
