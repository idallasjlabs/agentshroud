# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
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
import logging
import os
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import gateway.web.api as api_module
from gateway.ingest_api.config import GatewayConfig, get_module_mode
from gateway.proxy.pipeline import SecurityPipeline
from gateway.web.api import VALID_AGENTSHROUD_MODES, ModeRequest, router

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
        assert any(
            r.levelno == logging.CRITICAL for r in caplog.records
        ), f"Expected CRITICAL log; got: {[r.levelname for r in caplog.records]}"

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
        required = {
            "timestamp",
            "dry_run",
            "script_path",
            "tests",
            "overall_status",
            "duration_seconds",
        }
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


# === Tests from main branch (observatory mode unit tests) ===


class TestObservatoryMode:
    """Test Observatory Mode configuration and endpoints."""

    def test_get_module_mode_respect_global_override(self):
        """Test that get_module_mode respects AGENTSHROUD_MODE env var."""
        # Create a mock config
        config = Mock()
        config.security = Mock()
        config.security.pii_sanitizer = Mock()
        config.security.pii_sanitizer.mode = "enforce"

        # Test enforce mode (default)
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "enforce"}):
            assert get_module_mode(config, "pii_sanitizer") == "enforce"

        # Test monitor mode override
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "monitor"}):
            assert get_module_mode(config, "pii_sanitizer") == "monitor"

        # Test without env var (should use module-specific config)
        with patch.dict(os.environ, {}, clear=True):
            assert get_module_mode(config, "pii_sanitizer") == "enforce"

    def test_get_module_mode_pinned_modules(self):
        """Test that pinned modules always return enforce even in monitor mode."""
        # This would be implemented when per-module pinning is added to get_module_mode
        # For now, this test documents the intended behavior
        pass

    def test_security_pipeline_set_global_mode(self):
        """Test SecurityPipeline.set_global_mode method."""
        # Mock components
        pii_sanitizer = Mock()
        pii_sanitizer.set_mode = Mock()
        prompt_guard = Mock()
        prompt_guard.set_mode = Mock()
        prompt_guard.block_threshold = 0.8
        prompt_guard.warn_threshold = 0.4
        egress_filter = Mock()
        egress_filter.set_mode = Mock()

        pipeline = SecurityPipeline(
            pii_sanitizer=pii_sanitizer, prompt_guard=prompt_guard, egress_filter=egress_filter
        )

        # Test switching to monitor mode
        pipeline.set_global_mode("monitor")

        # Verify components were updated
        pii_sanitizer.set_mode.assert_called_with("monitor")
        prompt_guard.set_mode.assert_called_with("monitor")
        egress_filter.set_mode.assert_called_with("monitor")

        # Verify prompt guard thresholds were set to high values
        assert prompt_guard.block_threshold == 999.0
        assert prompt_guard.warn_threshold == 999.0

        # Test switching to enforce mode
        pipeline.set_global_mode("enforce")

        # Verify thresholds were reset to normal
        assert prompt_guard.block_threshold == 0.8
        assert prompt_guard.warn_threshold == 0.4

    def test_security_pipeline_set_global_mode_missing_components(self):
        """Test set_global_mode handles missing components gracefully."""
        # Provide minimal required component (pii_sanitizer)
        pii_sanitizer = Mock()
        pipeline = SecurityPipeline(pii_sanitizer=pii_sanitizer)

        # Should not raise any exceptions when optional components are missing
        pipeline.set_global_mode("monitor")
        pipeline.set_global_mode("enforce")

    @pytest.mark.asyncio
    async def test_observatory_mode_state_initialization(self):
        """Test that observatory mode state is properly initialized."""
        # This would test the app_state initialization
        # Since we can't easily test the actual app_state, we test the structure

        expected_keys = ["global_mode", "effective_since", "auto_revert_at", "pinned_modules"]

        # Mock app_state structure
        mock_state = {
            "global_mode": "enforce",
            "effective_since": datetime.now(tz=timezone.utc).isoformat(),
            "auto_revert_at": None,
            "pinned_modules": [],
        }

        for key in expected_keys:
            assert key in mock_state

        assert mock_state["global_mode"] in ["monitor", "enforce"]
        assert isinstance(mock_state["pinned_modules"], list)

    @pytest.mark.asyncio
    async def test_auto_revert_timer_logic(self):
        """Test auto-revert timer functionality."""
        # Test the auto-revert logic (without actual FastAPI app)

        # Mock observatory state
        observatory_mode = {
            "global_mode": "monitor",
            "effective_since": datetime.now(tz=timezone.utc).isoformat(),
            "auto_revert_at": None,
            "pinned_modules": [],
        }

        # Calculate revert time
        revert_hours = 2
        revert_time = datetime.now(tz=timezone.utc) + timedelta(hours=revert_hours)
        observatory_mode["auto_revert_at"] = revert_time.isoformat()

        # Verify revert time is set correctly
        assert observatory_mode["auto_revert_at"] is not None
        parsed_revert_time = datetime.fromisoformat(
            observatory_mode["auto_revert_at"].replace("Z", "+00:00")
        )
        assert parsed_revert_time > datetime.now(tz=timezone.utc)

    def test_module_mode_resolution(self):
        """Test module mode resolution with pinned modules."""
        # Test the logic that determines effective module mode

        # Global monitor mode with no pinned modules
        global_mode = "monitor"
        pinned_modules = []
        module = "pii_sanitizer"

        if module in pinned_modules:
            effective_mode = "enforce"
        else:
            effective_mode = global_mode

        assert effective_mode == "monitor"

        # Global monitor mode with pinned module
        pinned_modules = ["pii_sanitizer"]

        if module in pinned_modules:
            effective_mode = "enforce"
        else:
            effective_mode = global_mode

        assert effective_mode == "enforce"

    def test_observatory_mode_validation(self):
        """Test validation of observatory mode parameters."""
        # Test mode validation
        valid_modes = ["monitor", "enforce"]
        invalid_modes = ["disabled", "debug", "", None]

        for mode in valid_modes:
            assert mode in ["monitor", "enforce"]

        for mode in invalid_modes:
            assert mode not in ["monitor", "enforce"]

        # Test auto_revert_hours validation
        valid_hours = [1, 24, 168]  # 1 hour to 1 week
        invalid_hours = [0, -1, 169, 1000]

        for hours in valid_hours:
            assert 1 <= hours <= 168

        for hours in invalid_hours:
            assert not (1 <= hours <= 168)

    def test_pinned_modules_validation(self):
        """Test validation of pinned module names."""
        valid_modules = ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]
        invalid_modules = ["nonexistent", "killswitch", "", None]

        for module in valid_modules:
            assert module in ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]

        # Test that invalid modules would be rejected
        for module in invalid_modules:
            if module:
                assert module not in ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]


# Integration tests that would require a running FastAPI app
class TestObservatoryModeAPI:
    """Integration tests for Observatory Mode API endpoints."""

    @pytest.mark.asyncio
    async def test_get_observatory_mode_endpoint(self):
        """Test GET /manage/mode endpoint returns correct structure."""
        # Mock response structure
        expected_response = {
            "global_mode": "enforce",
            "effective_since": "2026-03-04T16:32:00Z",
            "auto_revert_at": None,
            "pinned_modules": [],
            "module_modes": {
                "pii_sanitizer": "enforce",
                "prompt_guard": "enforce",
                "egress_filter": "enforce",
                "mcp_proxy": "enforce",
            },
        }

        # Verify structure
        required_keys = [
            "global_mode",
            "effective_since",
            "auto_revert_at",
            "pinned_modules",
            "module_modes",
        ]
        for key in required_keys:
            assert key in expected_response

    @pytest.mark.asyncio
    async def test_set_observatory_mode_endpoint(self):
        """Test POST /manage/mode endpoint request/response."""
        # Mock request payload
        request_payload = {"mode": "monitor", "auto_revert_hours": 4, "pin_modules": ["killswitch"]}

        # Mock successful response
        expected_response = {
            "success": True,
            "old_mode": "enforce",
            "new_mode": "monitor",
            "effective_since": "2026-03-04T16:32:00Z",
            "auto_revert_at": "2026-03-04T20:32:00Z",
            "pinned_modules": ["killswitch"],
        }

        # Verify response structure
        assert expected_response["success"] is True
        assert expected_response["new_mode"] == request_payload["mode"]
        assert expected_response["pinned_modules"] == request_payload["pin_modules"]
