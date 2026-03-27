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

    def test_standby_service(self):
        """STANDBY = binary installed but cannot run in this environment; should be healthy."""
        sd = ServiceDescriptor(
            name="agentshroud-wazuh",
            status=ServiceStatus.STANDBY,
            health=HealthStatus.HEALTHY,
            image="wazuh-agent:latest",
        )
        assert sd.status == ServiceStatus.STANDBY
        assert sd.status.value == "standby"
        assert sd.health == HealthStatus.HEALTHY


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


class TestServiceManagerGetLogs:
    """Unit tests for ServiceManager.get_logs — including module_filter behaviour."""

    @pytest.fixture
    def mgr_with_engine(self):
        from gateway.soc.services import ServiceManager
        engine = MagicMock()
        return ServiceManager(engine=engine), engine

    @pytest.mark.asyncio
    async def test_get_logs_no_filter_returns_tail(self, mgr_with_engine):
        mgr, engine = mgr_with_engine
        engine.logs.return_value = "line1\nline2\nline3"
        lines = await mgr.get_logs("agentshroud-gateway", tail=2)
        assert lines == ["line2", "line3"]

    @pytest.mark.asyncio
    async def test_get_logs_module_filter_keeps_matching_lines(self, mgr_with_engine):
        mgr, engine = mgr_with_engine
        raw = (
            "[INFO] agentshroud.proxy.http_proxy: accepted connection\n"
            "[INFO] agentshroud.security.egress_filter: checked domain\n"
            "[INFO] agentshroud.proxy.http_proxy: forwarded request\n"
        )
        engine.logs.return_value = raw
        lines = await mgr.get_logs("agentshroud-gateway", tail=50, module_filter="http_proxy")
        assert all("http_proxy" in l for l in lines)
        assert len(lines) == 2

    @pytest.mark.asyncio
    async def test_get_logs_module_filter_excludes_non_matching(self, mgr_with_engine):
        mgr, engine = mgr_with_engine
        raw = (
            "[INFO] agentshroud.security.egress_filter: pass\n"
            "[INFO] agentshroud.security.egress_filter: deny\n"
            "[INFO] agentshroud.proxy.http_proxy: connect\n"
        )
        engine.logs.return_value = raw
        lines = await mgr.get_logs("agentshroud-gateway", tail=50, module_filter="egress_filter")
        assert len(lines) == 2
        assert all("egress_filter" in l for l in lines)

    @pytest.mark.asyncio
    async def test_get_logs_module_filter_case_insensitive(self, mgr_with_engine):
        mgr, engine = mgr_with_engine
        engine.logs.return_value = "ClamAV: database loaded\nHTTP_PROXY: request\n"
        lines = await mgr.get_logs("agentshroud-gateway", tail=50, module_filter="clamav")
        assert len(lines) == 1
        assert "ClamAV" in lines[0]

    @pytest.mark.asyncio
    async def test_get_logs_module_filter_empty_returns_all(self, mgr_with_engine):
        mgr, engine = mgr_with_engine
        engine.logs.return_value = "line1\nline2\nline3"
        lines = await mgr.get_logs("agentshroud-gateway", tail=10, module_filter="")
        assert lines == ["line1", "line2", "line3"]

    @pytest.mark.asyncio
    async def test_get_logs_no_engine_returns_empty(self):
        from gateway.soc.services import ServiceManager
        mgr = ServiceManager(engine=None)
        with patch("os.path.exists", return_value=False):
            lines = await mgr.get_logs("agentshroud-gateway", tail=10)
        assert lines == []
