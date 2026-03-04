# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
TDD tests for D1: Observatory Mode /api/mode endpoint (v0.8.0).

Tests:
  1. GET /api/mode returns current AGENTSHROUD_MODE (default "enforce")
  2. PUT /api/mode with valid mode sets os.environ["AGENTSHROUD_MODE"]
  3. PUT /api/mode with invalid mode → 400
  4. PUT /api/mode to non-enforce writes CRITICAL log entry
  5. PUT /api/mode revert_after_minutes is clamped to [1, 480]
  6. Multiple PUT calls cancel the previous revert task
  7. Auto-revert task runs (short sleep, monkeypatched)
  8. ModeRequest model: default revert_after_minutes is 30

D2 kill switch verification assertions also live here.
"""
from __future__ import annotations

import asyncio
import os
import logging
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import gateway.web.api as api_module
from gateway.web.api import router, ModeRequest, VALID_AGENTSHROUD_MODES


# ── app fixture ─────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def reset_env_and_task():
    """Reset AGENTSHROUD_MODE and cancel any revert task between tests."""
    original = os.environ.get("AGENTSHROUD_MODE")
    api_module._revert_task = None
    yield
    # Restore
    if original is None:
        os.environ.pop("AGENTSHROUD_MODE", None)
    else:
        os.environ["AGENTSHROUD_MODE"] = original
    # Cancel outstanding task to avoid test bleed
    task = api_module._revert_task
    if task and not task.done():
        task.cancel()
    api_module._revert_task = None


def _make_app() -> FastAPI:
    """Minimal FastAPI app that mounts the management router with auth bypassed."""
    app = FastAPI()
    # Override auth dependency to always succeed
    from gateway.web.api import require_auth
    app.dependency_overrides[require_auth] = lambda: "test"
    app.include_router(router)
    return app


@pytest.fixture
def client():
    return TestClient(_make_app())


# ── GET /api/mode ───────────────────────────────────────────────────────────

class TestGetMode:
    def test_default_mode_is_enforce(self, client):
        os.environ.pop("AGENTSHROUD_MODE", None)
        resp = client.get("/api/mode")
        assert resp.status_code == 200
        assert resp.json()["mode"] == "enforce"

    def test_returns_monitor_when_set(self, client):
        os.environ["AGENTSHROUD_MODE"] = "monitor"
        resp = client.get("/api/mode")
        assert resp.status_code == 200
        assert resp.json()["mode"] == "monitor"

    def test_returns_observatory_when_set(self, client):
        os.environ["AGENTSHROUD_MODE"] = "observatory"
        resp = client.get("/api/mode")
        assert resp.status_code == 200
        assert resp.json()["mode"] == "observatory"

    def test_response_includes_timestamp(self, client):
        resp = client.get("/api/mode")
        assert "timestamp" in resp.json()


# ── PUT /api/mode ────────────────────────────────────────────────────────────

class TestSetMode:
    def test_set_monitor_mode(self, client):
        resp = client.put("/api/mode", json={"mode": "monitor"})
        assert resp.status_code == 200
        assert os.environ.get("AGENTSHROUD_MODE") == "monitor"

    def test_set_observatory_mode(self, client):
        resp = client.put("/api/mode", json={"mode": "observatory"})
        assert resp.status_code == 200
        assert os.environ.get("AGENTSHROUD_MODE") == "observatory"

    def test_set_enforce_mode(self, client):
        os.environ["AGENTSHROUD_MODE"] = "observatory"
        resp = client.put("/api/mode", json={"mode": "enforce"})
        assert resp.status_code == 200
        assert os.environ.get("AGENTSHROUD_MODE") == "enforce"

    def test_invalid_mode_returns_400(self, client):
        resp = client.put("/api/mode", json={"mode": "godmode"})
        assert resp.status_code == 400

    def test_response_includes_previous_mode(self, client):
        os.environ["AGENTSHROUD_MODE"] = "monitor"
        resp = client.put("/api/mode", json={"mode": "observatory"})
        data = resp.json()
        assert data["previous_mode"] == "monitor"
        assert data["mode"] == "observatory"

    def test_response_includes_revert_minutes(self, client):
        resp = client.put("/api/mode", json={"mode": "monitor", "revert_after_minutes": 15})
        assert resp.json()["auto_revert_in_minutes"] == 15

    def test_default_revert_minutes_is_30(self, client):
        resp = client.put("/api/mode", json={"mode": "monitor"})
        assert resp.json()["auto_revert_in_minutes"] == 30

    def test_revert_minutes_clamped_min(self, client):
        """revert_after_minutes below 1 is clamped to 1."""
        resp = client.put("/api/mode", json={"mode": "monitor", "revert_after_minutes": 0})
        assert resp.json()["auto_revert_in_minutes"] == 1

    def test_revert_minutes_clamped_max(self, client):
        """revert_after_minutes above 480 is clamped to 480."""
        resp = client.put("/api/mode", json={"mode": "monitor", "revert_after_minutes": 9999})
        assert resp.json()["auto_revert_in_minutes"] == 480


# ── CRITICAL log on non-enforce ──────────────────────────────────────────────

class TestCriticalLogging:
    def test_critical_logged_when_setting_non_enforce(self, client, caplog):
        with caplog.at_level(logging.CRITICAL, logger="agentshroud.web.api"):
            client.put("/api/mode", json={"mode": "observatory"})
        assert any(r.levelno == logging.CRITICAL for r in caplog.records), (
            f"Expected CRITICAL log; got: {[r.levelname for r in caplog.records]}"
        )

    def test_no_critical_when_setting_enforce(self, client, caplog):
        os.environ["AGENTSHROUD_MODE"] = "observatory"
        with caplog.at_level(logging.CRITICAL, logger="agentshroud.web.api"):
            client.put("/api/mode", json={"mode": "enforce"})
        assert not any(r.levelno == logging.CRITICAL for r in caplog.records)


# ── Auto-revert task ─────────────────────────────────────────────────────────

class TestAutoRevert:
    @pytest.mark.asyncio
    async def test_revert_task_created_on_put(self):
        """A revert task is created (and is an asyncio.Task)."""
        app = _make_app()
        from fastapi.testclient import TestClient
        async with app.router.lifespan_context(app):
            pass  # not needed — just verify task creation
        # Call the endpoint function directly to avoid event-loop issues
        from gateway.web.api import set_mode
        req = ModeRequest(mode="monitor", revert_after_minutes=60)
        await set_mode(req, user="test")
        task = api_module._revert_task
        assert task is not None
        assert isinstance(task, asyncio.Task)
        task.cancel()

    @pytest.mark.asyncio
    async def test_second_put_cancels_previous_task(self):
        """Second PUT cancels the first revert task."""
        from gateway.web.api import set_mode
        req1 = ModeRequest(mode="monitor", revert_after_minutes=60)
        await set_mode(req1, user="test")
        first_task = api_module._revert_task

        req2 = ModeRequest(mode="observatory", revert_after_minutes=60)
        await set_mode(req2, user="test")

        # Yield so the cancellation exception is delivered
        await asyncio.sleep(0)

        # The first task should be cancelled or done
        assert first_task.cancelled() or first_task.done()
        # New task is a different object
        assert api_module._revert_task is not first_task
        api_module._revert_task.cancel()

    @pytest.mark.asyncio
    async def test_auto_revert_restores_enforce(self, monkeypatch):
        """Auto-revert task sets mode back to enforce after delay."""
        from gateway.web.api import set_mode

        sleep_calls = []

        async def fast_sleep(seconds):
            sleep_calls.append(seconds)
            # Don't actually sleep — just record the call

        monkeypatch.setattr(asyncio, "sleep", fast_sleep)
        os.environ["AGENTSHROUD_MODE"] = "enforce"

        req = ModeRequest(mode="monitor", revert_after_minutes=5)
        await set_mode(req, user="test")

        # Mode is now "monitor"
        assert os.environ.get("AGENTSHROUD_MODE") == "monitor"

        # Drain the task
        task = api_module._revert_task
        await asyncio.sleep(0)  # yield to allow task to run
        await task

        # Should have reverted to "enforce"
        assert os.environ.get("AGENTSHROUD_MODE") == "enforce"
        assert sleep_calls, "asyncio.sleep was not called"


# ── ModeRequest model ────────────────────────────────────────────────────────

class TestModeRequestModel:
    def test_default_revert_minutes(self):
        req = ModeRequest(mode="monitor")
        assert req.revert_after_minutes == 30

    def test_custom_revert_minutes(self):
        req = ModeRequest(mode="observatory", revert_after_minutes=15)
        assert req.revert_after_minutes == 15

    def test_valid_modes_constant(self):
        assert "enforce" in VALID_AGENTSHROUD_MODES
        assert "monitor" in VALID_AGENTSHROUD_MODES
        assert "observatory" in VALID_AGENTSHROUD_MODES
        assert "godmode" not in VALID_AGENTSHROUD_MODES


# ── D2: Kill switch automated verification ──────────────────────────────────

class TestKillSwitchVerification:
    """Automated verification that verify_killswitch() returns required fields."""

    def _make_monitor(self, tmp_path: Path):
        from gateway.security.killswitch_config import KillSwitchConfig
        from gateway.security.killswitch_monitor import KillSwitchMonitor
        config = KillSwitchConfig()
        config.killswitch_script_path = Path("/nonexistent/killswitch.sh")
        config.verification_log_path = tmp_path / "verification.jsonl"
        config.heartbeat_log_path = tmp_path / "heartbeat.jsonl"
        return KillSwitchMonitor(config=config)

    def test_result_has_required_fields(self, tmp_path):
        monitor = self._make_monitor(tmp_path)
        result = monitor.verify_killswitch(dry_run=True)
        required = {"timestamp", "dry_run", "script_path", "tests", "overall_status", "duration_seconds"}
        missing = required - set(result.keys())
        assert not missing, f"Missing fields in verify_killswitch result: {missing}"

    def test_dry_run_true_does_not_kill(self, tmp_path):
        """dry_run=True must never trigger actual kill switch execution."""
        monitor = self._make_monitor(tmp_path)
        result = monitor.verify_killswitch(dry_run=True)
        assert result["dry_run"] is True

    def test_overall_status_is_valid_value(self, tmp_path):
        monitor = self._make_monitor(tmp_path)
        result = monitor.verify_killswitch(dry_run=True)
        assert result["overall_status"] in ("PASS", "FAIL", "PARTIAL", "UNKNOWN")

    def test_duration_is_non_negative(self, tmp_path):
        monitor = self._make_monitor(tmp_path)
        result = monitor.verify_killswitch(dry_run=True)
        assert result["duration_seconds"] >= 0.0

    def test_script_exists_test_is_present(self, tmp_path):
        monitor = self._make_monitor(tmp_path)
        result = monitor.verify_killswitch(dry_run=True)
        assert "script_exists" in result["tests"]

    def test_verification_log_written(self, tmp_path):
        """verify_killswitch() must write a log entry for auditability."""
        monitor = self._make_monitor(tmp_path)
        monitor.verify_killswitch(dry_run=True)
        log_path = monitor.config.verification_log_path
        assert log_path.exists(), "verification log not written"
        assert log_path.stat().st_size > 0
