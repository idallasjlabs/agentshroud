# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for EgressFilter — core filtering logic, allowlists, denylists, modes."""

import pytest

from gateway.security.egress_filter import (
    EgressFilter,
    EgressAction,
    EgressPolicy,
    EgressAttempt,
)
from gateway.security.egress_config import EgressFilterConfig


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_filter(mode="enforce", allowed_domains=None, denied_domains=None, allowed_ips=None):
    """Create an EgressFilter with a simple config."""
    cfg = EgressFilterConfig(
        mode=mode,
        default_allowlist=allowed_domains or [],
        default_denylist=denied_domains or [],
        allowed_ips=allowed_ips or [],
    )
    return EgressFilter(config=cfg)


# ---------------------------------------------------------------------------
# Basic allow / deny in enforce mode
# ---------------------------------------------------------------------------

class TestEnforceMode:
    """EgressFilter in enforce mode should block unlisted destinations."""

    def test_allowed_domain_passes(self):
        ef = _make_filter(mode="enforce", allowed_domains=["api.anthropic.com"])
        result = ef.check("bot", "https://api.anthropic.com/v1/messages")
        assert result.action == EgressAction.ALLOW

    def test_unlisted_domain_blocked(self):
        ef = _make_filter(mode="enforce", allowed_domains=["api.anthropic.com"])
        result = ef.check("bot", "https://evil.example.com/exfil")
        assert result.action == EgressAction.DENY

    def test_wildcard_one_level(self):
        ef = _make_filter(mode="enforce", allowed_domains=["*.github.com"])
        result = ef.check("bot", "https://api.github.com/repos")
        assert result.action == EgressAction.ALLOW

    def test_wildcard_does_not_match_deep_subdomain(self):
        ef = _make_filter(mode="enforce", allowed_domains=["*.github.com"])
        result = ef.check("bot", "https://a.b.github.com/deep")
        assert result.action == EgressAction.DENY

    def test_wildcard_matches_base_domain(self):
        ef = _make_filter(mode="enforce", allowed_domains=["*.github.com"])
        result = ef.check("bot", "https://github.com/home")
        assert result.action == EgressAction.ALLOW

    def test_denied_domain_overrides_allow(self):
        ef = _make_filter(
            mode="enforce",
            allowed_domains=["*.example.com"],
            denied_domains=["evil.example.com"],
        )
        result = ef.check("bot", "https://evil.example.com")
        assert result.action == EgressAction.DENY

    def test_port_not_allowed(self):
        ef = _make_filter(mode="enforce", allowed_domains=["example.com"])
        # Default allowed ports are 80, 443; port 9999 should be denied
        policy = EgressPolicy(allowed_domains=["example.com"], allowed_ports=[80, 443])
        ef2 = EgressFilter(config=ef.config, default_policy=policy)
        result = ef2.check("bot", "example.com:9999", port=9999)
        assert result.action == EgressAction.DENY


# ---------------------------------------------------------------------------
# Monitor mode
# ---------------------------------------------------------------------------

class TestMonitorMode:
    """EgressFilter in monitor mode should allow but log unlisted destinations."""

    def test_unlisted_domain_allowed_in_monitor(self):
        ef = _make_filter(mode="monitor", allowed_domains=["api.anthropic.com"])
        result = ef.check("bot", "https://unknown.example.com")
        assert result.action == EgressAction.ALLOW
        assert "monitor" in result.rule.lower() or "logged" in result.rule.lower()

    def test_allowed_domain_still_allowed_in_monitor(self):
        ef = _make_filter(mode="monitor", allowed_domains=["api.anthropic.com"])
        result = ef.check("bot", "https://api.anthropic.com/v1/messages")
        assert result.action == EgressAction.ALLOW


# ---------------------------------------------------------------------------
# IP-based rules
# ---------------------------------------------------------------------------

class TestIPRules:
    """IP allowlist and private-IP SSRF protection."""

    def test_allowed_ip(self):
        ef = _make_filter(mode="enforce", allowed_ips=["93.184.216.34"])
        result = ef.check("bot", "93.184.216.34", port=443)
        assert result.action == EgressAction.ALLOW

    def test_allowed_cidr(self):
        """CIDR in policy allowlist should match."""
        ef = _make_filter(mode="enforce")
        policy = EgressPolicy(allowed_ips=["10.0.0.0/8"], allowed_ports=[443])
        ef2 = EgressFilter(config=ef.config, default_policy=policy)
        result = ef2.check("bot", "10.1.2.3", port=443)
        assert result.action == EgressAction.ALLOW

    def test_private_ip_blocked_ssrf(self):
        """Private IPs are blocked by default to prevent SSRF."""
        ef = _make_filter(mode="enforce")
        result = ef.check("bot", "127.0.0.1", port=80)
        assert result.action == EgressAction.DENY

    def test_private_ip_allowed_if_in_policy_allowlist(self):
        """Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check)."""
        ef = _make_filter(mode="enforce")
        policy = EgressPolicy(allowed_ips=["127.0.0.1"], allowed_ports=[80])
        ef2 = EgressFilter(config=ef.config, default_policy=policy)
        result = ef2.check("bot", "127.0.0.1", port=80)
        assert result.action == EgressAction.ALLOW

    def test_localhost_hostname_blocked(self):
        ef = _make_filter(mode="enforce")
        result = ef.check("bot", "localhost", port=80)
        assert result.action == EgressAction.DENY

    def test_ipv4_mapped_ipv6_blocked(self):
        ef = _make_filter(mode="enforce")
        result = ef.check("bot", "::ffff:127.0.0.1", port=80)
        assert result.action == EgressAction.DENY


# ---------------------------------------------------------------------------
# Per-agent policies
# ---------------------------------------------------------------------------

class TestPerAgentPolicy:
    """Per-agent policies override the default."""

    def test_agent_specific_policy(self):
        ef = _make_filter(mode="enforce", allowed_domains=["default.com"])
        agent_policy = EgressPolicy(allowed_domains=["agent-only.com"])
        ef.set_agent_policy("special-agent", agent_policy)

        # Default agent uses global policy
        r1 = ef.check("bot", "https://default.com")
        assert r1.action == EgressAction.ALLOW

        # Special agent uses its own policy
        r2 = ef.check("special-agent", "https://agent-only.com")
        assert r2.action == EgressAction.ALLOW

        # Special agent cannot access random domain
        r3 = ef.check("special-agent", "https://random.example.com")
        assert r3.action == EgressAction.DENY


# ---------------------------------------------------------------------------
# URL parsing
# ---------------------------------------------------------------------------

class TestURLParsing:
    """EgressFilter correctly parses URLs, host:port, and bare hostnames."""

    def test_full_url(self):
        ef = _make_filter(mode="enforce", allowed_domains=["example.com"])
        result = ef.check("bot", "https://example.com/path?q=1")
        assert result.action == EgressAction.ALLOW

    def test_host_port_format(self):
        ef = _make_filter(mode="enforce", allowed_domains=["example.com"])
        result = ef.check("bot", "example.com:443")
        assert result.action == EgressAction.ALLOW

    def test_bare_hostname(self):
        ef = _make_filter(mode="enforce", allowed_domains=["example.com"])
        result = ef.check("bot", "example.com")
        assert result.action == EgressAction.ALLOW


# ---------------------------------------------------------------------------
# Logging / stats
# ---------------------------------------------------------------------------

class TestLogging:
    """EgressFilter records attempts and provides stats."""

    def test_log_records_attempts(self):
        ef = _make_filter(mode="enforce", allowed_domains=["ok.com"])
        ef.check("bot", "https://ok.com")
        ef.check("bot", "https://bad.com")
        log = ef.get_log()
        assert len(log) == 2
        assert log[0].action == EgressAction.ALLOW
        assert log[1].action == EgressAction.DENY

    def test_stats_counts(self):
        ef = _make_filter(mode="enforce", allowed_domains=["ok.com"])
        ef.check("bot", "https://ok.com")
        ef.check("bot", "https://bad.com")
        stats = ef.get_stats()
        assert stats["total"] == 2
        assert stats["allowed"] == 1
        assert stats["denied"] == 1

    def test_log_filters_by_agent(self):
        ef = _make_filter(mode="enforce", allowed_domains=["ok.com"])
        ef.check("agent-a", "https://ok.com")
        ef.check("agent-b", "https://ok.com")
        log_a = ef.get_log(agent_id="agent-a")
        assert len(log_a) == 1
        assert log_a[0].agent_id == "agent-a"

    def test_log_size_limit(self):
        ef = _make_filter(mode="enforce", allowed_domains=["ok.com"])
        ef._max_log_size = 10
        for i in range(20):
            ef.check("bot", "https://ok.com")
        assert len(ef._log) <= 10


# ---------------------------------------------------------------------------
# EgressAttempt dataclass
# ---------------------------------------------------------------------------

class TestEgressAttempt:
    """EgressAttempt stores the right fields."""

    def test_attempt_fields(self):
        ef = _make_filter(mode="enforce", allowed_domains=["ok.com"])
        result = ef.check("bot", "https://ok.com", port=443)
        assert isinstance(result, EgressAttempt)
        assert result.agent_id == "bot"
        assert result.action == EgressAction.ALLOW
        assert result.port == 443

    def test_deny_has_details(self):
        ef = _make_filter(mode="enforce")
        result = ef.check("bot", "https://blocked.example.com")
        assert result.action == EgressAction.DENY
        assert result.details  # Should have a helpful error message


# ---------------------------------------------------------------------------
# EgressPolicy standalone tests
# ---------------------------------------------------------------------------

class TestEgressPolicy:
    """Unit tests for EgressPolicy matching methods."""

    def test_matches_domain_exact(self):
        p = EgressPolicy(allowed_domains=["example.com"])
        assert p.matches_domain("example.com") is True
        assert p.matches_domain("other.com") is False

    def test_matches_domain_wildcard(self):
        p = EgressPolicy(allowed_domains=["*.example.com"])
        assert p.matches_domain("sub.example.com") is True
        assert p.matches_domain("a.b.example.com") is False
        assert p.matches_domain("example.com") is True

    def test_matches_ip_single(self):
        p = EgressPolicy(allowed_ips=["1.2.3.4"])
        assert p.matches_ip("1.2.3.4") is True
        assert p.matches_ip("5.6.7.8") is False

    def test_matches_ip_cidr(self):
        p = EgressPolicy(allowed_ips=["10.0.0.0/8"])
        assert p.matches_ip("10.255.0.1") is True
        assert p.matches_ip("192.168.1.1") is False

    def test_matches_port(self):
        p = EgressPolicy(allowed_ports=[80, 443])
        assert p.matches_port(80) is True
        assert p.matches_port(8080) is False
        assert p.matches_port(None) is True  # No port = allow

    def test_matches_port_empty_allows_all(self):
        p = EgressPolicy(allowed_ports=[])
        assert p.matches_port(9999) is True

    def test_matches_ip_invalid(self):
        p = EgressPolicy(allowed_ips=["10.0.0.0/8"])
        assert p.matches_ip("not-an-ip") is False
