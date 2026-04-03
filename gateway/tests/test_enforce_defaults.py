# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test enforce-by-default functionality for core security modules."""

import os
from unittest.mock import Mock, patch

import pytest

from gateway.ingest_api.config import (
    SecurityConfig,
    SecurityModuleConfig,
    check_monitor_mode_warnings,
    get_module_mode,
)


class TestEnforceDefaults:
    """Test that core security modules default to enforce mode."""

    def test_security_module_config_defaults(self):
        """Test that SecurityModuleConfig defaults to enforce mode."""
        config = SecurityModuleConfig()
        assert config.mode == "enforce"

    def test_pii_sanitizer_default_action(self):
        """Test that PII sanitizer defaults to redact action."""
        security_config = SecurityConfig()
        assert security_config.pii_sanitizer.action == "redact"

    def test_security_config_all_defaults_enforce(self):
        """Test that all core modules default to enforce mode."""
        security_config = SecurityConfig()
        assert security_config.pii_sanitizer.mode == "enforce"
        assert security_config.prompt_guard.mode == "enforce"
        assert security_config.egress_filter.mode == "enforce"
        assert security_config.mcp_proxy.mode == "enforce"

    @patch.dict(os.environ, {}, clear=True)
    def test_get_module_mode_no_override(self):
        """Test get_module_mode returns enforce when no override set."""
        mock_config = Mock()
        mock_config.security = SecurityConfig()

        mode = get_module_mode(mock_config, "pii_sanitizer")
        assert mode == "enforce"

    @patch.dict(os.environ, {"AGENTSHROUD_MODE": "monitor"}, clear=True)
    def test_get_module_mode_with_override(self):
        """Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor."""
        mock_config = Mock()
        mock_config.security = SecurityConfig()

        mode = get_module_mode(mock_config, "pii_sanitizer")
        assert mode == "monitor"

    @patch.dict(os.environ, {"AGENTSHROUD_MODE": "enforce"}, clear=True)
    def test_get_module_mode_enforce_override(self):
        """Test get_module_mode returns enforce when explicitly set."""
        mock_config = Mock()
        mock_config.security = SecurityConfig()

        mode = get_module_mode(mock_config, "pii_sanitizer")
        assert mode == "enforce"

    @patch.dict(os.environ, {}, clear=True)
    def test_monitor_mode_warnings_no_warnings_in_enforce(self):
        """Test that no warnings are logged when all modules are in enforce mode."""
        mock_logger = Mock()
        mock_config = Mock()
        mock_config.security = SecurityConfig()  # All defaults to enforce

        check_monitor_mode_warnings(mock_config, mock_logger)

        # Should not call warning for any module
        assert not mock_logger.warning.called

    @patch.dict(os.environ, {"AGENTSHROUD_MODE": "monitor"}, clear=True)
    def test_monitor_mode_warnings_all_modules(self):
        """Test that warnings are logged for all core modules in monitor mode."""
        mock_logger = Mock()
        mock_config = Mock()
        mock_config.security = SecurityConfig()

        check_monitor_mode_warnings(mock_config, mock_logger)

        # Should warn for each of the 8 core modules (expanded in v0.8.0)
        assert mock_logger.warning.call_count == 8
        warning_calls = [call[0][0] for call in mock_logger.warning.call_args_list]

        assert any("pii_sanitizer" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("prompt_guard" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("egress_filter" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("mcp_proxy" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("dns_filter" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("subagent_monitor" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("egress_monitor" in call and "MONITOR mode" in call for call in warning_calls)
        assert any("killswitch" in call and "MONITOR mode" in call for call in warning_calls)

    def test_monitor_mode_warning_message_format(self):
        """Test that monitor mode warnings contain required information."""
        mock_logger = Mock()
        mock_config = Mock()
        # Create config with one module in monitor mode
        security_config = SecurityConfig()
        security_config.pii_sanitizer.mode = "monitor"
        mock_config.security = security_config

        with patch.dict(os.environ, {}, clear=True):
            check_monitor_mode_warnings(mock_config, mock_logger)

        # Should warn for the one monitor mode module
        mock_logger.warning.assert_called_once()
        warning_msg = mock_logger.warning.call_args[0][0]

        assert "SECURITY: Module pii_sanitizer is in MONITOR mode" in warning_msg
        assert "Threats will be logged but NOT blocked" in warning_msg
        assert "Set mode: enforce" in warning_msg


class TestModuleEnforcement:
    """Test that individual modules respect the enforce/monitor mode."""

    def test_pii_sanitizer_mode_param(self):
        """Test PIISanitizer accepts and stores mode parameter."""
        from gateway.ingest_api.config import PIIConfig
        from gateway.ingest_api.sanitizer import PIISanitizer

        config = PIIConfig()
        sanitizer = PIISanitizer(config, mode="monitor", action="redact")

        assert sanitizer.get_mode() == "monitor"
        assert sanitizer.enforcement_action == "redact"

    def test_pii_sanitizer_default_enforcement(self):
        """Test PIISanitizer defaults to enforce mode."""
        from gateway.ingest_api.config import PIIConfig
        from gateway.ingest_api.sanitizer import PIISanitizer

        config = PIIConfig()
        sanitizer = PIISanitizer(config)

        assert sanitizer.get_mode() == "enforce"
        assert sanitizer.enforcement_action == "redact"
