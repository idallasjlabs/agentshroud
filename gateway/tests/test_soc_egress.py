# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SOC egress endpoints — model-level and confirmation model validation."""

from __future__ import annotations

import pytest
from gateway.soc.models import (
    EgressRequest,
    EgressStatus,
    RiskLevel,
    SCLConfirmationRequired,
    SCLError,
)


class TestEgressRequestModel:
    def test_pending_status_default(self):
        er = EgressRequest(
            request_id="r1",
            domain="api.openai.com",
            port=443,
            agent_id="main",
            tool_name="web_fetch",
            risk_level=RiskLevel.GREEN,
            submitted_at="2026-03-17T10:00:00Z",
            expires_at="2026-03-17T11:00:00Z",
            status=EgressStatus.PENDING,
        )
        assert er.status == EgressStatus.PENDING
        assert er.decided_by is None
        assert er.decided_at is None

    def test_approved_status(self):
        er = EgressRequest(
            request_id="r2",
            domain="github.com",
            port=443,
            agent_id="main",
            tool_name="web_fetch",
            risk_level=RiskLevel.GREEN,
            submitted_at="2026-03-17T10:00:00Z",
            expires_at="2026-03-17T11:00:00Z",
            status=EgressStatus.APPROVED,
            decided_by="8096968754",
            decided_at="2026-03-17T10:05:00Z",
        )
        assert er.status == EgressStatus.APPROVED
        assert er.decided_by == "8096968754"

    def test_red_risk_high_threat(self):
        er = EgressRequest(
            request_id="r3",
            domain="unknown-host.xyz",
            port=8080,
            agent_id="main",
            tool_name="web_fetch",
            risk_level=RiskLevel.RED,
            submitted_at="2026-03-17T10:00:00Z",
            expires_at="2026-03-17T11:00:00Z",
            status=EgressStatus.PENDING,
        )
        assert er.risk_level == RiskLevel.RED


class TestConfirmationModel:
    def test_destructive_requires_confirmation(self):
        resp = SCLConfirmationRequired(
            message="This will block all egress traffic.",
            action="emergency_block",
            target="all",
        )
        assert resp.error is True
        assert resp.code == "CONFIRMATION_REQUIRED"
        assert "block" in resp.message.lower()

    def test_permission_denied_error(self):
        err = SCLError(
            code="PERMISSION_DENIED",
            message="Only OWNER/ADMIN can approve egress.",
        )
        assert err.error is True
