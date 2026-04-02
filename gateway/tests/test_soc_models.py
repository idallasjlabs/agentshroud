# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/soc/models.py — SCL data models."""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from gateway.soc.models import (
    ContributorRecord,
    EgressRequest,
    EgressStatus,
    HealthStatus,
    Platform,
    ResourceUsage,
    RiskLevel,
    SCLConfirmationRequired,
    SCLError,
    SecurityEvent,
    ServiceDescriptor,
    ServiceStatus,
    Severity,
    UserRole,
    WSEvent,
    WSEventType,
)


class TestSecurityEvent:
    def test_minimal_construction(self):
        ev = SecurityEvent(
            event_id="abc-123",
            event_type="inbound_blocked",
            severity=Severity.HIGH,
            timestamp="2026-03-17T12:00:00Z",
            source_module="prompt_guard",
            agent_id="main",
            action_taken="blocked",
            summary="Injection attempt blocked",
        )
        assert ev.event_id == "abc-123"
        assert ev.severity == Severity.HIGH

    def test_severity_ordering(self):
        assert Severity.CRITICAL != Severity.HIGH
        assert Severity.LOW != Severity.MEDIUM

    def test_optional_fields_default_none(self):
        ev = SecurityEvent(
            event_id="x",
            event_type="egress_denied",
            severity=Severity.LOW,
            timestamp="2026-01-01T00:00:00Z",
            source_module="egress_filter",
            agent_id="main",
            action_taken="denied",
            summary="test",
        )
        assert ev.user_id is None
        assert ev.chain_hash is None
        assert ev.details == {}


class TestEgressRequest:
    def test_construction(self):
        er = EgressRequest(
            request_id="req-1",
            domain="api.openai.com",
            port=443,
            agent_id="main",
            tool_name="web_fetch",
            risk_level=RiskLevel.YELLOW,
            submitted_at="2026-03-17T10:00:00Z",
            expires_at="2026-03-17T11:00:00Z",
            status=EgressStatus.PENDING,
        )
        assert er.domain == "api.openai.com"
        assert er.status == EgressStatus.PENDING
        assert er.decided_by is None


class TestServiceDescriptor:
    def test_defaults(self):
        sd = ServiceDescriptor(
            name="agentshroud-bot",
            status=ServiceStatus.RUNNING,
            health=HealthStatus.HEALTHY,
            image="agentshroud-bot:latest",
        )
        assert sd.container_id is None
        assert sd.resource_usage is not None
        assert sd.resource_usage.cpu_percent is None
        assert sd.restart_count == 0

    def test_with_resource_usage(self):
        ru = ResourceUsage(cpu_percent=12.5, memory_mb=256.0, memory_limit_mb=512.0)
        sd = ServiceDescriptor(
            name="agentshroud-bot",
            status=ServiceStatus.RUNNING,
            health=HealthStatus.HEALTHY,
            image="agentshroud-bot:latest",
            resource_usage=ru,
        )
        assert sd.resource_usage.cpu_percent == 12.5


class TestContributorRecord:
    def test_construction(self):
        cr = ContributorRecord(
            user_id="8506022825",
            platform=Platform.TELEGRAM,
            display_name="Brett",
            role=UserRole.COLLABORATOR,
            added_at="2026-01-01T00:00:00Z",
            added_by="8096968754",
        )
        assert cr.user_id == "8506022825"
        assert cr.groups == []
        assert cr.immunity_active is False


class TestSCLError:
    def test_error_model(self):
        err = SCLError(code="PERMISSION_DENIED", message="Access denied")
        assert err.error is True
        assert err.code == "PERMISSION_DENIED"

    def test_confirmation_required(self):
        conf = SCLConfirmationRequired(
            message="This will stop the container.",
            action="stop",
            target="agentshroud-bot",
        )
        assert conf.error is True
        assert conf.code == "CONFIRMATION_REQUIRED"


class TestWSEvent:
    def test_construction(self):
        ev = WSEvent(
            type=WSEventType.SECURITY_EVENT,
            timestamp="2026-03-17T12:00:00Z",
            severity="high",
            summary="injection attempt",
        )
        assert ev.type == WSEventType.SECURITY_EVENT
        assert ev.details == {}
