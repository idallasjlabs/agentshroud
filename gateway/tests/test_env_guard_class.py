# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Behavior tests for the EnvironmentGuard class (gateway/security/env_guard.py).

The existing test_env_guard.py exercises only the module-level check_command /
scrub_output helpers. These tests drive the EnvironmentGuard object directly:
file-access blocking, command blocking, output scrubbing, per-agent monitoring,
leakage summaries, and report export. All pure — no network, no sleeps.
"""

from __future__ import annotations

import json

import pytest

from gateway.security.env_guard import EnvironmentGuard


@pytest.fixture
def guard():
    return EnvironmentGuard()


class TestCheckFileAccess:
    def test_blocks_exact_proc_self_environ(self, guard):
        assert guard.check_file_access("/proc/self/environ", "agent-1") is False
        # Blocking must be recorded as a critical path_block leakage.
        assert len(guard.detected_leakages) == 1
        leak = guard.detected_leakages[0]
        assert leak.severity == "critical"
        assert leak.detection_method == "path_block"
        assert "agent-1" in leak.context

    def test_blocks_wildcard_proc_pid_environ(self, guard):
        # /proc/*/environ wildcard should match a numeric PID path.
        assert guard.check_file_access("/proc/1234/environ", "agent-2") is False
        assert guard.detected_leakages[0].detection_method == "path_block"

    def test_allows_unrelated_file(self, guard):
        assert guard.check_file_access("/tmp/notes.txt", "agent-3") is True
        assert guard.detected_leakages == []

    def test_allows_file_named_environ_elsewhere(self, guard):
        # A file literally called environ but not under /proc is fine.
        assert guard.check_file_access("/home/user/environ", "agent-4") is True
        assert guard.detected_leakages == []


class TestCheckCommandExecution:
    def test_blocks_env_command(self, guard):
        assert guard.check_command_execution("env", "a") is False
        assert guard.detected_leakages[0].severity == "high"
        assert guard.detected_leakages[0].detection_method == "command_block"

    def test_blocks_printenv(self, guard):
        assert guard.check_command_execution("printenv API_KEY", "a") is False

    def test_blocks_indirect_var_expansion(self, guard):
        # $SECRET expansion is a pattern_block (medium), not a base-command block.
        assert guard.check_command_execution("echo $SECRET", "a") is False
        assert guard.detected_leakages[0].detection_method == "pattern_block"
        assert guard.detected_leakages[0].severity == "medium"

    def test_blocks_cat_proc_environ_pattern(self, guard):
        assert guard.check_command_execution("cat /proc/self/environ", "a") is False

    def test_allows_plain_command(self, guard):
        assert guard.check_command_execution("ls -la", "a") is True
        assert guard.detected_leakages == []

    def test_empty_command_is_allowed(self, guard):
        assert guard.check_command_execution("", "a") is True

    def test_unparseable_text_is_allowed(self, guard):
        # Unbalanced quote raises in shlex → treated as not-a-command, allowed.
        assert guard.check_command_execution('he said "hello', "a") is True


class TestScrubCommandOutput:
    def test_scrubs_named_credential_env_var(self, guard):
        # The long alphanumeric secret matches the generic API-key pattern, which
        # redacts first; the env-var name is still recorded as a leaked var and
        # the overall severity is high because it is a known credential var.
        out = "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMIabcdefghijklmnop1234567890xy"
        scrubbed = guard.scrub_command_output(out, "env")
        assert "wJalrXUtnFEMIabcdefghijklmnop1234567890xy" not in scrubbed
        assert "REDACTED" in scrubbed
        assert guard.detected_leakages
        assert "AWS_SECRET_ACCESS_KEY" in guard.detected_leakages[0].leaked_vars
        assert guard.detected_leakages[0].severity == "high"

    def test_scrubs_credential_looking_value_for_unknown_var(self, guard):
        # MYVAR is not a known credential name; its token-like value is still
        # redacted (via the generic API-key pattern) and severity stays medium.
        out = "MYVAR=abcdefghijklmnopqrstuvwxyz0123456789"
        scrubbed = guard.scrub_command_output(out, "printenv")
        assert "abcdefghijklmnopqrstuvwxyz0123456789" not in scrubbed
        assert "REDACTED" in scrubbed
        assert guard.detected_leakages[0].severity == "medium"

    def test_named_var_with_short_value_uses_redacted_marker(self, guard):
        # A short value with punctuation does not match the generic API-key
        # pattern, so the name-based branch replaces VAR=value with [REDACTED].
        out = "PASSWORD=p@ss-w0rd!"
        scrubbed = guard.scrub_command_output(out, "env")
        assert scrubbed == "PASSWORD=[REDACTED]"
        assert guard.detected_leakages[0].leaked_vars == ["PASSWORD"]

    def test_scrubs_openai_key_pattern(self, guard):
        key = "sk-" + "A" * 48
        scrubbed = guard.scrub_command_output(f"leak {key}", "cat file")
        assert key not in scrubbed
        assert "[REDACTED-API-KEY]" in scrubbed

    def test_clean_output_unchanged_and_no_leakage(self, guard):
        out = "total 0\ndrwxr-xr-x  2 user  staff"
        scrubbed = guard.scrub_command_output(out, "ls")
        assert scrubbed == out
        assert guard.detected_leakages == []


class TestLooksLikeCredential:
    def test_short_value_is_not_credential(self, guard):
        assert guard._looks_like_credential("abc") is False

    def test_long_alphanumeric_is_credential(self, guard):
        assert guard._looks_like_credential("A1b2C3d4E5f6G7h8I9j0K1l2") is True

    def test_base64_padding_is_credential(self, guard):
        assert guard._looks_like_credential("c29tZS1sb25nLXNlY3JldA==") is True

    def test_plain_word_is_not_credential(self, guard):
        assert guard._looks_like_credential("hello world here") is False


class TestMonitorEnvironmentAccess:
    def test_no_activity_is_low_risk(self, guard):
        result = guard.monitor_environment_access("quiet-agent")
        assert result["risk_level"] == "low"
        assert result["environment_access_attempts"] == 0
        assert result["blocked_attempts"] == 0

    def test_critical_leakage_yields_critical_risk(self, guard):
        guard.check_file_access("/proc/self/environ", "danger-agent")
        result = guard.monitor_environment_access("danger-agent")
        assert result["risk_level"] == "critical"
        assert result["environment_access_attempts"] == 1
        assert result["blocked_attempts"] == 1

    def test_multiple_high_yields_high_risk(self, guard):
        # >2 high-severity command blocks → high risk (no critical present).
        for _ in range(3):
            guard.check_command_execution("env", "busy-agent")
        result = guard.monitor_environment_access("busy-agent")
        assert result["risk_level"] == "high"
        assert result["environment_access_attempts"] == 3

    def test_many_medium_yields_medium_risk(self, guard):
        # 6 medium pattern-blocks, no high/critical → medium risk.
        for i in range(6):
            guard.check_command_execution(f"echo $VAR{i}", "med-agent")
        result = guard.monitor_environment_access("med-agent")
        assert result["risk_level"] == "medium"


class TestSummaryAndExport:
    def test_summary_aggregates_by_severity_and_method(self, guard):
        guard.check_file_access("/proc/self/environ", "a")  # critical/path_block
        guard.check_command_execution("env", "a")  # high/command_block
        summary = guard.get_leakage_summary()
        assert summary["total_leakages"] == 2
        assert summary["by_severity"]["critical"] == 1
        assert summary["by_severity"]["high"] == 1
        assert summary["by_detection_method"]["path_block"] == 1
        assert summary["by_detection_method"]["command_block"] == 1
        assert isinstance(summary["unique_sources"], list)
        assert isinstance(summary["leaked_variables"], list)

    def test_clear_resets_leakages(self, guard):
        guard.check_command_execution("env", "a")
        assert guard.detected_leakages
        guard.clear_detected_leakages()
        assert guard.detected_leakages == []

    def test_export_writes_valid_json_report(self, guard, tmp_path):
        guard.scrub_command_output("API_KEY=supersecretvalue1234567890", "env")
        out = tmp_path / "report.json"
        guard.export_leakage_report(str(out))
        assert out.exists()
        data = json.loads(out.read_text())
        assert "timestamp" in data
        assert data["summary"]["total_leakages"] >= 1
        assert isinstance(data["leakages"], list)
        assert data["leakages"][0]["severity"] in {"low", "medium", "high", "critical"}
