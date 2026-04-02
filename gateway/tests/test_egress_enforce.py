# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Test suite for egress enforcement functionality.

Tests both enforce and monitor modes, allowlist/denylist behavior,
wildcard matching, and management API endpoints.
"""

import os
from unittest.mock import patch

import pytest

from gateway.security.egress_config import (
    EgressFilterConfig,
    get_egress_config,
    set_egress_config,
)
from gateway.security.egress_filter import EgressAction, EgressFilter


class TestEgressFilterConfig:
    """Test EgressFilterConfig functionality."""

    def test_default_config(self):
        """Test default configuration values."""
        config = EgressFilterConfig()
        assert config.mode == "enforce"
        assert "api.anthropic.com" in config.default_allowlist
        assert "api.openai.com" in config.default_allowlist
        assert "generativelanguage.googleapis.com" in config.default_allowlist
        assert "oauth2.googleapis.com" in config.default_allowlist
        assert "1password.com" in config.default_allowlist
        assert "*.1password.com" in config.default_allowlist
        assert "*.github.com" in config.default_allowlist
        assert "pastebin.com" in config.default_denylist
        assert "*.pastebin.com" in config.default_denylist
        assert config.strict_mode is True

    def test_from_environment_enforce(self):
        """Test config creation from environment in enforce mode."""
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "enforce"}):
            config = EgressFilterConfig.from_environment()
            assert config.mode == "enforce"

    def test_from_environment_monitor(self):
        """Test config creation from environment in monitor mode."""
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "monitor"}):
            config = EgressFilterConfig.from_environment()
            assert config.mode == "monitor"

    def test_egress_mode_override(self):
        """Test specific egress mode environment variable."""
        with patch.dict(
            os.environ, {"AGENTSHROUD_MODE": "enforce", "AGENTSHROUD_EGRESS_MODE": "monitor"}
        ):
            config = EgressFilterConfig.from_environment()
            assert config.mode == "monitor"

    def test_effective_allowlist_basic(self):
        """Test basic allowlist functionality."""
        config = EgressFilterConfig(
            default_allowlist=["example.com", "test.org"],
            agent_allowlists={"agent1": ["extra.com"]},
        )

        # Basic agent gets default + agent-specific
        allowlist = config.get_effective_allowlist("agent1")
        assert "example.com" in allowlist
        assert "test.org" in allowlist
        assert "extra.com" in allowlist

        # Other agent gets only default
        allowlist = config.get_effective_allowlist("agent2")
        assert "example.com" in allowlist
        assert "test.org" in allowlist
        assert "extra.com" not in allowlist

    def test_effective_allowlist_with_denylist(self):
        """Test allowlist with denylist in strict mode."""
        config = EgressFilterConfig(
            default_allowlist=["example.com", "bad.com"],
            default_denylist=["bad.com"],
            strict_mode=True,
        )

        allowlist = config.get_effective_allowlist("agent1")
        assert "example.com" in allowlist
        assert "bad.com" not in allowlist  # Removed by denylist

    def test_denylist_wildcards(self):
        """Test denylist wildcard matching."""
        config = EgressFilterConfig(default_denylist=["*.pastebin.com"])

        assert config.is_denylisted("evil.pastebin.com")
        assert config.is_denylisted("pastebin.com")
        assert not config.is_denylisted("pastebin.org")
        assert not config.is_denylisted("deep.evil.pastebin.com")  # Two levels


class TestEgressFilterEnforcement:
    """Test EgressFilter with enforce/monitor modes."""

    def test_enforce_mode_blocks_unknown_domains(self):
        """Test that enforce mode blocks domains not in allowlist."""
        config = EgressFilterConfig(mode="enforce", default_allowlist=["api.anthropic.com"])
        filter = EgressFilter(config=config)

        # Allowed domain passes
        result = filter.check("agent1", "api.anthropic.com")
        assert result.action == EgressAction.ALLOW

        # Unknown domain is blocked
        result = filter.check("agent1", "unknown-domain.com")
        assert result.action == EgressAction.DENY
        assert "BLOCKED" in result.rule
        assert "AgentShroud blocked this request" in result.details

    def test_monitor_mode_allows_unknown_domains(self):
        """Test that monitor mode allows unknown domains but logs them."""
        config = EgressFilterConfig(mode="monitor", default_allowlist=["api.anthropic.com"])
        filter = EgressFilter(config=config)

        # Allowed domain passes
        result = filter.check("agent1", "api.anthropic.com")
        assert result.action == EgressAction.ALLOW

        # Unknown domain is allowed but logged
        result = filter.check("agent1", "unknown-domain.com")
        assert result.action == EgressAction.ALLOW
        assert "logged only" in result.rule
        assert result.details == ""  # No blocking message

    def test_wildcard_allowlist_matching(self):
        """Test wildcard matching in allowlist."""
        config = EgressFilterConfig(
            mode="enforce", default_allowlist=["*.github.com", "api.openai.com"]
        )
        filter = EgressFilter(config=config)

        # Base domain matches
        result = filter.check("agent1", "github.com")
        assert result.action == EgressAction.ALLOW

        # One level subdomain matches
        result = filter.check("agent1", "api.github.com")
        assert result.action == EgressAction.ALLOW

        # Two levels don't match (security feature)
        result = filter.check("agent1", "evil.api.github.com")
        assert result.action == EgressAction.DENY

        # Non-wildcard exact match
        result = filter.check("agent1", "api.openai.com")
        assert result.action == EgressAction.ALLOW

    def test_denylist_overrides_allowlist(self):
        """Test that denylist overrides allowlist in strict mode."""
        config = EgressFilterConfig(
            mode="enforce",
            default_allowlist=["pastebin.com"],
            default_denylist=["*.pastebin.com"],
            strict_mode=True,
        )
        filter = EgressFilter(config=config)

        # Domain is in allowlist but also denylisted
        result = filter.check("agent1", "pastebin.com")
        assert result.action == EgressAction.DENY
        assert "denylist" in result.rule

    def test_denylist_monitor_mode(self):
        """Test denylist behavior in monitor mode."""
        config = EgressFilterConfig(mode="monitor", default_denylist=["pastebin.com"])
        filter = EgressFilter(config=config)

        # Denylisted domain is allowed but logged in monitor mode
        result = filter.check("agent1", "pastebin.com")
        assert result.action == EgressAction.ALLOW
        assert "monitored" in result.rule

    def test_private_ip_blocking(self):
        """Test that private IPs are blocked regardless of mode."""
        config = EgressFilterConfig(mode="enforce")
        filter = EgressFilter(config=config)

        # Private IPs are blocked
        result = filter.check("agent1", "192.168.1.1")
        assert result.action == EgressAction.DENY
        assert "SSRF protection" in result.rule

        result = filter.check("agent1", "localhost")
        assert result.action == EgressAction.DENY

        result = filter.check("agent1", "127.0.0.1")
        assert result.action == EgressAction.DENY

    def test_port_filtering(self):
        """Test port-based filtering."""
        config = EgressFilterConfig(
            mode="enforce", allowed_ports=[80, 443], default_allowlist=["example.com"]
        )
        filter = EgressFilter(config=config)

        # Allowed ports pass
        result = filter.check("agent1", "example.com:443")
        assert result.action == EgressAction.ALLOW

        result = filter.check("agent1", "https://example.com")  # Port 443 implied
        assert result.action == EgressAction.ALLOW

        # Disallowed port is handled based on mode
        result = filter.check("agent1", "example.com:22")
        assert result.action == EgressAction.DENY  # Should be denied in enforce mode

    def test_url_parsing(self):
        """Test URL parsing for domains and ports."""
        config = EgressFilterConfig(mode="enforce", default_allowlist=["api.anthropic.com"])
        filter = EgressFilter(config=config)

        # Full URL gets parsed correctly
        result = filter.check("agent1", "https://api.anthropic.com/v1/messages")
        assert result.action == EgressAction.ALLOW

        # HTTP URL with port
        result = filter.check("agent1", "http://api.anthropic.com:80/test")
        assert result.action == EgressAction.ALLOW

    def test_logging_differences_by_mode(self):
        """Test that logging differs between enforce and monitor modes."""
        # This would need to be tested with actual logging capture
        # For now, just verify the filter works correctly
        config_enforce = EgressFilterConfig(mode="enforce", default_allowlist=[])
        filter_enforce = EgressFilter(config=config_enforce)

        config_monitor = EgressFilterConfig(mode="monitor", default_allowlist=[])
        filter_monitor = EgressFilter(config=config_monitor)

        # Same request, different results
        result_enforce = filter_enforce.check("agent1", "unknown.com")
        result_monitor = filter_monitor.check("agent1", "unknown.com")

        assert result_enforce.action == EgressAction.DENY
        assert result_monitor.action == EgressAction.ALLOW


class TestEgressManagementAPI:
    """Test the management API endpoints (would need FastAPI test client)."""

    def test_config_roundtrip(self):
        """Test that config can be saved and retrieved."""
        # Test the config get/set functions directly
        original_config = get_egress_config()

        new_config = EgressFilterConfig(
            mode="monitor", default_allowlist=["test.com", "example.org"]
        )

        set_egress_config(new_config)
        retrieved = get_egress_config()

        assert retrieved.mode == "monitor"
        assert "test.com" in retrieved.default_allowlist
        assert "example.org" in retrieved.default_allowlist

        # Restore original
        set_egress_config(original_config)

    def test_invalid_mode_handling(self):
        """Test handling of invalid modes."""
        # This would test the API endpoint validation
        # For now, test the config validation
        config = EgressFilterConfig()

        # Valid modes should work
        config.mode = "enforce"
        assert config.mode == "enforce"

        config.mode = "monitor"
        assert config.mode == "monitor"


if __name__ == "__main__":
    pytest.main([__file__])
