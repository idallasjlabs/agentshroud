# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Behavior tests for ConfigIntegrityMonitor (gateway/security/config_integrity.py).

These tests exercise the tamper-detection state machine with a real temporary
filesystem: first-boot baseline establishment, unchanged runs, and the three
change events (modified / added / removed). No network, no sleeps, no mocks of
the code under test — only real files under pytest's tmp_path.
"""

from __future__ import annotations

import json

import pytest

from gateway.security.config_integrity import ConfigIntegrityMonitor


@pytest.fixture
def dirs(tmp_path):
    """Return (bot_config_dir, baseline_path) rooted in an isolated tmp dir."""
    cfg = tmp_path / "bot-config"
    cfg.mkdir()
    baseline = tmp_path / "gateway-data" / "config-integrity-baseline.json"
    return cfg, baseline


def _write_openclaw(cfg_dir, content: str) -> None:
    (cfg_dir / "openclaw.json").write_text(content, encoding="utf-8")


def test_first_boot_establishes_baseline_without_alerts(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, '{"tools": ["read"]}')
    mon = ConfigIntegrityMonitor(cfg, baseline)

    changes = mon.check()

    # First boot must be silent: every file "looks new" so no alert fires.
    assert changes == []
    # Baseline is persisted so the next run has something to compare against.
    assert baseline.exists()
    stored = json.loads(baseline.read_text())
    assert "openclaw.json" in stored["hashes"]
    assert stored["hashes"]["openclaw.json"] is not None
    assert "updated_at" in stored


def test_unchanged_second_run_reports_no_changes(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, '{"tools": ["read"]}')
    mon = ConfigIntegrityMonitor(cfg, baseline)

    mon.check()  # establish baseline
    changes = mon.check()  # nothing changed

    assert changes == []


def test_modified_file_is_detected(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, '{"tools": ["read"]}')
    mon = ConfigIntegrityMonitor(cfg, baseline)
    mon.check()  # baseline of original content

    _write_openclaw(cfg, '{"tools": ["read", "write", "delete"]}')  # tamper
    changes = mon.check()

    assert len(changes) == 1
    rec = changes[0]
    assert rec["file"] == "openclaw.json"
    assert rec["event"] == "modified"
    assert rec["previous"] is not None
    assert rec["current"] is not None
    assert rec["previous"] != rec["current"]


def test_removed_file_is_detected(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, '{"tools": ["read"]}')
    mon = ConfigIntegrityMonitor(cfg, baseline)
    mon.check()  # baseline with the file present

    (cfg / "openclaw.json").unlink()  # file deleted
    changes = mon.check()

    assert len(changes) == 1
    assert changes[0]["event"] == "removed"
    assert changes[0]["previous"] is not None
    assert changes[0]["current"] is None


def test_added_file_is_detected(dirs):
    cfg, baseline = dirs
    # Seed a baseline where openclaw.json is absent (hash None), by writing the
    # baseline file directly to simulate a prior run with no config present.
    baseline.parent.mkdir(parents=True, exist_ok=True)
    baseline.write_text(json.dumps({"updated_at": 0, "hashes": {"openclaw.json": None}}))
    mon = ConfigIntegrityMonitor(cfg, baseline)

    _write_openclaw(cfg, '{"tools": ["read"]}')  # file appears
    changes = mon.check()

    assert len(changes) == 1
    assert changes[0]["event"] == "added"
    assert changes[0]["previous"] is None
    assert changes[0]["current"] is not None


def test_tamper_baseline_is_not_advanced_so_alert_refires(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, "original")
    mon = ConfigIntegrityMonitor(cfg, baseline)
    mon.check()  # baseline = hash(original)
    original_baseline = baseline.read_text()

    _write_openclaw(cfg, "tampered")
    first = mon.check()
    assert first and first[0]["event"] == "modified"
    # Baseline must NOT advance on tamper, so the alert persists across restarts.
    assert baseline.read_text() == original_baseline

    # Re-running with the still-tampered file re-fires the same alert.
    second = mon.check()
    assert second and second[0]["event"] == "modified"


def test_baseline_advances_only_when_clean(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, "v1")
    mon = ConfigIntegrityMonitor(cfg, baseline)
    mon.check()
    b1 = json.loads(baseline.read_text())

    # A clean re-run rewrites the baseline (updated_at moves forward or equal),
    # and the stored hash still matches the current file.
    mon.check()
    b2 = json.loads(baseline.read_text())
    assert b2["hashes"] == b1["hashes"]


def test_reset_baseline_accepts_current_state(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, "original")
    mon = ConfigIntegrityMonitor(cfg, baseline)
    mon.check()  # baseline = original

    _write_openclaw(cfg, "owner-rebuilt-config")
    mon.reset_baseline()  # owner acknowledges the change

    # After reset, the new content is the accepted baseline: no changes reported.
    changes = mon.check()
    assert changes == []
    stored = json.loads(baseline.read_text())
    assert stored["hashes"]["openclaw.json"] is not None


def test_hash_file_returns_none_for_missing(dirs):
    cfg, baseline = dirs
    mon = ConfigIntegrityMonitor(cfg, baseline)
    assert mon._hash_file(cfg / "does-not-exist.json") is None


def test_hash_file_is_stable_and_content_sensitive(dirs):
    cfg, baseline = dirs
    _write_openclaw(cfg, "abc")
    mon = ConfigIntegrityMonitor(cfg, baseline)
    p = cfg / "openclaw.json"
    h1 = mon._hash_file(p)
    h2 = mon._hash_file(p)
    assert h1 == h2  # deterministic
    _write_openclaw(cfg, "abcd")
    assert mon._hash_file(p) != h1  # content-sensitive


def test_load_baseline_tolerates_corrupt_json(dirs):
    cfg, baseline = dirs
    baseline.parent.mkdir(parents=True, exist_ok=True)
    baseline.write_text("{ this is not valid json ")
    mon = ConfigIntegrityMonitor(cfg, baseline)
    # Corrupt baseline is treated as "no baseline" → empty dict, not a crash.
    assert mon._load_baseline() == {}


def test_load_baseline_missing_file_returns_empty(dirs):
    cfg, baseline = dirs
    mon = ConfigIntegrityMonitor(cfg, baseline)
    assert mon._load_baseline() == {}


def test_format_alert_text_includes_event_and_hash_prefixes(dirs):
    cfg, baseline = dirs
    mon = ConfigIntegrityMonitor(cfg, baseline)
    changes = [
        {
            "file": "openclaw.json",
            "previous": "aaaaaaaabbbbbbbb",
            "current": "ccccccccdddddddd",
            "event": "modified",
        }
    ]
    text = mon.format_alert_text(changes)
    assert "Config Integrity Alert" in text
    assert "openclaw.json" in text
    assert "MODIFIED" in text
    assert "aaaaaaaa" in text  # previous prefix (8 chars)
    assert "cccccccc" in text  # current prefix (8 chars)


def test_format_alert_text_handles_missing_hashes(dirs):
    cfg, baseline = dirs
    mon = ConfigIntegrityMonitor(cfg, baseline)
    changes = [
        {"file": "openclaw.json", "previous": None, "current": "abcd1234", "event": "added"},
        {"file": "openclaw.json", "previous": "abcd1234", "current": None, "event": "removed"},
    ]
    text = mon.format_alert_text(changes)
    assert "MISSING" in text
    assert "ADDED" in text
    assert "REMOVED" in text
