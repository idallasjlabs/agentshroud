# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway.security.daily_cve_report."""

from __future__ import annotations

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.security.daily_cve_report import (
    _LAST_REPORT_PATH,
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
        severity_lines = [l for l in lines if "🔴" in l or "🟠" in l]
        assert not any("CRITICAL" in l for l in severity_lines)
        assert not any("HIGH" in l for l in severity_lines)


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


def _make_github_advisory(cve_id: str, severity: str = "high", score: float = 7.5) -> dict:
    """Build a minimal GitHub Security Advisory payload."""
    return {
        "ghsa_id": f"GHSA-xxxx-xxxx-{cve_id[-4:]}",
        "cve_id": cve_id,
        "summary": f"Test vulnerability {cve_id}",
        "description": "Test description.",
        "severity": severity,
        "cvss": {"vector_string": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "score": score},
        "published_at": "2026-04-10T00:00:00Z",
        "html_url": f"https://github.com/openclaw/openclaw/security/advisories/GHSA-xxxx",
    }


class TestCheckUpstreamCves:
    def _patch_urllib(self, monkeypatch, advisories: list) -> None:
        """Stub urllib.request.urlopen to return a list of advisories."""
        import io
        import urllib.request as _ur

        import gateway.security.daily_cve_report as _mod

        fake_resp = MagicMock()
        fake_resp.__enter__ = lambda s: s
        fake_resp.__exit__ = MagicMock(return_value=False)
        fake_resp.read.return_value = json.dumps(advisories).encode()
        monkeypatch.setattr(_ur, "urlopen", lambda *a, **kw: fake_resp)

    def test_returns_new_cve_not_in_registry(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        new_id = "CVE-2026-99999"
        self._patch_urllib(monkeypatch, [_make_github_advisory(new_id)])
        result = check_upstream_cves()
        assert len(result) == 1
        assert result[0]["id"] == new_id
        assert result[0]["severity"] == "HIGH"
        assert result[0]["cvss"] == 7.5

    def test_skips_advisory_without_cve_id(self, monkeypatch):
        from gateway.security.daily_cve_report import check_upstream_cves

        adv = _make_github_advisory("CVE-2026-99998")
        adv["cve_id"] = None  # no CVE assigned yet
        self._patch_urllib(monkeypatch, [adv])
        assert check_upstream_cves() == []

    def test_skips_cve_already_in_registry(self, monkeypatch):
        from gateway.security import daily_cve_report as _mod
        from gateway.security.daily_cve_report import check_upstream_cves

        # CVE-2026-22171 is in AGENT_CVE_REGISTRY
        self._patch_urllib(monkeypatch, [_make_github_advisory("CVE-2026-22171")])
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
        orig_urlopen = _ur.urlopen

        import io

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
