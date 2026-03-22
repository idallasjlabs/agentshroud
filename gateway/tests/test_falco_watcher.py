# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for FalcoAlertWatcher — enforcement bridge from Falco alerts to progressive lockdown.

Covers:
  - Alert deduplication (same alert not processed twice)
  - Non-CRITICAL alerts ignored
  - CRITICAL alert → record_block() called on progressive_lockdown
  - CRITICAL alert → audit_store.log_event() called
  - Missing alert directory → no-op (graceful degradation)
  - Alert watcher stops when stop() is called
"""
from __future__ import annotations

import asyncio
import json
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, call

import pytest

from gateway.security.falco_monitor import FalcoAlertWatcher


def _make_alert(rule: str, priority: str, container: str = "agentshroud-bot") -> dict:
    return {
        "time": "2026-03-22T10:00:00Z",
        "rule": rule,
        "priority": priority,
        "output": f"{rule} in {container}",
        "source": "syscall",
        "hostname": "gateway",
        "output_fields": {
            "container.id": "abc123",
            "container.name": container,
            "proc.name": "sh",
        },
    }


@pytest.mark.asyncio
async def test_critical_alert_triggers_lockdown():
    with tempfile.TemporaryDirectory() as tmpdir:
        alert_dir = Path(tmpdir)
        alert_file = alert_dir / "falco_alerts.json"
        alert_file.write_text(json.dumps(_make_alert("Container Shell Spawn", "Critical", "agentshroud-bot")) + "\n")

        lockdown = MagicMock()
        lockdown.record_block = MagicMock()
        audit_store = MagicMock()
        audit_store.log_event = AsyncMock()

        watcher = FalcoAlertWatcher(alert_dir=alert_dir, progressive_lockdown=lockdown, audit_store=audit_store)
        await watcher._process_new_alerts()

        lockdown.record_block.assert_called_once()
        call_args = lockdown.record_block.call_args
        assert call_args[0][0] == "agentshroud-bot"
        assert "Container Shell Spawn" in call_args[1].get("reason", call_args[0][1] if len(call_args[0]) > 1 else "")
        audit_store.log_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_warning_alert_not_blocked():
    with tempfile.TemporaryDirectory() as tmpdir:
        alert_dir = Path(tmpdir)
        alert_file = alert_dir / "falco_alerts.json"
        alert_file.write_text(json.dumps(_make_alert("Unexpected Network Connection", "Warning")) + "\n")

        lockdown = MagicMock()
        lockdown.record_block = MagicMock()

        watcher = FalcoAlertWatcher(alert_dir=alert_dir, progressive_lockdown=lockdown)
        await watcher._process_new_alerts()

        lockdown.record_block.assert_not_called()


@pytest.mark.asyncio
async def test_deduplication_same_alert_twice():
    with tempfile.TemporaryDirectory() as tmpdir:
        alert_dir = Path(tmpdir)
        alert = _make_alert("Privilege Escalation", "Critical")
        line = json.dumps(alert)
        (alert_dir / "falco_alerts.json").write_text(line + "\n" + line + "\n")

        lockdown = MagicMock()
        lockdown.record_block = MagicMock()

        watcher = FalcoAlertWatcher(alert_dir=alert_dir, progressive_lockdown=lockdown)
        await watcher._process_new_alerts()
        await watcher._process_new_alerts()  # second pass — everything already seen

        # Only called once despite two identical lines and two passes
        assert lockdown.record_block.call_count == 1


@pytest.mark.asyncio
async def test_missing_alert_dir_noop():
    watcher = FalcoAlertWatcher(alert_dir=Path("/nonexistent/falco"))
    # Should not raise
    await watcher._process_new_alerts()


@pytest.mark.asyncio
async def test_multiple_critical_alerts():
    with tempfile.TemporaryDirectory() as tmpdir:
        alert_dir = Path(tmpdir)
        alerts = [
            _make_alert("Container Shell Spawn", "Critical", "agentshroud-bot"),
            _make_alert("Secret File Access", "Emergency", "agentshroud-gateway"),
        ]
        (alert_dir / "falco_alerts.json").write_text("\n".join(json.dumps(a) for a in alerts) + "\n")

        lockdown = MagicMock()
        lockdown.record_block = MagicMock()

        watcher = FalcoAlertWatcher(alert_dir=alert_dir, progressive_lockdown=lockdown)
        await watcher._process_new_alerts()

        assert lockdown.record_block.call_count == 2


@pytest.mark.asyncio
async def test_stop_halts_run_loop():
    with tempfile.TemporaryDirectory() as tmpdir:
        watcher = FalcoAlertWatcher(alert_dir=Path(tmpdir))
        watcher._POLL_INTERVAL_SECS = 0  # no sleep delay in test

        poll_count = 0
        original = watcher._process_new_alerts

        async def counting_poll():
            nonlocal poll_count
            poll_count += 1
            watcher.stop()
            return await original()

        watcher._process_new_alerts = counting_poll
        await watcher.run()
        assert poll_count == 1
        assert not watcher._running


@pytest.mark.asyncio
async def test_no_progressive_lockdown_configured():
    """Watcher works without a lockdown module — only logs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        alert_dir = Path(tmpdir)
        (alert_dir / "falco_alerts.json").write_text(
            json.dumps(_make_alert("Container Shell Spawn", "Critical")) + "\n"
        )
        # Should not raise even with no lockdown module
        watcher = FalcoAlertWatcher(alert_dir=alert_dir, progressive_lockdown=None)
        await watcher._process_new_alerts()
