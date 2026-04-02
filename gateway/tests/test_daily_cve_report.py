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
