# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud. All rights reserved.

import pytest
from unittest.mock import MagicMock, patch
import time


class TestEnhancedStatus:
    """Test enhanced status endpoint with observatory mode and egress info."""

    def test_status_response_model(self):
        """Test that StatusResponse model accepts new fields."""
        from gateway.ingest_api.models import StatusResponse
        
        resp = StatusResponse(
            status="healthy",
            version="0.8.0",
            uptime_seconds=100.0,
            ledger_entries=0,
            pending_approvals=0,
            pii_engine="regex",
            config_loaded=True,
            observatory_mode={
                "global_mode": "enforce",
                "effective_since": "2026-01-01T00:00:00Z",
                "auto_revert_at": None,
            },
            security_summary={
                "modules_active": 33,
                "modules_enforcing": 33,
                "modules_monitoring": 0,
                "blocked_today": 0,
                "canary_status": "green",
            },
            egress={
                "pending_approvals": 0,
                "rules_count": 5,
                "blocked_today": 0,
                "allowed_today": 10,
            },
        )
        
        assert resp.version == "0.8.0"
        assert resp.observatory_mode["global_mode"] == "enforce"
        assert resp.security_summary["modules_active"] == 33
        assert resp.security_summary["canary_status"] == "green"
        assert resp.egress["rules_count"] == 5

    def test_status_response_optional_fields(self):
        """Test that new fields are optional (backward compat)."""
        from gateway.ingest_api.models import StatusResponse
        
        resp = StatusResponse(
            status="healthy",
            version="0.7.0",
            uptime_seconds=50.0,
            ledger_entries=0,
            pending_approvals=0,
            pii_engine="regex",
            config_loaded=True,
        )
        
        assert resp.observatory_mode is None
        assert resp.security_summary is None
        assert resp.egress is None

    def test_status_response_monitor_mode(self):
        """Test status response in monitor mode."""
        from gateway.ingest_api.models import StatusResponse
        
        resp = StatusResponse(
            status="healthy",
            version="0.8.0",
            uptime_seconds=100.0,
            ledger_entries=0,
            pending_approvals=0,
            pii_engine="regex",
            config_loaded=True,
            observatory_mode={
                "global_mode": "monitor",
                "effective_since": "2026-03-04T22:00:00Z",
                "auto_revert_at": "2026-03-05T22:00:00Z",
            },
            security_summary={
                "modules_active": 33,
                "modules_enforcing": 0,
                "modules_monitoring": 33,
                "blocked_today": 0,
                "canary_status": "green",
            },
        )
        
        assert resp.observatory_mode["global_mode"] == "monitor"
        assert resp.observatory_mode["auto_revert_at"] is not None
        assert resp.security_summary["modules_enforcing"] == 0
        assert resp.security_summary["modules_monitoring"] == 33
