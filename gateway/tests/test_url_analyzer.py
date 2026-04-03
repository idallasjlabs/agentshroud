# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for URL Analyzer — SSRF detection, PII in URLs, data exfiltration."""

from __future__ import annotations

import base64

import pytest

from gateway.proxy.url_analyzer import URLAnalyzer, URLVerdict, _looks_like_base64


@pytest.fixture
def analyzer():
    return URLAnalyzer(resolve_dns=False)


class TestSSRFDetection:
    """SSRF blocking — the one hard block."""

    def test_localhost_blocked(self, analyzer):
        r = analyzer.analyze("http://localhost/admin")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_127_0_0_1_blocked(self, analyzer):
        r = analyzer.analyze("http://127.0.0.1/secret")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_127_x_blocked(self, analyzer):
        r = analyzer.analyze("http://127.0.0.2:8080/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ipv6_loopback_blocked(self, analyzer):
        r = analyzer.analyze("http://[::1]/admin")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_10_x_blocked(self, analyzer):
        r = analyzer.analyze("http://10.0.0.1/internal")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_10_255_blocked(self, analyzer):
        r = analyzer.analyze("http://10.255.255.255/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_172_16_blocked(self, analyzer):
        r = analyzer.analyze("http://172.16.0.1/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_172_31_blocked(self, analyzer):
        r = analyzer.analyze("http://172.31.255.255/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_192_168_blocked(self, analyzer):
        r = analyzer.analyze("http://192.168.1.1/router")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_169_254_link_local_blocked(self, analyzer):
        r = analyzer.analyze("http://169.254.169.254/latest/meta-data/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_0_0_0_0_blocked(self, analyzer):
        r = analyzer.analyze("http://0.0.0.0/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ipv4_mapped_ipv6_blocked(self, analyzer):
        r = analyzer.analyze("http://[::ffff:127.0.0.1]/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ipv4_mapped_ipv6_private_blocked(self, analyzer):
        r = analyzer.analyze("http://[::ffff:192.168.1.1]/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_decimal_ip_blocked(self, analyzer):
        """2130706433 = 127.0.0.1 in decimal."""
        r = analyzer.analyze("http://2130706433/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_hex_ip_blocked(self, analyzer):
        """0x7f000001 = 127.0.0.1 in hex."""
        r = analyzer.analyze("http://0x7f000001/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ip6_localhost_blocked(self, analyzer):
        r = analyzer.analyze("http://ip6-localhost/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ipv6_ula_blocked(self, analyzer):
        r = analyzer.analyze("http://[fd00::1]/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf

    def test_ipv6_link_local_blocked(self, analyzer):
        r = analyzer.analyze("http://[fe80::1]/")
        assert r.verdict == URLVerdict.BLOCK
        assert r.is_ssrf


class TestLegitimateURLsAllowed:
    """Ensure normal browsing URLs pass through."""

    def test_https_allowed(self, analyzer):
        r = analyzer.analyze("https://www.google.com/search?q=hello")
        assert r.verdict == URLVerdict.ALLOW
        assert not r.is_ssrf

    def test_github_allowed(self, analyzer):
        r = analyzer.analyze("https://github.com/agentshroud/agentshroud")
        assert r.verdict == URLVerdict.ALLOW

    def test_stackoverflow_allowed(self, analyzer):
        r = analyzer.analyze("https://stackoverflow.com/questions/12345/some-question")
        assert r.verdict == URLVerdict.ALLOW

    def test_news_site_allowed(self, analyzer):
        r = analyzer.analyze("https://www.bbc.com/news/world-12345678")
        assert r.verdict == URLVerdict.ALLOW

    def test_api_endpoint_allowed(self, analyzer):
        r = analyzer.analyze("https://api.openai.com/v1/chat/completions")
        assert r.verdict == URLVerdict.ALLOW

    def test_docs_allowed(self, analyzer):
        r = analyzer.analyze("https://docs.python.org/3/library/asyncio.html")
        assert r.verdict == URLVerdict.ALLOW

    def test_public_ip_allowed(self, analyzer):
        r = analyzer.analyze("http://8.8.8.8/")
        assert r.verdict == URLVerdict.ALLOW
        assert not r.is_ssrf


class TestPIIInURLs:
    """PII detection in URLs — flagged, not blocked."""

    def test_email_in_url_flagged(self, analyzer):
        r = analyzer.analyze("https://example.com/lookup?email=john@example.com")
        assert r.verdict == URLVerdict.FLAG
        assert any(f.category == "pii" for f in r.findings)
        assert not r.is_ssrf  # Not blocked

    def test_ssn_in_url_flagged(self, analyzer):
        r = analyzer.analyze("https://example.com/verify?ssn=123-45-6789")
        assert r.verdict == URLVerdict.FLAG
        assert any("ssn" in f.description for f in r.findings)

    def test_credit_card_in_url_flagged(self, analyzer):
        r = analyzer.analyze("https://example.com/pay?cc=4111111111111111")
        assert r.verdict == URLVerdict.FLAG
        assert any("credit_card" in f.description for f in r.findings)

    def test_phone_in_url_flagged(self, analyzer):
        r = analyzer.analyze("https://example.com/contact?phone=555-123-4567")
        assert r.verdict == URLVerdict.FLAG


class TestDataExfiltration:
    """Data exfiltration patterns in URLs — flagged, not blocked."""

    def test_base64_in_path_flagged(self, analyzer):
        # Encode something long enough to trigger
        payload = base64.b64encode(
            b"This is a secret message that should be detected by the analyzer"
        ).decode()
        r = analyzer.analyze(f"https://attacker.com/exfil/{payload}")
        assert r.verdict == URLVerdict.FLAG
        assert any(f.category == "exfiltration" for f in r.findings)

    def test_base64_in_query_flagged(self, analyzer):
        payload = base64.b64encode(b"Stolen data with secret information and credentials").decode()
        r = analyzer.analyze(f"https://attacker.com/collect?data={payload}")
        assert r.verdict == URLVerdict.FLAG
        assert any(f.category == "exfiltration" for f in r.findings)

    def test_long_query_string_flagged(self, analyzer):
        long_query = "data=" + "A" * 2500
        r = analyzer.analyze(f"https://example.com/api?{long_query}")
        assert r.verdict == URLVerdict.FLAG
        assert any("long query" in f.description.lower() for f in r.findings)

    def test_many_params_flagged(self, analyzer):
        params = "&".join(f"p{i}=val{i}" for i in range(35))
        r = analyzer.analyze(f"https://example.com/dump?{params}")
        assert r.verdict == URLVerdict.FLAG
        assert any("parameters" in f.description.lower() for f in r.findings)

    def test_short_base64_not_flagged(self, analyzer):
        """Short base64 strings are normal (e.g., API tokens in URLs)."""
        r = analyzer.analyze("https://example.com/api?token=abc123")
        # Should not be flagged for base64
        base64_findings = [f for f in r.findings if "base64" in f.description.lower()]
        assert len(base64_findings) == 0

    def test_normal_query_not_flagged(self, analyzer):
        r = analyzer.analyze("https://www.google.com/search?q=python+tutorial&hl=en")
        assert r.verdict == URLVerdict.ALLOW


class TestMalformedURLs:
    """Edge cases and malformed URLs."""

    def test_empty_url(self, analyzer):
        r = analyzer.analyze("")
        # Should not crash
        assert r is not None

    def test_no_scheme(self, analyzer):
        r = analyzer.analyze("example.com/page")
        assert r is not None

    def test_weird_scheme(self, analyzer):
        r = analyzer.analyze("ftp://files.example.com/doc.pdf")
        assert r is not None
        assert not r.is_ssrf


class TestBase64Heuristic:
    """Test the _looks_like_base64 helper."""

    def test_actual_base64(self):
        encoded = base64.b64encode(b"This is a test message for base64 detection").decode()
        assert _looks_like_base64(encoded)

    def test_short_string_not_base64(self):
        assert not _looks_like_base64("abc123")

    def test_non_base64_chars(self):
        assert not _looks_like_base64("this is not base64!!! definitely not encoded")

    def test_all_lowercase_not_base64(self):
        assert not _looks_like_base64("a" * 100)
