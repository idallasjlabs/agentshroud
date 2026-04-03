# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for DNS exfiltration prevention."""

from __future__ import annotations

import pytest

from gateway.security.dns_filter import (
    DNSFilter,
    DNSFilterConfig,
    EntropyCalculator,
)


@pytest.fixture
def default_config():
    return DNSFilterConfig()


@pytest.fixture
def strict_config():
    return DNSFilterConfig(
        mode="enforce",
        max_subdomain_length=50,
        max_label_length=30,
        entropy_threshold=3.5,
        allowed_domains=["github.com", "api.openai.com", "pypi.org"],
        max_queries_per_minute=60,
    )


@pytest.fixture
def monitor_config():
    return DNSFilterConfig(mode="monitor")


@pytest.fixture
def dns_filter(default_config):
    return DNSFilter(config=default_config)


@pytest.fixture
def monitor_filter(monitor_config):
    return DNSFilter(config=monitor_config)


@pytest.fixture
def strict_filter(strict_config):
    return DNSFilter(config=strict_config)


class TestDNSFilterConfig:
    def test_default_mode_is_enforce(self, default_config):
        """Default mode is enforce after v0.8.0 enforcement hardening."""
        assert default_config.mode == "enforce"

    def test_default_allows_all_domains(self, default_config):
        assert default_config.allowed_domains is None  # None = allow all

    def test_strict_has_allowlist(self, strict_config):
        assert "github.com" in strict_config.allowed_domains

    def test_generous_defaults(self, default_config):
        assert default_config.max_subdomain_length >= 60
        assert default_config.max_label_length >= 40
        assert default_config.entropy_threshold >= 4.0
        assert default_config.max_queries_per_minute >= 120


class TestNormalDNSResolution:
    def test_normal_domain_allowed(self, dns_filter):
        v = dns_filter.check("api.github.com", agent_id="agent1")
        assert v.allowed is True

    def test_subdomain_allowed(self, dns_filter):
        v = dns_filter.check("us-east-1.api.aws.amazon.com", agent_id="agent1")
        assert v.allowed is True

    def test_common_services_allowed(self, dns_filter):
        domains = [
            "api.openai.com",
            "pypi.org",
            "registry.npmjs.org",
            "github.com",
            "smtp.gmail.com",
            "imap.mail.me.com",
        ]
        for d in domains:
            v = dns_filter.check(d, agent_id="agent1")
            assert v.allowed is True, f"{d} should be allowed"

    def test_long_but_legitimate_domain(self, dns_filter):
        # Real AWS domains can be long
        d = "my-service.us-east-1.elb.amazonaws.com"
        v = dns_filter.check(d, agent_id="agent1")
        assert v.allowed is True

    def test_monitor_mode_never_blocks(self, monitor_filter):
        """Even suspicious queries pass in monitor mode."""
        suspicious = "aGVsbG8gd29ybGQgdGhpcyBpcyBiYXNlNjQ.data.evil.com"
        v = monitor_filter.check(suspicious, agent_id="agent1")
        assert v.allowed is True
        assert v.flagged is True  # flagged but allowed


class TestDNSTunnelingDetection:
    def test_base64_in_subdomain_flagged(self, dns_filter):
        query = "aGVsbG8gd29ybGQgdGhpcyBpcyBhIHRlc3Q.exfil.evil.com"
        v = dns_filter.check(query, agent_id="agent1")
        assert v.flagged is True
        assert "base64" in v.reason.lower() or "entropy" in v.reason.lower()

    def test_hex_encoded_subdomain_flagged(self, dns_filter):
        query = "68656c6c6f776f726c6468656c6c6f.exfil.evil.com"
        v = dns_filter.check(query, agent_id="agent1")
        assert v.flagged is True

    def test_very_long_subdomain_flagged(self, dns_filter):
        long_label = "a" * 63  # max DNS label is 63
        query = f"{long_label}.{long_label}.evil.com"
        v = dns_filter.check(query, agent_id="agent1")
        assert v.flagged is True

    def test_high_entropy_subdomain_flagged(self, dns_filter):
        query = "x8k2m9qr4z7bv1nc.exfil.evil.com"
        v = dns_filter.check(query, agent_id="agent1")
        assert v.flagged is True

    def test_enforce_mode_blocks_tunneling(self, strict_filter):
        query = "aGVsbG8gd29ybGQgdGhpcyBpcyBhIHRlc3Q.exfil.evil.com"
        v = strict_filter.check(query, agent_id="agent1")
        assert v.allowed is False

    def test_multiple_long_labels_flagged(self, dns_filter):
        query = "abcdefghij1234567890.klmnopqrst1234567890.evil.com"
        v = dns_filter.check(query, agent_id="agent1")
        assert v.flagged is True


class TestDNSAllowlist:
    def test_allowlist_permits_listed_domain(self, strict_filter):
        v = strict_filter.check("github.com", agent_id="agent1")
        assert v.allowed is True

    def test_allowlist_permits_subdomain(self, strict_filter):
        v = strict_filter.check("api.github.com", agent_id="agent1")
        assert v.allowed is True

    def test_allowlist_blocks_unlisted_in_enforce(self, strict_filter):
        v = strict_filter.check("evil.com", agent_id="agent1")
        assert v.allowed is False

    def test_no_allowlist_allows_all(self, dns_filter):
        v = dns_filter.check("anything.example.com", agent_id="agent1")
        assert v.allowed is True


class TestRateLimiting:
    def test_burst_queries_flagged(self, dns_filter):
        flagged_any = False
        for i in range(200):
            v = dns_filter.check(f"q{i}.example.com", agent_id="agent1")
            if v.flagged:
                flagged_any = True
        assert flagged_any

    def test_normal_rate_not_flagged(self, dns_filter):
        v = dns_filter.check("example.com", agent_id="agent1")
        assert v.flagged is False


class TestAuditLogging:
    def test_queries_logged(self, dns_filter):
        dns_filter.check("example.com", agent_id="agent1")
        dns_filter.check("github.com", agent_id="agent1")
        logs = dns_filter.get_audit_log(agent_id="agent1")
        assert len(logs) == 2

    def test_log_contains_timestamp(self, dns_filter):
        dns_filter.check("example.com", agent_id="agent1")
        logs = dns_filter.get_audit_log(agent_id="agent1")
        assert logs[0].timestamp > 0

    def test_log_contains_verdict(self, dns_filter):
        dns_filter.check("example.com", agent_id="agent1")
        logs = dns_filter.get_audit_log(agent_id="agent1")
        assert hasattr(logs[0], "allowed")

    def test_flagged_queries_in_log(self, dns_filter):
        dns_filter.check("aGVsbG8gd29ybGQgdGhpcyBpcyBiYXNlNjQ.evil.com", agent_id="agent1")
        flagged = dns_filter.get_flagged_queries(agent_id="agent1")
        assert len(flagged) >= 1


class TestEntropyCalculator:
    def test_low_entropy_string(self):
        assert EntropyCalculator.shannon_entropy("aaaaaaa") < 1.0

    def test_high_entropy_string(self):
        assert EntropyCalculator.shannon_entropy("x8k2m9qr4z7b") > 3.0

    def test_empty_string(self):
        assert EntropyCalculator.shannon_entropy("") == 0.0


# ── C44: DNS Rebinding Prevention tests ──────────────────────────────────────


class TestDNSRebinding:
    @pytest.fixture
    def dns_filter(self):
        return DNSFilter(DNSFilterConfig(mode="enforce"))

    def test_stable_resolution_passes(self, dns_filter):
        """Seeding the same IP twice should not flag rebinding."""
        domain = "example.com"
        # Manually seed cache with a public IP
        dns_filter._resolved_ip_cache[domain] = ("93.184.216.34", 0.0)
        result = dns_filter._is_private_ip("93.184.216.34")
        assert not result

    def test_private_ip_detection(self, dns_filter):
        """Known private ranges should be detected."""
        private_ips = ["10.0.0.1", "192.168.1.1", "172.16.0.5", "127.0.0.1"]
        for ip in private_ips:
            assert dns_filter._is_private_ip(ip), f"Should flag {ip} as private"

    def test_public_ip_not_private(self, dns_filter):
        """Public IPs should not be flagged as private."""
        public_ips = ["8.8.8.8", "93.184.216.34", "1.1.1.1"]
        for ip in public_ips:
            assert not dns_filter._is_private_ip(ip), f"Should not flag {ip} as private"

    def test_resolve_and_cache_empty_domain_graceful(self, dns_filter):
        """Resolving a domain that fails should return empty string gracefully."""
        # Non-existent domain should not raise
        result = dns_filter.resolve_and_cache("this.domain.does.not.exist.invalid")
        assert isinstance(result, str)
