# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — vendor policy profiles (SCRUM-209)."""

import copy
import logging

import pytest
import yaml

from gateway.inbound_edge import profiles as p

BASE = {
    "vendor": "test-vendor",
    "display_name": "Test Vendor",
    "connection": "mcp",
    "support": "documented",
    "enabled": True,
    "mode": "enforce",
    "auth": {
        "oauth": True,
        "dynamic_registration": False,
        "redirect_uris": ["https://vendor.example/callback"],
        "static_bearer": False,
    },
    "tools": {"lab_search": "read", "delegate_to_hermes": "write"},
    "limits": {
        "per_client_per_minute": 30,
        "per_vendor_per_minute": 60,
        "max_concurrency": 4,
        "daily_calls": 500,
        "daily_delegations": 20,
    },
    "dlp": {"mode": "redact", "min_confidence": 0.9},
    "max_response_bytes": 1048576,
}


def _write(tmp_path, data, name="test-vendor"):
    path = tmp_path / f"{name}.yaml"
    path.write_text(yaml.safe_dump(data))
    return tmp_path


def _variant(**changes):
    data = copy.deepcopy(BASE)
    for dotted, value in changes.items():
        node = data
        keys = dotted.split("__")
        for key in keys[:-1]:
            node = node[key]
        if value is _DELETE:
            node.pop(keys[-1])
        else:
            node[keys[-1]] = value
    return data


_DELETE = object()


class TestValidProfile:
    def test_loads(self, tmp_path):
        profiles = p.load_profiles(_write(tmp_path, BASE))
        prof = profiles["test-vendor"]
        assert prof.enabled and prof.mode == "enforce"
        assert prof.tool_access("lab_search") == "read"
        assert prof.tool_access("delegate_to_hermes") == "write"
        assert prof.tool_access("pke_status") is None

    def test_connection_support_and_docs_are_exposed(self, tmp_path):
        data = _variant(enabled=False, connection="chat-bridge", support="unconfirmed")
        data["docs"] = ["https://vendor.example/docs"]
        prof = p.load_profiles(_write(tmp_path, data))["test-vendor"]
        assert prof.connection == "chat-bridge" and prof.support == "unconfirmed"
        assert prof.docs == ("https://vendor.example/docs",)

    def test_file_name_must_match_vendor(self, tmp_path):
        with pytest.raises(p.ProfileError, match="file name"):
            p.load_profiles(_write(tmp_path, BASE, name="other"))


class TestFailClosed:
    @pytest.mark.parametrize(
        "changes,match",
        [
            ({"surprise": 1}, "surprise"),
            ({"tools__shell_exec": "read"}, "shell_exec"),
            ({"tools__lab_search": "admin"}, "admin"),
            ({"tools__lab_search": "write"}, "declared read"),
            ({"dlp__min_confidence": 0.5}, "0.9"),
            ({"dlp__mode": "off"}, "off"),
            ({"mode": "monitor"}, "monitor_ack"),
            ({"limits__max_concurrency": 0}, "max_concurrency"),
            ({"limits": _DELETE}, "limits"),
            ({"auth__redirect_uris": ["http://vendor.example/cb"]}, "https"),
            ({"max_response_bytes": 10 * 1024 * 1024}, "max_response_bytes"),
            ({"source_cidrs": ["not-a-cidr"]}, "not-a-cidr"),
            ({"auth__static_bearer": True}, "not implemented"),
            ({"connection": _DELETE}, "connection"),
            ({"connection": "smtp"}, "smtp"),
            ({"support": _DELETE}, "support"),
            ({"support": "rumoured"}, "rumoured"),
            ({"docs": ["http://vendor.example/docs"]}, "https"),
            # The Slack/Teams chat bridge (SCRUM-220) is not built: an enabled
            # chat-bridge vendor must refuse, not load and silently do nothing.
            ({"connection": "chat-bridge"}, "chat-bridge.*not implemented"),
        ],
    )
    def test_invalid_profile_refuses_to_load(self, tmp_path, changes, match):
        with pytest.raises(p.ProfileError, match=match):
            p.load_profiles(_write(tmp_path, _variant(**changes)))

    def test_unparseable_yaml_refuses(self, tmp_path):
        (tmp_path / "broken.yaml").write_text("vendor: [unclosed")
        with pytest.raises(p.ProfileError):
            p.load_profiles(tmp_path)

    def test_duplicate_vendor_refuses(self, tmp_path):
        _write(tmp_path, BASE)
        (tmp_path / "test-vendor.yml").write_text(yaml.safe_dump(BASE))
        with pytest.raises(p.ProfileError, match="duplicate"):
            p.load_profiles(tmp_path)

    def test_missing_directory_refuses(self, tmp_path):
        with pytest.raises(p.ProfileError):
            p.load_profiles(tmp_path / "nope")


class TestMonitorMode:
    def test_monitor_needs_ack_and_warns_loudly(self, tmp_path, caplog):
        data = _variant(mode="monitor", monitor_ack=True)
        with caplog.at_level(logging.WARNING, logger="agentshroud.inbound_edge.profiles"):
            prof = p.load_profiles(_write(tmp_path, data))["test-vendor"]
        assert prof.mode == "monitor"
        assert any("MONITOR MODE" in r.message for r in caplog.records)


class TestDlpFloor:
    def test_threshold_may_be_raised(self, tmp_path):
        prof = p.load_profiles(_write(tmp_path, _variant(dlp__min_confidence=0.95)))
        assert prof["test-vendor"].dlp_min_confidence == 0.95

    def test_floor_follows_global_pii_config(self):
        from gateway.ingest_api.config import PIIConfig

        assert p.GLOBAL_DLP_FLOOR == PIIConfig().min_confidence


class TestShippedProfiles:
    def test_every_shipped_vendor_is_disabled_and_enforcing(self):
        profiles = p.load_profiles(p.VENDORS_DIR)
        assert set(profiles) == {
            "claude-duet",
            "poke",
            "gemini-spark",
            "openai-dots",
            "meta-muse",
            "xai-grok-bot",
        }
        for vendor, prof in profiles.items():
            assert prof.enabled is False, vendor
            assert prof.mode == "enforce", vendor
            assert prof.static_bearer is False, vendor
            assert prof.docs, f"{vendor}: cite the vendor docs the profile is based on"

    def test_unconfirmed_vendors_cannot_register_or_write(self):
        """A vendor whose custom-MCP support is not confirmed ships with no redirect
        URI (so OAuth cannot complete) and read-only tools."""
        for vendor, prof in p.load_profiles(p.VENDORS_DIR).items():
            if prof.support != "unconfirmed":
                continue
            assert prof.redirect_uris == (), vendor
            assert set(prof.tools.values()) <= {"read"}, vendor

    def test_connection_types_of_shipped_vendors(self):
        profiles = p.load_profiles(p.VENDORS_DIR)
        assert profiles["openai-dots"].connection == "chat-bridge"
        for vendor in ("claude-duet", "poke", "gemini-spark", "meta-muse", "xai-grok-bot"):
            assert profiles[vendor].connection == "mcp", vendor

    def test_claude_profile_covers_every_claude_surface(self):
        """Duet, chat and Cowork share one Claude account and client identity, so the
        edge cannot tell them apart; the profile must not claim it can."""
        prof = p.load_profiles(p.VENDORS_DIR)["claude-duet"]
        assert prof.display_name == "Anthropic Claude (Duet, chat, Cowork)"

    def test_claude_duet_allows_both_claude_callbacks(self):
        prof = p.load_profiles(p.VENDORS_DIR)["claude-duet"]
        assert "https://claude.ai/api/mcp/auth_callback" in prof.redirect_uris
        assert "https://claude.com/api/mcp/auth_callback" in prof.redirect_uris

    def test_delegate_is_write_everywhere(self):
        for vendor, prof in p.load_profiles(p.VENDORS_DIR).items():
            if prof.tool_access("delegate_to_hermes"):
                assert prof.tool_access("delegate_to_hermes") == "write", vendor
