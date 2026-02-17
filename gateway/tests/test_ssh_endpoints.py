"""Tests for SSH API endpoints"""

import asyncio
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, patch, MagicMock

import pytest
import pytest_asyncio
from starlette.testclient import TestClient

from gateway.ingest_api.config import (
    ApprovalQueueConfig,
    GatewayConfig,
    LedgerConfig,
    PIIConfig,
    RouterConfig,
)
from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig
from gateway.ingest_api.main import app, app_state
from gateway.ingest_api.ledger import DataLedger
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.approval_queue.queue import ApprovalQueue
from gateway.ingest_api.router import MultiAgentRouter
from gateway.ssh_proxy.proxy import SSHProxy, SSHResult

import time


@pytest.fixture
def ssh_config():
    return SSHConfig(
        enabled=True,
        hosts={
            "pi": SSHHostConfig(
                host="192.168.1.100",
                port=22,
                username="deploy",
                key_path="/home/user/.ssh/id_rsa",
                allowed_commands=["git status", "ls", "cat", "whoami"],
                denied_commands=["rm -rf", "shutdown"],
                max_session_seconds=30,
                auto_approve_commands=["git status", "ls"],
            ),
        },
        global_denied_commands=["rm -rf /"],
        require_approval=True,
    )


@pytest.fixture
def test_config_with_ssh(ssh_config):
    return GatewayConfig(
        bind="127.0.0.1",
        port=8080,
        auth_method="shared_secret",
        auth_token="test-token-12345",
        ledger=LedgerConfig(backend="sqlite", path=Path(":memory:"), retention_days=90),
        router=RouterConfig(enabled=True, default_target="test-agent", targets={}),
        pii=PIIConfig(engine="regex", entities=[], enabled=True),
        approval_queue=ApprovalQueueConfig(enabled=True, actions=["ssh_exec"], timeout_seconds=3600),
        log_level="WARNING",
        ssh=ssh_config,
    )


@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test-token-12345"}


@pytest_asyncio.fixture
async def client(test_config_with_ssh):
    """Set up app state and provide TestClient."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    test_config_with_ssh.ledger.path = tmp_path
    app_state.config = test_config_with_ssh
    app_state.sanitizer = PIISanitizer(test_config_with_ssh.pii)
    app_state.ledger = DataLedger(test_config_with_ssh.ledger)
    await app_state.ledger.initialize()
    app_state.router = MultiAgentRouter(test_config_with_ssh.router)
    app_state.approval_queue = ApprovalQueue(test_config_with_ssh.approval_queue)
    app_state.ssh_proxy = SSHProxy(test_config_with_ssh.ssh)
    app_state.start_time = time.time()

    # Patch load_config to return our test config so lifespan doesn't override
    with patch("gateway.ingest_api.main.load_config", return_value=test_config_with_ssh):
        with TestClient(app) as c:
            yield c

    await app_state.ledger.close()
    tmp_path.unlink(missing_ok=True)


class TestSSHExec:
    def test_ssh_exec_no_auth(self, client):
        resp = client.post("/ssh/exec", json={"host": "pi", "command": "ls"})
        assert resp.status_code == 401

    def test_ssh_exec_auto_approved(self, client, auth_headers):
        mock_result = SSHResult(
            stdout="file1\nfile2\n", stderr="", exit_code=0,
            duration_seconds=0.5, host="pi", command="ls",
        )
        with patch.object(app_state.ssh_proxy, "execute", new_callable=AsyncMock, return_value=mock_result):
            resp = client.post("/ssh/exec", json={"host": "pi", "command": "ls"}, headers=auth_headers)
            assert resp.status_code == 200
            data = resp.json()
            assert data["stdout"] == "file1\nfile2\n"
            assert data["exit_code"] == 0
            assert data["approved_by"] == "auto"

    def test_ssh_exec_requires_approval(self, client, auth_headers):
        resp = client.post("/ssh/exec", json={"host": "pi", "command": "cat /etc/hosts"}, headers=auth_headers)
        assert resp.status_code == 202
        data = resp.json()
        assert "request_id" in data

    def test_ssh_exec_denied_command(self, client, auth_headers):
        resp = client.post("/ssh/exec", json={"host": "pi", "command": "rm -rf /tmp"}, headers=auth_headers)
        assert resp.status_code == 403

    def test_ssh_exec_unknown_host(self, client, auth_headers):
        resp = client.post("/ssh/exec", json={"host": "unknown", "command": "ls"}, headers=auth_headers)
        assert resp.status_code == 404

    def test_ssh_exec_injection_attempt(self, client, auth_headers):
        resp = client.post("/ssh/exec", json={"host": "pi", "command": "ls; rm -rf /"}, headers=auth_headers)
        assert resp.status_code == 403

    def test_ssh_exec_command_not_in_allowlist(self, client, auth_headers):
        resp = client.post("/ssh/exec", json={"host": "pi", "command": "curl http://evil.com"}, headers=auth_headers)
        assert resp.status_code == 403


class TestSSHHosts:
    def test_ssh_hosts_list(self, client, auth_headers):
        resp = client.get("/ssh/hosts", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert "pi" in data["hosts"]


class TestSSHHistory:
    def test_ssh_history(self, client, auth_headers):
        mock_result = SSHResult(
            stdout="output", stderr="", exit_code=0,
            duration_seconds=0.1, host="pi", command="ls",
        )
        with patch.object(app_state.ssh_proxy, "execute", new_callable=AsyncMock, return_value=mock_result):
            client.post("/ssh/exec", json={"host": "pi", "command": "ls"}, headers=auth_headers)
        resp = client.get("/ssh/history", headers=auth_headers)
        assert resp.status_code == 200
        data = resp.json()
        assert "entries" in data
