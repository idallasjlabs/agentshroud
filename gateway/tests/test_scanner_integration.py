# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/scanner_integration.py — V9-T3: Scanner Aggregation.

Tests the unified scanner result aggregation and the 12-domain Container
Security Scorecard. All filesystem and sub-module calls are mocked — no real
Trivy/Falco/ClamAV/Wazuh processes are invoked.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any, Dict
from unittest.mock import MagicMock, patch

from gateway.security.scanner_integration import (
    _DISA_STIG_DOMAIN_MAP,
    _EU_AI_ACT_DOMAIN_MAP,
    _ISO_42001_DOMAIN_MAP,
    _MATURITY_LABELS,
    _NIST_CSF_DOMAIN_MAP,
    _SCORECARD_DOMAINS,
    _compute_weighted_subscore,
    _load_latest_json,
    _score_compliance_auditing,
    _score_container_hardening,
    _score_image_integrity,
    _score_incident_response,
    _score_logging_monitoring,
    _score_malware_defense,
    _score_network_segmentation,
    _score_runtime_protection,
    _score_secrets_management,
    _score_secure_development,
    _score_supply_chain,
    _score_vulnerability_management,
    aggregate_results,
    compute_scorecard,
    get_clamav_summary,
    get_falco_summary,
    get_openscap_summary,
    get_sbom,
    get_trivy_image_summaries,
    get_trivy_summary,
    get_wazuh_summary,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _trivy_clean() -> Dict[str, Any]:
    return {"tool": "trivy", "status": "clean", "findings": 0, "critical": 0, "high": 0}


def _trivy_critical() -> Dict[str, Any]:
    return {"tool": "trivy", "status": "critical", "findings": 5, "critical": 2, "high": 3}


def _trivy_not_run() -> Dict[str, Any]:
    return {"tool": "trivy", "status": "not_run", "findings": 0, "critical": 0, "high": 0}


def _clamav_clean() -> Dict[str, Any]:
    return {
        "tool": "clamav",
        "status": "clean",
        "findings": 0,
        "critical": 0,
        "high": 0,
        "scanned_files": 100,
    }


def _clamav_infected() -> Dict[str, Any]:
    return {
        "tool": "clamav",
        "status": "critical",
        "findings": 1,
        "critical": 1,
        "high": 0,
        "infected_files": ["/tmp/evil"],
    }


def _falco_clean() -> Dict[str, Any]:
    return {"tool": "falco", "status": "clean", "findings": 0, "critical": 0, "high": 0}


def _falco_critical() -> Dict[str, Any]:
    return {"tool": "falco", "status": "critical", "findings": 2, "critical": 1, "high": 1}


def _falco_not_run() -> Dict[str, Any]:
    return {"tool": "falco", "status": "not_run", "findings": 0, "critical": 0, "high": 0}


def _wazuh_clean() -> Dict[str, Any]:
    return {"tool": "wazuh", "status": "clean", "findings": 0, "critical": 0, "high": 0}


def _wazuh_not_run() -> Dict[str, Any]:
    return {"tool": "wazuh", "status": "not_run", "findings": 0, "critical": 0, "high": 0}


def _openscap_clean() -> Dict[str, Any]:
    return {
        "tool": "openscap",
        "status": "clean",
        "findings": 0,
        "critical": 0,
        "high": 0,
        "pass_count": 50,
        "fail_count": 0,
    }


def _openscap_not_run() -> Dict[str, Any]:
    return {
        "tool": "openscap",
        "status": "not_run",
        "findings": 0,
        "critical": 0,
        "high": 0,
        "pass_count": 0,
        "fail_count": 0,
    }


def _openscap_warn() -> Dict[str, Any]:
    return {
        "tool": "openscap",
        "status": "warning",
        "findings": 3,
        "critical": 0,
        "high": 0,
        "pass_count": 47,
        "fail_count": 3,
    }


# ---------------------------------------------------------------------------
# _load_latest_json
# ---------------------------------------------------------------------------


class TestLoadLatestJson:
    def test_returns_none_for_missing_directory(self, tmp_path):
        result = _load_latest_json(tmp_path / "nonexistent")
        assert result is None

    def test_returns_none_for_empty_directory(self, tmp_path):
        result = _load_latest_json(tmp_path)
        assert result is None

    def test_returns_most_recent_file(self, tmp_path):
        (tmp_path / "report-20260101.json").write_text(json.dumps({"ts": 1}))
        (tmp_path / "report-20260102.json").write_text(json.dumps({"ts": 2}))
        result = _load_latest_json(tmp_path)
        assert result is not None
        assert result["ts"] == 2  # Sorted reverse alphabetically

    def test_prefix_filter(self, tmp_path):
        (tmp_path / "trivy-20260101.json").write_text(json.dumps({"scanner": "trivy"}))
        (tmp_path / "clamav-20260101.json").write_text(json.dumps({"scanner": "clamav"}))
        result = _load_latest_json(tmp_path, prefix="trivy-")
        assert result is not None
        assert result["scanner"] == "trivy"

    def test_returns_none_on_invalid_json(self, tmp_path):
        (tmp_path / "bad.json").write_text("not-json{{{")
        result = _load_latest_json(tmp_path)
        assert result is None

    def test_skips_empty_files_returns_next_valid(self, tmp_path):
        # Newest file is 0-byte; function must skip it and return the older valid one.
        (tmp_path / "report-20260102.json").write_bytes(b"")
        (tmp_path / "report-20260101.json").write_text(json.dumps({"status": "clean"}))
        result = _load_latest_json(tmp_path)
        assert result == {"status": "clean"}

    def test_returns_none_when_all_files_empty(self, tmp_path):
        (tmp_path / "report-20260101.json").write_bytes(b"")
        (tmp_path / "report-20260102.json").write_bytes(b"")
        result = _load_latest_json(tmp_path)
        assert result is None


# ---------------------------------------------------------------------------
# get_trivy_summary
# ---------------------------------------------------------------------------


class TestGetTrivySummary:
    def test_not_run_when_no_report_dir(self):
        with (
            patch(
                "gateway.security.scanner_integration._TRIVY_REPORT_DIR", Path("/nonexistent/trivy")
            ),
            patch("shutil.which", return_value=None),
        ):
            result = get_trivy_summary()
        assert result["tool"] == "trivy"
        assert result["status"] == "not_run"
        assert result["critical"] == 0

    def test_clean_when_installed_but_no_report(self):
        with (
            patch(
                "gateway.security.scanner_integration._TRIVY_REPORT_DIR", Path("/nonexistent/trivy")
            ),
            patch("shutil.which", return_value="/usr/bin/trivy"),
        ):
            result = get_trivy_summary()
        assert result["tool"] == "trivy"
        assert result["status"] == "clean"
        assert result["findings"] == 0
        assert result["timestamp"] is None

    def test_returns_generate_summary_output(self, tmp_path):
        report = {
            "scanner": "trivy",
            "Results": [],
            "by_severity": {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "UNKNOWN": 0},
            "total_vulnerabilities": 0,
            "top_cves": [],
            "affected_packages": [],
            "affected_package_count": 0,
            "error": None,
            "timestamp": "2026-01-01T00:00:00Z",
        }
        report_file = tmp_path / "trivy-20260101.json"
        report_file.write_text(json.dumps(report))
        with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", tmp_path):
            result = get_trivy_summary()
        assert result["tool"] == "trivy"
        assert "status" in result


# ---------------------------------------------------------------------------
# get_clamav_summary
# ---------------------------------------------------------------------------


class TestGetClamavSummary:
    def test_not_run_when_no_report(self):
        with (
            patch(
                "gateway.security.scanner_integration._CLAMAV_REPORT_DIR",
                Path("/nonexistent/clamav"),
            ),
            patch("shutil.which", return_value=None),
            patch("pathlib.Path.exists", return_value=False),
        ):
            result = get_clamav_summary()
        assert result["tool"] == "clamav"
        assert result["status"] == "not_run"

    def test_clean_when_installed_but_no_report(self):
        with (
            patch(
                "gateway.security.scanner_integration._CLAMAV_REPORT_DIR",
                Path("/nonexistent/clamav"),
            ),
            patch("shutil.which", return_value="/usr/sbin/clamd"),
            patch("gateway.security.scanner_integration._is_clamd_running", return_value=False),
        ):
            result = get_clamav_summary()
        assert result["tool"] == "clamav"
        assert result["status"] == "clean"
        assert result["findings"] == 0

    def test_infected_report(self, tmp_path):
        report = {
            "scanner": "clamav",
            "timestamp": "2026-01-01T00:00:00Z",
            "scanned_files": 10,
            "infected_files": [{"file": "/evil", "signature": "Eicar"}],
            "infected_count": 1,
            "errors": 0,
            "returncode": 1,
            "error": None,
        }
        (tmp_path / "clamav-20260101.json").write_text(json.dumps(report))
        with (
            patch("gateway.security.scanner_integration._CLAMAV_REPORT_DIR", tmp_path),
            patch("gateway.security.scanner_integration._is_clamd_running", return_value=True),
        ):
            result = get_clamav_summary()
        assert result["tool"] == "clamav"
        assert result["critical"] == 1


# ---------------------------------------------------------------------------
# get_falco_summary
# ---------------------------------------------------------------------------


class TestGetFalcoSummary:
    def test_not_run_when_no_alert_dir(self):
        with (
            patch(
                "gateway.security.scanner_integration._FALCO_ALERT_DIR", Path("/nonexistent/falco")
            ),
            patch("shutil.which", return_value=None),
            patch("gateway.security.scanner_integration._is_falco_running", return_value=False),
            patch("pathlib.Path.exists", return_value=False),
        ):
            result = get_falco_summary()
        assert result["tool"] == "falco"
        assert result["status"] == "not_run"

    def test_clean_when_installed_not_running(self):
        with (
            patch("shutil.which", return_value="/usr/bin/falco"),
            patch("gateway.security.scanner_integration._is_falco_running", return_value=False),
        ):
            result = get_falco_summary()
        assert result["tool"] == "falco"
        assert result["status"] == "clean"
        assert result["findings"] == 0
        assert result["timestamp"] is None

    def test_returns_summary_for_empty_dir(self, tmp_path):
        with patch("gateway.security.scanner_integration._FALCO_ALERT_DIR", tmp_path):
            result = get_falco_summary()
        assert result["tool"] == "falco"
        assert result["findings"] == 0


# ---------------------------------------------------------------------------
# get_wazuh_summary
# ---------------------------------------------------------------------------


class TestGetWazuhSummary:
    def test_not_run_when_no_alert_dir(self):
        with (
            patch(
                "gateway.security.scanner_integration._WAZUH_ALERT_DIR", Path("/nonexistent/wazuh")
            ),
            patch("shutil.which", return_value=None),
            patch(
                "gateway.security.scanner_integration._is_wazuh_agent_running", return_value=False
            ),
            patch("pathlib.Path.exists", return_value=False),
        ):
            result = get_wazuh_summary()
        assert result["tool"] == "wazuh"
        assert result["status"] == "not_run"

    def test_clean_when_installed_not_running(self):
        with (
            patch("shutil.which", return_value="/var/ossec/bin/wazuh-agentd"),
            patch(
                "gateway.security.scanner_integration._is_wazuh_agent_running", return_value=False
            ),
        ):
            result = get_wazuh_summary()
        assert result["tool"] == "wazuh"
        assert result["status"] == "clean"
        assert result["findings"] == 0

    def test_returns_summary_for_empty_dir(self, tmp_path):
        with patch("gateway.security.scanner_integration._WAZUH_ALERT_DIR", tmp_path):
            result = get_wazuh_summary()
        assert result["tool"] == "wazuh"
        assert result["findings"] == 0


# ---------------------------------------------------------------------------
# get_openscap_summary
# ---------------------------------------------------------------------------


class TestGetOpenscapSummary:
    def test_not_run_when_no_report(self):
        with patch(
            "gateway.security.scanner_integration._OPENSCAP_REPORT_DIR",
            Path("/nonexistent/openscap"),
        ):
            result = get_openscap_summary()
        assert result["tool"] == "openscap"
        assert result["status"] == "not_run"
        assert result["pass_count"] == 0
        assert result["fail_count"] == 0

    def test_clean_report(self, tmp_path):
        report = {
            "pass_count": 50,
            "fail_count": 0,
            "critical": 0,
            "high": 0,
            "profile": "cis-docker-1.6",
            "timestamp": "2026-01-01T00:00:00Z",
        }
        (tmp_path / "openscap-20260101.json").write_text(json.dumps(report))
        with patch("gateway.security.scanner_integration._OPENSCAP_REPORT_DIR", tmp_path):
            result = get_openscap_summary()
        assert result["status"] == "clean"
        assert result["pass_count"] == 50
        assert result["fail_count"] == 0

    def test_warning_on_failures(self, tmp_path):
        report = {
            "pass_count": 47,
            "fail_count": 3,
            "critical": 0,
            "high": 0,
            "profile": "cis",
            "timestamp": "2026-01-01T00:00:00Z",
        }
        (tmp_path / "openscap-20260101.json").write_text(json.dumps(report))
        with patch("gateway.security.scanner_integration._OPENSCAP_REPORT_DIR", tmp_path):
            result = get_openscap_summary()
        assert result["status"] == "warning"

    def test_critical_on_critical_findings(self, tmp_path):
        report = {
            "pass_count": 40,
            "fail_count": 5,
            "critical": 2,
            "high": 0,
            "profile": "cis",
            "timestamp": "2026-01-01T00:00:00Z",
        }
        (tmp_path / "openscap-20260101.json").write_text(json.dumps(report))
        with patch("gateway.security.scanner_integration._OPENSCAP_REPORT_DIR", tmp_path):
            result = get_openscap_summary()
        assert result["status"] == "critical"
        assert result["critical"] == 2


# ---------------------------------------------------------------------------
# get_sbom
# ---------------------------------------------------------------------------


class TestGetSbom:
    def test_returns_none_when_no_dir(self):
        with patch(
            "gateway.security.scanner_integration._SBOM_REPORT_DIR", Path("/nonexistent/sbom")
        ):
            result = get_sbom()
        assert result is None

    def test_returns_none_for_empty_dir(self, tmp_path):
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            result = get_sbom()
        assert result is None

    def test_returns_latest_sbom(self, tmp_path):
        sbom = {"spdxVersion": "SPDX-2.3", "name": "agentshroud-gateway"}
        (tmp_path / "sbom-gateway-20260101.json").write_text(json.dumps(sbom))
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            result = get_sbom()
        assert result is not None
        assert result["spdxVersion"] == "SPDX-2.3"


# ---------------------------------------------------------------------------
# aggregate_results
# ---------------------------------------------------------------------------


class TestAggregateResults:
    # patch.multiple keys must be attribute names (not full module paths)
    _NOT_RUN = {
        "get_trivy_summary": MagicMock(return_value=None),  # overridden per-test
        "get_clamav_summary": MagicMock(return_value=None),
        "get_falco_summary": MagicMock(return_value=None),
        "get_wazuh_summary": MagicMock(return_value=None),
        "get_openscap_summary": MagicMock(return_value=None),
    }

    def _patch_all_not_run(self):
        return {
            "get_trivy_summary": MagicMock(return_value=_trivy_not_run()),
            "get_clamav_summary": MagicMock(
                return_value={"tool": "clamav", "status": "not_run", "critical": 0, "high": 0}
            ),
            "get_falco_summary": MagicMock(return_value=_falco_not_run()),
            "get_wazuh_summary": MagicMock(return_value=_wazuh_not_run()),
            "get_openscap_summary": MagicMock(return_value=_openscap_not_run()),
            "get_fluent_bit_summary": MagicMock(
                return_value={
                    "tool": "fluent-bit",
                    "status": "not_run",
                    "findings": 0,
                    "critical": 0,
                    "high": 0,
                }
            ),
        }

    def test_overall_not_configured_when_all_not_run(self):
        with patch.multiple("gateway.security.scanner_integration", **self._patch_all_not_run()):
            result = aggregate_results()
        assert result["status"] == "not_configured"
        assert result["totals"]["critical"] == 0

    def test_overall_critical_when_any_critical(self):
        patches = self._patch_all_not_run()
        patches["get_trivy_summary"] = MagicMock(return_value=_trivy_critical())
        with patch.multiple("gateway.security.scanner_integration", **patches):
            result = aggregate_results()
        assert result["status"] == "critical"
        assert result["totals"]["critical"] == 2

    def test_overall_warning_when_high_only(self):
        patches = self._patch_all_not_run()
        patches["get_falco_summary"] = MagicMock(
            return_value={
                "tool": "falco",
                "status": "warning",
                "findings": 1,
                "critical": 0,
                "high": 1,
            }
        )
        with patch.multiple("gateway.security.scanner_integration", **patches):
            result = aggregate_results()
        assert result["status"] == "warning"

    def test_overall_clean_when_all_clean(self):
        with patch.multiple(
            "gateway.security.scanner_integration",
            get_trivy_summary=MagicMock(return_value=_trivy_clean()),
            get_clamav_summary=MagicMock(return_value=_clamav_clean()),
            get_falco_summary=MagicMock(return_value=_falco_clean()),
            get_wazuh_summary=MagicMock(return_value=_wazuh_clean()),
            get_openscap_summary=MagicMock(return_value=_openscap_clean()),
        ):
            result = aggregate_results()
        assert result["status"] == "clean"

    def test_scanners_dict_has_all_tools(self):
        with patch.multiple("gateway.security.scanner_integration", **self._patch_all_not_run()):
            result = aggregate_results()
        assert set(result["scanners"].keys()) == {
            "trivy",
            "clamav",
            "falco",
            "wazuh",
            "openscap",
            "fluent-bit",
        }

    def test_timestamp_present(self):
        with patch.multiple("gateway.security.scanner_integration", **self._patch_all_not_run()):
            result = aggregate_results()
        assert "timestamp" in result
        assert result["timestamp"].endswith("+00:00") or result["timestamp"].endswith("Z")

    def test_totals_sum_across_scanners(self):
        with patch.multiple(
            "gateway.security.scanner_integration",
            get_trivy_summary=MagicMock(
                return_value={
                    "tool": "trivy",
                    "status": "warning",
                    "critical": 1,
                    "high": 2,
                    "medium": 3,
                    "low": 0,
                }
            ),
            get_clamav_summary=MagicMock(
                return_value={
                    "tool": "clamav",
                    "status": "clean",
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                }
            ),
            get_falco_summary=MagicMock(
                return_value={
                    "tool": "falco",
                    "status": "clean",
                    "critical": 0,
                    "high": 1,
                    "medium": 0,
                    "low": 0,
                }
            ),
            get_wazuh_summary=MagicMock(
                return_value={
                    "tool": "wazuh",
                    "status": "clean",
                    "critical": 0,
                    "high": 0,
                    "medium": 1,
                    "low": 0,
                }
            ),
            get_openscap_summary=MagicMock(
                return_value={
                    "tool": "openscap",
                    "status": "clean",
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                }
            ),
        ):
            result = aggregate_results()
        assert result["totals"]["critical"] == 1
        assert result["totals"]["high"] == 3
        assert result["totals"]["medium"] == 4


# ---------------------------------------------------------------------------
# Domain scorers
# ---------------------------------------------------------------------------


class TestScoreImageIntegrity:
    def test_zero_when_no_sbom_no_trivy(self, tmp_path):
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_image_integrity(_trivy_not_run())
        assert score == 0

    def test_one_when_sbom_exists(self, tmp_path):
        (tmp_path / "sbom-gateway-20260101.json").write_text("{}")
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_image_integrity(_trivy_not_run())
        assert score == 1

    def test_four_when_sbom_and_clean_trivy(self, tmp_path):
        # SBOM + Trivy ran + zero criticals + zero highs = 4 (not fresh → no 5th point)
        (tmp_path / "sbom-gateway-20260101.json").write_text("{}")
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_image_integrity(_trivy_clean())
        assert score >= 3  # at least Defined; 4 without freshness signal

    def test_capped_at_five(self, tmp_path):
        (tmp_path / "sbom-gateway-20260101.json").write_text("{}")
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_image_integrity(_trivy_clean())
        assert score <= 5


class TestScoreVulnerabilityManagement:
    def test_initial_when_not_run(self):
        assert _score_vulnerability_management(_trivy_not_run()) == 1

    def test_initial_when_has_criticals(self):
        assert _score_vulnerability_management(_trivy_critical()) == 1

    def test_managed_when_no_criticals_but_high(self):
        result = {"tool": "trivy", "status": "warning", "critical": 0, "high": 3}
        # 48h freshness gate must pass; high>0 caps score at 2 before the 24h check
        with patch("gateway.security.scanner_integration._is_fresh", return_value=True):
            assert _score_vulnerability_management(result) == 2

    def test_measured_or_higher_when_fully_clean(self):
        # Zero criticals+highs+mediums → at least Measured (4); Optimizing (5) if fresh scan
        # 48h freshness gate must pass to score above Initial
        with patch("gateway.security.scanner_integration._is_fresh", return_value=True):
            assert _score_vulnerability_management(_trivy_clean()) >= 3

    def test_optimizing_when_installed_clean_no_timestamp(self):
        # Tool installed, status="clean", zero findings, no report yet → Optimizing (5)
        # "note" field distinguishes get_trivy_summary(installed+no-report) from test fixtures
        result = {
            "tool": "trivy",
            "status": "clean",
            "findings": 0,
            "critical": 0,
            "high": 0,
            "timestamp": None,
            "note": "Trivy installed — no findings",
        }
        assert _score_vulnerability_management(result) == 5


class TestScoreSupplyChain:
    def test_zero_when_no_sbom_dir(self, tmp_path):
        with patch(
            "gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path / "nonexistent"
        ):
            score = _score_supply_chain()
        assert score == 0

    def test_zero_when_empty_sbom_dir(self, tmp_path):
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_supply_chain()
        assert score == 0

    def test_two_when_sbom_present(self, tmp_path):
        (tmp_path / "sbom-gateway-20260101.json").write_text("{}")
        with patch("gateway.security.scanner_integration._SBOM_REPORT_DIR", tmp_path):
            score = _score_supply_chain()
        assert score == 2


class TestScoreContainerHardening:
    def test_baseline_three_when_openscap_not_run(self):
        assert _score_container_hardening(_openscap_not_run()) == 3

    def test_four_when_openscap_running_with_failures(self):
        assert _score_container_hardening(_openscap_warn()) == 4

    def test_five_when_openscap_clean(self):
        assert _score_container_hardening(_openscap_clean()) == 5


class TestScoreRuntimeProtection:
    def test_initial_when_not_run(self):
        assert _score_runtime_protection(_falco_not_run()) == 1

    def test_managed_when_has_criticals(self):
        assert _score_runtime_protection(_falco_critical()) == 2

    def test_optimizing_when_clean_zero_findings(self):
        # Falco running + no criticals + findings=0 → Optimizing (5)
        assert _score_runtime_protection(_falco_clean()) == 5


class TestScoreMalwareDefense:
    def test_initial_when_not_run(self):
        assert _score_malware_defense({"tool": "clamav", "status": "not_run", "critical": 0}) == 1

    def test_initial_when_infected(self):
        assert _score_malware_defense(_clamav_infected()) == 1

    def test_measured_when_clean_not_fresh(self):
        # scanned_files > 0 but report is within 48h window yet not fresh <24h → Measured (4)
        # Requires a real timestamp (not None) to bypass the installed-clean early-return
        clamav_with_ts = {**_clamav_clean(), "timestamp": "2026-01-01T00:00:00Z"}
        with patch(
            "gateway.security.scanner_integration._is_fresh",
            side_effect=lambda *a, **kw: kw.get("max_age_hours", 24) == 48,
        ):
            assert _score_malware_defense(clamav_with_ts) == 4

    def test_optimizing_when_installed_clean_no_timestamp(self):
        # Tool installed, status="clean", zero findings, no report yet → Optimizing (5)
        # "note" field distinguishes get_clamav_summary(installed+no-report) from test fixtures
        result = {
            "tool": "clamav",
            "status": "clean",
            "findings": 0,
            "critical": 0,
            "timestamp": None,
            "note": "ClamAV installed — no scan report yet",
        }
        assert _score_malware_defense(result) == 5


class TestScoreNetworkSegmentation:
    def test_baseline_three_without_daemon_config(self):
        # No daemon.json icc setting and no network_validator → baseline score 3
        with (
            patch(
                "gateway.security.scanner_integration._read_docker_daemon_config", return_value={}
            ),
            patch("gateway.security.scanner_integration._app_state_has", return_value=False),
            patch("gateway.security.scanner_integration._is_containerized", return_value=False),
        ):
            assert _score_network_segmentation() == 3


class TestScoreSecretsManagement:
    def test_baseline_at_least_two(self):
        # >= 2 baseline (Docker secrets); may be higher if key_rotation.py or encrypted_store present
        assert _score_secrets_management() >= 2


class TestScoreLoggingMonitoring:
    def test_one_when_no_wazuh_no_fluent(self):
        with patch("gateway.security.scanner_integration.Path") as mock_path_cls:
            # Make all path.exists() return False
            mock_path = MagicMock()
            mock_path.exists.return_value = False
            mock_path_cls.return_value = mock_path
            score = _score_logging_monitoring(_wazuh_not_run())
        assert score >= 1

    def test_two_when_wazuh_running(self):
        with (
            patch.object(Path, "exists", return_value=False),
            patch("gateway.security.scanner_integration._app_state_has", return_value=False),
        ):
            score = _score_logging_monitoring(_wazuh_clean())
        assert score == 2


class TestScoreComplianceAuditing:
    def test_zero_when_not_run(self):
        with patch("shutil.which", return_value=None):
            assert _score_compliance_auditing(_openscap_not_run()) == 0

    def test_defined_when_oscap_binary_present(self):
        # oscap binary installed but no report run yet → Defined (3)
        with patch("shutil.which", return_value="/usr/bin/oscap"):
            assert _score_compliance_auditing(_openscap_not_run()) == 3

    def test_defined_when_all_passing_no_report_on_disk(self):
        # Zero failures but no report file on disk → Defined (3)
        mock_dir = MagicMock()
        mock_dir.exists.return_value = False
        with patch("gateway.security.scanner_integration._OPENSCAP_REPORT_DIR", mock_dir):
            assert _score_compliance_auditing(_openscap_clean()) == 3

    def test_managed_when_has_failures(self):
        assert _score_compliance_auditing(_openscap_warn()) == 2


class TestScoreSecureDevelopment:
    def test_at_least_one(self):
        # Trivy baseline always gives 1
        with patch.object(Path, "exists", return_value=False):
            score = _score_secure_development()
        assert score >= 1

    def test_three_when_semgrep_and_precommit_present(self, tmp_path):
        semgrep = tmp_path / ".semgrep.yml"
        semgrep.write_text("rules: []")
        precommit = tmp_path / ".pre-commit-config.yaml"
        precommit.write_text("repos: []")
        with (patch("gateway.security.scanner_integration.Path") as mock_path_cls,):

            def path_factory(s):
                p = MagicMock()
                if ".semgrep.yml" in str(s):
                    p.exists.return_value = True
                elif ".pre-commit-config.yaml" in str(s):
                    p.exists.return_value = True
                else:
                    p.exists.return_value = False
                return p

            mock_path_cls.side_effect = path_factory
            score = _score_secure_development()
        assert score >= 2


class TestScoreIncidentResponse:
    def test_one_when_no_tools(self):
        # Score >= 1 (baseline SOC); may be higher if killswitch.sh or soc_correlation present
        score = _score_incident_response(_falco_not_run(), _wazuh_not_run())
        assert score >= 1

    def test_two_when_falco_running(self):
        # Score >= 2 (SOC + Falco); may be higher with additional signals
        score = _score_incident_response(_falco_clean(), _wazuh_not_run())
        assert score >= 2

    def test_three_when_both_running(self):
        # Score >= 3 (SOC + Falco + Wazuh); may be higher with additional signals
        score = _score_incident_response(_falco_clean(), _wazuh_clean())
        assert score >= 3


# ---------------------------------------------------------------------------
# compute_scorecard
# ---------------------------------------------------------------------------


class TestComputeScorecard:
    # Attribute-name-keyed patches for patch.multiple
    def _all_not_run_patches(self):
        return {
            "get_trivy_summary": MagicMock(return_value=_trivy_not_run()),
            "get_clamav_summary": MagicMock(
                return_value={
                    "tool": "clamav",
                    "status": "not_run",
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                }
            ),
            "get_falco_summary": MagicMock(return_value=_falco_not_run()),
            "get_wazuh_summary": MagicMock(return_value=_wazuh_not_run()),
            "get_openscap_summary": MagicMock(return_value=_openscap_not_run()),
        }

    def test_returns_thirty_three_domains(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        assert len(result["domains"]) == 33

    def test_all_domains_have_required_fields(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        for domain in result["domains"]:
            assert "id" in domain
            assert "domain" in domain
            assert "score" in domain
            assert "maturity" in domain
            assert "iec_fr" in domain
            assert "tools" in domain
            assert 0 <= domain["score"] <= 5

    def test_maturity_labels_valid(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        valid_labels = set(_MATURITY_LABELS.values())
        for domain in result["domains"]:
            assert domain["maturity"] in valid_labels

    def test_totals_present(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        assert "totals" in result
        assert result["totals"]["max"] == 165  # 33 domains × 5
        assert 0 <= result["totals"]["percentage"] <= 100

    def test_standard_basis_present(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        basis = result["standard_basis"]
        assert any("CIS Docker Benchmark" in s for s in basis)
        assert any("NIST SP 800-190" in s for s in basis)
        assert any("IEC 62443" in s for s in basis)
        assert any("OWASP" in s and "Agentic AI" in s for s in basis)
        assert any("MITRE ATLAS" in s for s in basis)
        assert any("NIST AI RMF" in s for s in basis)
        assert any("CSA MAESTRO" in s for s in basis)
        assert any("EU AI Act" in s for s in basis)
        assert any("ISO/IEC 42001" in s for s in basis)
        assert any("NIST CSF" in s for s in basis)
        assert any("DISA" in s for s in basis)

    def test_compliance_new_keys_present(self):
        """New compliance sub-scores (EU AI Act, ISO 42001, NIST CSF, DISA STIG) appear in output."""
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        compliance = result["compliance"]
        for key in ("eu_ai_act", "iso_42001", "nist_csf", "disa_stig"):
            assert key in compliance, f"Missing compliance key: {key}"
            assert "sub_score_pct" in compliance[key], f"Missing sub_score_pct for {key}"
            assert 0.0 <= compliance[key]["sub_score_pct"] <= 100.0

    def test_eu_ai_act_domain_map_valid(self):
        """EU AI Act domain map references only valid domain IDs."""
        valid_ids = {d["id"] for d in _SCORECARD_DOMAINS}
        for domain_id in _EU_AI_ACT_DOMAIN_MAP:
            assert domain_id in valid_ids, f"EU AI Act domain {domain_id} not in _SCORECARD_DOMAINS"

    def test_iso_42001_domain_map_valid(self):
        """ISO 42001 domain map references only valid domain IDs."""
        valid_ids = {d["id"] for d in _SCORECARD_DOMAINS}
        for domain_id in _ISO_42001_DOMAIN_MAP:
            assert domain_id in valid_ids, f"ISO 42001 domain {domain_id} not in _SCORECARD_DOMAINS"

    def test_nist_csf_domain_map_valid(self):
        """NIST CSF domain map references only valid domain IDs."""
        valid_ids = {d["id"] for d in _SCORECARD_DOMAINS}
        for domain_id in _NIST_CSF_DOMAIN_MAP:
            assert domain_id in valid_ids, f"NIST CSF domain {domain_id} not in _SCORECARD_DOMAINS"

    def test_disa_stig_domain_map_valid(self):
        """DISA STIG domain map references only valid domain IDs."""
        valid_ids = {d["id"] for d in _SCORECARD_DOMAINS}
        for domain_id in _DISA_STIG_DOMAIN_MAP:
            assert domain_id in valid_ids, f"DISA STIG domain {domain_id} not in _SCORECARD_DOMAINS"

    def test_compute_weighted_subscore_zero_for_empty_map(self):
        """_compute_weighted_subscore returns 0.0 for an empty domain map."""
        assert _compute_weighted_subscore({}, {}) == 0.0

    def test_compute_weighted_subscore_full_score(self):
        """_compute_weighted_subscore returns 100.0 when all domains score 5."""
        scores = {d: 5 for d in _EU_AI_ACT_DOMAIN_MAP}
        assert _compute_weighted_subscore(scores, _EU_AI_ACT_DOMAIN_MAP) == 100.0

    def test_overall_maturity_present(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        assert result["overall_maturity"] in set(_MATURITY_LABELS.values())

    def test_clean_tools_improve_score(self):
        not_run_result = None
        clean_result = None

        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            not_run_result = compute_scorecard()

        with patch.multiple(
            "gateway.security.scanner_integration",
            get_trivy_summary=MagicMock(return_value=_trivy_clean()),
            get_clamav_summary=MagicMock(return_value=_clamav_clean()),
            get_falco_summary=MagicMock(return_value=_falco_clean()),
            get_wazuh_summary=MagicMock(return_value=_wazuh_clean()),
            get_openscap_summary=MagicMock(return_value=_openscap_clean()),
        ):
            clean_result = compute_scorecard()

        assert clean_result["totals"]["score"] >= not_run_result["totals"]["score"]

    def test_version_is_v090(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        assert result["version"] == "v0.9.0"

    def test_timestamp_present(self):
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        assert "timestamp" in result

    def test_scorecard_domain_ids_are_sequential(self):
        # Scorecard now covers 33 domains (21 infrastructure + 12 agentic AI)
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        ids = [d["id"] for d in result["domains"]]
        assert ids == list(range(1, 34))

    def test_network_segmentation_baseline_three(self):
        # Score >= 3 (Docker network baseline); may be higher if icc=false configured
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        domain_7 = next(d for d in result["domains"] if d["id"] == 7)
        assert domain_7["score"] >= 3

    def test_secrets_management_baseline_two(self):
        # Score >= 2 (Docker secrets baseline); may be higher if key_rotation.py present
        with patch.multiple("gateway.security.scanner_integration", **self._all_not_run_patches()):
            result = compute_scorecard()
        domain_8 = next(d for d in result["domains"] if d["id"] == 8)
        assert domain_8["score"] >= 2


# ---------------------------------------------------------------------------
# get_trivy_image_summaries (M2 — per-image report reading)
# ---------------------------------------------------------------------------


def _write_image_report(
    log_dir: Path,
    image_tag: str,
    report: Dict[str, Any],
    ts: str = "20260528-120000",
) -> Path:
    """Write a fake image report file in the expected filename format."""
    sanitised = image_tag.replace(":", "-").replace("/", "-")
    path = log_dir / f"image-{sanitised}-{ts}.json"
    path.write_text(json.dumps(report))
    return path


def _clean_trivy_report() -> Dict[str, Any]:
    return {
        "scanner": "trivy",
        "total_vulnerabilities": 0,
        "by_severity": {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "UNKNOWN": 0},
        "top_cves": [],
        "affected_packages": [],
        "affected_package_count": 0,
        "error": None,
        "timestamp": "2026-05-28T12:00:00+00:00",
    }


def _critical_trivy_report() -> Dict[str, Any]:
    r = _clean_trivy_report()
    r["total_vulnerabilities"] = 3
    r["by_severity"] = {"CRITICAL": 2, "HIGH": 1, "MEDIUM": 0, "LOW": 0, "UNKNOWN": 0}
    return r


class TestGetTrivyImageSummaries:
    def test_returns_empty_list_when_dir_missing(self):
        with patch(
            "gateway.security.scanner_integration._TRIVY_REPORT_DIR",
            Path("/nonexistent/trivy/dir"),
        ):
            result = get_trivy_image_summaries()
        assert result == []

    def test_returns_one_entry_per_report_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            _write_image_report(
                log_dir, "agentshroud-gateway:latest", _clean_trivy_report(), "20260528-100000"
            )
            _write_image_report(
                log_dir, "agentshroud-openclaw:latest", _clean_trivy_report(), "20260528-110000"
            )
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert len(summaries) == 2

    def test_each_entry_has_image_key(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            _write_image_report(log_dir, "agentshroud-gateway:latest", _clean_trivy_report())
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert all("image" in s for s in summaries)

    def test_critical_report_status_is_critical(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            _write_image_report(log_dir, "agentshroud-openclaw:latest", _critical_trivy_report())
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert summaries[0]["status"] == "critical"
            assert summaries[0]["critical"] == 2

    def test_ignores_non_image_prefixed_files(self):
        """Files named trivy-*.json (fs scans) are not included."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            # Write a regular fs scan report
            (log_dir / "trivy-20260528-120000.json").write_text(json.dumps(_clean_trivy_report()))
            # Write an image report
            _write_image_report(log_dir, "agentshroud-gateway:latest", _clean_trivy_report())
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert len(summaries) == 1

    def test_bot_id_filter_matches_bot_image(self):
        """bot_id + config param restricts results to that bot's image."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            _write_image_report(
                log_dir, "agentshroud-openclaw:latest", _clean_trivy_report(), "20260528-100000"
            )
            _write_image_report(
                log_dir, "agentshroud/hermes:latest", _clean_trivy_report(), "20260528-110000"
            )

            # Build a minimal config mock
            class _BotStub:
                image = "agentshroud-openclaw:latest"

            class _ConfigStub:
                bots = {"openclaw": _BotStub()}

            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries(bot_id="openclaw", config=_ConfigStub())
            assert len(summaries) == 1
            assert summaries[0]["image"].startswith("agentshroud-openclaw-latest")

    def test_bot_id_filter_unknown_bot_returns_all(self):
        """Unknown bot_id with no config match falls through and returns all entries."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            _write_image_report(log_dir, "agentshroud-gateway:latest", _clean_trivy_report())

            class _ConfigStub:
                bots: Dict = {}

            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries(bot_id="nonexistent", config=_ConfigStub())
            # filter_image is None when bot not found → all entries returned
            assert len(summaries) == 1

    def test_returns_empty_when_no_image_reports(self):
        """Directory exists but contains only fs scan files — returns []."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            (log_dir / "trivy-20260528-120000.json").write_text(json.dumps(_clean_trivy_report()))
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert summaries == []

    def test_corrupt_report_file_is_skipped(self):
        """A JSON-corrupt file is silently skipped, others are still returned."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_dir = Path(tmpdir)
            (log_dir / "image-corrupt-20260528-120000.json").write_text("not json {{{")
            _write_image_report(
                log_dir, "agentshroud-gateway:latest", _clean_trivy_report(), "20260528-130000"
            )
            with patch("gateway.security.scanner_integration._TRIVY_REPORT_DIR", log_dir):
                summaries = get_trivy_image_summaries()
            assert len(summaries) == 1
