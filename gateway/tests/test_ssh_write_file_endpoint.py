# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for POST /ssh/write_file — structured (non-shell-string) file writes.

Mirrors gateway/tests/test_ssh_endpoints.py's fixture/mocking style: the SSH
transport itself is mocked (SSHProxy.write_file / asyncio.create_subprocess_exec),
never a real host.
"""

from __future__ import annotations

import base64
import tempfile
import time
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
import pytest_asyncio
from starlette.testclient import TestClient

from gateway.approval_queue.queue import ApprovalQueue
from gateway.ingest_api.config import (
    ApprovalQueueConfig,
    GatewayConfig,
    LedgerConfig,
    PIIConfig,
    RouterConfig,
)
from gateway.ingest_api.ledger import DataLedger
from gateway.ingest_api.main import app, app_state
from gateway.ingest_api.router import MultiAgentRouter
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig
from gateway.ssh_proxy.proxy import (
    _ALLOWED_WRITE_ROOT,
    _MAX_WRITE_FILE_BYTES,
    _REMOTE_WRITE_FILE_SCRIPT_B64,
    INJECTION_PATTERNS,
    SSHProxy,
    SSHWriteResult,
)


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
        approval_queue=ApprovalQueueConfig(
            enabled=True, actions=["ssh_exec"], timeout_seconds=3600
        ),
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

    with patch("gateway.ingest_api.lifespan.load_config", return_value=test_config_with_ssh):
        with TestClient(app) as c:
            yield c

    await app_state.ledger.close()
    tmp_path.unlink(missing_ok=True)


def _b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


class TestSSHWriteFileEndpoint:
    def test_write_file_no_auth(self, client):
        resp = client.post(
            "/ssh/write_file",
            json={"host": "pi", "path": "gateway/foo.py", "content_base64": _b64(b"x")},
        )
        assert resp.status_code == 401

    def test_write_file_valid_round_trip(self, client, auth_headers):
        """Valid request: SSHProxy.write_file() is invoked with decoded path/content
        transported as structured data, and a success response is returned."""
        mock_result = SSHWriteResult(
            host="pi",
            path="gateway/foo.py",
            bytes_written=13,
            stdout="13",
            stderr="",
            exit_code=0,
            duration_seconds=0.05,
        )
        with patch.object(
            app_state.ssh_proxy,
            "write_file",
            new_callable=AsyncMock,
            return_value=mock_result,
        ) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/foo.py",
                    "content_base64": _b64(b"print('hello')"),
                    "reason": "add helper script",
                },
                headers=auth_headers,
            )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert data["bytes_written"] == 13
        assert data["exit_code"] == 0
        assert data["host"] == "pi"
        assert data["path"] == "gateway/foo.py"
        assert "audit_id" in data
        # proxy.write_file() called with host/path/content_base64 as DATA args,
        # not folded into any shell command string.
        mock_write.assert_awaited_once_with("pi", "gateway/foo.py", _b64(b"print('hello')"))

    def test_write_file_remote_failure_returns_200_with_success_false(self, client, auth_headers):
        """Mirrors /ssh/exec: a nonzero remote exit code is surfaced in the 200
        response body (success=False), not as an HTTP error status."""
        mock_result = SSHWriteResult(
            host="pi",
            path="gateway/foo.py",
            bytes_written=0,
            stdout="",
            stderr="Permission denied",
            exit_code=1,
            duration_seconds=0.02,
        )
        with patch.object(
            app_state.ssh_proxy,
            "write_file",
            new_callable=AsyncMock,
            return_value=mock_result,
        ):
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/foo.py",
                    "content_base64": _b64(b"data"),
                },
                headers=auth_headers,
            )
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is False
        assert data["exit_code"] == 1
        assert data["stderr"] == "Permission denied"

    def test_write_file_path_traversal_dotdot_rejected(self, client, auth_headers):
        """'../' escaping the allowed root is rejected — never reaches proxy.write_file()."""
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "../../../etc/passwd",
                    "content_base64": _b64(b"malicious"),
                },
                headers=auth_headers,
            )
        assert resp.status_code == 403
        assert "escapes allowed root" in resp.json()["detail"]
        mock_write.assert_not_awaited()

    def test_write_file_absolute_path_outside_root_rejected(self, client, auth_headers):
        """Absolute path outside the approved root is rejected."""
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "/etc/passwd",
                    "content_base64": _b64(b"malicious"),
                },
                headers=auth_headers,
            )
        assert resp.status_code == 403
        assert "escapes allowed root" in resp.json()["detail"]
        mock_write.assert_not_awaited()

    def test_write_file_absolute_path_prefix_collision_rejected(self, client, auth_headers):
        """A sibling directory that merely shares the root as a string prefix
        (no '/' separator) must NOT be treated as inside the root."""
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": f"{_ALLOWED_WRITE_ROOT}-evil/x.py",
                    "content_base64": _b64(b"malicious"),
                },
                headers=auth_headers,
            )
        assert resp.status_code == 403
        mock_write.assert_not_awaited()

    def test_write_file_oversized_content_rejected(self, client, auth_headers):
        """Decoded content exceeding the ~500KB cap is rejected with 413, and
        proxy.write_file() is never invoked."""
        oversized = _b64(b"x" * (_MAX_WRITE_FILE_BYTES + 1))
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/big.py",
                    "content_base64": oversized,
                },
                headers=auth_headers,
            )
        assert resp.status_code == 413
        assert "exceeds maximum size" in resp.json()["detail"]
        mock_write.assert_not_awaited()

    def test_write_file_invalid_base64_rejected(self, client, auth_headers):
        """Malformed base64 is rejected at the Pydantic model layer (422),
        never silently truncated or ignored."""
        resp = client.post(
            "/ssh/write_file",
            json={
                "host": "pi",
                "path": "gateway/foo.py",
                "content_base64": "not-valid-base64!!!",
            },
            headers=auth_headers,
        )
        assert resp.status_code == 422

    def test_write_file_disallowed_host_rejected(self, client, auth_headers):
        """A host not present in the SSH allowlist is rejected with 404."""
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "unknown-host",
                    "path": "gateway/foo.py",
                    "content_base64": _b64(b"data"),
                },
                headers=auth_headers,
            )
        assert resp.status_code == 404
        mock_write.assert_not_awaited()

    def test_write_file_ssh_disabled_returns_503(self, client, auth_headers):
        app_state.ssh_proxy = None
        try:
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/foo.py",
                    "content_base64": _b64(b"data"),
                },
                headers=auth_headers,
            )
            assert resp.status_code == 503
        finally:
            pass  # client fixture teardown reconstructs app_state next test

    def test_write_file_empty_path_rejected(self, client, auth_headers):
        resp = client.post(
            "/ssh/write_file",
            json={"host": "pi", "path": "   ", "content_base64": _b64(b"data")},
            headers=auth_headers,
        )
        assert resp.status_code == 422

    def test_write_file_denial_is_audited(self, client, auth_headers):
        """Denied write attempts are logged to the ledger for audit (no raw
        content stored — only path/host/reason)."""
        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock):
            client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "/etc/passwd",
                    "content_base64": _b64(b"malicious"),
                    "reason": "attempted escape",
                },
                headers=auth_headers,
            )
        resp = client.get("/ssh/history", headers=auth_headers)
        assert resp.status_code == 200
        assert resp.json()["total"] >= 1


class TestSSHProxyValidateWriteFile:
    """Unit tests for SSHProxy.validate_write_file()."""

    def test_relative_path_resolved_under_root_accepted(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, _ = proxy.validate_write_file("pi", "gateway/foo.py", _b64(b"content"))
        assert ok

    def test_absolute_path_under_root_accepted(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, _ = proxy.validate_write_file(
            "pi", f"{_ALLOWED_WRITE_ROOT}/gateway/foo.py", _b64(b"content")
        )
        assert ok

    def test_dotdot_traversal_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", "../../etc/passwd", _b64(b"x"))
        assert not ok
        assert "escapes allowed root" in reason

    def test_dotdot_traversal_from_absolute_path_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file(
            "pi", f"{_ALLOWED_WRITE_ROOT}/../../etc/passwd", _b64(b"x")
        )
        assert not ok
        assert "escapes allowed root" in reason

    def test_absolute_path_outside_root_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", "/etc/passwd", _b64(b"x"))
        assert not ok
        assert "escapes allowed root" in reason

    def test_null_byte_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file(
            "pi", f"{_ALLOWED_WRITE_ROOT}/foo\x00.py", _b64(b"x")
        )
        assert not ok
        assert "null byte" in reason

    def test_unknown_host_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("nope", "gateway/foo.py", _b64(b"x"))
        assert not ok
        assert "Unknown host" in reason

    def test_invalid_base64_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", "gateway/foo.py", "!!!not-base64!!!")
        assert not ok
        assert "not valid base64" in reason

    def test_oversized_content_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        big = _b64(b"x" * (_MAX_WRITE_FILE_BYTES + 1))
        ok, reason = proxy.validate_write_file("pi", "gateway/foo.py", big)
        assert not ok
        assert "exceeds maximum size" in reason

    def test_content_at_exact_cap_accepted(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        exact = _b64(b"x" * _MAX_WRITE_FILE_BYTES)
        ok, _ = proxy.validate_write_file("pi", "gateway/foo.py", exact)
        assert ok

    def test_root_itself_rejected(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", _ALLOWED_WRITE_ROOT, _b64(b"x"))
        assert not ok
        assert "root itself" in reason

    def test_prefix_collision_sibling_dir_rejected(self, ssh_config):
        """A directory that shares the root as a raw string prefix but is not
        actually nested under it (no separator) must be rejected."""
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", f"{_ALLOWED_WRITE_ROOT}-evil/x.py", _b64(b"x"))
        assert not ok
        assert "escapes allowed root" in reason

    def test_whitespace_only_path_rejected_at_proxy_layer(self, ssh_config):
        """Direct unit coverage of validate_write_file()'s own empty-path guard
        (the endpoint test for this goes through Pydantic's path_not_empty
        validator instead and never reaches this code path)."""
        proxy = SSHProxy(ssh_config)
        ok, reason = proxy.validate_write_file("pi", "   ", _b64(b"x"))
        assert not ok
        assert reason == "Empty path"


class TestSSHProxyWriteFileTransport:
    """Unit tests for SSHProxy.write_file() — verifies path/content travel as
    DATA over stdin into a FIXED remote command, never interpolated into the
    SSH command string."""

    @pytest.mark.asyncio
    async def test_write_file_sends_path_and_content_via_stdin(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        captured = {}

        class FakeProc:
            returncode = 0

            async def communicate(self, input=None):
                captured["stdin"] = input
                path_b64, _, content_b64 = input.partition(b"\n")
                content = base64.b64decode(content_b64)
                return (str(len(content)).encode(), b"")

            def kill(self):
                pass

            async def wait(self):
                pass

        async def fake_create_subprocess_exec(*args, **kwargs):
            captured["argv"] = args
            return FakeProc()

        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            result = await proxy.write_file("pi", "gateway/foo.py; rm -rf /", _b64(b"print('hi')"))

        assert result.exit_code == 0
        assert result.bytes_written == len(b"print('hi')")

        # The remote command (last argv element passed to `ssh`) is FIXED —
        # it must be identical across calls, including this one where the
        # "path" itself contains shell metacharacters (`; rm -rf /`).
        remote_command = captured["argv"][-1]
        assert "; rm -rf /" not in remote_command
        assert "print" not in remote_command  # content never in argv either
        assert remote_command.startswith('python3 -c "')

        # path/content instead travel on stdin as base64-encoded DATA.
        stdin_payload = captured["stdin"]
        sent_path_b64, _, sent_content_b64 = stdin_payload.partition(b"\n")
        assert (
            base64.b64decode(sent_path_b64).decode()
            == f"{_ALLOWED_WRITE_ROOT}/gateway/foo.py; rm -rf /"
        )
        assert base64.b64decode(sent_content_b64) == b"print('hi')"

    @pytest.mark.asyncio
    async def test_write_file_remote_command_is_identical_across_calls(self, ssh_config):
        """The remote command string must not vary with request content —
        proving it carries no interpolated attacker data."""
        proxy = SSHProxy(ssh_config)
        seen_commands = []

        class FakeProc:
            returncode = 0

            async def communicate(self, input=None):
                return (b"0", b"")

            def kill(self):
                pass

            async def wait(self):
                pass

        async def fake_create_subprocess_exec(*args, **kwargs):
            seen_commands.append(args[-1])
            return FakeProc()

        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            await proxy.write_file("pi", "a.py", _b64(b"one"))
            await proxy.write_file("pi", "b.py`whoami`", _b64(b"two; three"))

        assert seen_commands[0] == seen_commands[1]

    @pytest.mark.asyncio
    async def test_write_file_unknown_host_raises(self, ssh_config):
        proxy = SSHProxy(ssh_config)
        with pytest.raises(ValueError, match="Unknown host"):
            await proxy.write_file("nope", "a.py", _b64(b"x"))

    @pytest.mark.asyncio
    async def test_write_file_timeout(self, ssh_config):
        proxy = SSHProxy(ssh_config)

        class HangingProc:
            returncode = None

            async def communicate(self, input=None):
                import asyncio as _asyncio

                await _asyncio.sleep(5)
                return (b"", b"")

            def kill(self):
                pass

            async def wait(self):
                pass

        async def fake_create_subprocess_exec(*args, **kwargs):
            return HangingProc()

        # NOTE: `timeout or host.max_session_seconds` treats 0 as falsy (same
        # quirk as the pre-existing execute() method this mirrors), so use a
        # small positive timeout rather than 0 to force an immediate timeout.
        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            result = await proxy.write_file("pi", "a.py", _b64(b"x"), timeout=0.05)

        assert result.exit_code == -1
        assert "Timeout" in result.stderr

    @pytest.mark.asyncio
    async def test_write_file_oserror_from_subprocess(self, ssh_config):
        """ssh binary missing / spawn failure surfaces as exit_code=-1 with
        the OSError text in stderr, not an unhandled exception."""
        proxy = SSHProxy(ssh_config)

        async def fake_create_subprocess_exec(*args, **kwargs):
            raise OSError("ssh: command not found")

        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            result = await proxy.write_file("pi", "a.py", _b64(b"x"))

        assert result.exit_code == -1
        assert "command not found" in result.stderr

    @pytest.mark.asyncio
    async def test_write_file_non_numeric_stdout_falls_back_to_zero_bytes(self, ssh_config):
        """If the remote script exits 0 but its stdout isn't a parseable
        integer, bytes_written falls back to 0 rather than raising."""
        proxy = SSHProxy(ssh_config)

        class FakeProc:
            returncode = 0

            async def communicate(self, input=None):
                return (b"not-a-number", b"")

            def kill(self):
                pass

            async def wait(self):
                pass

        async def fake_create_subprocess_exec(*args, **kwargs):
            return FakeProc()

        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            result = await proxy.write_file("pi", "a.py", _b64(b"x"))

        assert result.exit_code == 0
        assert result.bytes_written == 0


class TestSSHWriteFileShellMetacharacterContentRoundTrip:
    """Gap coverage: prove the 'content is DATA, not a shell string' design
    goal actually holds end-to-end through the real HTTP endpoint, using
    file content that the OLD /ssh/exec command-string endpoint's
    INJECTION_PATTERNS regex would have rejected outright.

    Unlike test_write_file_valid_round_trip (which mocks SSHProxy.write_file
    itself and never exercises validate_write_file()'s or write_file()'s
    actual bytes-in/bytes-out path) and
    TestSSHProxyWriteFileTransport.test_write_file_sends_path_and_content_via_stdin
    (proxy-layer only, and only the *path* argument carries injection chars —
    the content argument there is plain source text), this drives the full
    stack: HTTP request -> Pydantic model -> validate_write_file() ->
    write_file() -> subprocess stdin, with the shell metacharacters living in
    the file CONTENT itself.
    """

    def test_content_with_semicolon_backtick_redirect_round_trips_through_full_endpoint(
        self, client, auth_headers, ssh_config
    ):
        # Content containing a semicolon, a backtick, and a shell redirect —
        # exactly the class of bytes INJECTION_PATTERNS exists to catch.
        payload = b"echo hi; ls `whoami` > /tmp/out.txt"

        # Sanity-check the premise: the OLD /ssh/exec command-string endpoint
        # would have rejected this same content via validate_command()'s
        # injection regex had it been sent as a `command` string.
        proxy = SSHProxy(ssh_config)
        cmd_ok, cmd_reason = proxy.validate_command("pi", payload.decode())
        assert cmd_ok is False
        assert "injection" in cmd_reason.lower() or "metacharacter" in cmd_reason.lower()
        assert INJECTION_PATTERNS.search(payload.decode()) is not None

        captured = {}

        class FakeProc:
            returncode = 0

            async def communicate(self, input=None):
                captured["stdin"] = input
                _, _, content_b64 = input.partition(b"\n")
                content = base64.b64decode(content_b64)
                captured["decoded_content"] = content
                return (str(len(content)).encode(), b"")

            def kill(self):
                pass

            async def wait(self):
                pass

        async def fake_create_subprocess_exec(*args, **kwargs):
            captured["argv"] = args
            return FakeProc()

        with patch("asyncio.create_subprocess_exec", new=fake_create_subprocess_exec):
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/injection_probe.py",
                    "content_base64": _b64(payload),
                    "reason": "prove content is data, not shell text",
                },
                headers=auth_headers,
            )

        # The NEW endpoint accepts it — validate_write_file() only checks
        # host/path/base64-validity/size, never content shell-safety.
        assert resp.status_code == 200
        data = resp.json()
        assert data["success"] is True
        assert data["bytes_written"] == len(payload)

        # ...and transmits it byte-for-byte unmodified over stdin, never as
        # part of the remote command string. (The fixed launcher command
        # itself legitimately contains a literal ';' — `import base64,sys;
        # exec(...)` — so we assert on the payload's own injection bytes
        # being absent, not on the metacharacter class in general, and cross-
        # check against the module's known-fixed base64 blob.)
        assert captured["decoded_content"] == payload
        remote_command = captured["argv"][-1]
        assert payload.decode() not in remote_command
        assert _b64(payload) not in remote_command
        assert remote_command == (
            'python3 -c "import base64,sys;exec(base64.b64decode('
            f"'{_REMOTE_WRITE_FILE_SCRIPT_B64}'))\""
        )


class TestSSHWriteFileLedgerAudit:
    """Gap coverage: confirm a real audit-ledger row is created for BOTH a
    successful write and a denied write, mirroring test_ssh_endpoints.py's
    TestSSHHistory assertion style (POST, then GET /ssh/history) but tying
    the returned entry back to the specific request's audit_id rather than
    only checking that *some* entry exists — the existing
    test_write_file_denial_is_audited only asserts total >= 1, which would
    still pass even if the wrong entry (or a leftover from another test) were
    counted.
    """

    def test_write_file_success_creates_matching_ledger_entry(self, client, auth_headers):
        mock_result = SSHWriteResult(
            host="pi",
            path="gateway/ok.py",
            bytes_written=5,
            stdout="5",
            stderr="",
            exit_code=0,
            duration_seconds=0.01,
        )
        with patch.object(
            app_state.ssh_proxy,
            "write_file",
            new_callable=AsyncMock,
            return_value=mock_result,
        ):
            resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/ok.py",
                    "content_base64": _b64(b"hello"),
                    "reason": "audit check",
                },
                headers=auth_headers,
            )
        assert resp.status_code == 200
        audit_id = resp.json()["audit_id"]
        assert audit_id == resp.json()["request_id"]

        history = client.get("/ssh/history", headers=auth_headers)
        assert history.status_code == 200
        history_data = history.json()
        assert history_data["total"] >= 1

        matching = [e for e in history_data["entries"] if e["id"] == audit_id]
        assert len(matching) == 1, "success write must create exactly one matching ledger entry"
        assert matching[0]["forwarded_to"] == "pi"
        assert matching[0]["source"] == "ssh"

    def test_write_file_success_and_denial_both_create_distinct_ledger_entries(
        self, client, auth_headers
    ):
        """Both outcomes append to the SAME audit trail — a denial is not
        silently dropped once a successful write has already been logged,
        and vice versa."""
        mock_result = SSHWriteResult(
            host="pi",
            path="gateway/ok2.py",
            bytes_written=3,
            stdout="3",
            stderr="",
            exit_code=0,
            duration_seconds=0.01,
        )
        with patch.object(
            app_state.ssh_proxy,
            "write_file",
            new_callable=AsyncMock,
            return_value=mock_result,
        ):
            success_resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "gateway/ok2.py",
                    "content_base64": _b64(b"abc"),
                },
                headers=auth_headers,
            )
        assert success_resp.status_code == 200
        success_audit_id = success_resp.json()["audit_id"]

        with patch.object(app_state.ssh_proxy, "write_file", new_callable=AsyncMock) as mock_write:
            denied_resp = client.post(
                "/ssh/write_file",
                json={
                    "host": "pi",
                    "path": "/etc/shadow",
                    "content_base64": _b64(b"malicious"),
                },
                headers=auth_headers,
            )
        assert denied_resp.status_code == 403
        mock_write.assert_not_awaited()

        history = client.get("/ssh/history", headers=auth_headers)
        assert history.status_code == 200
        history_data = history.json()
        assert history_data["total"] == 2

        entry_ids = {e["id"] for e in history_data["entries"]}
        assert success_audit_id in entry_ids
        # The denial path never returns an audit id to the caller (only a
        # 403 detail string), so its entry is identified by exclusion: the
        # second entry present that is NOT the success entry.
        assert len(entry_ids) == 2
