# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/security/scanner_integration.py.

Exercises the filesystem-probe helpers, per-scanner summary accessors,
all 33 scorecard domain scorers, mandatory-gate evaluation, IEC SL /
compliance-level determination, and the per-bot scorecard.

All hardcoded absolute paths (/proc, /var/log, /app, /run/secrets, ...) are
redirected into a tmp_path sandbox by replacing the module's ``Path`` symbol,
so no real system state is read and no real processes/sockets are touched.
"""

from __future__ import annotations

import http.client
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import types
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict
from unittest.mock import MagicMock

import pytest

import gateway.security.scanner_integration as si

# ---------------------------------------------------------------------------
# Fixtures and helpers
# ---------------------------------------------------------------------------


def _w(root: Path, rel: str, text: str = "x") -> Path:
    """Write a file under the sandbox root, creating parents."""
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def _age(p: Path, hours: float) -> None:
    """Set a file's mtime to `hours` hours in the past."""
    t = time.time() - hours * 3600
    os.utime(p, (t, t))


@pytest.fixture
def fs(monkeypatch, tmp_path):
    """Redirect every Path(...) constructed inside the module into a sandbox.

    Absolute paths map to <root>/<path>; relative paths map to <root>/rel/<path>.
    The module-level report-directory constants are redirected as well.
    """
    root = tmp_path / "fs"
    root.mkdir()

    def fake_path(*args: Any) -> Path:
        p = Path(*args)
        s = str(p)
        if s.startswith("/"):
            return root / s.lstrip("/")
        return root / "rel" / s

    monkeypatch.setattr(si, "Path", fake_path)
    monkeypatch.setattr(si, "_TRIVY_REPORT_DIR", root / "var/log/security/trivy")
    monkeypatch.setattr(si, "_CLAMAV_REPORT_DIR", root / "var/log/security/clamav")
    monkeypatch.setattr(si, "_FALCO_ALERT_DIR", root / "var/log/falco")
    monkeypatch.setattr(si, "_WAZUH_ALERT_DIR", root / "var/ossec/logs/alerts")
    monkeypatch.setattr(si, "_OPENSCAP_REPORT_DIR", root / "var/log/security/openscap")
    monkeypatch.setattr(si, "_SBOM_REPORT_DIR", root / "var/log/security/sbom")
    return root


@pytest.fixture
def flags(monkeypatch):
    """Replace _app_state_has with a controllable membership set."""
    active: set = set()
    monkeypatch.setattr(si, "_app_state_has", lambda name: name in active)
    return active


@pytest.fixture
def tools(monkeypatch):
    """Replace shutil.which with a controllable name → path mapping."""
    available: Dict[str, str] = {}
    monkeypatch.setattr(shutil, "which", lambda name: available.get(name))
    return available


# ---------------------------------------------------------------------------
# _is_fresh / _app_state_has
# ---------------------------------------------------------------------------


class TestIsFresh:
    def test_empty_dir_returns_false(self, tmp_path):
        assert si._is_fresh(tmp_path) is False

    def test_fresh_file_returns_true(self, tmp_path):
        _w(tmp_path, "trivy-1.json", "{}")
        assert si._is_fresh(tmp_path, "trivy-") is True

    def test_old_file_returns_false(self, tmp_path):
        p = _w(tmp_path, "trivy-1.json", "{}")
        _age(p, 50)
        assert si._is_fresh(tmp_path, "trivy-") is False

    def test_stat_error_returns_false(self):
        fake_dir = MagicMock()
        fake_dir.exists.return_value = True
        bad = MagicMock()
        bad.stat.side_effect = OSError("boom")
        fake_dir.glob.return_value = [bad]
        assert si._is_fresh(fake_dir) is False


class TestAppStateHas:
    def test_true_and_false_against_real_app_state(self, monkeypatch):
        from gateway.ingest_api.state import app_state

        monkeypatch.setattr(app_state, "zz_cov_probe", object(), raising=False)
        assert si._app_state_has("zz_cov_probe") is True
        assert si._app_state_has("definitely_not_set_xyz") is False

    def test_import_failure_returns_false(self, monkeypatch):
        stub = types.ModuleType("gateway.ingest_api.state")
        monkeypatch.setitem(sys.modules, "gateway.ingest_api.state", stub)
        assert si._app_state_has("anything") is False


# ---------------------------------------------------------------------------
# Process / socket probes
# ---------------------------------------------------------------------------


class _FakeResp:
    def __init__(self, status: int, body: bytes):
        self.status = status
        self._body = body

    def read(self) -> bytes:
        return self._body


class TestIsContainerRunning:
    def _patch_http(self, monkeypatch, status: int, body: bytes) -> None:
        monkeypatch.setattr(socket, "socket", lambda *a, **k: MagicMock())
        monkeypatch.setattr(
            http.client.HTTPConnection, "getresponse", lambda conn: _FakeResp(status, body)
        )

    def test_running_container_returns_true(self, monkeypatch):
        body = json.dumps({"State": {"Status": "running"}}).encode()
        self._patch_http(monkeypatch, 200, body)
        assert si._is_container_running("agentshroud-gateway") is True

    def test_stopped_container_returns_false(self, monkeypatch):
        body = json.dumps({"State": {"Status": "exited"}}).encode()
        self._patch_http(monkeypatch, 200, body)
        assert si._is_container_running("agentshroud-gateway") is False

    def test_404_returns_false(self, monkeypatch):
        self._patch_http(monkeypatch, 404, b'{"message": "no such container"}')
        assert si._is_container_running("nope") is False

    def test_socket_error_returns_false(self, monkeypatch):
        def boom(*a, **k):
            raise OSError("no docker socket")

        monkeypatch.setattr(socket, "socket", boom)
        assert si._is_container_running("nope") is False


class TestSocketAndPidProbes:
    def test_clamd_running_true_with_connectable_socket(self, monkeypatch):
        monkeypatch.setattr(socket, "socket", lambda *a, **k: MagicMock())
        assert si._is_clamd_running() is True

    def test_fluent_bit_running_true_with_live_pid(self, fs):
        _w(fs, "tmp/fluent-bit.pid", str(os.getpid()))
        assert si._is_fluent_bit_running() is True

    def test_fluent_bit_running_false_without_pidfile(self, fs):
        assert si._is_fluent_bit_running() is False


class TestProcScans:
    def test_falco_running_detected(self, fs):
        _w(fs, "proc/abc/comm", "ignored")  # non-digit dir name skipped
        _w(fs, "proc/111/comm", "bash\n")
        _w(fs, "proc/222/comm", "falco\n")
        _w(fs, "proc/222/status", "Name:\tfalco\nState:\tZ (zombie)\n")
        _w(fs, "proc/333/comm", "falco\n")
        _w(fs, "proc/333/status", "Name:\tfalco\nState:\tS (sleeping)\n")
        (fs / "proc/444").mkdir(parents=True)  # digit dir without comm → OSError path
        assert si._is_falco_running() is True

    def test_falco_zombie_only_returns_false(self, fs):
        _w(fs, "proc/222/comm", "falco\n")
        _w(fs, "proc/222/status", "Name:\tfalco\nState:\tZ (zombie)\n")
        assert si._is_falco_running() is False

    def test_falco_no_proc_returns_false(self, fs):
        assert si._is_falco_running() is False

    def test_wazuh_agent_detected(self, fs):
        _w(fs, "proc/555/comm", "wazuh-agentd\n")
        (fs / "proc/666").mkdir(parents=True)  # missing comm → OSError continue
        assert si._is_wazuh_agent_running() is True

    def test_wazuh_agent_absent(self, fs):
        _w(fs, "proc/555/comm", "nginx\n")
        assert si._is_wazuh_agent_running() is False


# ---------------------------------------------------------------------------
# Compose / script text readers
# ---------------------------------------------------------------------------


class TestTextReaders:
    def test_compose_text_skips_unreadable_then_reads(self, fs):
        # First candidate exists but is a directory → read_text raises → skipped.
        (fs / "app/docker/docker-compose.yml").mkdir(parents=True)
        _w(fs, "app/docker-compose.yml", "services:\n  gateway: {}\n")
        assert "services:" in si._read_compose_text()

    def test_compose_text_empty_when_absent(self, fs):
        assert si._read_compose_text() == ""

    def test_security_scan_sh_read(self, fs):
        (fs / "app/scripts/security-scan.sh").mkdir(parents=True)  # dir → except path
        _w(fs, "rel/scripts/security-scan.sh", "#!/bin/sh\ncosign sign image\n")
        assert "cosign" in si._security_scan_sh_text()

    def test_security_scan_sh_empty_when_absent(self, fs):
        assert si._security_scan_sh_text() == ""


class TestLoadLatestJson:
    def test_missing_dir_returns_none(self, tmp_path):
        assert si._load_latest_json(tmp_path / "nope") is None

    def test_empty_files_skipped(self, tmp_path):
        _w(tmp_path, "r-1.json", "")
        assert si._load_latest_json(tmp_path, "r-") is None

    def test_invalid_then_valid(self, tmp_path):
        _w(tmp_path, "r-2.json", "{not json")
        _w(tmp_path, "r-1.json", json.dumps({"ok": True}))
        assert si._load_latest_json(tmp_path, "r-") == {"ok": True}


# ---------------------------------------------------------------------------
# Per-scanner summaries
# ---------------------------------------------------------------------------


class TestTrivySummary:
    def test_not_run_without_binary_or_report(self, fs, tools):
        out = si.get_trivy_summary()
        assert out["status"] == "not_run"

    def test_clean_when_installed_without_report(self, fs, tools):
        tools["trivy"] = "/usr/bin/trivy"
        out = si.get_trivy_summary()
        assert out["status"] == "clean"
        assert out["note"] == "Trivy installed — no findings"

    def test_timestamp_falls_back_to_file_mtime(self, fs, tools):
        _w(
            fs,
            "var/log/security/trivy/trivy-1.json",
            json.dumps({"by_severity": {}, "total_vulnerabilities": 0}),
        )
        out = si.get_trivy_summary()
        assert out["status"] == "clean"
        assert out["timestamp"]  # populated from mtime


class TestTrivyImageSummaries:
    def test_missing_dir_returns_empty(self, fs):
        assert si.get_trivy_image_summaries() == []

    def test_plain_name_and_mtime_timestamp(self, fs):
        _w(
            fs,
            "var/log/security/trivy/image-foo.json",
            json.dumps({"by_severity": {"HIGH": 1}, "total_vulnerabilities": 1}),
        )
        _w(fs, "var/log/security/trivy/image-bad.json", "{broken")
        out = si.get_trivy_image_summaries()
        assert len(out) == 1
        assert out[0]["image"] == "foo"
        assert out[0]["status"] == "warning"
        assert out[0]["timestamp"]

    def test_timestamp_suffix_strip_branch(self, fs):
        # Crafted name satisfying the parser: 8 trailing digits, '-' at -9 and -15.
        _w(
            fs,
            "var/log/security/trivy/image-myimage-20260-12000000.json",
            json.dumps({"by_severity": {}, "total_vulnerabilities": 0}),
        )
        out = si.get_trivy_image_summaries()
        assert out[0]["image"] == "myimag"  # inner[:-16] per implementation

    def test_bot_filter_matches_normalised_image(self, fs):
        _w(
            fs,
            "var/log/security/trivy/image-repo-img-1.0.json",
            json.dumps({"by_severity": {}, "total_vulnerabilities": 0}),
        )
        _w(
            fs,
            "var/log/security/trivy/image-other.json",
            json.dumps({"by_severity": {}, "total_vulnerabilities": 0}),
        )
        cfg = SimpleNamespace(bots={"b1": SimpleNamespace(image="repo/img:1.0")})
        out = si.get_trivy_image_summaries(bot_id="b1", config=cfg)
        assert [s["image"] for s in out] == ["repo-img-1.0"]
        # Unknown bot → no filter applied
        out_all = si.get_trivy_image_summaries(bot_id="missing", config=cfg)
        assert len(out_all) == 2


class TestClamavSummary:
    def test_not_run_when_not_installed(self, fs, tools, monkeypatch):
        monkeypatch.setattr(si, "_is_clamd_running", lambda: False)
        out = si.get_clamav_summary()
        assert out["status"] == "not_run"
        assert "clamd not running" in out["error"]

    def test_clean_when_installed_not_running(self, fs, tools, monkeypatch):
        monkeypatch.setattr(si, "_is_clamd_running", lambda: False)
        tools["clamdscan"] = "/usr/bin/clamdscan"
        out = si.get_clamav_summary()
        assert out["status"] == "clean"
        assert "ClamAV installed" in out["note"]

    def test_running_without_report(self, fs, monkeypatch):
        monkeypatch.setattr(si, "_is_clamd_running", lambda: True)
        out = si.get_clamav_summary()
        assert out["status"] == "clean"
        assert "no scan report yet" in out["note"]

    def test_running_report_mtime_timestamp(self, fs, monkeypatch):
        monkeypatch.setattr(si, "_is_clamd_running", lambda: True)
        _w(
            fs,
            "var/log/security/clamav/clamav-1.json",
            json.dumps({"infected_count": 0, "scanned_files": 7}),
        )
        out = si.get_clamav_summary()
        assert out["status"] == "clean"
        assert out["scanned_files"] == 7
        assert out["timestamp"]  # mtime fallback


class TestFalcoSummary:
    def test_installed_not_running_is_clean_note(self, fs, tools):
        _w(fs, "usr/bin/falco", "")
        out = si.get_falco_summary()
        assert out["status"] == "clean"
        assert "eBPF unavailable" in out["note"]

    def test_not_installed_not_running(self, fs, tools):
        assert si.get_falco_summary()["status"] == "not_run"

    def test_running_without_alert_dir(self, fs, tools, monkeypatch):
        monkeypatch.setattr(si, "_is_falco_running", lambda: True)
        assert si.get_falco_summary()["status"] == "not_run"

    def test_running_with_alerts_sets_timestamp(self, fs, tools, monkeypatch):
        import gateway.security.falco_monitor as fm

        monkeypatch.setattr(si, "_is_falco_running", lambda: True)
        (fs / "var/log/falco").mkdir(parents=True)
        monkeypatch.setattr(fm, "read_alerts", lambda alert_dir: [])
        monkeypatch.setattr(
            fm,
            "generate_summary",
            lambda alerts: {
                "tool": "falco",
                "status": "clean",
                "findings": 0,
                "critical": 0,
                "high": 0,
            },
        )
        out = si.get_falco_summary()
        assert out["status"] == "clean"
        assert out["timestamp"]


class TestWazuhSummary:
    def test_not_installed(self, fs, tools):
        assert si.get_wazuh_summary()["status"] == "not_run"

    def test_installed_not_running(self, fs, tools):
        _w(fs, "var/ossec/bin/wazuh-agentd", "")
        out = si.get_wazuh_summary()
        assert out["status"] == "clean"
        assert "no manager connection" in out["note"]

    def test_running_no_alert_dir(self, fs, monkeypatch):
        monkeypatch.setattr(si, "_is_wazuh_agent_running", lambda: True)
        assert si.get_wazuh_summary()["status"] == "clean"

    def test_running_with_alert_dir(self, fs, monkeypatch):
        import gateway.security.wazuh_client as wc

        monkeypatch.setattr(si, "_is_wazuh_agent_running", lambda: True)
        (fs / "var/ossec/logs/alerts").mkdir(parents=True)
        monkeypatch.setattr(wc, "read_alerts", lambda alert_dir: [])
        out = si.get_wazuh_summary()
        assert out["tool"] == "wazuh"
        assert out["status"] == "clean"


class TestOpenscapSummary:
    def test_not_run(self, fs):
        assert si.get_openscap_summary()["status"] == "not_run"

    def test_critical_and_warning_statuses(self, fs):
        _w(
            fs,
            "var/log/security/openscap/openscap-1.json",
            json.dumps({"pass_count": 1, "fail_count": 2, "critical": 1}),
        )
        assert si.get_openscap_summary()["status"] == "critical"
        _w(
            fs,
            "var/log/security/openscap/openscap-1.json",
            json.dumps({"pass_count": 1, "fail_count": 2, "critical": 0}),
        )
        assert si.get_openscap_summary()["status"] == "warning"

    def test_compact_timestamp_normalised_to_iso(self, fs):
        _w(
            fs,
            "var/log/security/openscap/openscap-1.json",
            json.dumps(
                {"pass_count": 5, "fail_count": 0, "critical": 0, "timestamp": "20260321-095212"}
            ),
        )
        out = si.get_openscap_summary()
        assert out["status"] == "clean"
        # Accept either ISO 8601 ("2026-03-21T09:52:12...") or compact
        # ("20260321-095212") — Python 3.14's datetime.fromisoformat is lenient
        # enough to accept the compact form, leaving raw_ts unchanged.
        ts = out["timestamp"]
        assert ts.startswith("2026-03-21T09:52:12") or ts == "20260321-095212"

    def test_garbage_timestamp_falls_back_to_mtime(self, fs):
        _w(
            fs,
            "var/log/security/openscap/openscap-1.json",
            json.dumps(
                {"pass_count": 5, "fail_count": 0, "critical": 0, "timestamp": "not-a-date"}
            ),
        )
        out = si.get_openscap_summary()
        assert out["timestamp"]
        assert out["timestamp"] != "not-a-date"


class TestFluentBitSummary:
    def test_not_running(self, fs):
        assert si.get_fluent_bit_summary()["status"] == "not_run"

    def test_running_with_fresh_log(self, fs, monkeypatch):
        monkeypatch.setattr(si, "_is_fluent_bit_running", lambda: True)
        _w(fs, "var/log/fluent-bit/agentshroud-out.log", "line\n")
        out = si.get_fluent_bit_summary()
        assert out["status"] == "clean"
        assert out["active"] is True

    def test_running_without_logs(self, fs, monkeypatch):
        monkeypatch.setattr(si, "_is_fluent_bit_running", lambda: True)
        out = si.get_fluent_bit_summary()
        assert out["status"] == "clean"
        assert out["active"] is False


class TestGetSbom:
    def test_missing_dir(self, fs):
        assert si.get_sbom() is None

    def test_no_files(self, fs):
        (fs / "var/log/security/sbom").mkdir(parents=True)
        assert si.get_sbom() is None

    def test_invalid_json(self, fs):
        _w(fs, "var/log/security/sbom/sbom-1.json", "{broken")
        assert si.get_sbom() is None

    def test_valid(self, fs):
        _w(fs, "var/log/security/sbom/sbom-1.json", json.dumps({"packages": [{"name": "a"}]}))
        assert si.get_sbom() == {"packages": [{"name": "a"}]}


# ---------------------------------------------------------------------------
# aggregate_results
# ---------------------------------------------------------------------------


def _stub_summary(tool: str, status: str, critical: int = 0, high: int = 0) -> Dict[str, Any]:
    return {"tool": tool, "status": status, "critical": critical, "high": high}


class TestAggregateResults:
    def _patch_all(self, monkeypatch, statuses, critical=0, high=0):
        tools_ = ["trivy", "clamav", "falco", "wazuh", "openscap", "fluent-bit"]
        getters = [
            "get_trivy_summary",
            "get_clamav_summary",
            "get_falco_summary",
            "get_wazuh_summary",
            "get_openscap_summary",
            "get_fluent_bit_summary",
        ]
        for i, (tool, getter) in enumerate(zip(tools_, getters)):
            crit = critical if i == 0 else 0
            hi = high if i == 0 else 0
            summary = _stub_summary(tool, statuses[i], crit, hi)
            monkeypatch.setattr(si, getter, lambda s=summary: s)

    def test_all_not_run_is_not_configured(self, monkeypatch):
        self._patch_all(monkeypatch, ["not_run"] * 6)
        assert si.aggregate_results()["status"] == "not_configured"

    def test_critical_dominates(self, monkeypatch):
        self._patch_all(monkeypatch, ["critical"] + ["clean"] * 5, critical=2)
        out = si.aggregate_results()
        assert out["status"] == "critical"
        assert out["totals"]["critical"] == 2

    def test_high_means_warning(self, monkeypatch):
        self._patch_all(monkeypatch, ["warning"] + ["clean"] * 5, high=3)
        assert si.aggregate_results()["status"] == "warning"

    def test_all_clean(self, monkeypatch):
        self._patch_all(monkeypatch, ["clean"] * 6)
        out = si.aggregate_results()
        assert out["status"] == "clean"
        assert set(out["scanners"]) == {
            "trivy",
            "clamav",
            "falco",
            "wazuh",
            "openscap",
            "fluent-bit",
        }


# ---------------------------------------------------------------------------
# Infrastructure domain scorers
# ---------------------------------------------------------------------------


class TestVulnerabilityManagement:
    def test_stale_report_caps_at_one(self, fs):
        assert si._score_vulnerability_management({"status": "clean", "critical": 0}) == 1

    def test_critical_high_medium_branches(self, fs):
        _w(fs, "var/log/security/trivy/trivy-1.json", "{}")
        assert si._score_vulnerability_management({"status": "critical", "critical": 3}) == 1
        assert (
            si._score_vulnerability_management(
                {"status": "warning", "critical": 0, "high": 2, "timestamp": "t"}
            )
            == 2
        )
        assert (
            si._score_vulnerability_management(
                {"status": "clean", "critical": 0, "high": 0, "medium": 4, "timestamp": "t"}
            )
            == 3
        )

    def test_fresh_clean_is_optimizing(self, fs):
        _w(fs, "var/log/security/trivy/trivy-1.json", "{}")
        trivy = {"status": "clean", "critical": 0, "high": 0, "medium": 0, "timestamp": "t"}
        assert si._score_vulnerability_management(trivy) == 5

    def test_two_day_old_clean_is_measured(self, fs):
        p = _w(fs, "var/log/security/trivy/trivy-1.json", "{}")
        _age(p, 30)
        trivy = {"status": "clean", "critical": 0, "high": 0, "medium": 0, "timestamp": "t"}
        assert si._score_vulnerability_management(trivy) == 4


class TestSupplyChain:
    def test_sbom_with_packages_trivy_branches(self, fs, monkeypatch):
        _w(fs, "var/log/security/sbom/sbom-1.json", json.dumps({"packages": [{"name": "a"}]}))
        monkeypatch.setattr(si, "get_trivy_summary", lambda: {"status": "not_run"})
        assert si._score_supply_chain() == 3
        monkeypatch.setattr(si, "get_trivy_summary", lambda: {"status": "critical", "critical": 1})
        assert si._score_supply_chain() == 4
        monkeypatch.setattr(si, "get_trivy_summary", lambda: {"status": "clean", "critical": 0})
        assert si._score_supply_chain() == 5

    def test_empty_sbom_scores_two(self, fs):
        _w(fs, "var/log/security/sbom/sbom-1.json", json.dumps({"packages": []}))
        assert si._score_supply_chain() == 2


class TestRuntimeProtectionAndMalware:
    def test_runtime_noncritical_findings_scores_four(self):
        falco = {"status": "info", "critical": 0, "findings": 3}
        assert si._score_runtime_protection(falco) == 4

    def test_malware_fresh_scan_optimizing(self, fs):
        _w(fs, "var/log/security/clamav/clamav-1.json", "{}")
        clamav = {"status": "clean", "critical": 0, "timestamp": "t", "scanned_files": 9}
        assert si._score_malware_defense(clamav) == 5

    def test_malware_30h_old_scan_measured(self, fs):
        p = _w(fs, "var/log/security/clamav/clamav-1.json", "{}")
        _age(p, 30)
        clamav = {"status": "clean", "critical": 0, "timestamp": "t", "scanned_files": 9}
        assert si._score_malware_defense(clamav) == 4

    def test_malware_running_but_nothing_scanned(self, fs):
        _w(fs, "var/log/security/clamav/clamav-1.json", "{}")
        clamav = {"status": "clean", "critical": 0, "timestamp": "t", "scanned_files": 0}
        assert si._score_malware_defense(clamav) == 3


class TestDaemonConfigReader:
    def test_reads_daemon_json(self, fs):
        _w(fs, "etc/docker/daemon.json", json.dumps({"icc": False}))
        assert si._read_docker_daemon_config() == {"icc": False}

    def test_invalid_json_returns_empty(self, fs):
        _w(fs, "etc/docker/daemon.json", "{broken")
        assert si._read_docker_daemon_config() == {}


class TestNetworkSegmentation:
    def test_icc_disabled_with_validator(self, fs, flags):
        _w(fs, "etc/docker/daemon.json", json.dumps({"icc": False}))
        assert si._score_network_segmentation() == 4
        flags.add("network_validator")
        assert si._score_network_segmentation() == 5

    def test_containerized_compose_internal_network(self, fs, flags):
        _w(fs, ".dockerenv", "")
        _w(fs, "app/docker/docker-compose.yml", "networks:\n  internal: true\n")
        flags.add("network_validator")
        assert si._score_network_segmentation() == 5


class TestSecretsManagement:
    def test_full_stack_scores_five(self, fs, flags):
        _w(fs, "run/secrets/api_key", "k")
        _w(fs, "app/gateway/security/key_rotation.py", "# module")
        flags.add("encrypted_store")
        assert si._score_secrets_management() == 5

    def test_secrets_path_is_file_iterdir_error(self, fs, flags):
        _w(fs, "run/secrets", "not a dir")
        assert si._score_secrets_management() == 2


class TestLoggingMonitoring:
    def test_all_pillars_scores_five(self, fs, flags):
        _w(fs, "etc/fluent-bit/fluent-bit.conf", "[SERVICE]")
        flags.add("event_bus")
        assert si._score_logging_monitoring({"status": "clean"}) == 5

    def test_baseline_only(self, fs, flags):
        assert si._score_logging_monitoring({"status": "not_run"}) == 1


class TestComplianceAuditing:
    def test_oscap_binary_present_not_run(self, fs, tools):
        tools["oscap"] = "/usr/bin/oscap"
        assert si._score_compliance_auditing({"status": "not_run"}) == 3

    def test_not_run_no_binary(self, fs, tools):
        assert si._score_compliance_auditing({"status": "not_run"}) == 0

    def test_failures_score_two(self, fs):
        assert si._score_compliance_auditing({"status": "warning", "fail_count": 2}) == 2

    def test_clean_no_report_three(self, fs):
        assert si._score_compliance_auditing({"status": "clean", "fail_count": 0}) == 3

    def test_clean_fresh_and_stale_reports(self, fs):
        p = _w(fs, "var/log/security/openscap/openscap-1.json", "{}")
        assert si._score_compliance_auditing({"status": "clean", "fail_count": 0}) == 5
        _age(p, 50)
        assert si._score_compliance_auditing({"status": "clean", "fail_count": 0}) == 4


class TestIncidentResponse:
    def test_full_stack(self, fs, flags):
        flags.add("soc_correlation")
        _w(fs, "app/docker/scripts/killswitch.sh", "#!/bin/sh")
        falco = {"status": "clean"}
        wazuh = {"status": "clean"}
        assert si._score_incident_response(falco, wazuh) == 5


class TestIdentityAuth:
    def test_missing_auth_module_zero(self, fs, flags):
        assert si._score_identity_authentication() == 0

    def test_full_stack(self, fs, flags):
        _w(fs, "app/gateway/ingest_api/auth.py", "# auth")
        flags.update({"pipeline", "session_manager", "ledger", "trust_manager"})
        assert si._score_identity_authentication() == 5


class TestAccessControl:
    def test_missing_rbac_zero(self, fs, flags):
        assert si._score_access_control_authorization() == 0

    def test_full_stack_with_review_evidence(self, fs, flags):
        _w(fs, "app/gateway/security/rbac_config.py", "# rbac")
        _w(fs, "app/data/collaborator_activity.jsonl", '{"event": "x"}\n')
        flags.update({"session_manager", "collaborator_tracker", "ledger"})
        assert si._score_access_control_authorization() == 5


class TestDataConfidentiality:
    def test_full_stack(self, fs, flags):
        _w(fs, "run/secrets/tls_cert", "cert")
        _w(fs, "app/data/key_rotation.log", "rotated\n")
        flags.update({"http_proxy", "encrypted_store"})
        assert si._score_data_confidentiality_encryption() == 5

    def test_baseline_only(self, fs, flags):
        assert si._score_data_confidentiality_encryption() == 1


class TestResourceAvailability:
    def test_no_compose_zero(self, fs, flags):
        assert si._score_resource_availability() == 0

    def test_full_compose(self, fs, flags):
        _w(
            fs,
            "app/docker/docker-compose.yml",
            "services:\n  g:\n    mem_limit: 512m\n    healthcheck: {}\n    restart: always\n",
        )
        flags.update({"http_proxy", "event_bus"})
        assert si._score_resource_availability() == 5

    def test_unreadable_first_path_falls_through(self, fs, flags):
        (fs / "app/docker/docker-compose.yml").mkdir(parents=True)  # dir → read error
        _w(fs, "rel/docker/docker-compose.yml", "mem_limit: 512m\n")
        assert si._score_resource_availability() == 2


class TestImageSigningProvenance:
    def test_containerized_no_cosign_no_pipeline_evidence(self, fs, tools):
        _w(fs, ".dockerenv", "")
        _w(fs, "app/scripts/security-scan.sh", "trivy image scan only\n")
        assert si._score_image_signing_provenance() == 0

    def test_containerized_pipeline_evidence_full(self, fs, tools):
        _w(fs, ".dockerenv", "")
        _w(fs, "app/scripts/security-scan.sh", "syft packages\ncosign sign image\n")
        _w(fs, "app/.github/workflows/ci.yml", "steps:\n  - run: cosign verify\n")
        tools["slsa-verifier"] = "/usr/local/bin/slsa-verifier"
        assert si._score_image_signing_provenance() == 5

    def test_no_cosign_outside_container_zero(self, fs, tools):
        assert si._score_image_signing_provenance() == 0

    def test_cosign_with_runtime_verification(self, fs, tools, monkeypatch):
        from gateway.ingest_api.state import app_state

        tools["cosign"] = "/usr/bin/cosign"
        tools["slsa-verifier"] = "/usr/bin/slsa-verifier"
        _w(fs, "app/.github/workflows/ci.yml", "uses: sigstore/cosign-installer\n")
        monkeypatch.setattr(
            app_state, "image_verification", {"img": {"verified": True}}, raising=False
        )
        assert si._score_image_signing_provenance() == 5

    def test_cosign_with_wired_verifier_module(self, fs, tools, monkeypatch):
        from gateway.ingest_api.state import app_state

        tools["cosign"] = "/usr/bin/cosign"
        _w(fs, "app/.github/workflows/ci.yml", "uses: sigstore/cosign-installer\n")
        _w(fs, "app/gateway/security/image_verifier.py", "# verifier")
        monkeypatch.setattr(app_state, "image_verification", None, raising=False)
        assert si._score_image_signing_provenance() == 4


class TestRegistrySecurity:
    def test_docker_config_auths_full(self, fs, flags):
        _w(fs, "home/agentshroud/.docker/config.json", "{broken")  # except → next path
        _w(
            fs,
            "root/.docker/config.json",
            json.dumps({"auths": {"ghcr.io": {"auth": "dXNlcjpwYXNz"}}}),
        )
        flags.add("ledger")
        assert si._score_registry_security() == 5

    def test_containerized_compose_private_registry(self, fs, flags):
        _w(fs, ".dockerenv", "")
        _w(fs, "app/docker/docker-compose.yml", "services:\n  g:\n    image: ghcr.io/x/y:1\n")
        flags.add("ledger")
        assert si._score_registry_security() == 5

    def test_containerized_public_image_zero(self, fs, flags):
        _w(fs, ".dockerenv", "")
        _w(fs, "app/docker/docker-compose.yml", "services:\n  g:\n    image: nginx:latest\n")
        assert si._score_registry_security() == 0

    def test_no_config_not_containerized_zero(self, fs, flags):
        assert si._score_registry_security() == 0

    def test_empty_auths_zero(self, fs, flags):
        _w(fs, "home/agentshroud/.docker/config.json", json.dumps({"auths": {}}))
        assert si._score_registry_security() == 0


class TestHostOsHardening:
    def test_no_kernel_info_zero(self, fs, tools):
        assert si._score_host_os_hardening() == 0

    def test_full_host_evidence(self, fs, tools, monkeypatch):
        _w(fs, "proc/version", "Linux version 6.1.0")
        _w(fs, "var/run/docker.sock", "")
        _w(fs, "var/log/audit/audit.log", "type=SYSCALL\n")
        _w(fs, "etc/cis-hardening-applied", "")
        tools["docker"] = "/usr/bin/docker"
        monkeypatch.setattr(
            subprocess,
            "run",
            lambda *a, **k: SimpleNamespace(returncode=0, stdout="24.0.7\n"),
        )
        assert si._score_host_os_hardening() == 5

    def test_containerized_fallback_evidence(self, fs, tools, monkeypatch):
        _w(fs, "proc/version", "Linux version 6.1.0")
        _w(fs, ".dockerenv", "")
        _w(fs, "app/data/audit.log", "event\n")
        _w(
            fs,
            "app/docker/docker-compose.yml",
            "cap_drop:\n  - ALL\nsecurity_opt:\n  - no-new-privileges:true\nread_only: true\n",
        )
        tools["docker"] = "/usr/bin/docker"

        def boom(*a, **k):
            raise OSError("docker info failed")

        monkeypatch.setattr(subprocess, "run", boom)
        assert si._score_host_os_hardening() == 3


class TestDockerDaemonConfig:
    def test_full_daemon_json(self, fs):
        _w(
            fs,
            "etc/docker/daemon.json",
            json.dumps(
                {
                    "icc": False,
                    "no-new-privileges": True,
                    "log-driver": "local",
                    "log-opts": {"max-size": "10m"},
                    "live-restore": True,
                    "userland-proxy": False,
                    "userns-remap": "default",
                }
            ),
        )
        assert si._score_docker_daemon_config() == 5

    def test_icc_only(self, fs):
        _w(fs, "etc/docker/daemon.json", json.dumps({"icc": False}))
        assert si._score_docker_daemon_config() == 1

    def test_not_containerized_no_config_zero(self, fs):
        assert si._score_docker_daemon_config() == 0

    def test_containerized_no_compose_zero(self, fs):
        _w(fs, ".dockerenv", "")
        assert si._score_docker_daemon_config() == 0

    def test_containerized_compose_equivalents(self, fs):
        _w(fs, ".dockerenv", "")
        _w(
            fs,
            "app/docker/docker-compose.yml",
            "cap_drop:\n  - ALL\n"
            "security_opt:\n  - no-new-privileges:true\n  - seccomp:profile.json\n"
            "logging:\n  options:\n    max-size: 10m\n"
            'restart: always\nread_only: true\nuser: "1000:1000"\n',
        )
        assert si._score_docker_daemon_config() == 5


class TestContainerRuntimeIsolation:
    def test_unreadable_status_zero(self, fs):
        assert si._score_container_runtime_isolation() == 0

    def test_full_root_caps_zero(self, fs):
        _w(fs, "proc/self/status", "CapEff:\tffffffffffffffff\n")
        assert si._score_container_runtime_isolation() == 0

    def test_fully_isolated_container_scores_five(self, fs):
        _w(fs, "proc/self/status", "CapEff:\t0000000000000000\nSeccomp:\t2\n")
        _w(fs, ".dockerenv", "")
        _w(fs, "proc/mounts", "overlay / overlay ro,relatime 0 0\n")
        assert si._score_container_runtime_isolation() == 5

    def test_shared_mount_namespace_returns_one(self, fs):
        _w(fs, "proc/self/status", "CapEff:\t00000000a80425fb\n")
        target = _w(fs, "mntns-target", "")
        (fs / "proc/1/ns").mkdir(parents=True)
        (fs / "proc/self/ns").mkdir(parents=True)
        (fs / "proc/1/ns/mnt").symlink_to(target)
        (fs / "proc/self/ns/mnt").symlink_to(target)
        assert si._score_container_runtime_isolation() == 1

    def test_distinct_namespaces_partial_caps(self, fs):
        _w(fs, "proc/self/status", "CapEff:\t00000000a80425fb\n")
        t1 = _w(fs, "mnt1", "")
        t2 = _w(fs, "mnt2", "")
        (fs / "proc/1/ns").mkdir(parents=True)
        (fs / "proc/self/ns").mkdir(parents=True)
        (fs / "proc/1/ns/mnt").symlink_to(t1)
        (fs / "proc/self/ns/mnt").symlink_to(t2)
        assert si._score_container_runtime_isolation() == 2

    def test_namespace_check_exception_assumes_isolated(self, fs, monkeypatch):
        sandbox_path = si.Path  # current sandboxed factory

        def raising_path(*args):
            if "ns/mnt" in str(Path(*args)):
                raise RuntimeError("no ns access")
            return sandbox_path(*args)

        _w(fs, "proc/self/status", "CapEff:\t00000000a80425fb\n")
        monkeypatch.setattr(si, "Path", raising_path)
        assert si._score_container_runtime_isolation() == 2


# ---------------------------------------------------------------------------
# Agentic AI domain scorers (22–33)
# ---------------------------------------------------------------------------

_ALL_FLAGS = {
    "prompt_guard",
    "pipeline",
    "ledger",
    "event_bus",
    "session_manager",
    "soc_correlation",
    "tool_acl_enforcer",
    "approval_queue",
    "egress_filter",
    "delegation_manager",
    "collaborator_tracker",
    "trust_manager",
    "memory_integrity",
    "killswitch_monitor",
    "egress_approval_queue",
    "privacy_enforcer",
}


class TestAgenticScorers:
    def _build_modules(self, fs):
        for mod in ("prompt_guard", "tool_acl", "egress_filter", "memory_integrity"):
            _w(fs, f"app/gateway/security/{mod}.py", "# module")
        _w(fs, "app/docker/scripts/killswitch.sh", "#!/bin/sh")
        (fs / "var/log/security").mkdir(parents=True, exist_ok=True)

    def test_all_scorers_optimizing_with_full_stack(self, fs, flags):
        self._build_modules(fs)
        flags.update(_ALL_FLAGS)
        assert si._score_prompt_injection_defense() == 5
        assert si._score_agent_behavior_integrity() == 5
        assert si._score_tool_use_safety() == 5
        assert si._score_least_agency() == 5
        assert si._score_agent_identity_nhi() == 5
        assert si._score_memory_integrity() == 5
        assert si._score_inter_agent_trust() == 5
        assert si._score_ai_observability() == 5
        assert si._score_human_in_the_loop() == 5
        assert si._score_rogue_agent_containment() == 5
        assert si._score_data_exfiltration_prevention() == 5

    def test_all_scorers_zero_without_modules_or_state(self, fs, flags):
        assert si._score_prompt_injection_defense() == 0
        assert si._score_agent_behavior_integrity() == 0
        assert si._score_tool_use_safety() == 0
        assert si._score_least_agency() == 0
        assert si._score_agent_identity_nhi() == 0
        assert si._score_memory_integrity() == 0
        assert si._score_inter_agent_trust() == 0
        assert si._score_ai_observability() == 0
        assert si._score_human_in_the_loop() == 0
        assert si._score_rogue_agent_containment() == 0
        assert si._score_data_exfiltration_prevention() == 0


class TestAiModelSupplyChain:
    def test_no_sbom_zero(self, fs, monkeypatch):
        assert si._score_ai_model_supply_chain() == 0

    def test_full_attestation_chain(self, fs, monkeypatch):
        _w(fs, "var/log/security/sbom/sbom-1.json", json.dumps({"packages": []}))
        _w(fs, "var/log/security/trivy/trivy-1.json", "{}")
        _w(fs, "rel/gateway/Dockerfile", "FROM python@sha256:abc123\n")
        monkeypatch.setattr(si, "get_trivy_summary", lambda: {"status": "clean", "critical": 0})
        assert si._score_ai_model_supply_chain() == 5


# ---------------------------------------------------------------------------
# Mandatory gates
# ---------------------------------------------------------------------------


class TestMandatoryGates:
    def test_gates_zero_affected_domains(self, fs, flags, tools, monkeypatch):
        monkeypatch.delenv("DOCKER_CONTENT_TRUST", raising=False)
        _w(fs, "proc/self/status", "CapEff:\tffffffffffffffff\n")
        flags.add("pipeline")  # pipeline active but no prompt_guard module on disk
        scores = {i: 5 for i in range(1, 34)}
        updated = si._evaluate_mandatory_gates(scores, {"critical": 2})
        assert updated[21] == 0  # privileged container
        assert updated[2] == 0  # critical CVE running
        assert updated[13] == 0  # no auth module
        assert updated[15] == 1  # no TLS and no encrypted store → capped
        assert updated[17] == 0  # no DCT / cosign / pipeline evidence
        assert updated[22] == 0  # pipeline without prompt_guard
        assert updated[24] == 0  # no tool_acl
        assert updated[33] == 0  # no egress_filter
        assert updated[32] == 0  # no killswitch
        assert updated[30] == 1  # no audit trail → capped

    def test_gates_pass_with_full_evidence(self, fs, flags, tools, monkeypatch):
        monkeypatch.setenv("DOCKER_CONTENT_TRUST", "1")
        _w(fs, "proc/self/status", "CapEff:\t0000000000000000\n")
        _w(fs, "app/gateway/ingest_api/auth.py", "# auth")
        for mod in ("prompt_guard", "tool_acl", "egress_filter"):
            _w(fs, f"app/gateway/security/{mod}.py", "# module")
        _w(fs, "app/docker/scripts/killswitch.sh", "#!/bin/sh")
        _w(fs, "run/secrets/tls_cert", "cert")
        flags.update({"pipeline", "event_bus", "encrypted_store"})
        scores = {i: 5 for i in range(1, 34)}
        updated = si._evaluate_mandatory_gates(scores, {"critical": 0})
        assert updated == scores


# ---------------------------------------------------------------------------
# Compliance maths
# ---------------------------------------------------------------------------


class TestComplianceMaths:
    def test_weighted_subscore_empty_map(self):
        assert si._compute_weighted_subscore({1: 5}, {}) == 0.0

    def test_weighted_subscore_partial(self):
        out = si._compute_weighted_subscore({13: 5, 14: 0}, {13: ("FR1", 2), 14: ("FR2", 2)})
        assert out == 50.0

    def test_iec_sl_levels(self):
        iec_ids = list(si._IEC_DOMAIN_MAP.keys())
        assert si._determine_iec_sl({}) == 0
        assert si._determine_iec_sl({d: 2 for d in iec_ids}) == 1
        sl2 = {d: 3 for d in iec_ids}
        sl2[13] = 4
        sl2[14] = 4
        assert si._determine_iec_sl(sl2) == 2
        sl3 = {d: 4 for d in iec_ids}
        sl3[15] = 5
        assert si._determine_iec_sl(sl3) == 3
        assert si._determine_iec_sl({i: 5 for i in range(1, 34)}) == 4

    @pytest.mark.parametrize(
        "minval,expected",
        [
            (96.0, "Optimizing"),
            (81.0, "Advanced"),
            (61.0, "Hardened"),
            (41.0, "Standard"),
            (21.0, "Foundational"),
            (5.0, "Not Assessed"),
        ],
    )
    def test_compliance_levels(self, minval, expected):
        assert si._determine_compliance_level(99, 99, 99, 99, 99, 99, minval) == expected


# ---------------------------------------------------------------------------
# compute_scorecard end-to-end
# ---------------------------------------------------------------------------


class TestComputeScorecard:
    def test_bare_environment(self, fs, flags, tools, monkeypatch):
        monkeypatch.delenv("DOCKER_CONTENT_TRUST", raising=False)
        monkeypatch.setattr(si, "_is_clamd_running", lambda: False)
        out = si.compute_scorecard()
        assert len(out["domains"]) == 33
        assert out["totals"]["max"] == 165
        assert 0 <= out["totals"]["percentage"] <= 100
        assert out["compliance"]["iec_62443"]["security_level"] in range(0, 5)
        assert out["overall_level"] == out["overall_maturity"]
        # Hard gates fire in an empty environment
        by_id = {d["id"]: d["score"] for d in out["domains"]}
        assert by_id[13] == 0 and by_id[24] == 0 and by_id[32] == 0 and by_id[33] == 0
        for d in out["domains"]:
            assert d["maturity"] == si._MATURITY_LABELS[d["score"]]
            assert d["urgency"] in {"critical", "high", "medium", "low", "info"}

    def test_rich_environment(self, fs, flags, tools, monkeypatch):
        import gateway.security.falco_monitor as fm
        import gateway.security.wazuh_client as wc

        monkeypatch.setenv("DOCKER_CONTENT_TRUST", "1")
        monkeypatch.setattr(si, "_is_clamd_running", lambda: True)
        monkeypatch.setattr(fm, "read_alerts", lambda alert_dir: [])
        monkeypatch.setattr(wc, "read_alerts", lambda alert_dir: [])

        ts = "2026-06-12T00:00:00+00:00"
        _w(fs, "var/log/security/sbom/sbom-1.json", json.dumps({"packages": [{"name": "a"}]}))
        _w(
            fs,
            "var/log/security/trivy/trivy-1.json",
            json.dumps({"by_severity": {}, "total_vulnerabilities": 0, "timestamp": ts}),
        )
        _w(
            fs,
            "var/log/security/clamav/clamav-1.json",
            json.dumps({"infected_count": 0, "scanned_files": 4, "timestamp": ts}),
        )
        _w(
            fs,
            "var/log/security/openscap/openscap-1.json",
            json.dumps({"pass_count": 9, "fail_count": 0, "critical": 0, "timestamp": ts}),
        )
        (fs / "var/log/falco").mkdir(parents=True)
        (fs / "var/ossec/logs/alerts").mkdir(parents=True)
        _w(fs, "var/log/fluent-bit/agentshroud-a.log", "line\n")
        _w(fs, "tmp/fluent-bit.pid", str(os.getpid()))
        # Processes
        _w(fs, "proc/123/comm", "falco\n")
        _w(fs, "proc/123/status", "State:\tS (sleeping)\n")
        _w(fs, "proc/124/comm", "wazuh-agentd\n")
        _w(fs, "proc/self/status", "CapEff:\t0000000000000000\nSeccomp:\t2\n")
        _w(fs, "proc/version", "Linux version 6.1.0")
        _w(fs, "proc/mounts", "overlay / overlay ro,relatime 0 0\n")
        # Container + compose evidence
        _w(fs, ".dockerenv", "")
        _w(
            fs,
            "app/docker/docker-compose.yml",
            "services:\n  g:\n    image: ghcr.io/x/y:1\n    mem_limit: 512m\n"
            "    healthcheck: {}\n    restart: always\n    read_only: true\n"
            '    user: "1000"\n    cap_drop:\n      - ALL\n'
            "    security_opt:\n      - no-new-privileges:true\n      - seccomp:p.json\n"
            "    logging:\n      options:\n        max-size: 10m\n"
            "networks:\n  internal: true\n",
        )
        # Security modules + evidence files
        _w(fs, "app/gateway/ingest_api/auth.py", "# auth")
        for mod in (
            "rbac_config",
            "key_rotation",
            "prompt_guard",
            "tool_acl",
            "egress_filter",
            "memory_integrity",
            "image_verifier",
        ):
            _w(fs, f"app/gateway/security/{mod}.py", "# module")
        _w(fs, "app/data/collaborator_activity.jsonl", '{"e": 1}\n')
        _w(fs, "app/data/key_rotation.log", "rotated\n")
        _w(fs, "app/data/audit.log", "event\n")
        _w(fs, "run/secrets/tls_cert", "cert")
        _w(fs, "run/secrets/api_key", "key")
        _w(fs, "app/docker/scripts/killswitch.sh", "#!/bin/sh")
        _w(fs, "app/scripts/security-scan.sh", "syft packages\ncosign sign image\n")
        _w(fs, "app/.github/workflows/ci.yml", "run: cosign verify\n")
        _w(fs, "etc/fluent-bit/fluent-bit.conf", "[SERVICE]")
        _w(fs, "app/.semgrep.yml", "rules: []")
        _w(fs, "app/.pre-commit-config.yaml", "repos: []")
        _w(fs, "app/.gitleaks.toml", "[allowlist]")
        _w(fs, "app/CONTRIBUTING.md", "# SDL")
        _w(fs, "rel/gateway/Dockerfile", "FROM python@sha256:abc\n")
        flags.update(_ALL_FLAGS | {"encrypted_store", "http_proxy", "network_validator"})

        out = si.compute_scorecard()
        by_id = {d["id"]: d["score"] for d in out["domains"]}
        for domain_id in range(22, 34):
            assert by_id[domain_id] == 5, f"domain {domain_id} = {by_id[domain_id]}"
        assert by_id[13] == 5  # identity & auth full stack
        assert out["totals"]["score"] > 120
        assert out["compliance"]["level"] != "Not Assessed"
        assert isinstance(out["overall_score"], float)


# ---------------------------------------------------------------------------
# compute_bot_scorecard
# ---------------------------------------------------------------------------


class TestComputeBotScorecard:
    def _state(self, image="img:1", summary=None, denied=0, raise_stats=False):
        ef = MagicMock()
        if raise_stats:
            ef.get_stats.side_effect = RuntimeError("stats unavailable")
        else:
            ef.get_stats.return_value = {"denied": denied}
        bots = {"b1": SimpleNamespace(image=image)} if image else {}
        return SimpleNamespace(
            config=SimpleNamespace(bots=bots),
            scanner_results=(
                {f"trivy:image:{image}": {"summary": summary}} if summary is not None else {}
            ),
            egress_filter=ef,
        )

    def test_findings_and_denials_penalised(self):
        state = self._state(summary={"critical": 1, "high": 1, "medium": 2}, denied=1)
        out = si.compute_bot_scorecard("b1", state)
        assert out["score"] == 100 - 20 - 10 - 6 - 5
        assert out["risk_level"] == "yellow"
        assert out["egress_denials"] == 1
        assert out["image"] == "img:1"
        assert {d["domain"] for d in out["domains"]} == {"vuln_scan", "egress"}

    def test_stats_exception_defaults_to_zero_denials(self):
        state = self._state(summary={"critical": 0, "high": 0, "medium": 0}, raise_stats=True)
        out = si.compute_bot_scorecard("b1", state)
        assert out["score"] == 100
        assert out["risk_level"] == "green"

    def test_unknown_bot_clean_score(self):
        state = SimpleNamespace(config=None, scanner_results={}, egress_filter=None)
        out = si.compute_bot_scorecard("ghost", state)
        assert out["score"] == 100
        assert out["image"] == ""
        assert out["risk_level"] == "green"

    def test_heavy_findings_clamp_to_red_zero(self):
        state = self._state(summary={"critical": 5, "high": 3, "medium": 10}, denied=4)
        out = si.compute_bot_scorecard("b1", state)
        assert out["score"] == 0
        assert out["risk_level"] == "red"
