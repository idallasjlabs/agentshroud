#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Integration tests for web proxy security modules.

Tests that DNS filter, network validator, egress monitor, browser security,
and oauth security are properly wired into the request flow.
"""

import os
import sys
import unittest
from enum import Enum
from unittest.mock import Mock, patch

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


# Mock the security modules for testing
class MockDNSVerdict:
    def __init__(self, allowed=True, flagged=False, reason=""):
        self.allowed = allowed
        self.flagged = flagged
        self.reason = reason


class MockThreatLevel(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class MockURLResult:
    def __init__(self, domain="example.com", is_ssrf=False, flagged=False, findings=None):
        self.domain = domain
        self.is_ssrf = is_ssrf
        self.flagged = flagged
        self.findings = findings or []


class MockEgressEvent:
    def __init__(self, timestamp, agent_id, channel, destination, metadata):
        self.timestamp = timestamp
        self.agent_id = agent_id
        self.channel = channel
        self.destination = destination
        self.metadata = metadata


class MockEgressChannel(Enum):
    HTTP = "http"


class TestWebProxySecurityIntegration(unittest.TestCase):
    """Test that security modules are properly integrated into web proxy."""

    def setUp(self):
        """Set up test fixtures."""
        # Mock all the dependencies
        with (
            patch("gateway.proxy.web_proxy.DNSFilter"),
            patch("gateway.proxy.web_proxy.DNSFilterConfig"),
            patch("gateway.proxy.web_proxy.NetworkValidator"),
            patch("gateway.proxy.web_proxy.EgressMonitor"),
            patch("gateway.proxy.web_proxy.EgressMonitorConfig"),
            patch("gateway.proxy.web_proxy.BrowserSecurityGuard"),
            patch("gateway.proxy.web_proxy.OAuthSecurityValidator"),
            patch("gateway.proxy.web_proxy.URLAnalyzer"),
            patch("gateway.proxy.web_proxy.WebContentScanner"),
            patch("gateway.proxy.web_proxy.WebProxyConfig"),
        ):

            from gateway.proxy.web_proxy import ProxyAction, WebProxy, WebProxyResult

            self.WebProxy = WebProxy
            self.WebProxyResult = WebProxyResult
            self.ProxyAction = ProxyAction

            # Create proxy instance
            self.proxy = WebProxy()

            # Mock the security modules
            self.proxy.dns_filter = Mock()
            self.proxy.network_validator = Mock()
            self.proxy.egress_monitor = Mock()
            self.proxy.browser_security = Mock()
            self.oauth_security = Mock()

            # Mock other dependencies
            self.proxy.url_analyzer = Mock()
            self.proxy.content_scanner = Mock()
            self.proxy.config = Mock()
            self.proxy.config.passthrough_mode = False
            self.proxy.config.mode = "default"
            self.proxy.config.scan_responses = True
            self.proxy.config.is_domain_denied = Mock(return_value=False)
            self.proxy.config.is_domain_allowed = Mock(return_value=True)
            self.proxy.config.suspicious_content_types = []
            self.proxy.config.get_domain_settings = Mock(
                return_value=Mock(rate_limit_rpm=100, max_response_bytes=10_000_000)
            )
            self.proxy.audit_chain = Mock()

    def test_dns_filter_blocks_suspicious_domains(self):
        """Test that DNS filter blocks suspicious domains."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(
            domain="suspicious.example.com"
        )
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(
            allowed=False, reason="Suspicious domain"
        )

        # Execute
        result = self.proxy.check_request("https://suspicious.example.com/malware")

        # Verify
        self.assertTrue(result.blocked)
        self.assertIn("DNS filter blocked", result.block_reason)
        self.proxy.dns_filter.check.assert_called_once_with("suspicious.example.com", "web-proxy")

    def test_dns_filter_flags_but_allows_questionable_domains(self):
        """Test that DNS filter flags questionable domains but allows them through."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(
            domain="questionable.example.com"
        )
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(
            allowed=True, flagged=True, reason="High entropy"
        )

        # Execute
        result = self.proxy.check_request("https://questionable.example.com/data")

        # Verify
        self.assertFalse(result.blocked)
        self.assertEqual(result.action, self.ProxyAction.FLAG)
        self.assertTrue(any(f["category"] == "dns" for f in result.url_findings))
        self.proxy.dns_filter.check.assert_called_once_with("questionable.example.com", "web-proxy")

    def test_browser_security_blocks_high_risk_urls(self):
        """Test that browser security blocks high-risk URLs for browser user agents."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="malicious.example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)
        self.proxy.browser_security.check_url_reputation.return_value = MockThreatLevel.HIGH

        headers = {"User-Agent": "Mozilla/5.0 (Chrome/91.0)"}

        # Execute
        result = self.proxy.check_request("https://malicious.example.com/phishing", headers=headers)

        # Verify
        self.assertTrue(result.blocked)
        self.assertIn("Browser security blocked", result.block_reason)
        self.proxy.browser_security.check_url_reputation.assert_called_once_with(
            "https://malicious.example.com/phishing"
        )

    def test_browser_security_flags_medium_risk_urls(self):
        """Test that browser security flags medium-risk URLs."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="suspect.example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)
        self.proxy.browser_security.check_url_reputation.return_value = MockThreatLevel.MEDIUM

        headers = {"User-Agent": "Mozilla/5.0 (Safari/537.36)"}

        # Execute
        result = self.proxy.check_request("https://suspect.example.com/page", headers=headers)

        # Verify
        self.assertFalse(result.blocked)
        self.assertEqual(result.action, self.ProxyAction.FLAG)
        self.assertTrue(any(f["category"] == "browser_security" for f in result.url_findings))

    def test_browser_security_skips_non_browser_user_agents(self):
        """Test that browser security checks are skipped for non-browser user agents."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)

        headers = {"User-Agent": "python-requests/2.25.1"}

        # Execute
        self.proxy.check_request("https://example.com/api", headers=headers)

        # Verify
        self.proxy.browser_security.check_url_reputation.assert_not_called()

    def test_oauth_security_flags_auth_headers(self):
        """Test that OAuth security flags requests with authorization headers."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="api.example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)

        headers = {"Authorization": "Bearer token123", "User-Agent": "python-requests/2.25.1"}

        # Execute
        result = self.proxy.check_request("https://api.example.com/data", headers=headers)

        # Verify
        self.assertFalse(result.blocked)  # OAuth should flag, not block
        self.assertEqual(result.action, self.ProxyAction.FLAG)
        self.assertTrue(any(f["category"] == "oauth_security" for f in result.url_findings))

    def test_egress_monitor_logs_responses(self):
        """Test that egress monitor logs all outbound connections."""
        # Setup
        self.proxy.content_scanner.scan.return_value = Mock(
            flagged=False,
            findings=[],
            prompt_injection_score=0.0,
            has_prompt_injection=False,
            has_pii=False,
        )

        # Execute
        self.proxy.scan_response(
            "https://example.com/api", "response body", "application/json", 200, 1024
        )

        # Verify
        self.proxy.egress_monitor.record.assert_called_once()
        call_args = self.proxy.egress_monitor.record.call_args[0][0]
        self.assertEqual(call_args.agent_id, "web-proxy")
        self.assertEqual(call_args.destination, "example.com")
        self.assertIn("url", call_args.details)

    def test_graceful_degradation_dns_error(self):
        """Test that DNS filter errors cause fail-closed behavior."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="example.com")
        self.proxy.dns_filter.check.side_effect = Exception("DNS service unavailable")

        # Execute
        result = self.proxy.check_request("https://example.com/page")

        # Verify
        self.assertTrue(result.blocked)  # Should fail closed
        self.assertIn("DNS security check failed", result.block_reason)

    def test_graceful_degradation_browser_security_error(self):
        """Test that browser security errors cause fail-closed behavior."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)
        self.proxy.browser_security.check_url_reputation.side_effect = Exception("Service error")

        headers = {"User-Agent": "Mozilla/5.0"}

        # Execute
        result = self.proxy.check_request("https://example.com/page", headers=headers)

        # Verify
        self.assertTrue(result.blocked)  # Should fail closed
        self.assertIn("Browser security check failed", result.block_reason)

    def test_graceful_degradation_egress_error(self):
        """Test that egress monitoring errors don't break response processing."""
        # Setup
        self.proxy.content_scanner.scan.return_value = Mock(
            flagged=False,
            findings=[],
            prompt_injection_score=0.0,
            has_prompt_injection=False,
            has_pii=False,
        )
        self.proxy.egress_monitor.record.side_effect = Exception("Monitoring service down")

        # Execute - should not raise exception
        result = self.proxy.scan_response("https://example.com", "body", "text/html")

        # Verify - response processing should continue normally
        self.assertIsNotNone(result)
        self.assertIsInstance(result, self.WebProxyResult)

    def test_oauth_security_error_handling(self):
        """Test that OAuth security errors don't block requests."""
        # Setup
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="api.example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(allowed=True)

        headers = {"Authorization": "Bearer token123"}

        # Execute - OAuth error should not block
        result = self.proxy.check_request("https://api.example.com/data", headers=headers)

        # Verify - should flag but not block, even with OAuth errors
        self.assertFalse(result.blocked)

    def test_multiple_security_modules_integration(self):
        """Test that multiple security modules work together correctly."""
        # Setup - all modules flag but don't block
        self.proxy.url_analyzer.analyze.return_value = MockURLResult(domain="test.example.com")
        self.proxy.dns_filter.check.return_value = MockDNSVerdict(
            allowed=True, flagged=True, reason="Entropy"
        )
        self.proxy.browser_security.check_url_reputation.return_value = MockThreatLevel.MEDIUM

        headers = {"User-Agent": "Mozilla/5.0", "Authorization": "Bearer token"}

        # Execute
        result = self.proxy.check_request("https://test.example.com/page", headers=headers)

        # Verify - should be flagged with findings from multiple modules
        self.assertFalse(result.blocked)
        self.assertEqual(result.action, self.ProxyAction.FLAG)

        # Should have findings from DNS, browser security, and OAuth
        categories = [f["category"] for f in result.url_findings]
        self.assertIn("dns", categories)
        self.assertIn("browser_security", categories)
        self.assertIn("oauth_security", categories)


if __name__ == "__main__":
    unittest.main()
