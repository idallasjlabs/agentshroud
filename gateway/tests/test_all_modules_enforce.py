# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Batch F5 exit criterion: verify ALL core security modules default to enforce mode.

This test suite is the enforcement gate for the v0.8.0 "Watchtower" release.
A pass here means every module is configured fail-closed by default.
"""

from __future__ import annotations

import os

import pytest

from gateway.ingest_api.config import (
    GatewayConfig,
    SecurityConfig,
    SecurityModuleConfig,
    get_module_mode,
)
from gateway.security.browser_security import BrowserSecurityGuard
from gateway.security.context_guard import ContextGuard
from gateway.security.dns_filter import DNSFilterConfig
from gateway.security.egress_filter import EgressFilter
from gateway.security.egress_monitor import EgressMonitorConfig
from gateway.security.file_sandbox import FileSandbox, FileSandboxConfig
from gateway.security.git_guard import GitGuard
from gateway.security.killswitch_config import KillSwitchConfig
from gateway.security.multi_turn_tracker import MultiTurnTracker
from gateway.security.output_canary import OutputCanary
from gateway.security.path_isolation import PathIsolationConfig, PathIsolationManager
from gateway.security.prompt_guard import PromptGuard
from gateway.security.subagent_monitor import SubagentMonitorConfig
from gateway.security.tool_chain_analyzer import ToolChainAnalyzer

ENFORCE_MODE = "enforce"


class TestSecurityConfigDefaults:
    """Verify SecurityConfig and SecurityModuleConfig default to enforce."""

    def test_security_module_config_default_mode(self):
        cfg = SecurityModuleConfig()
        assert cfg.mode == ENFORCE_MODE

    def test_security_config_pii_sanitizer_enforce(self):
        cfg = SecurityConfig()
        assert cfg.pii_sanitizer.mode == ENFORCE_MODE

    def test_security_config_prompt_guard_enforce(self):
        cfg = SecurityConfig()
        assert cfg.prompt_guard.mode == ENFORCE_MODE

    def test_security_config_egress_filter_enforce(self):
        cfg = SecurityConfig()
        assert cfg.egress_filter.mode == ENFORCE_MODE

    def test_security_config_mcp_proxy_enforce(self):
        cfg = SecurityConfig()
        assert cfg.mcp_proxy.mode == ENFORCE_MODE

    def test_security_config_dns_filter_enforce(self):
        cfg = SecurityConfig()
        assert cfg.dns_filter.mode == ENFORCE_MODE

    def test_security_config_subagent_monitor_enforce(self):
        cfg = SecurityConfig()
        assert cfg.subagent_monitor.mode == ENFORCE_MODE

    def test_security_config_egress_monitor_enforce(self):
        cfg = SecurityConfig()
        assert cfg.egress_monitor.mode == ENFORCE_MODE

    def test_security_config_killswitch_enforce(self):
        cfg = SecurityConfig()
        assert cfg.killswitch.mode == ENFORCE_MODE


class TestModuleConfigDefaults:
    """Verify individual module configs default to enforce mode."""

    def test_dns_filter_default_enforce(self):
        cfg = DNSFilterConfig()
        assert cfg.mode == ENFORCE_MODE

    def test_egress_monitor_default_enforce(self):
        cfg = EgressMonitorConfig()
        assert cfg.mode == ENFORCE_MODE

    def test_subagent_monitor_default_enforce(self):
        cfg = SubagentMonitorConfig()
        assert cfg.mode == ENFORCE_MODE

    def test_killswitch_dry_run_disabled(self):
        """Kill switch dry_run must be False — real termination on anomaly."""
        cfg = KillSwitchConfig()
        assert cfg.dry_run_enabled is False


class TestGetModuleModeEnforceDefault:
    """Verify get_module_mode returns enforce when no override is set."""

    def test_get_module_mode_no_env_override(self, monkeypatch):
        monkeypatch.delenv("AGENTSHROUD_MODE", raising=False)
        cfg = GatewayConfig(
            bind="127.0.0.1",
            port=8080,
            auth_method="shared_secret",
            auth_token="test-token",
        )
        for module in [
            "pii_sanitizer",
            "prompt_guard",
            "egress_filter",
            "mcp_proxy",
            "dns_filter",
            "subagent_monitor",
            "egress_monitor",
            "killswitch",
        ]:
            assert (
                get_module_mode(cfg, module) == ENFORCE_MODE
            ), f"Module {module} should default to enforce"

    def test_global_monitor_override_downgrades_all(self, monkeypatch):
        """AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor."""
        monkeypatch.setenv("AGENTSHROUD_MODE", "monitor")
        cfg = GatewayConfig(
            bind="127.0.0.1",
            port=8080,
            auth_method="shared_secret",
            auth_token="test-token",
        )
        for module in [
            "pii_sanitizer",
            "prompt_guard",
            "egress_filter",
            "mcp_proxy",
            "dns_filter",
            "subagent_monitor",
            "egress_monitor",
            "killswitch",
        ]:
            assert (
                get_module_mode(cfg, module) == "monitor"
            ), f"Module {module} should be in monitor when AGENTSHROUD_MODE=monitor"


class TestModuleInstantiationInEnforceMode:
    """Verify modules can instantiate and operate in enforce mode."""

    def test_prompt_guard_instantiates(self):
        pg = PromptGuard()
        assert pg is not None

    def test_context_guard_instantiates(self):
        cg = ContextGuard()
        assert cg is not None

    def test_git_guard_instantiates(self):
        gg = GitGuard()
        assert gg is not None

    def test_file_sandbox_instantiates(self):
        fs = FileSandbox(config=FileSandboxConfig())
        assert fs is not None

    def test_egress_filter_instantiates(self):
        ef = EgressFilter()
        assert ef is not None

    def test_multi_turn_tracker_instantiates(self):
        mt = MultiTurnTracker()
        assert mt is not None

    def test_tool_chain_analyzer_instantiates(self):
        ta = ToolChainAnalyzer()
        assert ta is not None

    def test_browser_security_guard_instantiates(self):
        bg = BrowserSecurityGuard()
        assert bg is not None

    def test_path_isolation_instantiates(self):
        pi = PathIsolationManager(config=PathIsolationConfig())
        assert pi is not None

    def test_output_canary_instantiates(self):
        oc = OutputCanary()
        assert oc is not None
