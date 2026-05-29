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
    assert entry["is_owner"] is False


def test_username_is_normalized_for_log_safety(tracker, log_file):
    tracker.record_activity("7614658040", "Ali|ce (ops)", "Hello", "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert entry["username"] == "Ali/ce [ops]"


def test_owner_is_recorded_with_is_owner_flag(tracker, log_file):
    """Owner messages are now recorded with is_owner=True (not silently dropped)."""
    tracker.record_activity("1111111", "Owner", "secret command", "telegram")
    assert log_file.exists() and log_file.read_text().strip() != ""
    entry = json.loads(log_file.read_text().strip())
    assert entry["user_id"] == "1111111"
    assert entry["is_owner"] is True


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


def test_get_activity_ignores_non_numeric_timestamps(tracker, log_file):
    log_file.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "timestamp": "not-a-number",
                        "user_id": "7614658040",
                        "username": "Alice",
                        "message_preview": "bad-ts",
                        "source": "telegram",
                    }
                ),
                json.dumps(
                    {
                        "timestamp": time.time(),
                        "user_id": "7614658040",
                        "username": "Alice",
                        "message_preview": "good-ts",
                        "source": "telegram",
                    }
                ),
            ]
        )
    )
    results = tracker.get_activity(since=time.time() - 60)
    assert len(results) == 1
    assert results[0]["message_preview"] == "good-ts"


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


def test_summary_handles_non_numeric_timestamps(tracker, log_file):
    log_file.write_text(
        json.dumps(
            {
                "timestamp": "not-a-number",
                "user_id": "7614658040",
                "username": "Alice",
                "message_preview": "bad-ts",
                "source": "telegram",
            }
        )
        + "\n"
    )
    s = tracker.get_activity_summary()
    assert s["total_messages"] == 1
    assert s["last_activity"] == 0.0
    assert s["by_user"]["7614658040"]["last_active"] == 0.0


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


def test_record_activity_mirror_handles_delimiter_chars_in_username(tracker, log_file):
    tracker.record_activity("7614658040", "Ali|ce (ops)", "Need update", "telegram")
    contributor_dir = log_file.parent / "contributors"
    file_path = next(iter(contributor_dir.glob("*-7614658040.md")))
    content = file_path.read_text()
    assert "Ali/ce [ops] (7614658040)" in content


# ── correlation_id and is_owner ───────────────────────────────────────────────


def test_correlation_id_included_when_provided(tracker, log_file):
    tracker.record_activity(
        "7614658040", "Alice", "hello", "telegram", correlation_id="7614658040:42"
    )
    entry = json.loads(log_file.read_text().strip())
    assert entry["correlation_id"] == "7614658040:42"


def test_correlation_id_absent_when_not_provided(tracker, log_file):
    tracker.record_activity("7614658040", "Alice", "hello", "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert "correlation_id" not in entry


def test_collaborator_entry_has_is_owner_false(tracker, log_file):
    tracker.record_activity("9999999", "Bob", "hey", "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert entry["is_owner"] is False


def test_owner_correlation_id_is_stored(tracker, log_file):
    tracker.record_activity(
        "1111111", "Owner", "run scan", "telegram", correlation_id="1111111:100"
    )
    entry = json.loads(log_file.read_text().strip())
    assert entry["is_owner"] is True
    assert entry["correlation_id"] == "1111111:100"


# ── bot_id field (M4) ────────────────────────────────────────────────────────


def test_record_activity_stores_bot_id_when_provided(tracker, log_file):
    """record_activity with bot_id='hermes' stores bot_id in the entry."""
    tracker.record_activity("7614658040", "Alice", "hello", "telegram", bot_id="hermes")
    entry = json.loads(log_file.read_text().strip())
    assert entry["bot_id"] == "hermes"


def test_record_activity_stores_bot_id_none_when_omitted(tracker, log_file):
    """record_activity without bot_id stores bot_id=None in the entry."""
    tracker.record_activity("7614658040", "Alice", "hello", "telegram")
    entry = json.loads(log_file.read_text().strip())
    assert entry["bot_id"] is None


def test_get_activity_filters_by_bot_id(tracker, log_file):
    """get_activity(bot_id=...) returns only entries matching that bot_id."""
    tracker.record_activity("7614658040", "Alice", "from hermes", "telegram", bot_id="hermes")
    tracker.record_activity("9999999", "Bob", "from openclaw", "telegram", bot_id="openclaw")
    tracker.record_activity("7614658040", "Alice", "no bot id", "telegram")

    hermes_entries = tracker.get_activity(bot_id="hermes")
    assert len(hermes_entries) == 1
    assert hermes_entries[0]["message_preview"] == "from hermes"

    openclaw_entries = tracker.get_activity(bot_id="openclaw")
    assert len(openclaw_entries) == 1
    assert openclaw_entries[0]["message_preview"] == "from openclaw"

    # Without filter: all three entries returned
    all_entries = tracker.get_activity()
    assert len(all_entries) == 3


def test_get_activity_summary_includes_by_bot(tracker, log_file):
    """get_activity_summary returns a by_bot breakdown keyed by bot_id."""
    tracker.record_activity("7614658040", "Alice", "msg1", "telegram", bot_id="hermes")
    tracker.record_activity("7614658040", "Alice", "msg2", "telegram", bot_id="hermes")
    tracker.record_activity("9999999", "Bob", "msg3", "telegram", bot_id="openclaw")
    tracker.record_activity("9999999", "Bob", "msg4", "telegram")  # no bot_id → "unknown"

    s = tracker.get_activity_summary()
    assert "by_bot" in s
    assert s["by_bot"]["hermes"] == 2
    assert s["by_bot"]["openclaw"] == 1
    assert s["by_bot"]["unknown"] == 1


def test_get_activity_summary_by_bot_empty_when_no_file(tracker):
    """get_activity_summary returns empty by_bot when no log file exists."""
    s = tracker.get_activity_summary()
    assert s["by_bot"] == {}


@pytest.mark.asyncio
async def test_webhook_receiver_passes_agent_id_as_bot_id():
    """process_webhook passes agent_id as bot_id to record_activity."""
    from unittest.mock import MagicMock, patch

    from gateway.proxy.webhook_receiver import WebhookReceiver

    tracker = MagicMock()
    mock_session = MagicMock()
    mock_session.add_conversation_message = MagicMock()

    receiver = WebhookReceiver(pipeline=None, forwarder=None, session_manager=mock_session)

    # Patch the lazy import of app_state inside the function body
    mock_state = MagicMock()
    mock_state.collaborator_tracker = tracker

    with (
        patch("gateway.ingest_api.state.app_state", mock_state),
        patch.object(receiver, "_extract_user_id", return_value="7614658040"),
        patch.object(receiver, "_extract_username", return_value="TestUser"),
    ):
        await receiver.process_webhook(
            payload={"message": {"text": "hello from hermes"}},
            source="telegram",
            agent_id="hermes",
        )

    tracker.record_activity.assert_called_once()
    call_kwargs = tracker.record_activity.call_args.kwargs
    assert call_kwargs["bot_id"] == "hermes"


# ── pruner heuristic ──────────────────────────────────────────────────────────


def test_pruner_short_numeric_ids_are_test_fixtures():
    """IDs < 10000 should be treated as test fixtures by the pruner heuristic."""
    test_ids = ["42", "99", "999", "1234"]
    for uid in test_ids:
        assert uid.isdigit() and int(uid) < 10000, f"{uid} should be flagged as test fixture"


def test_pruner_real_telegram_uids_not_flagged():
    """Real Telegram UIDs (9-10 digits) must NOT be pruned."""
    real_ids = ["7614658040", "8506022825", "123456789012"]
    for uid in real_ids:
        assert not (uid.isdigit() and int(uid) < 10000), f"{uid} should NOT be flagged"
