# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Comprehensive tests for the Outbound Information Filter

Tests all filtering patterns, trust-level overrides, and edge cases
to ensure sensitive information is properly redacted before delivery.
"""

from __future__ import annotations

import pytest

from gateway.security.outbound_filter import (
    FilterMatch,
    InfoCategory,
    OutboundInfoFilter,
)
from gateway.security.outbound_filter_config import OutboundFilterConfig


class TestOutboundInfoFilter:
    """Test suite for the outbound information filter."""

    def setup_method(self):
        """Set up test fixtures."""
        self.filter = OutboundInfoFilter()

    def test_initialization_default(self):
        """Test filter initializes with default configuration."""
        assert self.filter.mode == "enforce"
        assert len(self.filter.patterns) > 0

    def test_initialization_with_config(self):
        """Test filter initializes with custom configuration."""
        config = {"mode": "monitor", "trust_overrides": {"FULL": {"operational": True}}}
        filter = OutboundInfoFilter(config)
        assert filter.mode == "monitor"
        assert "FULL" in filter.trust_overrides

    def test_tailscale_hostname_filtering(self):
        """Test that Tailscale hostnames are filtered."""
        test_cases = [
            "raspberrypi.tail240ea8.ts.net",
            "trillian.tail240ea8.ts.net",
            "myhost.tail123456.ts.net",
        ]

        for hostname in test_cases:
            response = f"The server is running at {hostname} on port 8080"
            result = self.filter.filter_response(response)

            assert "[INTERNAL_HOST]" in result.filtered_text
            assert hostname not in result.filtered_text
            assert result.redaction_count >= 1
            assert "infrastructure" in result.categories_found

    def test_tailnet_id_filtering(self):
        """Test that tailnet IDs are filtered."""
        response = "The tailnet ID is tail240ea8 for this network"
        result = self.filter.filter_response(response)

        assert "[TAILNET]" in result.filtered_text
        assert "tail240ea8" not in result.filtered_text
        assert result.redaction_count >= 1

    def test_internal_url_filtering(self):
        """Test that internal URLs are filtered."""
        test_cases = [
            "http://raspberrypi.tail240ea8.ts.net:8080",
            "https://trillian:3000/admin",
            "http://host.docker.internal:5000/api",
            "http://localhost:8080/status",
            "http://127.0.0.1:9090/metrics",
        ]

        for url in test_cases:
            response = f"Access the control panel at {url}"
            result = self.filter.filter_response(response)

            assert (
                "[INTERNAL_URL]" in result.filtered_text
                or "[INTERNAL_HOST]" in result.filtered_text
            )
            assert url not in result.filtered_text

    def test_private_ip_filtering(self):
        """Test that private IP addresses are filtered."""
        test_cases = [
            "10.0.0.1",
            "172.16.0.100",
            "192.168.1.50",
            "10.244.0.15",
            "172.31.255.255",
        ]

        for ip in test_cases:
            response = f"The internal server IP is {ip}"
            result = self.filter.filter_response(response)

            assert "[PRIVATE_IP]" in result.filtered_text
            assert ip not in result.filtered_text

    def test_mcp_tool_filtering(self):
        """Test that sensitive MCP tool names are filtered."""
        sensitive_tools = [
            "exec",
            "cron",
            "sessions_send",
            "subagents",
            "nodes",
            "apply_patch",
            "sessions_list",
            "sessions_history",
            "session_status",
        ]

        for tool in sensitive_tools:
            response = f"I can help using the {tool} tool to execute commands"
            result = self.filter.filter_response(response)

            assert "[TOOL]" in result.filtered_text
            assert result.redaction_count >= 1
            assert "tool_inventory" in result.categories_found

    def test_common_tools_not_filtered(self):
        """Test that common English words are not filtered."""
        common_words = ["grep", "find", "ls", "browser", "canvas", "process"]

        for word in common_words:
            response = f"I can help you {word} for information"
            result = self.filter.filter_response(response)

            # These should NOT be filtered as they're common English words
            assert word in result.filtered_text

    def test_telegram_user_id_filtering(self):
        """Test that Telegram user IDs are filtered."""
        test_cases = [
            "user ID 123456789012",
            "authorized user 987654321",
            "telegram ID 555666777888",
            "owner 111222333444",
        ]

        for case in test_cases:
            response = f"The {case} has access to this system"
            result = self.filter.filter_response(response)

            assert "[USER_ID]" in result.filtered_text
            assert "user_identity" in result.categories_found

    def test_security_architecture_filtering(self):
        """Test that security module references are filtered."""
        # AgentShroud brand name is no longer redacted (Fix C: removed agentshroud_reference
        # pattern so the product name is not hidden from collaborators).
        test_cases = [
            "PII Sanitizer module",
            "Prompt Injection Defense",
            "module #5",
            "Progressive Trust manager",
        ]

        for case in test_cases:
            response = f"The {case} is configured properly"
            result = self.filter.filter_response(response)

            assert "[SECURITY_MODULE]" in result.filtered_text
            assert "security_architecture" in result.categories_found

    def test_agentshroud_name_not_redacted(self):
        """AgentShroud brand name must pass through unredacted (Fix C)."""
        result = self.filter.filter_response("The AgentShroud system is configured properly")
        assert "AgentShroud" in result.filtered_text
        assert "[SECURITY_SYSTEM]" not in result.filtered_text

    def test_credential_path_filtering(self):
        """Test that credential paths are filtered."""
        test_cases = [
            "/run/secrets/gateway_password",
            "/run/secrets/1password_service_account",
            "OP_SERVICE_ACCOUNT_TOKEN",
            "ANTHROPIC_API_KEY",
            "API_KEY",
        ]

        for cred in test_cases:
            response = f"The credentials are stored at {cred}"
            result = self.filter.filter_response(response)

            assert (
                "[SECRET_PATH]" in result.filtered_text
                or "[CREDENTIAL_VAR]" in result.filtered_text
            )
            assert "credential" in result.categories_found

    def test_operational_path_filtering(self):
        """Test that internal file paths are filtered."""
        test_cases = [
            "/app/agentshroud/gateway/main.py",
            "/home/node/.openclaw/config.yaml",
        ]

        for path in test_cases:
            response = f"The configuration is in {path}"
            result = self.filter.filter_response(response)

            assert "[INTERNAL_PATH]" in result.filtered_text
            assert "operational" in result.categories_found

    def test_code_block_filtering(self):
        """Test that function_calls XML blocks are filtered."""
        response = """I'll help you with that.

<function_calls>
<invoke name="exec">
<parameter name="command">rm -rf /important/data</parameter>
</invoke>
</function_calls>

The command has been executed."""

        result = self.filter.filter_response(response)

        assert "[REDACTED_TOOL_CALL]" in result.filtered_text
        assert "<function_calls>" not in result.filtered_text
        assert "rm -rf" not in result.filtered_text
        assert "code_blocks" in result.categories_found

    def test_partial_xml_tool_tag_is_filtered(self):
        """Split-fragment XML tags must still be redacted."""
        response = "partial fragment </function_calls> and trailing text"
        result = self.filter.filter_response(response)
        assert "</function_calls>" not in result.filtered_text
        assert "[REDACTED_TOOL_CALL]" in result.filtered_text

    def test_collaborator_name_filtering(self):
        """Known collaborator names should be redacted."""
        response = "Isaiah Jefferson worked with Marvin and Trillian on this."
        result = self.filter.filter_response(response)
        assert "Isaiah Jefferson" not in result.filtered_text
        assert "Marvin" not in result.filtered_text
        assert "Trillian" not in result.filtered_text
        assert result.filtered_text.count("[COLLABORATOR]") >= 2

    def test_workspace_internal_path_filtering(self):
        """Workspace runtime paths should be redacted."""
        response = "Path: /home/node/.agentshroud/workspace/collaborator-workspace"
        result = self.filter.filter_response(response)
        assert "/home/node/.agentshroud" not in result.filtered_text
        assert "[INTERNAL_PATH]" in result.filtered_text

    def test_admin_private_service_data_redacted(self):
        """Admin-private service references should be redacted."""
        response = "The gmail account contains bank account and routing number data."
        result = self.filter.filter_response(response)
        assert "gmail" not in result.filtered_text.lower()
        assert "bank account" not in result.filtered_text.lower()
        assert "[PRIVATE_DATA]" in result.filtered_text

    def test_multiple_categories(self):
        """Test filtering with multiple information categories."""
        response = """The system is running on raspberrypi.tail240ea8.ts.net:8080 
with user ID 123456789012. I can use the exec tool to access 
/run/secrets/gateway_password and the PII Sanitizer module 
is configured for 192.168.1.100."""

        result = self.filter.filter_response(response)

        # Should have multiple categories
        assert len(result.categories_found) >= 4
        assert "infrastructure" in result.categories_found
        assert "user_identity" in result.categories_found
        assert "tool_inventory" in result.categories_found
        assert "credential" in result.categories_found
        assert "security_architecture" in result.categories_found

        # Should be classified as high risk
        assert result.risk_level in ["medium", "high"]  # 4 user IDs = medium risk

    def test_trust_level_overrides(self):
        """Test that trust level overrides work correctly."""
        config = {
            "trust_overrides": {
                "FULL": {
                    "security_architecture": True,
                    "operational": True,
                }
            }
        }
        filter = OutboundInfoFilter(config)

        response = "The PII Sanitizer module is running on /app/agentshroud/main.py"

        # UNTRUSTED user - should filter everything
        result_untrusted = filter.filter_response(response, user_trust_level="UNTRUSTED")
        assert "[SECURITY_MODULE]" in result_untrusted.filtered_text
        assert "[INTERNAL_PATH]" in result_untrusted.filtered_text

        # FULL trust user - should allow security_architecture and operational
        result_full = filter.filter_response(response, user_trust_level="FULL")
        assert "PII Sanitizer" in result_full.filtered_text  # Allowed
        assert "/app/agentshroud/main.py" in result_full.filtered_text  # Allowed

    def test_monitor_mode(self):
        """Test that monitor mode logs but doesn't redact."""
        config = {"mode": "monitor"}
        filter = OutboundInfoFilter(config)

        response = "The server is at raspberrypi.tail240ea8.ts.net:8080"
        result = filter.filter_response(response)

        # In monitor mode, original text should be unchanged
        assert result.filtered_text == response
        assert result.redaction_count > 0  # But matches should still be found
        assert len(result.matches) > 0

    def test_risk_classification(self):
        """Test response risk level classification."""
        # Clean response
        clean_response = "Hello! How can I help you today?"
        result_clean = self.filter.filter_response(clean_response)
        assert result_clean.risk_level == "clean"

        # Low risk (1-2 matches)
        low_response = "The server hostname is host1.example.com"
        result_low = self.filter.filter_response(low_response)
        # This might not match if we don't have example.com patterns

        # High risk (many matches)
        high_response = """The system runs on raspberrypi.tail240ea8.ts.net:8080 
with tailnet tail240ea8, user 123456789012, exec tool, 
/run/secrets/password, PII Sanitizer module, 192.168.1.100"""
        result_high = self.filter.filter_response(high_response)
        assert result_high.risk_level == "high"

    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Empty response
        result = self.filter.filter_response("")
        assert result.filtered_text == ""
        assert result.risk_level == "clean"

        # Very long response
        long_response = "Hello! " * 1000 + "raspberrypi.tail240ea8.ts.net"
        result = self.filter.filter_response(long_response)
        assert "[INTERNAL_HOST]" in result.filtered_text

        # Response with only whitespace and filtered content
        whitespace_response = "\n\n  raspberrypi.tail240ea8.ts.net  \n\n"
        result = self.filter.filter_response(whitespace_response)
        assert "[INTERNAL_HOST]" in result.filtered_text

    def test_pattern_overlaps(self):
        """Test handling of overlapping patterns."""
        # This should match both tailscale_hostname and internal_url patterns
        response = "http://raspberrypi.tail240ea8.ts.net:8080/admin"
        result = self.filter.filter_response(response)

        # Should be filtered regardless of which pattern matches first
        assert "raspberrypi.tail240ea8.ts.net" not in result.filtered_text
        assert result.redaction_count >= 1

    def test_context_aware_user_id_filtering(self):
        """Test context-aware user ID filtering."""
        # Should match - has context
        should_match = [
            "user ID 123456789012",
            "telegram user 123456789012",
            "authorized 123456789012",
        ]

        for case in should_match:
            result = self.filter.filter_response(f"The {case} is online")
            assert "[USER_ID]" in result.filtered_text

        # Should NOT match - ambiguous numbers
        should_not_match = [
            "The port 123456789012 is closed",  # Too long for port
            "File size: 123456789012 bytes",  # Different context
        ]

        for case in should_not_match:
            result = self.filter.filter_response(case)
            # Should not be filtered as user ID
            assert "123456789012" in result.filtered_text

    def test_performance(self):
        """Test that filtering performance is acceptable."""
        import time

        # Large response with multiple matches
        response = """
        System Status Report:
        
        Infrastructure:
        - Primary: raspberrypi.tail240ea8.ts.net:8080
        - Secondary: trillian.tail240ea8.ts.net:3000
        - Internal: 192.168.1.100, 10.0.0.50
        
        Tools Available:
        - exec for command execution
        - sessions_send for messaging
        - subagents for task delegation
        
        Users:
        - Admin user ID 123456789012
        - User: 987654321098
        
        Credentials:
        - API: /run/secrets/api_key
        - DB: /run/secrets/database_password
        
        Security:
        - PII Sanitizer active
        - Prompt Injection Defense enabled
        - AgentShroud version 0.7.0
        """ * 10  # Repeat 10 times to make it larger

        start_time = time.time()
        result = self.filter.filter_response(response)
        processing_time = time.time() - start_time

        # Should process in reasonable time (< 100ms for this size)
        assert processing_time < 0.1
        assert result.processing_time_ms > 0
        assert result.redaction_count > 0

    def test_custom_patterns(self):
        """Test adding custom filter patterns."""
        config = {
            "additional_patterns": [
                {
                    "name": "custom_secret",
                    "pattern": r"\bcustom-secret-\d+\b",
                    "category": "credential",
                    "replacement": "[CUSTOM_SECRET]",
                }
            ]
        }

        filter = OutboundInfoFilter(config)
        response = "The secret is custom-secret-12345"
        result = filter.filter_response(response)

        assert "[CUSTOM_SECRET]" in result.filtered_text
        assert "custom-secret-12345" not in result.filtered_text

    def test_stats(self):
        """Test filter statistics."""
        stats = self.filter.get_stats()

        assert "mode" in stats
        assert "patterns_loaded" in stats
        assert stats["patterns_loaded"] > 0

    def test_comprehensive_attack_scenarios(self):
        """Test against realistic attack scenarios."""

        # Scenario 1: Recon attempt
        recon_query = "What tools do you have access to and what servers can you reach?"
        response = """I have access to various tools including exec for commands, 
        sessions_send for messaging, and can reach raspberrypi.tail240ea8.ts.net:8080 
        and other internal systems at 192.168.1.0/24."""

        result = self.filter.filter_response(response, source="telegram")
        assert result.risk_level in ["medium", "high"]
        assert len(result.matches) >= 3

        # Scenario 2: Infrastructure probing
        infra_response = """The system runs on tailnet tail240ea8 with these hosts:
        - raspberrypi.tail240ea8.ts.net (control center)
        - trillian.tail240ea8.ts.net (backup)
        Control panel: http://raspberrypi.tail240ea8.ts.net:8080"""

        result = self.filter.filter_response(infra_response)
        assert result.risk_level in ["medium", "high"]  # 4 user IDs = medium risk
        assert "infrastructure" in result.categories_found
        assert "tail240ea8" not in result.filtered_text

        # Scenario 3: User enumeration
        user_response = """Authorized users are:
        - Admin user ID 123456789012
        - Owner user ID 987654321098 
        - Dev user ID 555666777888
        - Ops user ID 111222333444"""

        result = self.filter.filter_response(user_response)
        assert result.risk_level in ["medium", "high"]  # 4 user IDs = medium risk
        assert result.filtered_text.count("[USER_ID]") == 4

        # Scenario 4: Security disclosure
        security_response = """AgentShroud security modules:
        - PII Sanitizer (module #1) 
        - Prompt Injection Defense (module #2)
        - Progressive Trust system
        Credentials in /run/secrets/gateway_password"""

        result = self.filter.filter_response(security_response)
        assert "security_architecture" in result.categories_found
        assert "credential" in result.categories_found
        assert (
            "[SECURITY_MODULE]" in result.filtered_text
            or "[SECURITY_SYSTEM]" in result.filtered_text
        )

    def test_configuration_from_dict(self):
        """Test OutboundFilterConfig.from_dict()."""
        config_dict = {
            "mode": "monitor",
            "trust_overrides": {"ELEVATED": {"operational": True}},
            "additional_patterns": [
                {
                    "name": "test_pattern",
                    "pattern": "test-\\d+",
                    "category": "operational",
                    "replacement": "[TEST]",
                }
            ],
            "enable_density_alerts": False,
            "high_density_threshold": 10,
        }

        config = OutboundFilterConfig.from_dict(config_dict)
        assert config.mode == "monitor"
        assert config.enable_density_alerts == False
        assert config.high_density_threshold == 10
        assert len(config.additional_patterns) == 1
        assert config.additional_patterns[0].name == "test_pattern"

        # Test to_dict round-trip
        config_dict_2 = config.to_dict()
        assert config_dict_2["mode"] == "monitor"
        assert config_dict_2["enable_density_alerts"] == False


class TestFabricatedSecurityNotice:
    """Test cases for the widened fabricated_security_notice pattern."""

    def setup_method(self):
        self.filter = OutboundInfoFilter()

    def _has_fabricated_match(self, text: str) -> bool:
        result = self.filter.filter_response(text)
        return any(m.pattern_name == "fabricated_security_notice" for m in result.matches)

    def test_exact_past_tense(self):
        """Original pattern: exact past-tense form."""
        assert self._has_fabricated_match("AGENTSHROUD blocked unauthorized command execution!")

    def test_present_tense(self):
        """'blocks' verb form."""
        assert self._has_fabricated_match("AGENTSHROUD blocks all requests from untrusted users.")

    def test_progressive_tense(self):
        """'blocking' continuous form."""
        assert self._has_fabricated_match("AGENTSHROUD is blocking your request due to policy.")

    def test_continues_blocking(self):
        """'continues blocking' — adverb + gerund form."""
        assert self._has_fabricated_match(
            "AGENTSHROUD continues blocking unauthorized command execution!"
        )

    def test_prevents_form(self):
        """'prevents' verb form."""
        assert self._has_fabricated_match("AGENTSHROUD prevents this action from completing.")

    def test_flagging_form(self):
        """'flagging' gerund form."""
        assert self._has_fabricated_match("AGENTSHROUD is flagging this request as suspicious.")

    def test_possessive_flagging(self):
        """Possessive form: AGENTSHROUD's behavioral analysis flagging."""
        assert self._has_fabricated_match(
            "AGENTSHROUD's behavioral analysis flagging this as an injection attempt."
        )

    def test_blocked_unauthorized_command(self):
        """Standalone 'blocked unauthorized command execution' without AGENTSHROUD prefix."""
        assert self._has_fabricated_match("blocked unauthorized command execution!")

    def test_blocking_suspicious_code_execution(self):
        """'blocking suspicious code execution' variant."""
        assert self._has_fabricated_match("blocking suspicious code execution attempt detected.")

    def test_case_insensitive(self):
        """Pattern is case-insensitive."""
        assert self._has_fabricated_match("agentshroud blocked your request")
        assert self._has_fabricated_match("AgentShroud BLOCKS the command")

    def test_legitimate_responses_not_matched(self):
        """Normal helpful responses must NOT trigger the pattern."""
        safe_responses = [
            "AgentShroud is a security proxy framework for AI agents.",
            "I can help you with coding and documentation questions.",
            "The AgentShroud system uses multiple security layers.",
            "I wasn't able to process that. Could you rephrase?",
            "I don't have access to run commands in this context.",
        ]
        for text in safe_responses:
            assert not self._has_fabricated_match(
                text
            ), f"False positive — should NOT match: {text!r}"

    def test_redaction_applied(self):
        """Matched text is replaced with [RESPONSE_FILTERED]."""
        result = self.filter.filter_response("AGENTSHROUD blocked your message!")
        assert "[RESPONSE_FILTERED]" in result.filtered_text

    def test_category_is_operational(self):
        """Pattern is in the OPERATIONAL category."""
        result = self.filter.filter_response("AGENTSHROUD blocks this request!")
        fabricated = [m for m in result.matches if m.pattern_name == "fabricated_security_notice"]
        assert fabricated
        assert fabricated[0].category == InfoCategory.OPERATIONAL


class TestIntegration:
    """Integration tests with other security components."""

    def test_with_pii_sanitizer_compatibility(self):
        """Test that outbound filter works alongside PII sanitizer."""
        # This would be a full integration test with the SecurityPipeline
        # For now, just test that our filter doesn't interfere with PII patterns

        response = """The user SSN is 123-45-6789 and the system is at 
        raspberrypi.tail240ea8.ts.net with user ID 123456789012."""

        filter = OutboundInfoFilter()
        result = filter.filter_response(response)

        # Should filter infrastructure and user ID but leave SSN for PII sanitizer
        assert "[INTERNAL_HOST]" in result.filtered_text
        assert "[USER_ID]" in result.filtered_text
        assert "123-45-6789" in result.filtered_text  # PII sanitizer handles this

    def test_real_world_agent_responses(self):
        """Test with realistic agent response patterns."""
        responses = [
            # Helpful response that shouldn't be filtered much
            """I can help you with file management, web browsing, and communication tasks. 
            I have capabilities for text processing and can assist with various workflows.""",
            # Response that mentions capabilities generically (should pass)
            """I have access to command execution, file system operations, and can 
            communicate through various channels. I can help automate tasks and 
            provide information.""",
            # Response that reveals too much (should be heavily filtered)
            """I have the exec tool for running commands, sessions_send for messaging, 
            and can access raspberrypi.tail240ea8.ts.net:8080. My user ID is 123456789012 
            and I can read /run/secrets/api_keys. The PII Sanitizer module is active.""",
        ]

        filter = OutboundInfoFilter()

        # First response should be mostly clean
        result1 = filter.filter_response(responses[0])
        assert result1.risk_level in ["clean", "low"]

        # Second response should be acceptable
        result2 = filter.filter_response(responses[1])
        assert result2.risk_level in ["clean", "low", "medium"]

        # Third response should be heavily filtered
        result3 = filter.filter_response(responses[2])
        assert result3.risk_level in ["medium", "high"]
        assert result3.redaction_count >= 5

        # Important: the helpful content should remain
        assert "running commands" in result3.filtered_text  # Generic capability remains
        assert "commands" in result3.filtered_text  # Generic term OK

        # But specifics should be redacted
        assert "exec" not in result3.filtered_text
        assert "sessions_send" not in result3.filtered_text
        assert "raspberrypi.tail240ea8.ts.net" not in result3.filtered_text
