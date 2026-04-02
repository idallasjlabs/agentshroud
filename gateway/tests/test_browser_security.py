# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for browser_security module.
TDD: Written before implementation.
"""

from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from security.browser_security import (
    BrowserSecurityGuard,
    CredentialEntryBlocked,
    ThreatAssessment,
    ThreatLevel,
)


@pytest.fixture
def guard():
    return BrowserSecurityGuard()


class TestSocialEngineeringDetection:
    def test_fake_dialog_detected(self, guard):
        content = '<div class="popup">Your computer has a virus! Call 1-800-SCAM now!</div>'
        result = guard.analyze_content(content)
        assert result.threat_level >= ThreatLevel.HIGH

    def test_fake_windows_alert(self, guard):
        content = "Windows Defender Alert! Your PC is infected. Click here to fix."
        result = guard.analyze_content(content)
        assert result.threat_level >= ThreatLevel.MEDIUM

    def test_urgent_action_required(self, guard):
        content = "URGENT: Your account will be suspended! Verify your identity immediately."
        result = guard.analyze_content(content)
        assert result.threat_level >= ThreatLevel.MEDIUM

    def test_safe_content_passes(self, guard):
        content = "<h1>Welcome to our documentation</h1><p>Here are the API docs.</p>"
        result = guard.analyze_content(content)
        assert result.threat_level == ThreatLevel.NONE

    def test_tech_support_scam(self, guard):
        content = "Microsoft Support: Error #DW6VB36. Call immediately to prevent data loss."
        result = guard.analyze_content(content)
        assert result.threat_level >= ThreatLevel.HIGH

    def test_fake_captcha(self, guard):
        content = "Press Win+R, paste this command to verify you are human: powershell -e"
        result = guard.analyze_content(content)
        assert result.threat_level >= ThreatLevel.HIGH

    def test_multiple_threats_aggregated(self, guard):
        content = "VIRUS DETECTED! Your account suspended! Call 1-800-HELP now! Click to fix!"
        result = guard.analyze_content(content)
        assert len(result.threats) >= 2


class TestURLReputation:
    def test_known_phishing_pattern(self, guard):
        assert (
            guard.check_url_reputation("http://login-paypal.security-verify.com/signin")
            == ThreatLevel.HIGH
        )

    def test_suspicious_subdomain(self, guard):
        level = guard.check_url_reputation("http://google.com.evil-domain.xyz/login")
        assert level >= ThreatLevel.MEDIUM

    def test_ip_address_url(self, guard):
        level = guard.check_url_reputation("http://192.168.1.1:8080/admin/login")
        assert level >= ThreatLevel.LOW

    def test_legitimate_url(self, guard):
        assert guard.check_url_reputation("https://github.com/user/repo") == ThreatLevel.NONE

    def test_data_uri_blocked(self, guard):
        level = guard.check_url_reputation("data:text/html,<script>alert(1)</script>")
        assert level >= ThreatLevel.HIGH

    def test_homograph_attack(self, guard):
        level = guard.check_url_reputation("https://аpple.com/login")  # Cyrillic 'а'
        assert level >= ThreatLevel.HIGH

    def test_excessive_subdomains(self, guard):
        level = guard.check_url_reputation("https://secure.login.account.verify.example.com/auth")
        assert level >= ThreatLevel.LOW


class TestCredentialProtection:
    def test_https_allowed(self, guard):
        assert guard.can_enter_credentials("https://accounts.google.com/login")

    def test_http_blocked(self, guard):
        with pytest.raises(CredentialEntryBlocked):
            guard.can_enter_credentials("http://accounts.google.com/login")

    def test_suspicious_domain_blocked(self, guard):
        with pytest.raises(CredentialEntryBlocked):
            guard.can_enter_credentials("https://g00gle-login.com/auth")

    def test_localhost_allowed(self, guard):
        assert guard.can_enter_credentials("http://localhost:3000/login")

    def test_ip_blocked_for_credentials(self, guard):
        with pytest.raises(CredentialEntryBlocked):
            guard.can_enter_credentials("http://45.33.32.156/login")


class TestScreenshotAnalysis:
    def test_screenshot_hook_registered(self, guard):
        called = []
        guard.register_screenshot_hook(
            lambda img: called.append(True) or ThreatAssessment(ThreatLevel.NONE, [])
        )
        guard.analyze_screenshot(b"fake-image-data")
        assert len(called) == 1

    def test_no_hook_returns_none_threat(self, guard):
        result = guard.analyze_screenshot(b"fake-image-data")
        assert result.threat_level == ThreatLevel.NONE

    def test_hook_can_flag_threat(self, guard):
        guard.register_screenshot_hook(
            lambda img: ThreatAssessment(ThreatLevel.HIGH, ["fake dialog detected"])
        )
        result = guard.analyze_screenshot(b"fake-image-data")
        assert result.threat_level == ThreatLevel.HIGH
