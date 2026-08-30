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
        "cvss": {
            "vector_string": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
            "score": score,
        },
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

    def test_contains_total_count(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        # Summary always states the total number of new CVEs.
        assert "1 New OpenClaw CVE" in msg

    def test_contains_severity_icon(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve(sev="CRITICAL", score=9.9)])
        assert "🔴" in msg

    def test_alert_states_auto_registered_under_review(self):
        """The alert says CVEs are auto-registered under_review (honest, not 'add manually')."""
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "under_review" in msg
        assert "/soc/v1/agent-cves" in msg
        # No longer instructs a manual add-to-registry triage.
        assert "add to" not in msg

    def test_alert_titled_for_agent_label(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()], agent_label="Hermes Agent")
        assert "New Hermes Agent CVE" in msg

    def test_plural_header_for_multiple_cves(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve("CVE-2026-1"), self._cve("CVE-2026-2")])
        assert "2 New OpenClaw CVEs" in msg

    def test_singular_header_for_one_cve(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        msg = format_upstream_cve_alert([self._cve()])
        assert "1 New OpenClaw CVE " in msg  # no trailing 's'

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

    def test_summary_under_telegram_limit_for_100_cves(self):
        from gateway.security.daily_cve_report import (
            _TELEGRAM_MAX_CHARS,
            format_upstream_cve_alert,
        )

        # ~100 new GHSA advisories — the historical HTTP 400 scenario.
        cves = [
            self._cve(cve_id=f"GHSA-aaaa-bbbb-{i:04d}", sev="HIGH", score=7.5) for i in range(120)
        ]
        msg = format_upstream_cve_alert(cves)

        assert len(msg) <= _TELEGRAM_MAX_CHARS
        # Total count is preserved even though only a subset is listed inline.
        assert "120 New OpenClaw CVEs" in msg
        # "N more" indicator accounts for the folded remainder (120 - 15 = 105).
        assert "…and 105 more" in msg

    def test_no_more_indicator_when_under_item_limit(self):
        from gateway.security.daily_cve_report import format_upstream_cve_alert

        cves = [self._cve(cve_id=f"GHSA-x-{i}") for i in range(5)]
        msg = format_upstream_cve_alert(cves)
        assert "more" not in msg
        # All 5 ids are listed inline.
        for i in range(5):
            assert f"GHSA-x-{i}" in msg


# ── _send_telegram over-length guard ──────────────────────────────────────────


class TestSendTelegramTruncation:
    @pytest.mark.asyncio
    async def test_truncates_over_length_text(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        captured = {}

        class _FakeResp:
            def read(self):
                return json.dumps({"ok": True}).encode("utf-8")

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def _fake_urlopen(req, timeout=30):
            captured["body"] = json.loads(req.data.decode("utf-8"))
            return _FakeResp()

        monkeypatch.setattr(_mod.urllib.request, "urlopen", _fake_urlopen)

        # 10k chars — well over Telegram's 4096 limit.
        over_long = "A" * 10_000
        ok = await _mod._send_telegram("tok", "123", over_long, "https://api.telegram.org")

        assert ok is True
        sent_text = captured["body"]["text"]
        assert len(sent_text) <= _mod._TELEGRAM_MAX_CHARS
        assert sent_text.endswith("…(truncated)")

    @pytest.mark.asyncio
    async def test_short_text_passes_through_unchanged(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        captured = {}

        class _FakeResp:
            def read(self):
                return json.dumps({"ok": True}).encode("utf-8")

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def _fake_urlopen(req, timeout=30):
            captured["body"] = json.loads(req.data.decode("utf-8"))
            return _FakeResp()

        monkeypatch.setattr(_mod.urllib.request, "urlopen", _fake_urlopen)

        short = "hello world"
        await _mod._send_telegram("tok", "123", short, "https://api.telegram.org")
        assert captured["body"]["text"] == short
        assert "truncated" not in captured["body"]["text"]


# ── run_upstream_cve_check ────────────────────────────────────────────────────


class TestRunUpstreamCveCheck:
    @pytest.mark.asyncio
    async def test_sends_alert_when_new_cves_found(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda token=None, agent_id="openclaw": [
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

        monkeypatch.setattr(_mod, "check_upstream_cves", lambda token=None, agent_id="openclaw": [])
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
            lambda token=None, agent_id="openclaw": [
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


# ── run_upstream_cve_check per-agent + all-agents ─────────────────────────────


class TestPerAgentUpstreamChecks:
    @pytest.mark.asyncio
    async def test_check_scoped_to_agent_registry_and_repo(self, monkeypatch):
        """check_upstream_cves(agent_id=...) selects that agent's OWN repo + list."""
        import gateway.security.daily_cve_report as _mod

        captured = {}

        def _fake_check(github_token=None, agent_id="openclaw"):
            captured["agent_id"] = agent_id
            return []

        monkeypatch.setattr(_mod, "check_upstream_cves", _fake_check)
        result = await _mod.run_upstream_cve_check(
            bot_token="", owner_chat_id="", agent_id="hermes"
        )
        assert captured["agent_id"] == "hermes"
        assert result["agent_id"] == "hermes"

    @pytest.mark.asyncio
    async def test_hermes_zero_still_reports_when_always_report_zero(self, monkeypatch):
        """Owner wants to SEE a Hermes report even with 0 new advisories."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [],
        )
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        result = await _mod.run_upstream_cve_check(
            bot_token="tok",
            owner_chat_id="123",
            agent_id="hermes",
            always_report_zero=True,
        )
        assert result["new_cves"] == 0
        assert result["telegram_sent"] is True
        assert len(sent) == 1
        assert "0 new" in sent[0]
        assert "Hermes Agent" in sent[0]

    @pytest.mark.asyncio
    async def test_openclaw_zero_stays_silent(self, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [],
        )
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        result = await _mod.run_upstream_cve_check(
            bot_token="tok", owner_chat_id="123", agent_id="openclaw"
        )
        assert result["new_cves"] == 0
        assert sent == []  # silent when nothing new (default behavior)

    @pytest.mark.asyncio
    async def test_agent_label_falls_back_when_source_missing(self, monkeypatch):
        """If the per-agent source config is missing, the label falls back gracefully."""
        import gateway.security.daily_cve_report as _mod
        from gateway.security import agent_cve_registry as _reg

        def _raise(bot_id):
            raise KeyError(bot_id)

        monkeypatch.setattr(_reg, "get_agent_cve_source", _raise)
        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [],
        )
        result = await _mod.run_upstream_cve_check(
            bot_token="", owner_chat_id="", agent_id="mystery"
        )
        assert result["agent_id"] == "mystery"

    @pytest.mark.asyncio
    async def test_zero_report_send_failure_is_swallowed(self, monkeypatch):
        """A Telegram failure on the zero-report path never raises."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [],
        )

        async def _boom_send(*a, **kw):
            raise RuntimeError("telegram down")

        monkeypatch.setattr(_mod, "_send_telegram", _boom_send)
        result = await _mod.run_upstream_cve_check(
            bot_token="tok",
            owner_chat_id="123",
            agent_id="hermes",
            always_report_zero=True,
        )
        assert result["new_cves"] == 0
        assert result["telegram_sent"] is False

    @pytest.mark.asyncio
    async def test_alert_send_failure_is_swallowed(self, monkeypatch):
        """A Telegram failure on the new-CVE alert path never raises."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [
                {"id": "GHSA-x", "severity": "HIGH", "cvss": 7.5}
            ],
        )

        async def _boom_send(*a, **kw):
            raise RuntimeError("telegram down")

        monkeypatch.setattr(_mod, "_send_telegram", _boom_send)
        result = await _mod.run_upstream_cve_check(
            bot_token="tok", owner_chat_id="123", agent_id="openclaw"
        )
        assert result["new_cves"] == 1
        assert result["telegram_sent"] is False

    @pytest.mark.asyncio
    async def test_hermes_zero_stays_silent_via_all_agents(self, monkeypatch):
        """2026-08-04 fix: Hermes zero-CVE heartbeats confused the owner because
        they're sent through the shared bot token and display under OpenClaw's
        Telegram identity regardless of which agent they're about. Both agents
        now stay silent at zero, exercised through the real all-agents wiring
        (not a mocked run_upstream_cve_check) so a future re-add of "hermes" to
        _ALWAYS_REPORT_ZERO_AGENTS would fail this test."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [],
        )
        sent = []

        async def _fake_send(token, chat_id, text, base_url):
            sent.append(text)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        results = await _mod.run_upstream_cve_check_all_agents(bot_token="tok", owner_chat_id="123")
        by_agent = {r["agent_id"]: r for r in results}
        assert by_agent["hermes"]["telegram_sent"] is False
        assert by_agent["openclaw"]["telegram_sent"] is False
        assert sent == []

    @pytest.mark.asyncio
    async def test_all_agents_uses_per_agent_token_when_provided(self, monkeypatch):
        """2026-08-04: each wrapped agent's alert must go out via ITS OWN bot
        token (so it displays under its own Telegram identity), not always the
        default token — a real new CVE is needed so telegram actually sends."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [
                {"id": f"GHSA-{agent_id}", "severity": "HIGH", "cvss": 7.5}
            ],
        )
        used_tokens = {}

        async def _fake_send(token, chat_id, text, base_url):
            used_tokens[text] = token
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        results = await _mod.run_upstream_cve_check_all_agents(
            bot_token="default-tok",
            owner_chat_id="123",
            bot_tokens={"hermes": "hermes-tok"},
        )
        by_agent = {r["agent_id"]: r for r in results}
        assert by_agent["openclaw"]["telegram_sent"] is True
        assert by_agent["hermes"]["telegram_sent"] is True
        tokens_seen = set(used_tokens.values())
        assert tokens_seen == {"default-tok", "hermes-tok"}

    @pytest.mark.asyncio
    async def test_all_agents_omitting_bot_tokens_preserves_default_behavior(self, monkeypatch):
        """Backward compatibility: no bot_tokens arg means every agent still
        gets the single shared bot_token, exactly like before this param existed."""
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(
            _mod,
            "check_upstream_cves",
            lambda github_token=None, agent_id="openclaw": [
                {"id": f"GHSA-{agent_id}", "severity": "HIGH", "cvss": 7.5}
            ],
        )
        used_tokens = []

        async def _fake_send(token, chat_id, text, base_url):
            used_tokens.append(token)
            return True

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        results = await _mod.run_upstream_cve_check_all_agents(
            bot_token="only-tok", owner_chat_id="123"
        )
        # 2 wrapped agents + 8 security-tool sources (added 2026-08-23).
        assert len(results) == 10
        assert set(used_tokens) == {"only-tok"}

    @pytest.mark.asyncio
    async def test_all_agents_runs_each_independently_and_isolates_failure(self, monkeypatch):
        """OpenClaw and Hermes are processed on fully separate paths; one failing
        never blocks the other."""
        import gateway.security.daily_cve_report as _mod

        seen = []

        async def _fake_run(**kwargs):
            aid = kwargs["agent_id"]
            seen.append(aid)
            if aid == "openclaw":
                raise RuntimeError("openclaw feed down")
            return {
                "agent_id": aid,
                "new_cves": 0,
                "cve_ids": [],
                "telegram_sent": True,
            }

        monkeypatch.setattr(_mod, "run_upstream_cve_check", _fake_run)
        results = await _mod.run_upstream_cve_check_all_agents(bot_token="tok", owner_chat_id="123")
        # Both agents attempted, in registered order.
        assert "openclaw" in seen and "hermes" in seen
        by_agent = {r["agent_id"]: r for r in results}
        # OpenClaw failed → isolated error dict; Hermes still produced its result.
        assert "error" in by_agent["openclaw"]
        assert by_agent["hermes"]["telegram_sent"] is True


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
    @pytest.fixture(autouse=True)
    def _no_docker(self, monkeypatch):
        """Pin _running_image to the docker-unavailable fallback path so these
        tests assert the configured-tag behavior deterministically, whether or
        not a real docker daemon (with real running containers) is present on
        the host running the suite. Running-image resolution has its own
        tests below."""
        from gateway.security import daily_cve_report as _mod

        monkeypatch.setattr(_mod, "_running_image", lambda _name: None)

    def test_always_includes_gateway_image(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)
        targets = _build_image_targets()
        assert "agentshroud-gateway:latest" in targets

    def test_env_var_adds_extra_targets(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv(
            "AGENTSHROUD_TRIVY_IMAGES",
            "agentshroud-openclaw:latest,agentshroud/hermes:latest",
        )
        targets = _build_image_targets()
        assert "agentshroud-openclaw:latest" in targets
        assert "agentshroud/hermes:latest" in targets

    def test_env_var_empty_string_ignored(self, monkeypatch):
        """Empty AGENTSHROUD_TRIVY_IMAGES adds no extra entries beyond
        gateway + the real per-bot images (always included regardless of
        this env var — see test_always_includes_every_configured_bot_image)."""
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv("AGENTSHROUD_TRIVY_IMAGES", "")
        targets = _build_image_targets()
        assert targets == [
            "agentshroud-gateway:latest",
            "agentshroud-openclaw:latest",
            "agentshroud/hermes:latest",
        ]

    def test_always_includes_every_configured_bot_image(self, monkeypatch):
        """Regression guard: AGENTSHROUD_TRIVY_IMAGES used to be the ONLY
        source of bot images and was hardcoded to just Hermes's, silently
        omitting OpenClaw from every CVE report ("why is openclaw reporting
        hermes?"). Bot images must now come from the real bots: registry,
        unconditionally — not an env var that can omit a bot entirely."""
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)
        targets = _build_image_targets()
        assert "agentshroud-openclaw:latest" in targets
        assert "agentshroud/hermes:latest" in targets

    def test_deduplication(self, monkeypatch):
        from gateway.security.daily_cve_report import _build_image_targets

        monkeypatch.setenv(
            "AGENTSHROUD_TRIVY_IMAGES",
            "agentshroud-gateway:latest,agentshroud-gateway:latest",
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


# ── _running_image / running-image preference ─────────────────────────────────


class TestRunningImageResolution:
    def test_prefers_running_image_over_configured_tag(self, monkeypatch):
        """Regression guard (2026-08-30): the report scanned :latest tags
        while deploys ran version tags — openclaw's report described a
        17-day-old image that wasn't running. The RUNNING image must win."""
        from gateway.security import daily_cve_report as _mod

        running = {
            "agentshroud-gateway": "agentshroud-gateway:1.6.0",
            "agentshroud-openclaw": "agentshroud-openclaw:1.6.0",
        }
        monkeypatch.setattr(_mod, "_running_image", lambda name: running.get(name))
        monkeypatch.delenv("AGENTSHROUD_TRIVY_IMAGES", raising=False)
        targets = _mod._build_image_targets()
        assert "agentshroud-gateway:1.6.0" in targets
        assert "agentshroud-gateway:latest" not in targets
        assert "agentshroud-openclaw:1.6.0" in targets
        assert "agentshroud-openclaw:latest" not in targets

    def test_running_image_parses_docker_inspect_stdout(self, monkeypatch):
        from gateway.security import daily_cve_report as _mod

        class _Result:
            returncode = 0
            stdout = "agentshroud-gateway:1.6.0\n"

        monkeypatch.setattr(_mod.subprocess, "run", lambda *a, **kw: _Result())
        assert _mod._running_image("agentshroud-gateway") == "agentshroud-gateway:1.6.0"

    def test_running_image_returns_none_on_inspect_failure(self, monkeypatch):
        from gateway.security import daily_cve_report as _mod

        class _Result:
            returncode = 1
            stdout = ""

        monkeypatch.setattr(_mod.subprocess, "run", lambda *a, **kw: _Result())
        assert _mod._running_image("nope") is None

    def test_running_image_returns_none_when_docker_missing(self, monkeypatch):
        from gateway.security import daily_cve_report as _mod

        def _raise(*a, **kw):
            raise FileNotFoundError("docker")

        monkeypatch.setattr(_mod.subprocess, "run", _raise)
        assert _mod._running_image("agentshroud-gateway") is None


# ── run_trivy_scan skip_dirs ──────────────────────────────────────────────────


class TestTrivySkipDirs:
    def test_skip_dirs_added_to_command(self, monkeypatch):
        from gateway.security import trivy_report as _tr

        captured = {}

        class _Result:
            returncode = 0
            stdout = '{"Results": []}'
            stderr = ""

        def _fake_run(cmd, **kw):
            captured["cmd"] = cmd
            return _Result()

        monkeypatch.setattr(_tr.subprocess, "run", _fake_run)
        _tr.run_trivy_scan(target="/", skip_dirs=["/var/log/security"])
        cmd = captured["cmd"]
        assert "--skip-dirs" in cmd
        assert cmd[cmd.index("--skip-dirs") + 1] == "/var/log/security"
        assert cmd[-1] == "/"

    def test_no_skip_dirs_flag_when_omitted(self, monkeypatch):
        from gateway.security import trivy_report as _tr

        captured = {}

        class _Result:
            returncode = 0
            stdout = '{"Results": []}'
            stderr = ""

        def _fake_run(cmd, **kw):
            captured["cmd"] = cmd
            return _Result()

        monkeypatch.setattr(_tr.subprocess, "run", _fake_run)
        _tr.run_trivy_scan(target="/")
        assert "--skip-dirs" not in captured["cmd"]

    @pytest.mark.asyncio
    async def test_daily_fs_scan_skips_security_log_tree(self, tmp_path, monkeypatch):
        """The daily fs scan of / must exclude /var/log/security (trivy's own
        cache + reports) — scanning its own 1.3GB cache blew the 600s trivy
        timeout under load and surfaced as intermittent empty_output."""
        import gateway.security.daily_cve_report as _mod

        fs_calls = []

        def _fake_trivy_scan(target="/", scan_type="fs", **kwargs):
            if scan_type == "fs":
                fs_calls.append(kwargs.get("skip_dirs"))
            return _make_report(critical=0, high=0, medium=0, low=0, total=0)

        async def _fake_send(*a, **kw):
            return True

        monkeypatch.setattr(_mod, "run_trivy_scan", _fake_trivy_scan)
        monkeypatch.setattr(_mod, "save_report", lambda *a, **kw: str(tmp_path / "r.json"))
        monkeypatch.setattr(_mod, "_build_image_targets", lambda: [])
        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)
        await _mod.run_and_send_cve_report("tok", "chat")
        assert fs_calls and "/var/log/security" in (fs_calls[0] or [])


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

        # Freeze the module's clock to a single fixed mid-day instant so the whole
        # test computes from ONE deterministic "now" — a real wall-clock now()
        # made this test flaky at UTC hour 0: `(0 - 1) % 24` wraps to 23, which
        # replace(hour=23) on TODAY's date lands ~22h in the FUTURE, not the past,
        # flipping the scheduler onto its "sleep and wait" branch instead of
        # triggering immediately (see the sibling fix a few tests down for the
        # mirror-image hour-23 case).
        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
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
        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )
        # Ingest ran once per registered agent (OpenClaw + Hermes) in iteration 1,
        # then recorded to disk + in-memory guard. Per-agent invocation is the
        # coordinator-required parallel-per-agent design.
        from gateway.security.agent_cve_registry import list_cve_agents

        assert ran["count"] == len(list_cve_agents())
        assert sentinel.exists()
        assert _FROZEN.date().isoformat() in _mod._ghsa_ingest_dates
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
    async def test_per_agent_check_error_is_isolated_not_fatal(self, tmp_path, monkeypatch):
        """A raised per-agent check error is ISOLATED — the ingest still completes.

        Per-agent isolation (coordinator requirement): one agent's fetch failure
        must never block another agent or crash the scheduler. Both agents log an
        error, the ingest records the date, and the loop proceeds to sleep until
        tomorrow (cancelled here). No exception escapes the per-agent boundary.
        """
        import asyncio

        import gateway.security.daily_cve_report as _mod

        # Freeze the clock — see test_runs_ingest_records_then_skips_next_iteration
        # for why a live datetime.now() makes the past_hour computation flaky at
        # UTC hour 0.
        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "last_ghsa.txt")

        async def _boom(**kwargs):
            raise RuntimeError("github down")

        # Patch the per-agent entrypoint: every agent's check raises.
        monkeypatch.setattr(_mod, "run_upstream_cve_check", _boom)

        sleeps = {"n": 0}

        async def _sleep(_secs):
            sleeps["n"] += 1
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        # No exception escapes: the loop runs the ingest (errors isolated), records
        # the date, then sleeps until tomorrow — the sleep is cancelled to exit.
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )
        # Ingest completed (date recorded); the sleep-to-tomorrow was reached.
        assert _FROZEN.date().isoformat() in _mod._ghsa_ingest_dates
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

        # Freeze the module's clock to a single fixed mid-day instant so the whole
        # test computes from ONE deterministic "now". A real wall-clock `now()`
        # made this test flaky in two ways: (1) at UTC hour 23 the `future_hour`
        # below wrapped to 0, which flipped the scheduler onto its "target in the
        # past" branch and skipped the sleep; (2) if UTC midnight crossed between
        # the mark-done `now()` and the scheduler's post-wake guard `now()`, the
        # two dates disagreed and the guard let ingest run. A frozen mid-day clock
        # eliminates both races.
        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
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
                _mod._ghsa_ingest_dates.add(_FROZEN.date().isoformat())
                return None
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        # Future hour → iteration 1 sleeps (waiting for the hour) then wakes.
        future_hour = (_FROZEN.hour + 1) % 24
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

        # Freeze the clock — see test_runs_ingest_records_then_skips_next_iteration
        # for why a live datetime.now() makes the past_hour computation flaky at
        # UTC hour 0.
        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
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

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )
        # Disk write failed but the in-memory dedup guard was still recorded.
        assert _FROZEN.date().isoformat() in _mod._ghsa_ingest_dates


# ── Regression: failed delivery must not be marked "sent" ──────────────────
#
# Previously all three schedulers recorded a day as done unconditionally,
# even when the Telegram send failed. That silently dropped that day's
# report/alert forever with no retry and no signal. These tests lock in the
# fix: a failed send is retried (bounded) before the day is ever marked done.


class TestRunAndSendCveReportFailedDeliveryNotMarkedSent:
    @pytest.mark.asyncio
    async def test_failed_send_does_not_write_stamp_or_mark_sent_date(self, tmp_path, monkeypatch):
        import gateway.security.daily_cve_report as _mod

        monkeypatch.setattr(_mod, "run_trivy_scan", lambda **_: _make_report())
        monkeypatch.setattr(_mod, "save_report", lambda r: None)
        sentinel = tmp_path / "last.txt"
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", sentinel)
        monkeypatch.setattr(_mod, "_sent_dates", set())

        async def _fake_send(token, chat_id, text, base_url):
            return False

        monkeypatch.setattr(_mod, "_send_telegram", _fake_send)

        result = await run_and_send_cve_report(bot_token="tok", owner_chat_id="12345")

        assert result["telegram_sent"] is False
        assert not sentinel.exists()
        assert _mod._sent_dates == set()


class TestCveReportSchedulerRetry:
    @pytest.mark.asyncio
    async def test_retries_on_failed_send_before_giving_up(self, tmp_path, monkeypatch):
        """A failed send retries (bounded) within the same day, not next-day."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_sent_dates", set())
        monkeypatch.setattr(_mod, "_report_send_failures", {})
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")
        monkeypatch.setattr(_mod, "_MAX_SEND_RETRIES_PER_DAY", 3)

        ran = {"count": 0}

        async def _fake_run(**kwargs):
            ran["count"] += 1
            return {"telegram_sent": False, "findings": 5}

        monkeypatch.setattr(_mod, "run_and_send_cve_report", _fake_run)

        sleeps = {"count": 0}

        async def _sleep(_secs):
            sleeps["count"] += 1
            if sleeps["count"] >= 3:
                raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.cve_report_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            report_hour=past_hour,
        )

        # Retried up to the cap (3 attempts), backing off between each — only
        # marked "sent" once the cap was hit, never on the first failure.
        assert ran["count"] == 3
        assert _mod._report_send_failures[_FROZEN.date().isoformat()] == 3
        assert _FROZEN.date().isoformat() in _mod._sent_dates

    @pytest.mark.asyncio
    async def test_gives_up_and_marks_sent_after_max_retries(self, tmp_path, monkeypatch):
        """After the retry cap, the day IS marked done so the loop moves on."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_sent_dates", set())
        monkeypatch.setattr(_mod, "_report_send_failures", {})
        sentinel = tmp_path / "last.txt"
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", sentinel)
        monkeypatch.setattr(_mod, "_MAX_SEND_RETRIES_PER_DAY", 2)

        ran = {"count": 0}

        async def _fake_run(**kwargs):
            ran["count"] += 1
            return {"telegram_sent": False, "findings": 5}

        monkeypatch.setattr(_mod, "run_and_send_cve_report", _fake_run)

        # Call 1 = retry backoff after attempt 1 (must NOT cut the loop short
        # here, or attempt 2 — the one that hits the cap — never runs). Call 2
        # = the post-give-up "wait for tomorrow" sleep; raise there to end
        # the test cleanly once give-up has already happened.
        sleeps = {"count": 0}

        async def _sleep(_secs):
            sleeps["count"] += 1
            if sleeps["count"] >= 2:
                raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.cve_report_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            report_hour=past_hour,
        )

        # Second attempt hit the cap (2) — gave up and marked today done so
        # the scheduler doesn't tight-loop forever on a persistent failure.
        assert ran["count"] == 2
        assert _FROZEN.date().isoformat() in _mod._sent_dates
        assert sentinel.exists()

    @pytest.mark.asyncio
    async def test_successful_send_marks_sent_immediately_no_retry(self, tmp_path, monkeypatch):
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_sent_dates", set())
        monkeypatch.setattr(_mod, "_report_send_failures", {})
        monkeypatch.setattr(_mod, "_LAST_REPORT_PATH", tmp_path / "last.txt")

        ran = {"count": 0}

        async def _fake_run(**kwargs):
            ran["count"] += 1
            # Mirror what the real function does on success: mark the day sent
            # using the module's (frozen) clock, matching what the scheduler's
            # own dedup check reads on its next iteration.
            _mod._sent_dates.add(_mod.datetime.now(timezone.utc).date().isoformat())
            return {"telegram_sent": True, "findings": 5}

        monkeypatch.setattr(_mod, "run_and_send_cve_report", _fake_run)

        async def _sleep(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.cve_report_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            report_hour=past_hour,
        )

        # Success on the first try — no retry-failure bookkeeping triggered,
        # and the loop only ran once (the "wait for tomorrow" sleep raised).
        assert ran["count"] == 1
        assert _mod._report_send_failures.get(_FROZEN.date().isoformat(), 0) == 0


class TestUpstreamCveCheckSchedulerRetry:
    @pytest.mark.asyncio
    async def test_undelivered_new_cves_retries_not_marked_checked(self, tmp_path, monkeypatch):
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_upstream_check_dates", set())
        monkeypatch.setattr(_mod, "_upstream_check_failures", {})
        monkeypatch.setattr(_mod, "_LAST_UPSTREAM_CHECK_PATH", tmp_path / "last.txt")
        monkeypatch.setattr(_mod, "_MAX_SEND_RETRIES_PER_DAY", 2)

        ran = {"count": 0}

        async def _fake_all_agents(**kwargs):
            ran["count"] += 1
            # Found a new CVE but the alert failed to deliver.
            return [{"agent_id": "openclaw", "new_cves": 1, "telegram_sent": False}]

        monkeypatch.setattr(_mod, "run_upstream_cve_check_all_agents", _fake_all_agents)

        async def _sleep(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.upstream_cve_check_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            report_hour=past_hour,
        )

        # First attempt failed to deliver a real new-CVE alert — must retry,
        # not be silently marked "checked" for today.
        assert ran["count"] == 1
        assert _FROZEN.date().isoformat() not in _mod._upstream_check_dates
        assert not (tmp_path / "last.txt").exists()

    @pytest.mark.asyncio
    async def test_zero_new_cves_marks_checked_immediately(self, tmp_path, monkeypatch):
        """Nothing to deliver is a legitimate 'done', not a failure to retry."""
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_upstream_check_dates", set())
        monkeypatch.setattr(_mod, "_upstream_check_failures", {})
        sentinel = tmp_path / "last.txt"
        monkeypatch.setattr(_mod, "_LAST_UPSTREAM_CHECK_PATH", sentinel)

        async def _fake_all_agents(**kwargs):
            return [{"agent_id": "openclaw", "new_cves": 0, "telegram_sent": False}]

        monkeypatch.setattr(_mod, "run_upstream_cve_check_all_agents", _fake_all_agents)

        async def _sleep(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.upstream_cve_check_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            report_hour=past_hour,
        )

        assert _FROZEN.date().isoformat() in _mod._upstream_check_dates
        assert sentinel.exists()


class TestGhsaIngestSchedulerRetry:
    @pytest.mark.asyncio
    async def test_undelivered_new_advisory_retries_not_marked_ingested(
        self, tmp_path, monkeypatch
    ):
        import asyncio

        import gateway.security.daily_cve_report as _mod

        _FROZEN = datetime(2026, 7, 14, 12, 0, 0, tzinfo=timezone.utc)

        class _FrozenDateTime(datetime):
            @classmethod
            def now(cls, tz=None):
                return _FROZEN if tz is None else _FROZEN.astimezone(tz)

        monkeypatch.setattr(_mod, "datetime", _FrozenDateTime)
        monkeypatch.setattr(_mod, "_ghsa_ingest_dates", set())
        monkeypatch.setattr(_mod, "_ghsa_ingest_failures", {})
        monkeypatch.setattr(_mod, "_LAST_GHSA_INGEST_PATH", tmp_path / "last.txt")
        monkeypatch.setattr(_mod, "_MAX_SEND_RETRIES_PER_DAY", 2)

        ran = {"count": 0}

        async def _fake_all_agents(**kwargs):
            ran["count"] += 1
            return [{"agent_id": "hermes", "new_cves": 1, "telegram_sent": False}]

        monkeypatch.setattr(_mod, "run_upstream_cve_check_all_agents", _fake_all_agents)

        async def _sleep(_secs):
            raise asyncio.CancelledError()

        monkeypatch.setattr(_mod.asyncio, "sleep", _sleep)

        past_hour = (_FROZEN.hour - 1) % 24
        await _mod.ghsa_ingest_scheduler(
            bot_token="tok",
            owner_chat_id="12345",
            ingest_hour=past_hour,
        )

        assert ran["count"] == 1
        assert _FROZEN.date().isoformat() not in _mod._ghsa_ingest_dates
        assert not (tmp_path / "last.txt").exists()
