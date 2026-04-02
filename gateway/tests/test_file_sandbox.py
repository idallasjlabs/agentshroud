# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for file I/O sandboxing."""

from __future__ import annotations

import pytest

from gateway.security.file_sandbox import (
    FileSandbox,
    FileSandboxConfig,
    PIIScanner,
)


@pytest.fixture
def default_config():
    return FileSandboxConfig()


@pytest.fixture
def strict_config():
    return FileSandboxConfig(
        mode="enforce",
        allowed_read_paths=["/workspace", "/tmp"],
        allowed_write_paths=["/workspace", "/tmp"],
        blocked_paths=["/etc/shadow", "/etc/passwd", "~/.ssh"],
    )


@pytest.fixture
def sandbox(default_config):
    return FileSandbox(config=default_config)


@pytest.fixture
def strict_sandbox(strict_config):
    return FileSandbox(config=strict_config)


class TestFileSandboxConfig:
    def test_default_mode_is_enforce(self, default_config):
        assert default_config.mode == "enforce"

    def test_default_has_reasonable_allowed_paths(self, default_config):
        assert (
            default_config.allowed_write_paths is None
            or "/workspace" in default_config.allowed_write_paths
        )

    def test_default_blocks_sensitive_paths(self, default_config):
        assert any("shadow" in p for p in default_config.blocked_paths)


class TestNormalFileOperations:
    def test_workspace_read_allowed(self, sandbox):
        v = sandbox.check_read("/workspace/project/main.py", agent_id="agent1")
        assert v.allowed is True

    def test_workspace_write_allowed(self, sandbox):
        v = sandbox.check_write("/home/user/output.txt", agent_id="agent1", content="hello")
        assert v.allowed is True

    def test_tmp_read_allowed(self, sandbox):
        v = sandbox.check_read("/tmp/cache.json", agent_id="agent1")
        assert v.allowed is True

    def test_tmp_write_allowed(self, sandbox):
        v = sandbox.check_write("/tmp/output.txt", agent_id="agent1", content="data")
        assert v.allowed is True

    def test_project_files_allowed(self, sandbox):
        v = sandbox.check_read("/workspace/src/app.py", agent_id="agent1")
        assert v.allowed is True

    def test_monitor_mode_allows_everything(self):
        """Even blocked paths are allowed in monitor mode (just flagged)."""
        monitor_sandbox = FileSandbox(config=FileSandboxConfig(mode="monitor"))
        v = monitor_sandbox.check_read("/etc/shadow", agent_id="agent1")
        assert v.allowed is True
        assert v.flagged is True


class TestSensitivePathBlocking:
    def test_etc_shadow_flagged(self, sandbox):
        v = sandbox.check_read("/etc/shadow", agent_id="agent1")
        assert v.flagged is True

    def test_etc_passwd_flagged(self, sandbox):
        v = sandbox.check_read("/etc/passwd", agent_id="agent1")
        assert v.flagged is True

    def test_ssh_private_key_flagged(self, sandbox):
        v = sandbox.check_read("/home/user/.ssh/id_rsa", agent_id="agent1")
        assert v.flagged is True

    def test_env_file_flagged(self, sandbox):
        v = sandbox.check_read("/workspace/.env", agent_id="agent1")
        assert v.flagged is True

    def test_credential_file_flagged(self, sandbox):
        v = sandbox.check_read("/home/user/.aws/credentials", agent_id="agent1")
        assert v.flagged is True

    def test_enforce_blocks_sensitive(self, strict_sandbox):
        v = strict_sandbox.check_read("/etc/shadow", agent_id="agent1")
        assert v.allowed is False

    def test_enforce_blocks_outside_allowed(self, strict_sandbox):
        v = strict_sandbox.check_read("/var/log/syslog", agent_id="agent1")
        assert v.allowed is False


class TestPIIScanning:
    def test_ssn_detected(self):
        scanner = PIIScanner()
        result = scanner.scan("My SSN is 123-45-6789")
        assert result.has_pii is True
        assert "ssn" in [f.type for f in result.findings]

    def test_credit_card_detected(self):
        scanner = PIIScanner()
        result = scanner.scan("Card: 4111-1111-1111-1111")
        assert result.has_pii is True

    def test_email_detected(self):
        scanner = PIIScanner()
        result = scanner.scan("Contact: secret@example.com")
        assert result.has_pii is True

    def test_no_pii_clean(self):
        scanner = PIIScanner()
        result = scanner.scan("Hello world, this is normal text")
        assert result.has_pii is False

    def test_pii_in_write_flagged(self, sandbox):
        v = sandbox.check_write("/workspace/out.txt", "agent1", "SSN: 123-45-6789")
        assert v.flagged is True

    def test_api_key_pattern_detected(self):
        scanner = PIIScanner()
        result = scanner.scan("sk-proj-abc123def456ghi789jkl012mno345")
        assert result.has_pii is True


class TestStagingPatternDetection:
    def test_large_write_then_network_flagged(self, sandbox):
        sandbox.check_write("/tmp/staging.bin", "agent1", "x" * 100_000)
        sandbox.record_network_activity("agent1")
        patterns = sandbox.detect_staging_patterns("agent1")
        assert len(patterns) > 0

    def test_small_writes_not_flagged(self, sandbox):
        sandbox.check_write("/workspace/small.txt", "agent1", "hello")
        sandbox.record_network_activity("agent1")
        patterns = sandbox.detect_staging_patterns("agent1")
        assert len(patterns) == 0

    def test_large_write_without_network_not_flagged(self, sandbox):
        sandbox.check_write("/tmp/big.bin", "agent1", "x" * 100_000)
        patterns = sandbox.detect_staging_patterns("agent1")
        assert len(patterns) == 0


class TestFileAudit:
    def test_read_logged(self, sandbox):
        sandbox.check_read("/workspace/file.py", agent_id="agent1")
        logs = sandbox.get_audit_log("agent1")
        assert len(logs) == 1
        assert logs[0].operation == "read"

    def test_write_logged(self, sandbox):
        sandbox.check_write("/workspace/out.txt", "agent1", "data")
        logs = sandbox.get_audit_log("agent1")
        assert len(logs) == 1
        assert logs[0].operation == "write"

    def test_audit_has_path(self, sandbox):
        sandbox.check_read("/workspace/file.py", agent_id="agent1")
        logs = sandbox.get_audit_log("agent1")
        assert logs[0].path == "/workspace/file.py"

    def test_temp_file_tracking(self, sandbox):
        sandbox.check_write("/tmp/tempfile1.txt", "agent1", "data")
        sandbox.check_write("/tmp/tempfile2.txt", "agent1", "data")
        temps = sandbox.get_temp_files("agent1")
        assert len(temps) == 2
