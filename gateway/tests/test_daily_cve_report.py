# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway.security.daily_cve_report."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest

from gateway.security.daily_cve_report import (
    _already_sent_today,
    format_cve_report,
    run_and_send_cve_report,
)

# ── Fixtures ─────────────────────────────────────────────────────────────────


def _make_report(critical=2, high=5, medium=10, low=3, total=20) -> dict:
    """Build a minimal parsed Trivy report."""
    return {
        "scanner": "trivy",
        "timestamp": "2026-04-01T06:00:00+00:00",
        "total_vulnerabilities": total,
        "by_severity": {
            "CRITICAL": critical,
            "HIGH": high,
            "MEDIUM": medium,
            "LOW": low,
            "UNKNOWN": 0,
        },
        "top_cves": [
            {
                "id": "CVE-2026-1234",
                "severity": "CRITICAL",
                "package": "libssl",
                "installed_version": "1.1.1k",
                "fixed_version": "1.1.1n",
                "title": "OpenSSL buffer overflow",
                "target": "/usr/lib",
            },
            {
                "id": "CVE-2026-5678",
                "severity": "HIGH",
                "package": "python3",
                "installed_version": "3.9.1",
                "fixed_version": "3.9.7",
                "title": "Python path traversal",
                "target": "/usr/bin",
            },
        ],
        "affected_packages": ["libssl", "python3"],
        "affected_package_count": 2,
        "error": None,
    }


def _make_error_report() -> dict:
    return {
        "scanner": "trivy",
        "timestamp": "2026-04-01T06:00:00+00:00",
        "error": "binary_not_found",
        "total_vulnerabilities": 0,
        "by_severity": {},
        "top_cves": [],
        "affected_packages": [],
        "affected_package_count": 0,
    }


# ── format_cve_report ─────────────────────────────────────────────────────────


class TestFormatCveReport:
    def test_contains_header(self):
        msg = format_cve_report(_make_report())
        assert "AgentShroud™ Daily CVE Report" in msg

    def test_contains_severity_counts(self):
        msg = format_cve_report(_make_report(critical=2, high=5))
        assert "CRITICAL" in msg
        assert "*2*" in msg
        assert "HIGH" in msg
        assert "*5*" in msg

    def test_contains_cve_ids(self):
        msg = format_cve_report(_make_report())
        assert "CVE-2026-1234" in msg
        assert "CVE-2026-5678" in msg

    def test_contains_package_names(self):
        msg = format_cve_report(_make_report())
        assert "libssl" in msg
        assert "python3" in msg

    def test_status_critical_when_critical_present(self):
        msg = format_cve_report(_make_report(critical=1))
        assert "CRITICAL" in msg

    def test_status_clean_when_no_critical_high(self):
        msg = format_cve_report(_make_report(critical=0, high=0, medium=3, total=3))
        assert "CLEAN" in msg

    def test_error_report_shows_error_message(self):
        msg = format_cve_report(_make_error_report())
        assert "error" in msg.lower()
        assert "binary_not_found" in msg

    def test_total_vulnerability_count_shown(self):
        msg = format_cve_report(_make_report(total=20))
        assert "20" in msg

    def test_affected_packages_count_shown(self):
        msg = format_cve_report(_make_report())
        assert "2" in msg  # affected_package_count

    def test_fixed_version_shown(self):
        msg = format_cve_report(_make_report())
        assert "1.1.1n" in msg  # fixed_version for CVE-2026-1234

    def test_zero_count_severity_omitted(self):
        msg = format_cve_report(_make_report(critical=0, high=0, medium=5, low=0))
        # CRITICAL and HIGH with 0 count should not appear in the breakdown
        lines = msg.split("\n")
        severity_lines = [ln for ln in lines if "🔴" in ln or "🟠" in ln]
        assert not any("CRITICAL" in ln for ln in severity_lines)
        assert not any("HIGH" in ln for ln in severity_lines)


# ── _already_sent_today ───────────────────────────────────────────────────────


class TestAlreadySentToday:
    def test_returns_false_when_file_missing(self, tmp_path, monkeypatch):
        monkeypatch.setattr(
            "gateway.security.daily_cve_report._LAST_REPORT_PATH",
            tmp_path / "does_not_exist.txt",
        )
        from gateway.security import daily_cve_report

        monkeypatch.setattr(daily_cve_report, "_LAST_REPORT_PATH", tmp_path / "no.txt")
        assert not _already_sent_today(datetime.now(timezone.utc))

    def test_returns_true_when_sent_today(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last.txt"
        now = datetime.now(timezone.utc)
        sentinel.write_text(now.isoformat())
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", sentinel)
        assert _mod._already_sent_today(now)

    def test_returns_false_when_sent_yesterday(self, tmp_path, monkeypatch):
        from datetime import timedelta

        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last.txt"
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        sentinel.write_text(yesterday.isoformat())
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", sentinel)
        assert not _mod._already_sent_today(datetime.now(timezone.utc))


# ── run_and_send_cve_report ───────────────────────────────────────────────────


class TestRunAndSendCveReport:
    @pytest.mark.asyncio
    async def test_sends_telegram_on_success(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        # Stub Trivy scan
        monkeypatch.setattr(_mod, "run_trivy_scan", lambda **_: _make_report())
        monkeypatch.setattr(_mod, "save_report", lambda r: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")

        sent_payloads = []

        async def _fake_send(token, chat_id, text, base_url):
            sent_payloads.append({"token": token, "chat_id": chat_id, "text": text})
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await run_and_send_cve_report(
            bot_token="test-token",
            owner_chat_id="12345",
        )

        assert result["telegram_sent"] is True
        assert len(sent_payloads) == 1
        assert "CVE-2026-1234" in sent_payloads[0]["text"]

    @pytest.mark.asyncio
    async def test_returns_summary_without_token(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "run_trivy_scan", lambda **_: _make_report())
        monkeypatch.setattr(_mod, "save_report", lambda r: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")

        result = await run_and_send_cve_report(
            bot_token="",  # no token
            owner_chat_id="",
        )

        # Should still return scan summary even without telegram delivery
        assert "findings" in result
        assert result["telegram_sent"] is False

    @pytest.mark.asyncio
    async def test_trivy_error_still_sends_error_report(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "run_trivy_scan", lambda **_: _make_error_report())
        monkeypatch.setattr(_mod, "save_report", lambda r: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")

        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await run_and_send_cve_report(
            bot_token="tok",
            owner_chat_id="12345",
        )

        assert result["telegram_sent"] is True
        assert "error" in sent[0].lower()


# ── check_upstream_cves ───────────────────────────────────────────────────────


def _make_github_advisory(
    ghsa_id: str,
    cve_id=None,
    severity: str = "high",
    score: float = 7.5,
) -> dict:
    """Build a minimal GitHub Security Advisory payload keyed on GHSA id.

    ``ghsa_id`` is the source-of-truth identifier the watcher now diffs on.
    ``cve_id`` is usually ``None`` (GitHub rarely assigns a CVE to these).
    """
    return {
        "ghsa_id": ghsa_id,
        "cve_id": cve_id,
        "summary": f"Test vulnerability {ghsa_id}",
        "description": "Test description.",
        "severity": severity,
        "cvss": {"vector_string": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "score": score},
        "published_at": "2026-04-10T00:00:00Z",
        "html_url": f"https://github.com/openclaw/openclaw/security/advisories/{ghsa_id}",
    }


class TestCheckUpstreamCves:
    def _patch_urllib(self, monkeypatch, advisories: list) -> None:
        """Stub urllib.request.urlopen to return a list of advisories."""
        import urllib.request as _ur

        fake_resp = MagicMock()
        fake_resp.__enter__ = lambda s: s
        fake_resp.__exit__ = MagicMock(return_value=False)
        fake_resp.read.return_value = json.dumps(advisories).encode()
        monkeypatch.setattr(_ur, "urlopen", lambda *a, **kw: fake_resp)

    def test_returns_new_advisory_not_in_registry(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        new_ghsa = "GHSA-zzzz-zzzz-zzzz"  # not in the registry
        self._patch_urllib(monkeypatch, [_make_github_advisory(new_ghsa)])
        result = check_upstream_cves()
        assert len(result) == 1
        # The GHSA id is now the primary identifier reported.
        assert result[0]["id"] == new_ghsa
        assert result[0]["ghsa_id"] == new_ghsa
        assert result[0]["cve_id"] is None
        assert result[0]["severity"] == "HIGH"
        assert result[0]["cvss"] == 7.5

    def test_skips_advisory_without_ghsa_id(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        adv = _make_github_advisory("GHSA-yyyy-yyyy-yyyy")
        adv["ghsa_id"] = None  # cannot key to the registry
        self._patch_urllib(monkeypatch, [adv])
        assert check_upstream_cves() == []

    def test_skips_ghsa_already_in_registry(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        # GHSA-p7gr-f84w-hqg5 is a real matched ghsa_id in AGENT_CVE_REGISTRY.
        self._patch_urllib(monkeypatch, [_make_github_advisory("GHSA-p7gr-f84w-hqg5")])
        assert check_upstream_cves() == []

    def test_skips_advisory_whose_cve_is_already_tracked(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        # New GHSA id, but its cve_id (CVE-2026-27002) is already tracked in the
        # registry — fallback dedup on cve_id keeps it from re-alerting.
        adv = _make_github_advisory("GHSA-newq-newq-newq", cve_id="CVE-2026-27002")
        self._patch_urllib(monkeypatch, [adv])
        assert check_upstream_cves() == []

    def test_returns_empty_when_all_known(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        self._patch_urllib(monkeypatch, [])
        assert check_upstream_cves() == []

    def test_raises_on_network_error(self, monkeypatch):
        import urllib.request as _ur

        from gateway.security.daily_cve_report import check_upstream_cves

        monkeypatch.setattr(_ur, "urlopen", MagicMock(side_effect=OSError("timeout")))
        with pytest.raises(OSError):
            check_upstream_cves()

    def test_uses_github_token_in_header(self, monkeypatch):
        import urllib.request as _ur

        from gateway.security.daily_cve_report import check_upstream_cves

        captured = {}

        fake_resp = MagicMock()
        fake_resp.__enter__ = lambda s: s
        fake_resp.__exit__ = MagicMock(return_value=False)
        fake_resp.read.return_value = b"[]"

        def _capture_req(req, **kw):
            captured["headers"] = dict(req.headers)
            return fake_resp

        monkeypatch.setattr(_ur, "urlopen", _capture_req)
        check_upstream_cves(github_token="ghp_test_token")
        assert captured["headers"].get("Authorization") == "Bearer ghp_test_token"


# ── format_upstream_cve_alert ─────────────────────────────────────────────────


class TestFormatUpstreamCveAlert:
    def _cve(self, cve_id="CVE-2026-99999", sev="HIGH", score=7.5):
        return {
            "id": cve_id,
            "summary": "Test summary text",
            "severity": sev,
            "cvss": score,
            "published_at": "2026-04-10T00:00:00Z",
            "html_url": "https://example.com",
        }

    def test_contains_cve_id(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "CVE-2026-99999" in msg

    def test_contains_summary(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "Test summary text" in msg

    def test_contains_severity_icon(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve(sev="CRITICAL", score=9.9)])
        assert "🔴" in msg

    def test_contains_action_required(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "Action required" in msg
        assert "agent_cve_registry.py" in msg

    def test_plural_header_for_multiple_cves(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve("CVE-2026-1"), self._cve("CVE-2026-2")])
        assert "2 New OpenClaw CVEs" in msg

    def test_singular_header_for_one_cve(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "1 New OpenClaw CVE " in msg  # no trailing 's'

    def test_contains_disclosed_date(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "2026-04-10" in msg

    def test_handles_missing_optional_fields(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        # cvss=None, no summary, no published_at — should not raise
        cve = {
            "id": "CVE-2026-99999",
            "severity": "HIGH",
            "cvss": None,
            "summary": "",
            "published_at": "",
        }
        msg = format_upstream_cve_alert([cve])
        assert "CVE-2026-99999" in msg


# ── run_upstream_cve_check ────────────────────────────────────────────────────


class TestRunUpstreamCveCheck:
    @pytest.mark.asyncio
    async def test_sends_alert_when_new_cves_found(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda token=None: [
                {
                    "id": "CVE-2026-99999",
                    "summary": "new vuln",
                    "severity": "HIGH",
                    "cvss": 7.5,
                    "published_at": "2026-04-10T00:00:00Z",
                    "html_url": "https://example.com",
                }
            ],
        )
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_upstream_cve_check(bot_token="tok", owner_chat_id="12345")

        assert result["new_cves"] == 1
        assert result["cve_ids"] == ["CVE-2026-99999"]
        assert result["telegram_sent"] is True
        assert len(sent) == 1
        assert "CVE-2026-99999" in sent[0]

    @pytest.mark.asyncio
    async def test_no_alert_when_registry_current(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "check_upstream_cves", lambda token=None: [])
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_upstream_cve_check(bot_token="tok", owner_chat_id="12345")

        assert result["new_cves"] == 0
        assert result["telegram_sent"] is False
        assert sent == []

    @pytest.mark.asyncio
    async def test_returns_error_on_github_api_failure(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            MagicMock(side_effect=OSError("connection refused")),
        )

        result = await _mod.run_upstream_cve_check(bot_token="tok", owner_chat_id="12345")

        assert result["new_cves"] == 0
        assert result["telegram_sent"] is False
        assert "connection refused" in result.get("error", "")

    @pytest.mark.asyncio
    async def test_no_telegram_send_when_no_token(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda token=None: [
                {
                    "id": "CVE-2026-99999",
                    "summary": "",
                    "severity": "HIGH",
                    "cvss": 7.5,
                    "published_at": "",
                    "html_url": "",
                }
            ],
        )
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_upstream_cve_check(
            bot_token="",  # no token
            owner_chat_id="",
        )

        assert result["new_cves"] == 1
        assert result["telegram_sent"] is False
        assert sent == []


# ── _already_checked_upstream_today ──────────────────────────────────────────


class TestAlreadyCheckedUpstreamToday:
    def test_returns_false_when_file_missing(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_LAST_UPSTREAM_CHECK_PATH", tmp_path / "no.txt")
        assert not _mod._already_checked_upstream_today(datetime.now(timezone.utc))

    def test_returns_true_when_checked_today(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last_upstream.txt"
        now = datetime.now(timezone.utc)
        sentinel.write_text(now.isoformat())
        monkeypatch.setattr(_mod, "_LAST_UPSTREAM_CHECK_PATH", sentinel)
        assert _mod._already_checked_upstream_today(now)

    def test_returns_false_when_checked_yesterday(self, tmp_path, monkeypatch):
        from datetime import timedelta

        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last_upstream.txt"
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        sentinel.write_text(yesterday.isoformat())
        monkeypatch.setattr(_mod, "_LAST_UPSTREAM_CHECK_PATH", sentinel)
        assert not _mod._already_checked_upstream_today(datetime.now(timezone.utc))


# ── _build_image_targets ──────────────────────────────────────────────────────


class TestBuildImageTargets:
    def test_always_includes_gateway_image(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)
        targets = _build_image_targets()
        assert "agentshroud-gateway:latest" in targets

    def test_env_var_adds_extra_targets(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv(
            "AGENTSHROUD_TRIVY_IMAGES", "agentshroud-openclaw:latest,agentshroud/hermes:latest"
        )
        targets = _build_image_targets()
        assert "agentshroud-openclaw:latest" in targets
        assert "agentshroud/hermes:latest" in targets

    def test_env_var_empty_string_ignored(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv("AGENTSHROUD_TRIVY_IMAGES", "")
        targets = _build_image_targets()
        # Only gateway image — no empty entries
        assert targets == ["agentshroud-gateway:latest"]

    def test_deduplication(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv(
            "AGENTSHROUD_TRIVY_IMAGES", "agentshroud-gateway:latest,agentshroud-gateway:latest"
        )
        targets = _build_image_targets()
        assert targets.count("agentshroud-gateway:latest") == 1

    def test_whitespace_stripped_from_env_var(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv(
            "AGENTSHROUD_TRIVY_IMAGES",
            "  agentshroud-openclaw:latest  ,  agentshroud/hermes:latest  ",
        )
        targets = _build_image_targets()
        assert "agentshroud-openclaw:latest" in targets
        assert "agentshroud/hermes:latest" in targets
        assert "  agentshroud-openclaw:latest  " not in targets


# ── run_and_send_cve_report — image scan integration ─────────────────────────


class TestRunAndSendCveReportImageScans:
    @pytest.mark.asyncio
    async def test_image_scans_run_for_each_target(self, tmp_path, monkeypatch):
        """run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each target."""
        import gateway.security.daily_cve_report as _mod

        scan_calls = []

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            scan_calls.append({"target": target, "scan_type": scan_type})
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda r, **kw: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.setenv("AGENTSHROUD_TRIVY_IMAGES", "agentshroud-openclaw:latest")

        async def _fake_send(token, chat_id, text, base_url):
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        await _mod.run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        image_calls = [c for c in scan_calls if c["scan_type"] == "image"]
        image_targets = {c["target"] for c in image_calls}
        assert "agentshroud-gateway:latest" in image_targets
        assert "agentshroud-openclaw:latest" in image_targets

    @pytest.mark.asyncio
    async def test_image_scan_summary_appended_to_message(self, tmp_path, monkeypatch):
        """Message sent via Telegram includes a Container Image Scans section."""
        import gateway.security.daily_cve_report as _mod

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda r, **kw: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)

        sent_messages = []

        async def _fake_send(token, chat_id, text, base_url):
            sent_messages.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        await _mod.run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        assert len(sent_messages) == 1
        assert "Container Image Scans" in sent_messages[0]
        assert "agentshroud-gateway:latest" in sent_messages[0]

    @pytest.mark.asyncio
    async def test_image_scan_result_in_return_value(self, tmp_path, monkeypatch):
        """Return value includes image_scans list."""
        import gateway.security.daily_cve_report as _mod

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda r, **kw: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)

        async def _fake_send(token, chat_id, text, base_url):
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        assert "image_scans" in result
        assert isinstance(result["image_scans"], list)
        assert len(result["image_scans"]) >= 1

    @pytest.mark.asyncio
    async def test_image_scan_error_does_not_abort_report(self, tmp_path, monkeypatch):
        """A failing image scan appends an error line but does not raise."""
        import gateway.security.daily_cve_report as _mod

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            if scan_type == "image":
                return {"error": "binary_not_found", "raw_output": ""}
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda r, **kw: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)

        async def _fake_send(token, chat_id, text, base_url):
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        assert result["telegram_sent"] is True
        # Error line present in image_scans
        assert any(
            "error" in line.lower() or "scan error" in line.lower()
            for line in result["image_scans"]
        )

    @pytest.mark.asyncio
    async def test_critical_image_finding_uses_red_icon(self, tmp_path, monkeypatch):
        """A critical finding in an image scan uses the red icon."""
        import gateway.security.daily_cve_report as _mod

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            if scan_type == "image":
                return _make_report(critical=3, high=1, medium=0, low=0, total=4)
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda r, **kw: None)
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)

        async def _fake_send(token, chat_id, text, base_url):
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await _mod.run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        assert any("🔴" in line for line in result["image_scans"])


# ── GHSA ingest scheduler ─────────────────────────────────────────────────────


class TestAlreadyIngestedGhsaToday:
    def test_returns_false_when_file_missing(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "no.txt")
        assert not _mod._already_ingested_ghsa_today(datetime.now(timezone.utc))

    def test_returns_true_when_ingested_today(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last_ghsa.txt"
        now = datetime.now(timezone.utc)
        sentinel.write_text(now.isoformat())
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", sentinel)
        assert _mod._already_ingested_ghsa_today(now)

    def test_returns_false_when_ingested_yesterday(self, tmp_path, monkeypatch):
        from datetime import timedelta

        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last_ghsa.txt"
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        sentinel.write_text(yesterday.isoformat())
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", sentinel)
        assert not _mod._already_ingested_ghsa_today(datetime.now(timezone.utc))


class TestGhsaIngestScheduler:
    @pytest.mark.asyncio
    async def test_runs_ingest_records_then_skips_next_iteration(self, tmp_path, monkeypatch):
        """First iteration ingests + records; second sees dedup and skips."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        # Isolate dedup state and disk paths for this test.
        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        sentinel = tmp_path / "last_ghsa.txt"
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", sentinel)

        ran = {"count": 0}

        async def _fake_ingest(**kwargs):
            ran["count"] += 1
            return {"new_cves": 2, "telegram_sent": True}

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _fake_ingest)

        # Iteration 1: no sleep (immediate). Iteration 2: sleep raises Cancelled.
        calls = {"sleep": 0}

        async def _sleep(_secs):
            calls["sleep"] += 1
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        # ingest_hour in the past → iteration 1 triggers immediately (no sleep).
        past_hour = (datetime.now(timezone.utc).hour - 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )
        # Ingest ran exactly once and recorded to disk + in-memory guard.
        assert ran["count"] == 1
        assert sentinel.exists()
        assert datetime.now(timezone.utc).date().isoformat() in _mod._ghsa_ingest_dates
        # Iteration 2 slept (waiting for tomorrow) then got cancelled.
        assert calls["sleep"] == 1

    @pytest.mark.asyncio
    async def test_skips_when_already_ingested_today(self, tmp_path, monkeypatch):
        """If already ingested today, the loop bumps to tomorrow and never ingests."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        today = datetime.now(timezone.utc).date().isoformat()
        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", {today})
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "last_ghsa.txt")

        called = {"n": 0}

        async def _fake_ingest(**kwargs):
            called["n"] += 1
            return {"new_cves": 0, "telegram_sent": False}

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _fake_ingest)

        async def _sleep_then_cancel(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep_then_cancel)

        # Future hour + already-ingested → exercises the `elif already` bump branch.
        future_hour = (datetime.now(timezone.utc).hour + 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=future_hour,
        )
        assert called["n"] == 0  # ingest never ran — dedup guard held

    @pytest.mark.asyncio
    async def test_ingest_error_is_swallowed_and_retries(self, tmp_path, monkeypatch):
        """A raised ingest error hits the retry branch (records date, sleeps 1h)."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "last_ghsa.txt")

        async def _boom(**kwargs):
            raise RuntimeError("github down")

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _boom)

        sleeps = {"n": 0}

        async def _sleep(_secs):
            sleeps["n"] += 1
            # The retry sleep (3600) is the only sleep reached here; cancel then.
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (datetime.now(timezone.utc).hour - 1) % 24
        # The 1-hour retry sleep is patched to raise CancelledError, which exits
        # the loop — that propagation is the expected end of the retry branch.
        with pytest.raises(asyncio.CancelledError):
            await _mod.ghsa_ingest_scheduler(
                bot_token="tok",
                owner_chat_id="12345",
                ingest_hour=past_hour,
            )
        # Error path recorded today so it won't hot-loop.
        assert datetime.now(timezone.utc).date().isoformat() in _mod._ghsa_ingest_dates
        assert sleeps["n"] == 1

    def test_already_ingested_helper_swallows_read_error(self, tmp_path, monkeypatch):
        """_already_ingested_ghsa_today returns False on a malformed sentinel."""
        import gateway.security.daily_cve_report as _mod

        sentinel = tmp_path / "last_ghsa.txt"
        sentinel.write_text("not-a-timestamp")
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", sentinel)
        assert _mod._already_ingested_ghsa_today(datetime.now(timezone.utc)) is False

    @pytest.mark.asyncio
    async def test_skips_ingest_when_marked_done_after_wake(self, tmp_path, monkeypatch):
        """After sleeping, if the day is now marked done, the loop skips ingest."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "last_ghsa.txt")

        called = {"ingest": 0, "sleep": 0}

        async def _fake_ingest(**kwargs):
            called["ingest"] += 1
            return {"new_cves": 0, "telegram_sent": False}

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _fake_ingest)

        # First sleep: mark today done (simulating a peer task), return normally.
        # After wake the post-sleep guard sees it and `continue`s; second sleep
        # cancels the loop.
        async def _sleep(_secs):
            called["sleep"] += 1
            if called["sleep"] == 1:
                _mod._ghsa_ingest_dates.add(datetime.now(timezone.utc).date().isoformat())
                return None
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        # Future hour → iteration 1 sleeps (waiting for the hour) then wakes.
        future_hour = (datetime.now(timezone.utc).hour + 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=future_hour,
        )
        assert called["ingest"] == 0  # post-wake guard skipped the ingest
        assert called["sleep"] == 2

    @pytest.mark.asyncio
    async def test_ingest_records_even_when_disk_write_fails(self, tmp_path, monkeypatch):
        """A disk-write failure on the sentinel is swallowed; in-memory guard set."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        # Point the sentinel at an un-writable location (parent is a file).
        broken_parent = tmp_path / "afile"
        broken_parent.write_text("x")
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", broken_parent / "sub" / "last.txt")

        async def _fake_ingest(**kwargs):
            return {"new_cves": 0, "telegram_sent": False}

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _fake_ingest)

        async def _sleep(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (datetime.now(timezone.utc).hour - 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )
        # Disk write failed but the in-memory dedup guard was still recorded.
        assert datetime.now(timezone.utc).date().isoformat() in _mod._ghsa_ingest_dates
