# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for port_manager — port conflict detection and auto-assignment."""
from __future__ import annotations


import socket
import pytest
from unittest.mock import patch

from gateway.tools.port_manager import (
    PortManager,
    PortAssignment,
    PortResolution,
    PORT_SEARCH_RANGE,
)


class TestIsPortAvailable:
    """Test port availability detection."""

    def test_unbound_port_is_available(self):
        pm = PortManager()
        # Use a high ephemeral port unlikely to be in use
        assert pm.is_port_available(59123, "127.0.0.1") is True

    def test_bound_port_is_not_available(self):
        """Bind a port then check it's detected as in-use."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 59124))
        sock.listen(1)
        try:
            pm = PortManager()
            assert pm.is_port_available(59124, "127.0.0.1") is False
        finally:
            sock.close()

    def test_udp_unbound_available(self):
        pm = PortManager()
        assert pm.is_port_available_udp(59125, "127.0.0.1") is True

    def test_udp_bound_not_available(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 59126))
        try:
            pm = PortManager()
            assert pm.is_port_available_udp(59126, "127.0.0.1") is False
        finally:
            sock.close()


class TestFindAvailablePort:
    """Test auto-port discovery."""

    def test_finds_base_when_free(self):
        pm = PortManager()
        port = pm.find_available_port(59130, "127.0.0.1")
        assert port == 59130

    def test_skips_bound_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 59131))
        sock.listen(1)
        try:
            pm = PortManager()
            port = pm.find_available_port(59131, "127.0.0.1")
            assert port > 59131
        finally:
            sock.close()

    def test_skips_excluded_ports(self):
        pm = PortManager()
        port = pm.find_available_port(59140, "127.0.0.1", exclude={59140, 59141})
        assert port == 59142

    def test_raises_if_no_port_found(self):
        """If all ports in range are excluded, raises RuntimeError."""
        pm = PortManager()
        exclude = set(range(59150, 59150 + PORT_SEARCH_RANGE + 1))
        with pytest.raises(RuntimeError, match="No available port"):
            pm.find_available_port(59150, "127.0.0.1", exclude=exclude)


class TestResolveports:
    """Test full port resolution logic."""

    def test_all_free_no_conflicts(self):
        pm = PortManager(host="127.0.0.1")
        ports = {"a": 59160, "b": 59161}
        result = pm.resolve_ports(ports)
        assert result.conflicts_found == 0
        assert result.ports == {"a": 59160, "b": 59161}

    def test_conflict_auto_resolved(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 59170))
        sock.listen(1)
        try:
            pm = PortManager(host="127.0.0.1")
            result = pm.resolve_ports({"svc": 59170})
            assert result.conflicts_found == 1
            assert result.ports["svc"] != 59170
            assert result.assignments["svc"].was_available is False
        finally:
            sock.close()

    def test_conflict_no_auto_resolve(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("127.0.0.1", 59175))
        sock.listen(1)
        try:
            pm = PortManager(host="127.0.0.1")
            result = pm.resolve_ports({"svc": 59175}, auto_resolve=False)
            assert result.conflicts_found == 1
            # Port stays as requested even though unavailable
            assert result.ports["svc"] == 59175
        finally:
            sock.close()

    def test_duplicate_port_detection(self):
        """Two services requesting same port — second gets reassigned."""
        pm = PortManager(host="127.0.0.1")
        # Both want 59180 — second should get bumped
        result = pm.resolve_ports({"a": 59180, "b": 59180})
        assert result.ports["a"] != result.ports["b"]

    @patch.dict("os.environ", {"AGENTSHROUD_PORT_OFFSET": "100"})
    def test_offset_applied(self):
        pm = PortManager(host="127.0.0.1")
        result = pm.resolve_ports({"svc": 59100})
        assert result.offset_applied == 100
        assert result.assignments["svc"].requested == 59200


class TestPortResolution:
    """Test PortResolution dataclass."""

    def test_ports_property(self):
        r = PortResolution()
        r.assignments["gw"] = PortAssignment("gw", 8080, 8080, True)
        assert r.ports == {"gw": 8080}

    def test_has_conflicts(self):
        r = PortResolution(conflicts_found=0)
        assert r.has_conflicts is False
        r.conflicts_found = 1
        assert r.has_conflicts is True

    def test_summary_format(self):
        r = PortResolution()
        r.assignments["gw"] = PortAssignment("gw", 8080, 8080, True)
        r.assignments["dns"] = PortAssignment("dns", 5353, 5354, False)
        s = r.summary()
        assert "gw" in s
        assert "dns" in s
        assert "✓" in s
        assert "conflict" in s


class TestGenerateComposePorts:
    """Test docker-compose port mapping generation."""

    def test_basic_mapping(self):
        pm = PortManager()
        r = PortResolution()
        r.assignments["gateway"] = PortAssignment("gateway", 8080, 8081, False)
        r.assignments["dns"] = PortAssignment("dns", 5353, 5354, False)
        mappings = pm.generate_compose_ports(r)
        assert mappings["gateway"] == "8081:8080"
        assert "udp" in mappings["dns"]

    def test_no_conflict_mapping(self):
        pm = PortManager()
        r = PortResolution()
        r.assignments["gateway"] = PortAssignment("gateway", 8080, 8080, True)
        mappings = pm.generate_compose_ports(r)
        assert mappings["gateway"] == "8080:8080"
