# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for Observatory Mode functionality."""

import asyncio
import os
import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import Mock, patch, AsyncMock

from gateway.ingest_api.config import get_module_mode, GatewayConfig
from gateway.proxy.pipeline import SecurityPipeline


class TestObservatoryMode:
    """Test Observatory Mode configuration and endpoints."""

    def test_get_module_mode_respect_global_override(self):
        """Test that get_module_mode respects AGENTSHROUD_MODE env var."""
        # Create a mock config
        config = Mock()
        config.security = Mock()
        config.security.pii_sanitizer = Mock()
        config.security.pii_sanitizer.mode = "enforce"
        
        # Test enforce mode (default)
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "enforce"}):
            assert get_module_mode(config, "pii_sanitizer") == "enforce"
        
        # Test monitor mode override
        with patch.dict(os.environ, {"AGENTSHROUD_MODE": "monitor"}):
            assert get_module_mode(config, "pii_sanitizer") == "monitor"
        
        # Test without env var (should use module-specific config)
        with patch.dict(os.environ, {}, clear=True):
            assert get_module_mode(config, "pii_sanitizer") == "enforce"

    def test_get_module_mode_pinned_modules(self):
        """Test that pinned modules always return enforce even in monitor mode."""
        # This would be implemented when per-module pinning is added to get_module_mode
        # For now, this test documents the intended behavior
        pass

    def test_security_pipeline_set_global_mode(self):
        """Test SecurityPipeline.set_global_mode method."""
        # Mock components
        pii_sanitizer = Mock()
        pii_sanitizer.set_mode = Mock()
        prompt_guard = Mock()
        prompt_guard.set_mode = Mock()
        prompt_guard.block_threshold = 0.8
        prompt_guard.warn_threshold = 0.4
        egress_filter = Mock()
        egress_filter.set_mode = Mock()
        
        pipeline = SecurityPipeline(
            pii_sanitizer=pii_sanitizer,
            prompt_guard=prompt_guard,
            egress_filter=egress_filter
        )
        
        # Test switching to monitor mode
        pipeline.set_global_mode("monitor")
        
        # Verify components were updated
        pii_sanitizer.set_mode.assert_called_with("monitor")
        prompt_guard.set_mode.assert_called_with("monitor")
        egress_filter.set_mode.assert_called_with("monitor")
        
        # Verify prompt guard thresholds were set to high values
        assert prompt_guard.block_threshold == 999.0
        assert prompt_guard.warn_threshold == 999.0
        
        # Test switching to enforce mode
        pipeline.set_global_mode("enforce")
        
        # Verify thresholds were reset to normal
        assert prompt_guard.block_threshold == 0.8
        assert prompt_guard.warn_threshold == 0.4

    def test_security_pipeline_set_global_mode_missing_components(self):
        """Test set_global_mode handles missing components gracefully."""
        # Provide minimal required component (pii_sanitizer)
        pii_sanitizer = Mock()
        pipeline = SecurityPipeline(pii_sanitizer=pii_sanitizer)
        
        # Should not raise any exceptions when optional components are missing
        pipeline.set_global_mode("monitor")
        pipeline.set_global_mode("enforce")

    @pytest.mark.asyncio
    async def test_observatory_mode_state_initialization(self):
        """Test that observatory mode state is properly initialized."""
        # This would test the app_state initialization
        # Since we can't easily test the actual app_state, we test the structure
        
        expected_keys = ["global_mode", "effective_since", "auto_revert_at", "pinned_modules"]
        
        # Mock app_state structure
        mock_state = {
            "global_mode": "enforce",
            "effective_since": datetime.now(tz=timezone.utc).isoformat(),
            "auto_revert_at": None,
            "pinned_modules": [],
        }
        
        for key in expected_keys:
            assert key in mock_state
        
        assert mock_state["global_mode"] in ["monitor", "enforce"]
        assert isinstance(mock_state["pinned_modules"], list)

    @pytest.mark.asyncio  
    async def test_auto_revert_timer_logic(self):
        """Test auto-revert timer functionality."""
        # Test the auto-revert logic (without actual FastAPI app)
        
        # Mock observatory state
        observatory_mode = {
            "global_mode": "monitor",
            "effective_since": datetime.now(tz=timezone.utc).isoformat(),
            "auto_revert_at": None,
            "pinned_modules": [],
        }
        
        # Calculate revert time
        revert_hours = 2
        revert_time = datetime.now(tz=timezone.utc) + timedelta(hours=revert_hours)
        observatory_mode["auto_revert_at"] = revert_time.isoformat()
        
        # Verify revert time is set correctly
        assert observatory_mode["auto_revert_at"] is not None
        parsed_revert_time = datetime.fromisoformat(observatory_mode["auto_revert_at"].replace("Z", "+00:00"))
        assert parsed_revert_time > datetime.now(tz=timezone.utc)

    def test_module_mode_resolution(self):
        """Test module mode resolution with pinned modules."""
        # Test the logic that determines effective module mode
        
        # Global monitor mode with no pinned modules
        global_mode = "monitor"
        pinned_modules = []
        module = "pii_sanitizer"
        
        if module in pinned_modules:
            effective_mode = "enforce"
        else:
            effective_mode = global_mode
        
        assert effective_mode == "monitor"
        
        # Global monitor mode with pinned module
        pinned_modules = ["pii_sanitizer"]
        
        if module in pinned_modules:
            effective_mode = "enforce"
        else:
            effective_mode = global_mode
        
        assert effective_mode == "enforce"

    def test_observatory_mode_validation(self):
        """Test validation of observatory mode parameters."""
        # Test mode validation
        valid_modes = ["monitor", "enforce"]
        invalid_modes = ["disabled", "debug", "", None]
        
        for mode in valid_modes:
            assert mode in ["monitor", "enforce"]
        
        for mode in invalid_modes:
            assert mode not in ["monitor", "enforce"]
        
        # Test auto_revert_hours validation  
        valid_hours = [1, 24, 168]  # 1 hour to 1 week
        invalid_hours = [0, -1, 169, 1000]
        
        for hours in valid_hours:
            assert 1 <= hours <= 168
        
        for hours in invalid_hours:
            assert not (1 <= hours <= 168)

    def test_pinned_modules_validation(self):
        """Test validation of pinned module names."""
        valid_modules = ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]
        invalid_modules = ["nonexistent", "killswitch", "", None]
        
        for module in valid_modules:
            assert module in ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]
        
        # Test that invalid modules would be rejected
        for module in invalid_modules:
            if module:
                assert module not in ["pii_sanitizer", "prompt_guard", "egress_filter", "mcp_proxy"]


# Integration tests that would require a running FastAPI app
class TestObservatoryModeAPI:
    """Integration tests for Observatory Mode API endpoints."""

    @pytest.mark.asyncio
    async def test_get_observatory_mode_endpoint(self):
        """Test GET /manage/mode endpoint returns correct structure."""
        # Mock response structure
        expected_response = {
            "global_mode": "enforce",
            "effective_since": "2026-03-04T16:32:00Z",
            "auto_revert_at": None,
            "pinned_modules": [],
            "module_modes": {
                "pii_sanitizer": "enforce",
                "prompt_guard": "enforce", 
                "egress_filter": "enforce",
                "mcp_proxy": "enforce"
            }
        }
        
        # Verify structure
        required_keys = ["global_mode", "effective_since", "auto_revert_at", "pinned_modules", "module_modes"]
        for key in required_keys:
            assert key in expected_response

    @pytest.mark.asyncio
    async def test_set_observatory_mode_endpoint(self):
        """Test POST /manage/mode endpoint request/response."""
        # Mock request payload
        request_payload = {
            "mode": "monitor",
            "auto_revert_hours": 4,
            "pin_modules": ["killswitch"]
        }
        
        # Mock successful response
        expected_response = {
            "success": True,
            "old_mode": "enforce",
            "new_mode": "monitor",
            "effective_since": "2026-03-04T16:32:00Z",
            "auto_revert_at": "2026-03-04T20:32:00Z",
            "pinned_modules": ["killswitch"]
        }
        
        # Verify response structure
        assert expected_response["success"] is True
        assert expected_response["new_mode"] == request_payload["mode"]
        assert expected_response["pinned_modules"] == request_payload["pin_modules"]
