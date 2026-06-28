# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/web/api.py (management REST API).

Exercises auth, scoped WebSocket tokens, mode switching with auto-revert,
status aggregation, service control, kill switch, config CRUD, bot/gateway
update flows, log retrieval, and both WebSocket endpoints — all with the
container runtime and subprocess boundaries mocked.
"""

from __future__ import annotations

import asyncio
import os
import time
from contextlib import suppress
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import yaml
from fastapi import FastAPI, HTTPException, WebSocketDisconnect
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.testclient import TestClient

import gateway.web.api as api_module
from gateway.web.api import (
    KillSwitchAction,
    ModeRequest,
    UpdateRequest,
    require_auth,
    router,
)

# ── Fixtures ─────────────────────────────────────────────────────────────────


@pytest.fixture(autouse=True)
def _module_state_guard():
    """Restore AGENTSHROUD_MODE, revert task, and WS token registry per test."""
    original = os.environ.get("AGENTSHROUD_MODE")
    api_module._revert_task = None
    api_module._mgmt_ws_tokens.clear()
    yield
    if original is None:
        os.environ.pop("AGENTSHROUD_MODE", None)
    else:
        os.environ["AGENTSHROUD_MODE"] = original
    task = api_module._revert_task
    if task is not None and not task.done():
        task.cancel()
    api_module._revert_task = None
    api_module._mgmt_ws_tokens.clear()


@pytest.fixture
def client():
    app = FastAPI()
    app.dependency_overrides[require_auth] = lambda: "test-user"
    app.include_router(router)
    with TestClient(app) as c:
        yield c


def _engine(**overrides) -> MagicMock:
    eng = MagicMock()
    eng.name = overrides.pop("name", "docker")
    for attr, value in overrides.items():
        setattr(eng, attr, value)
    return eng


def _container(name: str, status: str) -> SimpleNamespace:
    return SimpleNamespace(name=name, status=status, image="img:latest", id="abcdef123456789")


# ── Scoped WebSocket tokens ──────────────────────────────────────────────────


class TestMgmtWsTokens:
    def test_create_returns_registered_prefixed_token(self):
        token = api_module._create_mgmt_ws_token()
        assert token.startswith("mgmt_ws_")
        assert api_module._mgmt_ws_tokens[token] > time.time()

    def test_create_purges_expired_tokens(self):
        api_module._mgmt_ws_tokens["mgmt_ws_stale"] = time.time() - 10
        api_module._create_mgmt_ws_token()
        assert "mgmt_ws_stale" not in api_module._mgmt_ws_tokens

    def test_validate_rejects_empty_and_unprefixed(self):
        assert api_module._validate_mgmt_ws_token("") is False
        assert api_module._validate_mgmt_ws_token("master-auth-token") is False

    def test_validate_rejects_unknown_token(self):
        assert api_module._validate_mgmt_ws_token("mgmt_ws_never_issued") is False

    def test_validate_is_single_use(self):
        token = api_module._create_mgmt_ws_token()
        assert api_module._validate_mgmt_ws_token(token) is True
        assert api_module._validate_mgmt_ws_token(token) is False

    def test_validate_rejects_expired_token(self):
        api_module._mgmt_ws_tokens["mgmt_ws_expired"] = time.time() - 1
        assert api_module._validate_mgmt_ws_token("mgmt_ws_expired") is False


# ── require_auth ─────────────────────────────────────────────────────────────


class TestRequireAuth:
    async def test_valid_token_authenticates(self):
        creds = HTTPAuthorizationCredentials(scheme="Bearer", credentials="sekrit")
        with patch(
            "gateway.web.api.load_config",
            return_value=SimpleNamespace(auth_token="sekrit"),
        ):
            assert await require_auth(creds) == "authenticated"

    async def test_invalid_token_raises_401(self):
        creds = HTTPAuthorizationCredentials(scheme="Bearer", credentials="wrong")
        with patch(
            "gateway.web.api.load_config",
            return_value=SimpleNamespace(auth_token="sekrit"),
        ):
            with pytest.raises(HTTPException) as exc:
                await require_auth(creds)
        assert exc.value.status_code == 401


# ── Mode endpoints ───────────────────────────────────────────────────────────


class TestMode:
    def test_get_mode_default_enforce(self, client):
        os.environ.pop("AGENTSHROUD_MODE", None)
        resp = client.get("/api/mode")
        assert resp.status_code == 200
        body = resp.json()
        assert body["mode"] == "enforce"
        assert "timestamp" in body

    def test_set_mode_invalid_returns_400(self, client):
        resp = client.put("/api/mode", json={"mode": "yolo"})
        assert resp.status_code == 400
        assert "mode must be one of" in resp.json()["detail"]

    async def test_set_mode_monitor_auto_reverts(self):
        os.environ["AGENTSHROUD_MODE"] = "enforce"
        with patch("gateway.web.api.asyncio.sleep", new=AsyncMock(return_value=None)) as slp:
            resp = await api_module.set_mode(
                ModeRequest(mode="monitor", revert_after_minutes=0), user="t"
            )
            assert resp["mode"] == "monitor"
            assert resp["previous_mode"] == "enforce"
            assert resp["auto_revert_in_minutes"] == 1  # clamped low
            assert os.environ["AGENTSHROUD_MODE"] == "monitor"
            await api_module._revert_task
            slp.assert_awaited_once_with(60)
        assert os.environ["AGENTSHROUD_MODE"] == "enforce"

    async def test_set_mode_clamps_high_revert(self):
        with patch("gateway.web.api.asyncio.sleep", new=AsyncMock(return_value=None)):
            resp = await api_module.set_mode(
                ModeRequest(mode="observatory", revert_after_minutes=99999), user="t"
            )
            assert resp["auto_revert_in_minutes"] == 480
            await api_module._revert_task

    async def test_set_mode_enforce_revert_task_is_noop(self):
        os.environ["AGENTSHROUD_MODE"] = "monitor"
        with patch("gateway.web.api.asyncio.sleep", new=AsyncMock(return_value=None)):
            resp = await api_module.set_mode(ModeRequest(mode="enforce"), user="t")
            assert resp["previous_mode"] == "monitor"
            await api_module._revert_task
        assert os.environ["AGENTSHROUD_MODE"] == "enforce"

    async def test_set_mode_cancels_previous_revert_task(self):
        real_sleep = asyncio.sleep
        hang = asyncio.Event()

        async def fake_sleep(_seconds):
            await hang.wait()

        with patch("gateway.web.api.asyncio.sleep", new=fake_sleep):
            await api_module.set_mode(ModeRequest(mode="monitor"), user="t")
            task1 = api_module._revert_task
            await real_sleep(0)  # let task1 start awaiting
            await api_module.set_mode(ModeRequest(mode="observatory"), user="t")
            task2 = api_module._revert_task
            assert task2 is not task1
            with suppress(asyncio.CancelledError):
                await task1
            assert task1.cancelled()
            task2.cancel()
            with suppress(asyncio.CancelledError):
                await task2

    def test_mode_request_defaults(self):
        req = ModeRequest(mode="monitor")
        assert req.revert_after_minutes == 30


# ── Status ───────────────────────────────────────────────────────────────────


class TestStatus:
    def test_status_with_running_and_stopped_containers(self, client):
        eng = _engine()
        eng.health_check.return_value = True
        eng.ps.return_value = [
            _container("agentshroud-gateway", "Up 2 hours"),
            _container("agentshroud-openclaw", "Exited (0) 5 minutes ago"),
        ]
        with (
            patch("gateway.web.api.get_engine", return_value=eng),
            patch("gateway.web.api.detect_runtime", return_value=["docker"]),
        ):
            resp = client.get("/api/status")
        assert resp.status_code == 200
        data = resp.json()
        assert data["runtime"]["healthy"] is True
        assert data["runtime"]["active"] == "docker"
        services = data["services"]
        assert services["agentshroud-gateway"]["status"] == "running"
        assert services["agentshroud-gateway"]["id"] == "abcdef123456"
        assert services["agentshroud-openclaw"]["status"] == "stopped"
        assert services["falco"] == {"status": "not_found"}
        assert set(data["system"]) == {"disk_total_gb", "disk_free_gb", "disk_used_pct"}
        assert "comparison" in data["security"]

    def test_status_runtime_failure_degrades_gracefully(self, client):
        with (
            patch("gateway.web.api.get_engine", side_effect=RuntimeError("no runtime")),
            patch("gateway.web.api.detect_runtime", return_value=[]),
        ):
            resp = client.get("/api/status")
        assert resp.status_code == 200
        data = resp.json()
        assert data["runtime"]["healthy"] is False
        assert data["runtime"]["active"] is None
        assert data["services"]["clamav"] == {"status": "not_found"}
        assert data["security"]["warnings"] == []


# ── Service control ──────────────────────────────────────────────────────────


class TestServiceControl:
    def test_start_service_success(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/falco/start")
        assert resp.status_code == 200
        assert resp.json() == {"status": "started", "service": "falco"}

    def test_start_service_failure_returns_500(self, client):
        eng = _engine()
        eng.compose_up.side_effect = RuntimeError("compose broke")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/falco/start")
        assert resp.status_code == 500
        assert "compose broke" in resp.json()["detail"]

    def test_stop_service_success(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/clamav/stop")
        assert resp.status_code == 200
        assert resp.json() == {"status": "stopped", "service": "clamav"}
        eng.stop.assert_called_once_with("clamav")

    def test_stop_service_failure_returns_500(self, client):
        eng = _engine()
        eng.stop.side_effect = RuntimeError("nope")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/clamav/stop")
        assert resp.status_code == 500

    def test_restart_service_success(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/wazuh-agent/restart")
        assert resp.status_code == 200
        assert resp.json() == {"status": "restarted", "service": "wazuh-agent"}
        eng.rm.assert_called_once_with("wazuh-agent", force=True)

    def test_restart_service_failure_returns_500(self, client):
        eng = _engine()
        eng.stop.side_effect = RuntimeError("dead")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/services/wazuh-agent/restart")
        assert resp.status_code == 500

    def test_invalid_service_name_rejected(self, client):
        with patch("gateway.web.api._get_engine") as mock_engine:
            resp = client.post("/api/services/evil$(rm)/start")
        assert resp.status_code == 400
        assert "Invalid service name" in resp.json()["detail"]
        mock_engine.assert_not_called()


# ── Kill switch ──────────────────────────────────────────────────────────────


class TestKillSwitch:
    def test_requires_confirmation(self, client):
        resp = client.post("/api/killswitch/freeze", json={"confirm": False})
        assert resp.status_code == 400

    def test_invalid_mode_rejected(self, client):
        resp = client.post("/api/killswitch/detonate", json={"confirm": True})
        assert resp.status_code == 400

    def test_freeze_pauses_bot_even_if_pause_fails(self, client):
        eng = _engine()
        eng.pause.side_effect = RuntimeError("already paused")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/killswitch/freeze", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json() == {"status": "frozen", "mode": "freeze"}

    def test_shutdown_brings_stack_down(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/killswitch/shutdown", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json() == {"status": "shutdown", "mode": "shutdown"}
        eng.compose_down.assert_called_once()

    def test_shutdown_failure_still_reports_shutdown(self, client):
        eng = _engine()
        eng.compose_down.side_effect = RuntimeError("daemon gone")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/killswitch/shutdown", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json()["status"] == "shutdown"

    def test_disconnect_stops_and_removes_bot(self, client):
        eng = _engine()
        _two_bots = SimpleNamespace(bots={"openclaw": SimpleNamespace(), "hermes": SimpleNamespace()})
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("gateway.web.api.load_config", return_value=_two_bots),
        ):
            resp = client.post("/api/killswitch/disconnect", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json() == {"status": "disconnected", "mode": "disconnect"}
        # Hermes added — both bots must be stopped
        eng.stop.assert_any_call("agentshroud-openclaw")
        eng.stop.assert_any_call("agentshroud-hermes")

    def test_disconnect_swallows_engine_errors(self, client):
        eng = _engine()
        eng.stop.side_effect = RuntimeError("not running")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/killswitch/disconnect", json={"confirm": True})
        assert resp.status_code == 200
        assert resp.json()["status"] == "disconnected"

    def test_killswitch_action_default_unconfirmed(self):
        assert KillSwitchAction().confirm is False


# ── Configuration ────────────────────────────────────────────────────────────


class TestConfig:
    def test_get_config_when_file_missing(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        resp = client.get("/api/config")
        assert resp.status_code == 200
        assert resp.json() == {"config": {}, "path": "agentshroud.yaml", "exists": False}

    def test_get_config_reads_yaml(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        (tmp_path / "agentshroud.yaml").write_text("gateway:\n  port: 8080\n")
        resp = client.get("/api/config")
        assert resp.status_code == 200
        assert resp.json()["config"] == {"gateway": {"port": 8080}}

    def test_update_config_writes_yaml_and_backs_up(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        (tmp_path / "agentshroud.yaml").write_text("gateway:\n  port: 1\n")
        resp = client.put("/api/config", json={"config": {"gateway": {"port": 9}}})
        assert resp.status_code == 200
        assert resp.json()["status"] == "updated"
        written = yaml.safe_load((tmp_path / "agentshroud.yaml").read_text())
        assert written == {"gateway": {"port": 9}}
        backups = list(tmp_path.glob("agentshroud.yaml.bak.*"))
        assert len(backups) == 1
        assert "port: 1" in backups[0].read_text()

    def test_update_config_without_existing_file_skips_backup(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        resp = client.put("/api/config", json={"config": {"security": {"pii": True}}})
        assert resp.status_code == 200
        assert list(tmp_path.glob("*.bak.*")) == []

    def test_update_config_rejects_unknown_keys(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        resp = client.put("/api/config", json={"config": {"backdoor": {}}})
        assert resp.status_code == 400
        assert "backdoor" in resp.json()["detail"]
        assert not (tmp_path / "agentshroud.yaml").exists()

    def test_import_config_delegates_to_update(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        resp = client.post("/api/config/import", json={"config": {"logging": {"level": "INFO"}}})
        assert resp.status_code == 200
        assert resp.json()["status"] == "updated"

    def test_export_config_delegates_to_get(self, client, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        (tmp_path / "agentshroud.yaml").write_text("egress: {}\n")
        resp = client.get("/api/config/export")
        assert resp.status_code == 200
        assert resp.json()["config"] == {"egress": {}}


# ── Default bot Dockerfile resolution ────────────────────────────────────────


class TestDefaultBotDockerfile:
    def test_default_bot_dockerfile_used(self):
        bots = {
            "hermes": SimpleNamespace(default=False, dockerfile="docker/bots/hermes/Dockerfile"),
            "openclaw": SimpleNamespace(default=True, dockerfile="docker/bots/oc/Dockerfile"),
        }
        with patch("gateway.web.api.load_config", return_value=SimpleNamespace(bots=bots)):
            assert api_module._get_default_bot_dockerfile() == "docker/bots/oc/Dockerfile"

    def test_first_bot_used_when_no_default_flag(self):
        bots = {
            "hermes": SimpleNamespace(default=False, dockerfile="docker/bots/hermes/Dockerfile"),
        }
        with patch("gateway.web.api.load_config", return_value=SimpleNamespace(bots=bots)):
            assert api_module._get_default_bot_dockerfile() == "docker/bots/hermes/Dockerfile"

    def test_fallback_when_no_bots(self):
        with patch("gateway.web.api.load_config", return_value=SimpleNamespace(bots={})):
            assert api_module._get_default_bot_dockerfile() == "docker/bots/openclaw/Dockerfile"

    def test_fallback_when_default_bot_has_no_dockerfile(self):
        bots = {"openclaw": SimpleNamespace(default=True, dockerfile=None)}
        with patch("gateway.web.api.load_config", return_value=SimpleNamespace(bots=bots)):
            assert api_module._get_default_bot_dockerfile() == "docker/bots/openclaw/Dockerfile"

    def test_fallback_when_config_load_fails(self):
        with patch("gateway.web.api.load_config", side_effect=RuntimeError("no yaml")):
            assert api_module._get_default_bot_dockerfile() == "docker/bots/openclaw/Dockerfile"


# ── Rebuild ──────────────────────────────────────────────────────────────────


class TestRebuild:
    def test_rebuild_success(self, client):
        eng = _engine()
        _two_bots = SimpleNamespace(bots={"openclaw": SimpleNamespace(), "hermes": SimpleNamespace()})
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("gateway.web.api.load_config", return_value=_two_bots),
            patch(
                "gateway.web.api._get_default_bot_dockerfile",
                return_value="docker/bots/openclaw/Dockerfile",
            ),
        ):
            resp = client.post("/api/rebuild")
        assert resp.status_code == 200
        assert resp.json() == {"status": "rebuilt"}
        assert eng.build.call_count == 3  # gateway + openclaw + hermes
        eng.compose_up.assert_called_once()

    def test_rebuild_failure_returns_500(self, client):
        eng = _engine()
        eng.compose_down.side_effect = RuntimeError("stack stuck")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/rebuild")
        assert resp.status_code == 500
        assert "stack stuck" in resp.json()["detail"]


# ── Bot updates ──────────────────────────────────────────────────────────────


class TestBotUpdates:
    def test_check_bot_updates_update_available(self, client):
        eng = _engine()
        eng.exec.return_value = "1.0.0\n"
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("subprocess.run", return_value=MagicMock(returncode=0, stdout="2.0.0\n")),
        ):
            resp = client.get("/api/updates/bot/hermes")
        assert resp.status_code == 200
        data = resp.json()
        assert data == {
            "bot_id": "hermes",
            "current": "1.0.0",
            "latest": "2.0.0",
            "update_available": True,
        }
        eng.exec.assert_called_once_with("agentshroud-hermes", ["hermes", "--version"])

    def test_check_bot_updates_npm_failure_and_exec_failure(self, client):
        eng = _engine()
        eng.exec.side_effect = RuntimeError("container down")
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("subprocess.run", return_value=MagicMock(returncode=1, stdout="")),
        ):
            resp = client.get("/api/updates/bot/hermes")
        data = resp.json()
        assert data["current"] == "unknown"
        assert data["latest"] == "unknown"
        assert data["update_available"] is False

    def test_check_bot_updates_npm_missing_binary(self, client):
        eng = _engine()
        eng.exec.return_value = "1.0.0"
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("subprocess.run", side_effect=OSError("npm not found")),
        ):
            resp = client.get("/api/updates/bot/hermes")
        data = resp.json()
        assert data["latest"] == "unknown"
        assert data["update_available"] is False

    def test_upgrade_bot_success(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/updates/bot/hermes/upgrade", json={"version": "2.1.0"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "upgraded"
        assert data["version"] == "2.1.0"
        assert [s["status"] for s in data["steps"]] == ["done", "done"]
        eng.exec.assert_called_once_with(
            "agentshroud-hermes", ["npm", "install", "-g", "hermes@2.1.0"]
        )

    def test_upgrade_bot_failure_reports_error_step(self, client):
        eng = _engine()
        eng.exec.side_effect = RuntimeError("npm install failed")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/updates/bot/hermes/upgrade", json={})
        data = resp.json()
        assert data["status"] == "failed"
        assert data["error"] == "npm install failed"
        assert data["steps"][-1]["step"] == "error"

    def test_rollback_bot(self, client):
        resp = client.post("/api/updates/bot/hermes/rollback")
        assert resp.status_code == 200
        assert resp.json()["status"] == "rollback_initiated"
        assert resp.json()["bot_id"] == "hermes"


# ── OpenClaw backward-compat aliases ─────────────────────────────────────────


class TestOpenclawAliases:
    def test_check_openclaw_updates_alias(self, client):
        eng = _engine()
        eng.exec.return_value = "1.2.3"
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("subprocess.run", return_value=MagicMock(returncode=0, stdout="1.2.3\n")),
        ):
            resp = client.get("/api/updates/openclaw")
        data = resp.json()
        assert data["bot_id"] == "openclaw"
        assert data["update_available"] is False

    def test_upgrade_openclaw_alias(self, client):
        eng = _engine()
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.post("/api/updates/openclaw/upgrade", json={})
        data = resp.json()
        assert data["status"] == "upgraded"
        assert data["bot_id"] == "openclaw"
        assert data["version"] == "latest"

    def test_rollback_openclaw_alias(self, client):
        resp = client.post("/api/updates/openclaw/rollback")
        assert resp.json()["status"] == "rollback_initiated"
        assert resp.json()["bot_id"] == "openclaw"


# ── AgentShroud self-update ──────────────────────────────────────────────────


def _gitless_run(pull_rc: int = 0, tests_rc: int = 0):
    """Build a subprocess.run double that simulates the upgrade git flow."""

    def fake_run(cmd, **kwargs):
        result = MagicMock(returncode=0, stdout="", stderr="")
        if cmd[:3] == ["git", "rev-parse", "HEAD"]:
            result.stdout = "deadbeef0001\n"
        elif cmd[:2] == ["git", "pull"]:
            result.returncode = pull_rc
            result.stderr = "remote rejected" if pull_rc else ""
        elif cmd[:2] == ["git", "diff"]:
            result.stdout = "requirements.txt\ngateway/security/egress_filter.py\nREADME.md\n"
        elif cmd[0] == "python":
            result.returncode = tests_rc
            result.stdout = "1 failed" if tests_rc else "all passed"
        return result

    return fake_run


class TestAgentshroudUpdates:
    def test_check_updates_reports_behind(self, client):
        def fake_run(cmd, **kwargs):
            result = MagicMock(returncode=0, stdout="")
            if cmd[:3] == ["git", "rev-parse", "--short"]:
                result.stdout = "abc1234\n"
            elif "origin/main" in cmd and "describe" in cmd:
                result.stdout = "v1.1.0\n"
            elif "describe" in cmd:
                result.stdout = "v1.0.0\n"
            elif "rev-list" in cmd:
                result.stdout = "3\n"
            return result

        with patch("subprocess.run", side_effect=fake_run):
            resp = client.get("/api/updates/agentshroud")
        assert resp.status_code == 200
        assert resp.json() == {
            "current_version": "v1.0.0",
            "current_commit": "abc1234",
            "latest_version": "v1.1.0",
            "commits_behind": 3,
            "update_available": True,
        }

    def test_check_updates_git_failure_returns_error(self, client):
        with patch("subprocess.run", side_effect=OSError("git missing")):
            resp = client.get("/api/updates/agentshroud")
        assert resp.status_code == 200
        assert resp.json() == {"error": "git missing"}

    def test_upgrade_success_with_tests_and_security_review(self, client):
        eng = _engine()
        _two_bots = SimpleNamespace(bots={"openclaw": SimpleNamespace(), "hermes": SimpleNamespace()})
        with (
            patch("subprocess.run", side_effect=_gitless_run()),
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("gateway.web.api.load_config", return_value=_two_bots),
            patch(
                "gateway.web.api._get_default_bot_dockerfile",
                return_value="docker/bots/openclaw/Dockerfile",
            ),
        ):
            resp = client.post("/api/updates/agentshroud/upgrade", json={"skip_tests": False})
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "upgraded"
        assert data["rollback_hash"] == "deadbeef0001"
        step_names = [s["step"] for s in data["steps"]]
        assert step_names == ["git_pull", "security_review", "run_tests", "rebuild", "restart"]
        review = data["steps"][1]
        assert review["changed_files"] == 3
        assert review["security_concerns"] == [
            "Dependency change: requirements.txt",
            "Security module changed: gateway/security/egress_filter.py",
        ]
        assert eng.build.call_count == 3  # gateway + openclaw + hermes

    def test_upgrade_skip_tests_skips_test_step(self, client):
        eng = _engine()
        with (
            patch("subprocess.run", side_effect=_gitless_run()),
            patch("gateway.web.api._get_engine", return_value=eng),
            patch(
                "gateway.web.api._get_default_bot_dockerfile",
                return_value="docker/bots/openclaw/Dockerfile",
            ),
        ):
            resp = client.post("/api/updates/agentshroud/upgrade", json={"skip_tests": True})
        data = resp.json()
        assert data["status"] == "upgraded"
        assert "run_tests" not in [s["step"] for s in data["steps"]]

    def test_upgrade_pull_failure_triggers_rollback(self, client):
        with patch("subprocess.run", side_effect=_gitless_run(pull_rc=1)):
            resp = client.post("/api/updates/agentshroud/upgrade", json={})
        data = resp.json()
        assert data["status"] == "failed"
        assert "git pull failed" in data["error"]
        assert data["rolled_back_to"] == "deadbeef0001"
        assert data["steps"][-1] == {"step": "rollback", "status": "done"}

    def test_upgrade_test_failure_triggers_rollback(self, client):
        with patch("subprocess.run", side_effect=_gitless_run(tests_rc=1)):
            resp = client.post("/api/updates/agentshroud/upgrade", json={"skip_tests": False})
        data = resp.json()
        assert data["status"] == "failed"
        assert "Tests failed" in data["error"]
        assert data["steps"][-1]["step"] == "rollback"

    def test_rollback_agentshroud_success(self, client):
        eng = _engine()
        with (
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
            patch("gateway.web.api._get_engine", return_value=eng),
        ):
            resp = client.post("/api/updates/agentshroud/rollback")
        assert resp.status_code == 200
        assert resp.json() == {"status": "rolled_back"}
        eng.compose_up.assert_called_once()

    def test_rollback_agentshroud_failure_returns_500(self, client):
        eng = _engine()
        eng.build.side_effect = RuntimeError("build broke")
        with (
            patch("subprocess.run", return_value=MagicMock(returncode=0)),
            patch("gateway.web.api._get_engine", return_value=eng),
        ):
            resp = client.post("/api/updates/agentshroud/rollback")
        assert resp.status_code == 500
        assert "build broke" in resp.json()["detail"]

    def test_update_history_returns_commits(self, client):
        with patch(
            "subprocess.run",
            return_value=MagicMock(returncode=0, stdout="abc fix\ndef feat\n"),
        ):
            resp = client.get("/api/updates/history")
        assert resp.json() == {"history": ["abc fix", "def feat"]}

    def test_update_history_git_failure_returns_empty(self, client):
        with patch("subprocess.run", side_effect=OSError("git missing")):
            resp = client.get("/api/updates/history")
        assert resp.json() == {"history": []}

    def test_update_request_defaults(self):
        req = UpdateRequest()
        assert req.version is None
        assert req.skip_tests is False


# ── Security report ──────────────────────────────────────────────────────────


class TestSecurityReport:
    def test_report_with_healthy_runtime(self, client):
        eng = _engine(name="podman")
        eng.health_check.return_value = True
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.get("/api/security/report")
        assert resp.status_code == 200
        data = resp.json()
        assert "runtime_security" in data
        assert isinstance(data["warnings"], list)

    def test_report_with_unhealthy_runtime_falls_back_to_docker(self, client):
        eng = _engine()
        eng.health_check.return_value = False
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.get("/api/security/report")
        assert resp.status_code == 200
        assert isinstance(resp.json()["warnings"], list)


# ── Logs ─────────────────────────────────────────────────────────────────────


class TestLogs:
    def test_get_logs_for_service(self, client):
        eng = _engine()
        eng.logs.return_value = "line1\nline2"
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.get("/api/logs?service=agentshroud-gateway&tail=5000")
        assert resp.status_code == 200
        assert resp.json() == {"service": "agentshroud-gateway", "logs": ["line1", "line2"]}
        eng.logs.assert_called_once_with("agentshroud-gateway", tail=1000)  # clamped

    def test_get_logs_unknown_service_rejected(self, client):
        with patch("gateway.web.api._get_engine", return_value=_engine()):
            resp = client.get("/api/logs?service=../etc/passwd")
        assert resp.status_code == 400

    def test_get_logs_service_not_found_returns_404(self, client):
        eng = _engine()
        eng.logs.side_effect = RuntimeError("no such container")
        with patch("gateway.web.api._get_engine", return_value=eng):
            resp = client.get("/api/logs?service=falco")
        assert resp.status_code == 404
        assert "Service not found" in resp.json()["detail"]

    def test_get_logs_combined_handles_partial_failure(self, client):
        eng = _engine()
        # gateway OK, openclaw errors, hermes errors — both bots gracefully return []
        eng.logs.side_effect = ["g1\ng2", RuntimeError("bot down"), RuntimeError("bot down")]
        _two_bots = SimpleNamespace(bots={"openclaw": SimpleNamespace(), "hermes": SimpleNamespace()})
        with (
            patch("gateway.web.api._get_engine", return_value=eng),
            patch("gateway.web.api.load_config", return_value=_two_bots),
        ):
            resp = client.get("/api/logs?tail=0")
        assert resp.status_code == 200
        data = resp.json()
        assert data["logs"]["agentshroud-gateway"] == ["g1", "g2"]
        assert data["logs"]["agentshroud-openclaw"] == []
        assert data["logs"]["agentshroud-hermes"] == []
        eng.logs.assert_any_call("agentshroud-gateway", tail=1)  # clamped low


# ── WebSockets ───────────────────────────────────────────────────────────────


def _fake_ws() -> MagicMock:
    ws = MagicMock()
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_json = AsyncMock()
    ws.receive_text = AsyncMock()
    return ws


class TestWsLogs:
    async def test_missing_token_closes_4001(self):
        ws = _fake_ws()
        await api_module.ws_logs(ws, token="")
        ws.close.assert_awaited_once_with(code=4001, reason="Authentication required")
        ws.accept.assert_not_awaited()

    async def test_master_token_rejected_4003(self):
        ws = _fake_ws()
        await api_module.ws_logs(ws, token="master-auth-token")
        ws.close.assert_awaited_once_with(code=4003, reason="Invalid credentials")

    async def test_streams_logs_then_cleans_up_on_disconnect(self):
        token = api_module._create_mgmt_ws_token()
        ws = _fake_ws()
        eng = _engine()
        eng.logs.side_effect = ["l1\nl2", RuntimeError("svc down")]
        sleep_mock = AsyncMock(side_effect=[None, None, WebSocketDisconnect(code=1000)])
        with (
            patch(
                "gateway.web.api._get_engine",
                side_effect=[RuntimeError("engine flake"), eng],
            ),
            patch("gateway.web.api.asyncio.sleep", new=sleep_mock),
        ):
            await api_module.ws_logs(ws, token=token)
        ws.accept.assert_awaited_once()
        # First tick: engine flake swallowed. Second tick: gateway logs sent,
        # openclaw failure swallowed. Third tick: disconnect.
        ws.send_json.assert_awaited_once_with(
            {"service": "agentshroud-gateway", "logs": ["l1", "l2"]}
        )
        assert ws not in api_module.active_websockets


class TestWsUpdates:
    async def test_missing_token_closes_4001(self):
        ws = _fake_ws()
        await api_module.ws_updates(ws, token="")
        ws.close.assert_awaited_once_with(code=4001, reason="Authentication required")

    async def test_invalid_token_closes_4003(self):
        ws = _fake_ws()
        await api_module.ws_updates(ws, token="mgmt_ws_forged")
        ws.close.assert_awaited_once_with(code=4003, reason="Invalid credentials")

    async def test_echoes_status_until_disconnect(self):
        token = api_module._create_mgmt_ws_token()
        ws = _fake_ws()
        ws.receive_text.side_effect = ["progress?", WebSocketDisconnect(code=1000)]
        await api_module.ws_updates(ws, token=token)
        ws.accept.assert_awaited_once()
        ws.send_json.assert_awaited_once_with({"status": "connected"})


# ── Engine helper ────────────────────────────────────────────────────────────


class TestGetEngineHelper:
    def test_get_engine_uses_runtime_config(self, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_RUNTIME", "podman")
        sentinel = MagicMock()
        with patch("gateway.web.api.get_engine", return_value=sentinel) as mock_get:
            assert api_module._get_engine() is sentinel
        mock_get.assert_called_once_with("podman")
