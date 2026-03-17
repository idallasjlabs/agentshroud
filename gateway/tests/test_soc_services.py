# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/soc/services.py — ServiceManager unit tests."""

from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from gateway.soc.models import ServiceStatus, HealthStatus, ServiceDescriptor


class TestServiceDescriptorDefaults:
    """Validate ServiceDescriptor model defaults — no real container calls."""

    def test_running_service(self):
        sd = ServiceDescriptor(
            name="agentshroud-bot",
            status=ServiceStatus.RUNNING,
            health=HealthStatus.HEALTHY,
            image="agentshroud:latest",
        )
        assert sd.status == ServiceStatus.RUNNING
        assert sd.health == HealthStatus.HEALTHY
        assert sd.restart_count == 0
        assert sd.ports == []

    def test_stopped_service(self):
        sd = ServiceDescriptor(
            name="agentshroud-gateway",
            status=ServiceStatus.STOPPED,
            health=HealthStatus.UNKNOWN,
            image="agentshroud-gateway:latest",
        )
        assert sd.status == ServiceStatus.STOPPED
        assert sd.container_id is None

    def test_unhealthy_service(self):
        sd = ServiceDescriptor(
            name="agentshroud-bot",
            status=ServiceStatus.RUNNING,
            health=HealthStatus.UNHEALTHY,
            image="agentshroud:latest",
        )
        assert sd.health == HealthStatus.UNHEALTHY


class TestServiceManagerImport:
    """Verify ServiceManager can be imported without a running container engine."""

    def test_import(self):
        from gateway.soc.services import ServiceManager
        assert ServiceManager is not None

    def test_instantiate_without_engine(self):
        from gateway.soc.services import ServiceManager
        # Should not raise — engine is resolved lazily
        sm = ServiceManager()
        assert sm is not None
