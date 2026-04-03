# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the Output Canary System."""

from __future__ import annotations

import time
import uuid
from unittest.mock import patch

import pytest

from gateway.security.output_canary import CanaryConfig, CanaryResult, OutputCanary


class TestOutputCanary:
    """Test cases for the Output Canary System."""

    def setup_method(self):
        """Set up test fixtures."""
        self.config = CanaryConfig(
            canary_length=16,  # Shorter for testing
            use_zero_width_chars=True,
            use_unicode_tags=True,
            use_comment_markers=True,
            log_incidents=False,  # Disable logging in tests
            block_on_detection=True,
            max_canaries_per_session=2,
        )
        self.canary_system = OutputCanary(self.config)
        self.test_session_id = "test-session-123"

    def test_canary_generation_per_session(self):
        """Test that unique canaries are generated per session."""
        # Generate canary for test session
        canary1 = self.canary_system.generate_canary(self.test_session_id)
        assert canary1 is not None
        assert len(canary1) > 0

        # Generate another canary for same session (should work up to max)
        canary2 = self.canary_system.generate_canary(self.test_session_id)
        assert canary2 is not None
        assert canary2 != canary1  # Different canaries

        # Try to generate a third canary (should fail due to max limit)
        with pytest.raises(ValueError, match="already has maximum canaries"):
            self.canary_system.generate_canary(self.test_session_id)

    def test_different_sessions_get_different_canaries(self):
        """Test that different sessions get different canaries."""
        session1 = "session-1"
        session2 = "session-2"

        canary1 = self.canary_system.generate_canary(session1)
        canary2 = self.canary_system.generate_canary(session2)

        assert canary1 != canary2

        # Check internal state
        assert session1 in self.canary_system._session_canaries
        assert session2 in self.canary_system._session_canaries
        assert len(self.canary_system._session_canaries[session1]) == 1
        assert len(self.canary_system._session_canaries[session2]) == 1

    def test_leaked_canary_detected_in_response(self):
        """Test that leaked canaries are detected in responses."""
        # Generate a canary
        canary = self.canary_system.generate_canary(self.test_session_id)

        # Get the base canary (without invisible chars)
        canary_data = list(self.canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Create a response that contains the base canary
        leaked_response = f"The system prompt contains: {base_canary} and other content."

        # Check the response
        result = self.canary_system.check_response(self.test_session_id, leaked_response)

        assert result.canary_detected is True
        assert result.session_id == self.test_session_id
        assert len(result.matches_found) > 0
        assert base_canary in result.matches_found[0]
        assert result.risk_level in ["medium", "high"]
        assert result.incident_id is not None

    def test_clean_response_passes(self):
        """Test that clean responses pass without detection."""
        # Generate a canary
        self.canary_system.generate_canary(self.test_session_id)

        # Create a clean response
        clean_response = "This is a normal response without any canaries."

        # Check the response
        result = self.canary_system.check_response(self.test_session_id, clean_response)

        assert result.canary_detected is False
        assert result.session_id == self.test_session_id
        assert len(result.matches_found) == 0
        assert result.risk_level == "low"
        assert result.incident_id is None

    def test_partial_canary_match_handling(self):
        """Test handling of partial canary matches."""
        # Set up config for longer canaries to test partial matching
        config = CanaryConfig(canary_length=20, log_incidents=False)
        canary_system = OutputCanary(config)

        # Generate a canary
        canary = canary_system.generate_canary(self.test_session_id)

        # Get the base canary
        canary_data = list(canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Create response with partial canary (8+ chars should match)
        partial_canary = base_canary[:10]  # Take first 10 characters
        response_with_partial = f"Some text with partial leak: {partial_canary} end."

        # Check the response
        result = canary_system.check_response(self.test_session_id, response_with_partial)

        assert result.canary_detected is True
        assert result.detection_method == "partial_match"
        assert result.risk_level == "medium"

    def test_session_without_canary_returns_safe_result(self):
        """Test that sessions without canaries return safe results."""
        # Check response for session with no canaries
        result = self.canary_system.check_response("nonexistent-session", "Any response text")

        assert result.canary_detected is False
        assert result.session_id == "nonexistent-session"
        assert result.canary_id == "none"
        assert result.risk_level == "low"
        assert result.incident_id is None

    def test_status_reporting(self):
        """Test canary status reporting for dashboard."""
        # Test status for session without canaries
        status = self.canary_system.get_status("nonexistent-session")
        assert status["status"] == "red"
        assert status["canary_count"] == 0
        assert status["active_canaries"] == 0
        assert status["compromised_canaries"] == 0
        assert status["protection_level"] == "none"

        # Generate a canary and test active status
        self.canary_system.generate_canary(self.test_session_id)
        status = self.canary_system.get_status(self.test_session_id)
        assert status["status"] == "green"
        assert status["canary_count"] == 1
        assert status["active_canaries"] == 1
        assert status["compromised_canaries"] == 0
        assert status["protection_level"] == "protected"

        # Simulate a compromise by triggering detection
        canary_data = list(self.canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Detect the canary (simulates compromise)
        self.canary_system.check_response(self.test_session_id, f"Leaked: {base_canary}")

        # Check compromised status
        status = self.canary_system.get_status(self.test_session_id)
        assert status["status"] == "red"
        assert status["compromised_canaries"] == 1
        assert status["protection_level"] == "compromised"

    def test_invisible_canary_creation(self):
        """Test that invisible canaries are created properly."""
        base_canary = "testcanary123456"
        canary_id = "test-canary-1"

        invisible = self.canary_system._create_invisible_canary(base_canary, canary_id)

        # Should contain the base canary
        assert base_canary in invisible

        # Should be longer than base canary due to invisible chars
        assert len(invisible) > len(base_canary)

        # Should contain comment marker if enabled
        if self.config.use_comment_markers:
            assert "<!--" in invisible
            assert canary_id in invisible

    def test_detection_patterns_creation(self):
        """Test that detection patterns are created correctly."""
        base_canary = "testcanary123"
        patterns = self.canary_system._create_detection_patterns(base_canary)

        # Should have multiple patterns
        assert len(patterns) >= 3

        # First pattern should match exact canary
        exact_pattern = patterns[0]
        assert exact_pattern.search(base_canary) is not None
        assert exact_pattern.search("different text") is None

    def test_canary_cleanup(self):
        """Test cleanup of expired canaries."""
        # Generate canaries for multiple sessions
        session1 = "session-1"
        session2 = "session-2"

        self.canary_system.generate_canary(session1)
        self.canary_system.generate_canary(session2)

        # Manually set creation time to past for session1
        old_time = time.time() - 7200  # 2 hours ago
        for canary_data in self.canary_system._session_canaries[session1].values():
            canary_data["created_at"] = old_time

        # Clean up with 1 hour max age
        cleaned = self.canary_system.cleanup_expired_canaries(max_age_seconds=3600)

        # Should have cleaned up session1 canaries
        assert cleaned == 1
        assert session1 not in self.canary_system._session_canaries
        assert session2 in self.canary_system._session_canaries

    def test_zero_width_character_detection(self):
        """Test detection of canaries with zero-width characters."""
        # Generate canary
        self.canary_system.generate_canary(self.test_session_id)

        # Get base canary
        canary_data = list(self.canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Create text with zero-width chars inserted
        zw_canary = ""
        for i, char in enumerate(base_canary):
            zw_canary += char
            if i < len(base_canary) - 1:
                zw_canary += "\u200b"  # Add zero-width space

        # Check detection
        result = self.canary_system.check_response(self.test_session_id, f"Leaked: {zw_canary}")
        assert result.canary_detected is True
        assert result.detection_method == "zero_width_match"

    def test_unicode_normalization_resistance(self):
        """Test that canaries work with different Unicode representations."""
        # Generate canary
        self.canary_system.generate_canary(self.test_session_id)

        # Get base canary
        canary_data = list(self.canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Test with different case
        result = self.canary_system.check_response(
            self.test_session_id, f"Leaked: {base_canary.upper()}"
        )
        assert result.canary_detected is True  # Should be case-insensitive

    @patch("gateway.security.output_canary.logger")
    def test_incident_logging(self, mock_logger):
        """Test that incidents are logged when enabled."""
        # Enable incident logging
        config = CanaryConfig(log_incidents=True)
        canary_system = OutputCanary(config)

        # Generate canary and trigger detection
        canary_system.generate_canary(self.test_session_id)
        canary_data = list(canary_system._session_canaries[self.test_session_id].values())[0]
        base_canary = canary_data["base_canary"]

        # Trigger detection
        canary_system.check_response(self.test_session_id, f"Leaked: {base_canary}")

        # Check that warning was logged
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args[0][0]
        assert "CANARY DETECTED" in call_args
        assert self.test_session_id in call_args
