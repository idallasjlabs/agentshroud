# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the security toolchain modules.

Covers: Trivy, ClamAV, Falco, Wazuh, Health Report, Alert Dispatcher.
Target: 50+ tests.
"""

from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path
from unittest.mock import MagicMock, patch

from gateway.security.trivy_report import (
    generate_summary,
    parse_trivy_output,
    run_trivy_scan,
)

# ═══════════════════════════════════════════
# Trivy Report Tests
# ═══════════════════════════════════════════


SAMPLE_TRIVY_OUTPUT = {
    "Results": [
        {
            "Target": "python:3.13-slim",
            "Vulnerabilities": [
                {
                    "VulnerabilityID": "CVE-2024-0001",
                    "Severity": "CRITICAL",
                    "PkgName": "openssl",
                    "InstalledVersion": "3.0.1",
                    "FixedVersion": "3.0.2",
                    "Title": "OpenSSL buffer overflow",
                },
                {
                    "VulnerabilityID": "CVE-2024-0002",
                    "Severity": "HIGH",
                    "PkgName": "curl",
                    "InstalledVersion": "7.80.0",
                    "FixedVersion": "7.81.0",
                    "Title": "Curl header injection",
                },
                {
                    "VulnerabilityID": "CVE-2024-0003",
                    "Severity": "MEDIUM",
                    "PkgName": "zlib",
                    "InstalledVersion": "1.2.11",
                    "FixedVersion": "1.2.12",
                    "Title": "Zlib memory corruption",
                },
                {
                    "VulnerabilityID": "CVE-2024-0004",
                    "Severity": "LOW",
                    "PkgName": "bash",
                    "InstalledVersion": "5.1",
                    "FixedVersion": "",
                    "Title": "Bash minor issue",
                },
            ],
        },
        {
            "Target": "node_modules",
            "Vulnerabilities": [
                {
                    "VulnerabilityID": "CVE-2024-0005",
                    "Severity": "CRITICAL",
                    "PkgName": "lodash",
                    "InstalledVersion": "4.17.20",
                    "FixedVersion": "4.17.21",
                    "Title": "Prototype pollution",
                },
            ],
        },
    ]
}


class TestTrivyParser:
    def test_parse_empty_output(self):
        result = parse_trivy_output({})
        assert result["total_vulnerabilities"] == 0
        assert result["error"] is None

    def test_parse_no_results_key(self):
        result = parse_trivy_output({"SchemaVersion": 2})
        assert result["total_vulnerabilities"] == 0

    def test_parse_counts_by_severity(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert result["by_severity"]["CRITICAL"] == 2
        assert result["by_severity"]["HIGH"] == 1
        assert result["by_severity"]["MEDIUM"] == 1
        assert result["by_severity"]["LOW"] == 1

    def test_parse_total_vulnerabilities(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert result["total_vulnerabilities"] == 5

    def test_parse_affected_packages(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert "openssl" in result["affected_packages"]
        assert "lodash" in result["affected_packages"]
        assert result["affected_package_count"] == 5

    def test_parse_top_cves_ordered_by_severity(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        # Critical should come first
        assert result["top_cves"][0]["severity"] == "CRITICAL"

    def test_parse_top_cves_limited(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert len(result["top_cves"]) <= 20

    def test_parse_has_timestamp(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert "timestamp" in result

    def test_parse_scanner_name(self):
        result = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        assert result["scanner"] == "trivy"

    def test_parse_unknown_severity(self):
        raw = {
            "Results": [
                {
                    "Target": "t",
                    "Vulnerabilities": [
                        {"VulnerabilityID": "X", "Severity": "WEIRD", "PkgName": "p"}
                    ],
                }
            ]
        }
        result = parse_trivy_output(raw)
        assert result["by_severity"]["UNKNOWN"] == 1


class TestTrivySummary:
    def test_summary_clean(self):
        report = parse_trivy_output({})
        s = generate_summary(report)
        assert s["status"] == "clean"
        assert s["tool"] == "trivy"

    def test_summary_critical(self):
        report = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        s = generate_summary(report)
        assert s["status"] == "critical"
        assert s["critical"] == 2

    def test_summary_warning_high_only(self):
        raw = {
            "Results": [
                {
                    "Target": "t",
                    "Vulnerabilities": [
                        {"VulnerabilityID": "X", "Severity": "HIGH", "PkgName": "p"}
                    ],
                }
            ]
        }
        report = parse_trivy_output(raw)
        s = generate_summary(report)
        assert s["status"] == "warning"

    def test_summary_error(self):
        s = generate_summary({"error": "timeout"})
        assert s["status"] == "error"

    def test_summary_top_cves_ids(self):
        report = parse_trivy_output(SAMPLE_TRIVY_OUTPUT)
        s = generate_summary(report)
        assert "CVE-2024-0001" in s["top_cves"]


class TestTrivyRun:
    @patch("gateway.security.trivy_report.subprocess.run")
    def test_run_binary_not_found(self, mock_run):
        mock_run.side_effect = FileNotFoundError()
        result = run_trivy_scan(trivy_bin="/nonexistent/trivy")
        assert result["error"] == "binary_not_found"

    @patch("gateway.security.trivy_report.subprocess.run")
    def test_run_timeout(self, mock_run):
        import subprocess

        mock_run.side_effect = subprocess.TimeoutExpired(cmd="trivy", timeout=600)
        result = run_trivy_scan()
        assert result["error"] == "timeout"

    @patch("gateway.security.trivy_report.subprocess.run")
    def test_run_parse_error(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0, stdout="not json", stderr="")
        result = run_trivy_scan()
        assert result["error"] == "parse_error"

    @patch("gateway.security.trivy_report.subprocess.run")
    def test_run_success(self, mock_run):
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout=json.dumps(SAMPLE_TRIVY_OUTPUT),
            stderr="",
        )
        result = run_trivy_scan()
        assert result["total_vulnerabilities"] == 5


# ═══════════════════════════════════════════
# ClamAV Scanner Tests
# ═══════════════════════════════════════════

from gateway.security.clamav_scanner import (  # noqa: E402
    generate_summary as clamav_summary,
)
from gateway.security.clamav_scanner import (
    parse_clamscan_output,
    run_clamscan,
    update_virus_db,
)

SAMPLE_CLAMSCAN_CLEAN = """/home/node/file1.py: OK
/home/node/file2.js: OK
/home/node/file3.txt: OK
"""

SAMPLE_CLAMSCAN_INFECTED = """/home/node/file1.py: OK
/home/node/malware.exe: Win.Trojan.Agent-123 FOUND
/home/node/eicar.com: Eicar-Signature FOUND
/home/node/file3.txt: OK
"""


class TestClamAVParser:
    def test_parse_clean_output(self):
        result = parse_clamscan_output(SAMPLE_CLAMSCAN_CLEAN)
        assert result["infected_count"] == 0
        assert result["scanned_files"] == 3

    def test_parse_infected_output(self):
        result = parse_clamscan_output(SAMPLE_CLAMSCAN_INFECTED)
        assert result["infected_count"] == 2
        assert result["scanned_files"] == 4

    def test_parse_infected_files_details(self):
        result = parse_clamscan_output(SAMPLE_CLAMSCAN_INFECTED)
        files = [f["file"] for f in result["infected_files"]]
        assert "/home/node/malware.exe" in files
        assert "/home/node/eicar.com" in files

    def test_parse_signatures(self):
        result = parse_clamscan_output(SAMPLE_CLAMSCAN_INFECTED)
        sigs = [f["signature"] for f in result["infected_files"]]
        assert "Win.Trojan.Agent-123" in sigs
        assert "Eicar-Signature" in sigs

    def test_parse_empty_output(self):
        result = parse_clamscan_output("")
        assert result["infected_count"] == 0
        assert result["scanned_files"] == 0

    def test_parse_scanner_name(self):
        result = parse_clamscan_output("")
        assert result["scanner"] == "clamav"

    def test_parse_has_timestamp(self):
        result = parse_clamscan_output("")
        assert "timestamp" in result


class TestClamAVSummary:
    def test_summary_clean(self):
        report = parse_clamscan_output(SAMPLE_CLAMSCAN_CLEAN)
        s = clamav_summary(report)
        assert s["status"] == "clean"
        assert s["findings"] == 0

    def test_summary_infected(self):
        report = parse_clamscan_output(SAMPLE_CLAMSCAN_INFECTED)
        s = clamav_summary(report)
        assert s["status"] == "critical"
        assert s["critical"] == 2

    def test_summary_error(self):
        s = clamav_summary({"error": "binary_not_found", "scanner": "clamav"})
        assert s["status"] == "error"


class TestClamAVRun:
    @patch("gateway.security.clamav_scanner.subprocess.run")
    def test_run_not_found(self, mock_run):
        mock_run.side_effect = FileNotFoundError()
        result = run_clamscan(clamscan_bin="/nonexistent")
        assert result["error"] == "binary_not_found"

    @patch("gateway.security.clamav_scanner.subprocess.run")
    def test_update_db_not_found(self, mock_run):
        mock_run.side_effect = FileNotFoundError()
        result = update_virus_db(freshclam_bin="/nonexistent")
        assert result["status"] == "error"


# ═══════════════════════════════════════════
# Falco Monitor Tests
# ═══════════════════════════════════════════

from gateway.security.falco_monitor import (
    categorize_alerts,
)
from gateway.security.falco_monitor import (  # noqa: E402
    generate_summary as falco_summary,
)
from gateway.security.falco_monitor import (
    is_agentshroud_rule,
    parse_alert,
    read_alerts,
)

SAMPLE_FALCO_ALERT = {
    "time": "2024-01-15T10:30:00.000Z",
    "rule": "Container Shell Spawned",
    "priority": "Warning",
    "output": "Shell spawned in container (user=root container=openclaw shell=bash)",
    "source": "syscall",
    "hostname": "agentshroud-host",
    "output_fields": {
        "container.id": "abc123",
        "container.name": "openclaw",
        "proc.name": "bash",
    },
}

SAMPLE_FALCO_CRITICAL = {
    "time": "2024-01-15T10:31:00.000Z",
    "rule": "Secret File Access",
    "priority": "Critical",
    "output": "Sensitive file accessed",
    "source": "syscall",
    "hostname": "agentshroud-host",
    "output_fields": {},
}


class TestFalcoParser:
    def test_parse_valid_alert(self):
        result = parse_alert(SAMPLE_FALCO_ALERT)
        assert result is not None
        assert result["rule"] == "Container Shell Spawned"
        assert result["severity"] == "MEDIUM"

    def test_parse_critical_alert(self):
        result = parse_alert(SAMPLE_FALCO_CRITICAL)
        assert result["severity"] == "CRITICAL"

    def test_parse_empty_alert(self):
        assert parse_alert({}) is None
        assert parse_alert(None) is None

    def test_parse_container_info(self):
        result = parse_alert(SAMPLE_FALCO_ALERT)
        assert result["container_name"] == "openclaw"

    def test_is_agentshroud_rule_true(self):
        assert is_agentshroud_rule("Container Shell Spawned")
        assert is_agentshroud_rule("AgentShroud Custom Rule")
        assert is_agentshroud_rule("Crypto Mining Detection")

    def test_is_agentshroud_rule_false(self):
        assert not is_agentshroud_rule("Random System Rule")
        assert not is_agentshroud_rule("")


class TestFalcoCategorize:
    def test_categorize_empty(self):
        cats = categorize_alerts([])
        assert all(len(v) == 0 for v in cats.values())

    def test_categorize_mixed(self):
        alerts = [
            parse_alert(SAMPLE_FALCO_ALERT),
            parse_alert(SAMPLE_FALCO_CRITICAL),
        ]
        cats = categorize_alerts(alerts)
        assert len(cats["CRITICAL"]) == 1
        assert len(cats["MEDIUM"]) == 1


class TestFalcoSummary:
    def test_summary_clean(self):
        s = falco_summary([])
        assert s["status"] == "clean"
        assert s["findings"] == 0

    def test_summary_with_alerts(self):
        alerts = [parse_alert(SAMPLE_FALCO_ALERT), parse_alert(SAMPLE_FALCO_CRITICAL)]
        s = falco_summary(alerts)
        assert s["findings"] == 2
        assert s["critical"] == 1

    def test_summary_top_rules(self):
        alerts = [parse_alert(SAMPLE_FALCO_ALERT)] * 3
        s = falco_summary(alerts)
        assert s["top_rules"][0]["count"] == 3

    def test_read_alerts_missing_dir(self):
        alerts = read_alerts(Path("/nonexistent/falco"))
        assert alerts == []


# ═══════════════════════════════════════════
# Wazuh Client Tests
# ═══════════════════════════════════════════

from gateway.security.wazuh_client import generate_summary as wazuh_summary
from gateway.security.wazuh_client import (
    get_fim_events,
    get_rootkit_events,
    level_to_severity,
)
from gateway.security.wazuh_client import parse_alert as wazuh_parse  # noqa: E402

SAMPLE_WAZUH_FIM = {
    "timestamp": "2024-01-15T10:30:00Z",
    "rule": {"id": "553", "level": 7, "description": "File modified"},
    "agent": {"name": "agentshroud-agent"},
    "syscheck": {
        "path": "/host/workspace/config.yaml",
        "event": "modified",
        "md5_before": "abc123",
        "md5_after": "def456",
    },
}

SAMPLE_WAZUH_ROOTKIT = {
    "timestamp": "2024-01-15T10:31:00Z",
    "rule": {"id": "510", "level": 14, "description": "Trojan detected"},
    "agent": {"name": "agentshroud-agent"},
    "syscheck": {},
}


class TestWazuhParser:
    def test_parse_fim_event(self):
        result = wazuh_parse(SAMPLE_WAZUH_FIM)
        assert result["alert_type"] == "file_integrity_modified"
        assert result["file_path"] == "/host/workspace/config.yaml"

    def test_parse_rootkit_event(self):
        result = wazuh_parse(SAMPLE_WAZUH_ROOTKIT)
        assert result["alert_type"] == "rootkit_trojan"
        assert result["severity"] == "CRITICAL"

    def test_parse_empty(self):
        assert wazuh_parse(None) is None
        assert wazuh_parse({}) is None

    def test_level_to_severity(self):
        assert level_to_severity(0) == "LOW"
        assert level_to_severity(7) == "MEDIUM"
        assert level_to_severity(10) == "HIGH"
        assert level_to_severity(14) == "CRITICAL"

    def test_get_fim_events(self):
        alerts = [wazuh_parse(SAMPLE_WAZUH_FIM), wazuh_parse(SAMPLE_WAZUH_ROOTKIT)]
        fim = get_fim_events(alerts)
        assert len(fim) == 1

    def test_get_rootkit_events(self):
        alerts = [wazuh_parse(SAMPLE_WAZUH_FIM), wazuh_parse(SAMPLE_WAZUH_ROOTKIT)]
        rootkits = get_rootkit_events(alerts)
        assert len(rootkits) == 1


class TestWazuhSummary:
    def test_summary_clean(self):
        s = wazuh_summary([])
        assert s["status"] == "clean"

    def test_summary_with_rootkit(self):
        alerts = [wazuh_parse(SAMPLE_WAZUH_ROOTKIT)]
        s = wazuh_summary(alerts)
        assert s["status"] == "critical"
        assert s["rootkit_events"] == 1


# ═══════════════════════════════════════════
# Health Report Tests
# ═══════════════════════════════════════════

from gateway.security.health_report import (  # noqa: E402
    calculate_overall_score,
    calculate_tool_score,
    format_report,
    generate_report,
    get_trend,
    score_to_grade,
)


class TestHealthScoring:
    def test_perfect_score(self):
        s = calculate_tool_score({"critical": 0, "high": 0, "medium": 0, "low": 0})
        assert s == 100.0

    def test_one_critical(self):
        s = calculate_tool_score({"critical": 1, "high": 0, "medium": 0, "low": 0})
        assert s == 80.0

    def test_score_floor(self):
        s = calculate_tool_score({"critical": 10, "high": 0, "medium": 0, "low": 0})
        assert s == 0.0

    def test_error_status_gets_50(self):
        s = calculate_tool_score({"status": "error"})
        assert s == 50.0

    def test_mixed_severities(self):
        s = calculate_tool_score({"critical": 1, "high": 1, "medium": 1, "low": 1})
        assert s == 100 - 20 - 10 - 3 - 1  # 66

    def test_grade_a(self):
        assert score_to_grade(95) == "A"
        assert score_to_grade(90) == "A"

    def test_grade_b(self):
        assert score_to_grade(85) == "B"

    def test_grade_c(self):
        assert score_to_grade(75) == "C"

    def test_grade_d(self):
        assert score_to_grade(65) == "D"

    def test_grade_f(self):
        assert score_to_grade(50) == "F"
        assert score_to_grade(0) == "F"


class TestHealthOverallScore:
    def test_all_clean(self):
        summaries = {
            "trivy": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "clamav": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "falco": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "wazuh": {"critical": 0, "high": 0, "medium": 0, "low": 0},
            "gateway": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        }
        score = calculate_overall_score(summaries)
        assert score == 100.0

    def test_partial_tools(self):
        summaries = {
            "trivy": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        }
        score = calculate_overall_score(summaries)
        assert score == 100.0

    def test_empty_summaries(self):
        score = calculate_overall_score({})
        assert score == 100.0


class TestHealthReport:
    def test_generate_report(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            summaries = {
                "trivy": {
                    "critical": 1,
                    "high": 2,
                    "medium": 0,
                    "low": 0,
                    "findings": 3,
                },
                "clamav": {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "findings": 0,
                },
            }
            report = generate_report(summaries, db_path=db_path)
            assert "grade" in report
            assert "overall_score" in report
            assert report["total_critical"] == 1

    def test_format_report_string(self):
        report = {
            "timestamp": "2024-01-15T10:00:00Z",
            "overall_score": 85.0,
            "grade": "B",
            "total_findings": 5,
            "total_critical": 1,
            "total_high": 2,
            "tool_scores": {
                "trivy": {
                    "score": 70,
                    "weight": 0.25,
                    "summary": {
                        "status": "warning",
                        "critical": 1,
                        "high": 2,
                        "medium": 0,
                        "low": 0,
                    },
                },
            },
            "trend": [],
            "recommendations": ["🔴 TRIVY: 1 CRITICAL findings"],
        }
        text = format_report(report)
        assert "AgentShroud" in text
        assert "85.0" in text
        assert "Grade: B" in text

    def test_trend_empty_db(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            trend = get_trend(db_path=Path(tmpdir) / "nonexistent.db")
            assert trend == []

    def test_history_persistence(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            summaries = {
                "trivy": {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "findings": 0,
                },
            }
            generate_report(summaries, db_path=db_path, save_history=True)
            generate_report(summaries, db_path=db_path, save_history=True)
            trend = get_trend(db_path=db_path)
            assert len(trend) == 2


# ═══════════════════════════════════════════
# Alert Dispatcher Tests
# ═══════════════════════════════════════════

from gateway.security.alert_dispatcher import AlertDispatcher  # noqa: E402


class TestAlertDispatcher:
    def _make_dispatcher(self, tmpdir):
        return AlertDispatcher(
            alert_log=Path(tmpdir) / "alerts.jsonl",
            gateway_url="http://localhost:9999",
            max_per_hour=3,
            dedup_window=60,
        )

    def test_critical_alert_notified(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            with patch.object(d, "_send_notification", return_value=True):
                result = d.dispatch({"id": "CVE-1", "severity": "CRITICAL", "tool": "trivy"})
                assert result["action"] == "notified"

    def test_low_alert_buffered(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            result = d.dispatch({"id": "CVE-2", "severity": "LOW", "tool": "trivy"})
            assert result["action"] == "buffered"

    def test_medium_alert_buffered(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            result = d.dispatch({"id": "CVE-3", "severity": "MEDIUM", "tool": "trivy"})
            assert result["action"] == "buffered"

    def test_dedup(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            d.dispatch({"id": "CVE-4", "severity": "LOW", "tool": "trivy"})
            result = d.dispatch({"id": "CVE-4", "severity": "LOW", "tool": "trivy"})
            assert result["action"] == "deduped"

    def test_rate_limiting(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            with patch.object(d, "_send_notification", return_value=True):
                for i in range(3):
                    d.dispatch({"id": f"CVE-R{i}", "severity": "CRITICAL", "tool": "trivy"})
                result = d.dispatch({"id": "CVE-R3", "severity": "CRITICAL", "tool": "trivy"})
                assert result["action"] == "rate_limited"

    def test_get_digest(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            d.dispatch({"id": "CVE-D1", "severity": "LOW", "tool": "trivy"})
            d.dispatch({"id": "CVE-D2", "severity": "MEDIUM", "tool": "clamav"})
            digest = d.get_digest()
            assert len(digest) == 2
            # After clear
            assert len(d.get_digest()) == 0

    def test_get_stats(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            stats = d.get_stats()
            assert "alerts_sent_this_hour" in stats
            assert "rate_limit" in stats

    def test_cleanup_seen(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            d._seen_ids["old"] = time.time() - 100  # Within 60s dedup window? No, dedup=60
            d._seen_ids["very_old"] = time.time() - 200
            removed = d.cleanup_seen()
            assert removed == 2

    def test_log_to_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            d.dispatch({"id": "CVE-LOG", "severity": "LOW", "tool": "test"})
            log_content = (Path(tmpdir) / "alerts.jsonl").read_text()
            assert "CVE-LOG" in log_content

    def test_high_alert_notified(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            with patch.object(d, "_send_notification", return_value=True):
                result = d.dispatch({"id": "CVE-H1", "severity": "HIGH", "tool": "falco"})
                assert result["action"] == "notified"

    def test_notify_failure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = self._make_dispatcher(tmpdir)
            with patch.object(d, "_send_notification", return_value=False):
                result = d.dispatch({"id": "CVE-F1", "severity": "CRITICAL", "tool": "trivy"})
                assert result["action"] == "notify_failed"
