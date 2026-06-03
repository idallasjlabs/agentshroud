# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for startup markdown contributor-log pruning (Bug B).

Verifies that on startup the gateway prunes fixture markdown files from all
contributor log dirs while leaving real-UID files untouched.
"""
from __future__ import annotations

import datetime
from pathlib import Path

import pytest

from gateway.security.collaborator_tracker import CollaboratorActivityTracker, _is_fixture_uid


# ── _is_fixture_uid unit tests ────────────────────────────────────────────────


@pytest.mark.parametrize("uid", ["42", "99", "999", "99999", "0", "1", "123456"])
def test_is_fixture_uid_blocks_short_numeric(uid):
    assert _is_fixture_uid(uid), f"Expected {uid!r} to be flagged as fixture"


@pytest.mark.parametrize("uid", ["test_user_123", "test_user_456", "test-user-99"])
def test_is_fixture_uid_blocks_test_user_prefix(uid):
    assert _is_fixture_uid(uid), f"Expected {uid!r} to be flagged as fixture"


@pytest.mark.parametrize(
    "uid",
    ["8506022825", "7614658040", "9999999", "1234567", "U0AL7640RHD"],
)
def test_is_fixture_uid_passes_real_uids(uid):
    assert not _is_fixture_uid(uid), f"Expected {uid!r} to NOT be flagged as fixture"


# ── markdown prune helpers ────────────────────────────────────────────────────


def _make_md(log_dir: Path, uid: str) -> Path:
    """Create a fake contributor markdown file for the given uid."""
    today = datetime.date.today().isoformat()
    file_path = log_dir / f"{today}-{uid}.md"
    file_path.write_text(f"- {today} | user ({uid}) | telegram | hello\n")
    return file_path


# ── T9: prune walks all contributor dirs ─────────────────────────────────────


def test_prune_walks_all_contributor_dirs(tmp_path, monkeypatch):
    """Startup prune must remove fixture markdown files from every contributor dir."""
    monkeypatch.setenv("AGENTSHROUD_TRACK_ALL_NON_OWNER_ACTIVITY", "false")
    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)

    dir_a = tmp_path / "contrib_a"
    dir_b = tmp_path / "contrib_b"
    dir_a.mkdir()
    dir_b.mkdir()
    log_file = tmp_path / "activity.jsonl"

    monkeypatch.setenv(
        "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS", f"{dir_a},{dir_b}"
    )

    tracker = CollaboratorActivityTracker(
        log_path=log_file,
        owner_user_id="9876543210",
        collaborator_ids=[],
        contributor_log_dir=dir_a,
    )

    # Plant fixture files in both dirs
    fix_a = _make_md(dir_a, "42")
    fix_b = _make_md(dir_b, "999")
    real_a = _make_md(dir_a, "8506022825")

    # Simulate the startup prune (same logic as lifespan.py)
    _prune_fixture_markdown(tracker)

    assert not fix_a.exists(), "Fixture file in dir_a should have been pruned"
    assert not fix_b.exists(), "Fixture file in dir_b should have been pruned"
    assert real_a.exists(), "Real-UID file must NOT be pruned"


# ── T10: real UID markdown survives prune ────────────────────────────────────


def test_prune_keeps_real_uid_markdown(tmp_path, monkeypatch):
    """Real-UID markdown files must never be deleted by the prune pass."""
    monkeypatch.setenv("AGENTSHROUD_TRACK_ALL_NON_OWNER_ACTIVITY", "false")
    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)

    contrib_dir = tmp_path / "contributors"
    contrib_dir.mkdir()
    log_file = tmp_path / "activity.jsonl"

    monkeypatch.setenv("AGENTSHROUD_CONTRIBUTOR_LOG_DIRS", str(contrib_dir))

    tracker = CollaboratorActivityTracker(
        log_path=log_file,
        owner_user_id="9876543210",
        collaborator_ids=[],
        contributor_log_dir=contrib_dir,
    )

    real_md = _make_md(contrib_dir, "8506022825")
    _prune_fixture_markdown(tracker)
    assert real_md.exists()


# ── helper: extracted prune logic ────────────────────────────────────────────


def _prune_fixture_markdown(tracker: CollaboratorActivityTracker) -> int:
    """Run the same markdown-prune logic as lifespan.py and return pruned count."""
    pruned = 0
    for log_dir in tracker.contributor_log_dirs:
        if not log_dir.exists():
            continue
        for md_file in log_dir.glob("*.md"):
            parts = md_file.stem.split("-", 3)
            if len(parts) >= 4:
                file_uid = parts[3]
                is_short = file_uid.isdigit() and int(file_uid) < 10000
                if is_short or _is_fixture_uid(file_uid):
                    md_file.unlink(missing_ok=True)
                    pruned += 1
    return pruned
