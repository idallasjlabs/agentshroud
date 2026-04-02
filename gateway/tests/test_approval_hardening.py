# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

"""Tests for approval queue hardening functionality."""

import json
import time
from unittest.mock import patch

import pytest

from gateway.security.approval_hardening import (
    ApprovalHardening,
    ApprovalHardeningConfig,
    DeceptionDetection,
    DeniedRequest,
)


class TestApprovalHardeningConfig:
    """Test approval hardening configuration."""

    def test_default_config(self):
        """Test default configuration values."""
        config = ApprovalHardeningConfig()

        assert config.enable_deception_detection is True
        assert config.always_show_full_parameters is True
        assert config.enable_repeat_request_blocking is True
        assert config.denied_request_cooldown_minutes == 5
        assert config.max_parameter_display_length == 0
        assert config.enable_risk_highlighting is True
        assert "rm" in config.high_risk_keywords
        assert "sudo" in config.high_risk_keywords

    def test_custom_config(self):
        """Test custom configuration values."""
        config = ApprovalHardeningConfig(
            enable_deception_detection=False,
            denied_request_cooldown_minutes=10,
            high_risk_keywords=["custom", "danger"],
        )

        assert config.enable_deception_detection is False
        assert config.denied_request_cooldown_minutes == 10
        assert config.high_risk_keywords == ["custom", "danger"]


class TestApprovalHardening:
    """Test approval hardening functionality."""

    @pytest.fixture
    def config(self):
        """Create test configuration."""
        return ApprovalHardeningConfig()

    @pytest.fixture
    def hardening(self, config):
        """Create approval hardening instance for testing."""
        return ApprovalHardening(config)

    def test_initialization(self, hardening):
        """Test hardening initialization."""
        assert isinstance(hardening.config, ApprovalHardeningConfig)
        assert len(hardening._denied_requests) == 0
        assert len(hardening._parameter_fingerprints) == 0

    def test_normalize_description_removes_misleading_phrases(self, hardening):
        """Test description normalization removes misleading language."""
        original = "I just need to simply check this harmless file"
        normalized = hardening._normalize_description(original)

        # Should remove "just", "simply", "harmless"
        assert "just" not in normalized.lower()
        assert "simply" not in normalized.lower()
        assert "harmless" not in normalized.lower()
        assert "need to check this file" in normalized

    def test_normalize_description_handles_empty(self, hardening):
        """Test normalization handles empty descriptions."""
        assert hardening._normalize_description("") == ""
        assert hardening._normalize_description(None) is None

    def test_deception_detection_benign_request(self, hardening):
        """Test deception detection with legitimate request."""
        detection = hardening.analyze_request(
            tool_name="read",
            description="Read configuration file",
            parameters={"path": "/app/config.yaml"},
            agent_id="test_agent",
        )

        assert detection.is_deceptive is False
        assert detection.risk_score <= 0.25
        assert len(detection.issues) == 0

    def test_deception_detection_misleading_description(self, hardening):
        """Test detection of misleading descriptions."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Just checking system status",
            parameters={"command": "rm -rf /important/data"},
            agent_id="test_agent",
        )

        assert detection.is_deceptive is True
        assert detection.risk_score >= 0.5
        assert len(detection.issues) > 0

        # Should detect mismatch between description and parameters
        mismatch_detected = any(
            "Description suggests benign action but parameters contain potentially dangerous commands"
            in issue
            for issue in detection.issues
        )
        assert mismatch_detected

    def test_deception_detection_destructive_command_not_indicated(self, hardening):
        """Test detection of destructive commands not indicated in description."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Run system maintenance",
            parameters={"command": "rm -rf /tmp/cache"},
            agent_id="test_agent",
        )

        assert len(detection.issues) > 0
        destructive_detected = any(
            "Destructive command execution not clearly indicated" in issue
            for issue in detection.issues
        )
        assert destructive_detected

    def test_deception_detection_downplaying_language(self, hardening):
        """Test detection of downplaying language."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Just quickly checking the logs",
            parameters={"command": "cat /var/log/secure"},
            agent_id="test_agent",
        )

        assert len(detection.issues) > 0
        downplay_detected = any(
            "downplaying language" in issue.lower() for issue in detection.issues
        )
        assert downplay_detected

    def test_deception_detection_authority_claims(self, hardening):
        """Test detection of authority/legitimacy claims."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Running authorized system maintenance as admin",
            parameters={"command": "systemctl restart service"},
            agent_id="test_agent",
        )

        assert len(detection.issues) > 0
        authority_detected = any(
            "authority or legitimacy claims" in issue.lower() for issue in detection.issues
        )
        assert authority_detected

    def test_parameter_obfuscation_detection_base64(self, hardening):
        """Test detection of base64-encoded parameters."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Execute encoded command",
            parameters={
                "command": "echo SGVsbG8gV29ybGQhIFRoaXMgaXMgYSBsb25nZXIgdGVzdA== | base64 -d"
            },  # Contains base64
            agent_id="test_agent",
        )

        base64_detected = any(
            "base64-encoded content" in issue.lower() for issue in detection.issues
        )
        assert base64_detected

    def test_parameter_obfuscation_detection_hex(self, hardening):
        """Test detection of hex-encoded parameters."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Execute command",
            parameters={"command": "echo \\x48\\x65\\x6c\\x6c\\x6f"},  # Hex encoded
            agent_id="test_agent",
        )

        hex_detected = any("hex-encoded content" in issue.lower() for issue in detection.issues)
        assert hex_detected

    def test_parameter_obfuscation_detection_url(self, hardening):
        """Test detection of URL-encoded parameters."""
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Execute command",
            parameters={"command": "curl http://example.com/path%20with%20spaces"},
            agent_id="test_agent",
        )

        url_detected = any("url-encoded content" in issue.lower() for issue in detection.issues)
        assert url_detected

    def test_repeat_request_pattern_detection(self, hardening):
        """Test detection of repeat request patterns."""
        tool_name = "exec"
        parameters = {"command": "dangerous_command"}
        agent_id = "test_agent"

        # First request
        detection1 = hardening.analyze_request(tool_name, "Run command", parameters, agent_id)

        # Second identical request
        detection2 = hardening.analyze_request(tool_name, "Run command", parameters, agent_id)

        # Should detect similar request
        repeat_detected = any(
            "Similar request parameters have been submitted recently" in issue
            for issue in detection2.issues
        )
        assert repeat_detected

    @patch("time.time")
    def test_cooldown_period_enforcement(self, mock_time, hardening):
        """Test cooldown period enforcement for denied requests."""
        tool_name = "exec"
        parameters = {"command": "rm -rf /"}
        agent_id = "test_agent"
        request_id = "req_123"

        # Mock time progression
        initial_time = 1000000000
        mock_time.return_value = initial_time

        # Record denied request
        hardening.record_denied_request(request_id, tool_name, parameters, agent_id)

        # Check if request is in cooldown immediately
        assert hardening.is_request_in_cooldown(tool_name, parameters, agent_id) is True

        # Advance time beyond cooldown period
        cooldown_seconds = hardening.config.denied_request_cooldown_minutes * 60
        mock_time.return_value = initial_time + cooldown_seconds + 1

        # Should no longer be in cooldown
        assert hardening.is_request_in_cooldown(tool_name, parameters, agent_id) is False

    @patch("time.time")
    def test_different_requests_not_in_cooldown(self, mock_time, hardening):
        """Test that different requests are not affected by cooldown."""
        initial_time = 1000000000
        mock_time.return_value = initial_time

        # Record denied request for one command
        hardening.record_denied_request("req_123", "exec", {"command": "rm file1"}, "test_agent")

        # Different command should not be in cooldown
        assert (
            hardening.is_request_in_cooldown("exec", {"command": "rm file2"}, "test_agent") is False
        )

    def test_cooldown_disabled_when_feature_disabled(self):
        """Test cooldown is disabled when feature is disabled."""
        config = ApprovalHardeningConfig(enable_repeat_request_blocking=False)
        hardening = ApprovalHardening(config)

        # Record denied request
        hardening.record_denied_request("req_123", "exec", {"command": "rm -rf /"}, "test_agent")

        # Should not be in cooldown when feature disabled
        assert (
            hardening.is_request_in_cooldown("exec", {"command": "rm -rf /"}, "test_agent") is False
        )

    def test_format_hardened_message_basic(self, hardening):
        """Test basic hardened message formatting."""
        tool_name = "exec"
        description = "Execute command"
        parameters = {"command": "ls -la"}

        detection = DeceptionDetection(
            is_deceptive=False, risk_score=0.0, normalized_description=description
        )

        message = hardening.format_hardened_message(tool_name, description, parameters, detection)

        assert "**Action:** Execute command" in message
        assert "**Tool:** exec" in message
        assert "**Parameters:**" in message
        assert "ls -la" in message

    def test_format_hardened_message_with_normalization(self, hardening):
        """Test hardened message formatting when description is normalized."""
        tool_name = "exec"
        original_description = "Just simply check the file"
        normalized_description = "check the file"
        parameters = {"command": "cat file.txt"}

        detection = DeceptionDetection(
            is_deceptive=False, risk_score=0.2, normalized_description=normalized_description
        )

        message = hardening.format_hardened_message(
            tool_name, original_description, parameters, detection
        )

        assert "**Original:**" in message
        assert original_description in message
        assert "**Normalized:**" in message
        assert normalized_description in message

    def test_format_hardened_message_with_security_concerns(self, hardening):
        """Test hardened message formatting with security concerns."""
        tool_name = "exec"
        description = "Check system"
        parameters = {"command": "rm -rf /"}

        detection = DeceptionDetection(
            is_deceptive=True,
            risk_score=0.8,
            normalized_description=description,
            issues=[
                "Destructive command not indicated in description",
                "Contains high-risk keywords",
            ],
        )

        message = hardening.format_hardened_message(tool_name, description, parameters, detection)

        assert "**⚠️ SECURITY CONCERNS:**" in message
        assert "Destructive command not indicated" in message
        assert "Contains high-risk keywords" in message
        assert "**Risk Level:** HIGH" in message

    def test_format_parameters_with_highlighting(self, hardening):
        """Test parameter formatting with risk highlighting."""
        parameters = {"command": "sudo rm -rf /important"}

        formatted = hardening._format_parameters_with_highlighting(parameters)

        # Should highlight dangerous keywords
        assert "⚠️ sudo ⚠️" in formatted
        assert "⚠️ rm ⚠️" in formatted

    def test_parameter_fingerprinting_consistency(self, hardening):
        """Test that parameter fingerprinting is consistent."""
        tool_name = "exec"
        parameters = {"command": "ls", "path": "/tmp"}

        fingerprint1 = hardening._create_parameter_fingerprint(tool_name, parameters)
        fingerprint2 = hardening._create_parameter_fingerprint(tool_name, parameters)

        assert fingerprint1 == fingerprint2

    def test_parameter_fingerprinting_different_params(self, hardening):
        """Test that different parameters create different fingerprints."""
        tool_name = "exec"
        params1 = {"command": "ls"}
        params2 = {"command": "cat"}

        fingerprint1 = hardening._create_parameter_fingerprint(tool_name, params1)
        fingerprint2 = hardening._create_parameter_fingerprint(tool_name, params2)

        assert fingerprint1 != fingerprint2

    @patch("time.time")
    def test_cleanup_old_denied_requests(self, mock_time, hardening):
        """Test cleanup of old denied requests."""
        initial_time = 1000000000
        mock_time.return_value = initial_time

        # Record denied request
        hardening.record_denied_request("req_old", "exec", {"command": "old_command"}, "test_agent")

        # Advance time beyond cleanup period
        cooldown_seconds = hardening.config.denied_request_cooldown_minutes * 60
        mock_time.return_value = initial_time + cooldown_seconds + 1

        # Record new request (should trigger cleanup)
        hardening.record_denied_request("req_new", "exec", {"command": "new_command"}, "test_agent")

        # Old request should be cleaned up
        assert len(hardening._denied_requests["test_agent"]) == 1
        assert hardening._denied_requests["test_agent"][0].request_id == "req_new"

    def test_get_stats(self, hardening):
        """Test getting hardening statistics."""
        stats = hardening.get_stats()

        assert "total_denied_requests" in stats
        assert "active_cooldowns" in stats
        assert "tracked_agents" in stats
        assert "config" in stats

        assert stats["total_denied_requests"] == 0
        assert stats["active_cooldowns"] == 0
        assert stats["tracked_agents"] == 0

        # Add some denied requests and check stats update
        hardening.record_denied_request("req_123", "exec", {"command": "test"}, "agent1")
        hardening.record_denied_request("req_456", "exec", {"command": "test2"}, "agent2")

        updated_stats = hardening.get_stats()
        assert updated_stats["total_denied_requests"] == 2
        assert updated_stats["active_cooldowns"] == 2
        assert updated_stats["tracked_agents"] == 2

    def test_deception_detection_disabled(self):
        """Test that deception detection can be disabled."""
        config = ApprovalHardeningConfig(enable_deception_detection=False)
        hardening = ApprovalHardening(config)

        # Even suspicious request should not be flagged
        detection = hardening.analyze_request(
            tool_name="exec",
            description="Just checking",
            parameters={"command": "rm -rf /"},
            agent_id="test_agent",
        )

        assert detection.is_deceptive is False
        assert detection.risk_score == 0.0
        assert len(detection.issues) == 0


class TestDeceptionDetection:
    """Test DeceptionDetection dataclass."""

    def test_basic_detection(self):
        """Test basic detection result creation."""
        detection = DeceptionDetection(
            is_deceptive=True,
            risk_score=0.8,
            issues=["Test issue"],
            normalized_description="Test description",
        )

        assert detection.is_deceptive is True
        assert detection.risk_score == 0.8
        assert detection.issues == ["Test issue"]
        assert detection.normalized_description == "Test description"

    def test_default_detection(self):
        """Test detection with default values."""
        detection = DeceptionDetection(is_deceptive=False, risk_score=0.0)

        assert len(detection.issues) == 0
        assert detection.normalized_description == ""


class TestDeniedRequest:
    """Test DeniedRequest dataclass."""

    def test_denied_request_creation(self):
        """Test denied request creation."""
        request = DeniedRequest(
            request_id="req_123",
            tool_name="exec",
            parameters={"command": "test"},
            denial_time=1000000000,
            agent_id="test_agent",
        )

        assert request.request_id == "req_123"
        assert request.tool_name == "exec"
        assert request.parameters == {"command": "test"}
        assert request.denial_time == 1000000000
        assert request.agent_id == "test_agent"


if __name__ == "__main__":
    pytest.main([__file__])
