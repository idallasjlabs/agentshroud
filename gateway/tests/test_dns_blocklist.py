# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for the in-process DNS blocklist (replaced Pi-hole integration)."""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.dns_blocklist import SYSTEM_ALLOWLIST, DNSBlocklist


class TestParseHostsLine:
    """parse_hosts_line() — hosts format, adblock format, comments, empty, localhost."""

    def setup_method(self):
        self.bl = DNSBlocklist(blocklist_urls=[], data_dir=Path("/tmp/test_dns_bl"))

    def test_hosts_format_zero(self):
        assert self.bl.parse_hosts_line("0.0.0.0 evil.com") == "evil.com"

    def test_hosts_format_localhost(self):
        assert self.bl.parse_hosts_line("127.0.0.1 malware.net") == "malware.net"

    def test_hosts_format_localhost_skip(self):
        # Should skip the localhost entry itself
        assert self.bl.parse_hosts_line("127.0.0.1 localhost") is None

    def test_adblock_format(self):
        assert self.bl.parse_hosts_line("||adserver.com^") == "adserver.com"

    def test_domain_only(self):
        assert self.bl.parse_hosts_line("tracker.io") == "tracker.io"

    def test_comment_line(self):
        assert self.bl.parse_hosts_line("# this is a comment") is None

    def test_empty_line(self):
        assert self.bl.parse_hosts_line("") is None

    def test_blank_whitespace(self):
        assert self.bl.parse_hosts_line("   ") is None

    def test_inline_comment_stripped(self):
        result = self.bl.parse_hosts_line("tracker.net # inline comment")
        assert result == "tracker.net"

    def test_invalid_no_dot(self):
        assert self.bl.parse_hosts_line("localdomain") is None

    def test_adblock_format_invalid_chars(self):
        # Contains space — not a valid domain
        assert self.bl.parse_hosts_line("||bad domain.com^") is None


class TestIsBlocked:
    """is_blocked() — exact match, parent-domain wildcard, allowlist, denylist, case."""

    def setup_method(self):
        self.bl = DNSBlocklist(blocklist_urls=[], data_dir=Path("/tmp/test_dns_bl"))
        self.bl.blocked_domains = {"evil.com", "ads.example.org"}

    def test_exact_match(self):
        assert self.bl.is_blocked("evil.com") is True

    def test_not_blocked(self):
        assert self.bl.is_blocked("google.com") is False

    def test_parent_domain_wildcard(self):
        # ads.example.org is blocked → sub.ads.example.org should also be blocked
        assert self.bl.is_blocked("sub.ads.example.org") is True

    def test_allowlist_overrides_blocklist(self):
        # Add to blocklist and allowlist — allowlist wins
        self.bl.blocked_domains.add("api.telegram.org")
        assert self.bl.is_blocked("api.telegram.org") is False

    def test_system_allowlist(self):
        assert self.bl.is_blocked("api.anthropic.com") is False
        assert self.bl.is_blocked("localhost") is False

    def test_custom_denylist(self):
        bl = DNSBlocklist(
            blocklist_urls=[],
            custom_denylist={"always-blocked.com"},
            data_dir=Path("/tmp/test_dns_bl"),
        )
        assert bl.is_blocked("always-blocked.com") is True

    def test_case_normalization(self):
        assert self.bl.is_blocked("EVIL.COM") is True
        assert self.bl.is_blocked("Evil.Com") is True

    def test_trailing_dot_normalization(self):
        assert self.bl.is_blocked("evil.com.") is True


class TestLoadFromText:
    """load_from_text() — multi-line parsing, dedup, allowlist skip."""

    def setup_method(self):
        self.bl = DNSBlocklist(blocklist_urls=[], data_dir=Path("/tmp/test_dns_bl"))

    def test_multi_line_parsing(self):
        text = "0.0.0.0 a.com\n0.0.0.0 b.com\n0.0.0.0 c.com"
        count = self.bl.load_from_text(text)
        assert count == 3
        assert "a.com" in self.bl.blocked_domains
        assert "b.com" in self.bl.blocked_domains
        assert "c.com" in self.bl.blocked_domains

    def test_deduplication(self):
        text = "0.0.0.0 dup.com\n0.0.0.0 dup.com"
        initial = len(self.bl.blocked_domains)
        count = self.bl.load_from_text(text)
        # count may be 1 or 2 depending on implementation, but only 1 unique domain added
        assert len(self.bl.blocked_domains) - initial == 1

    def test_allowlist_skip(self):
        # System allowlist entries should not be added
        text = "0.0.0.0 api.anthropic.com\n0.0.0.0 malware.io"
        count = self.bl.load_from_text(text)
        assert "api.anthropic.com" not in self.bl.blocked_domains
        assert "malware.io" in self.bl.blocked_domains

    def test_comments_skipped(self):
        text = "# This is a comment\n0.0.0.0 blocked.com"
        count = self.bl.load_from_text(text)
        assert "blocked.com" in self.bl.blocked_domains

    def test_empty_text(self):
        count = self.bl.load_from_text("")
        assert count == 0


class TestStats:
    """stats() — verify blocked/allowlist/denylist counts."""

    def test_stats_attributes(self):
        bl = DNSBlocklist(
            blocklist_urls=[],
            custom_allowlist={"extra-safe.com"},
            custom_denylist={"always-block.net"},
            data_dir=Path("/tmp/test_dns_bl"),
        )
        bl.load_from_text("0.0.0.0 evil1.com\n0.0.0.0 evil2.com")
        assert len(bl.blocked_domains) == 2
        assert "extra-safe.com" in bl.allowlist
        assert "always-block.net" in bl.denylist


class TestLifecycle:
    """Lifecycle: start_periodic_updates()/stop() task management."""

    @pytest.mark.asyncio
    async def test_start_creates_task(self):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=Path("/tmp/test_dns_bl"))

        with patch.object(bl, "update", new=AsyncMock(return_value=None)):
            await bl.start_periodic_updates()
            assert bl.update_task is not None
            assert not bl.update_task.done()
            bl.stop()
            # Give event loop a tick to process cancellation
            await asyncio.sleep(0)

    @pytest.mark.asyncio
    async def test_stop_cancels_task(self):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=Path("/tmp/test_dns_bl"))

        with patch.object(bl, "update", new=AsyncMock(return_value=None)):
            await bl.start_periodic_updates()
            bl.stop()
            await asyncio.sleep(0)
            assert bl.update_task is None or bl.update_task.cancelled() or bl.update_task.done()

    def test_stats_returns_counts(self):
        """stats() returns the expected keys."""
        bl = DNSBlocklist(
            blocklist_urls=[],
            custom_denylist={"deny.net"},
            data_dir=Path("/tmp/test_dns_bl"),
        )
        bl.load_from_text("0.0.0.0 a.com\n0.0.0.0 b.com")
        s = bl.stats()
        assert "blocked_domains" in s
        assert s["blocked_domains"] == 2
        assert "allowlist_size" in s
        assert "denylist_size" in s
        assert s["denylist_size"] >= 1
