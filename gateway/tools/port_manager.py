# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Port Manager — detect port conflicts and auto-assign available ports.

When running multiple AgentShroud instances (e.g., Docker + Apple Containers
on the same Mac), ports may collide. This module:

1. Checks if configured ports are already in use
2. Auto-selects next available port if conflict detected
3. Logs all port assignments for visibility
4. Supports AGENTSHROUD_PORT_OFFSET env var for manual offset

Usage:
    from gateway.tools.port_manager import PortManager
    pm = PortManager()
    ports = pm.resolve_ports({"gateway": 8080, "dns": 5353, "dashboard": 8443})
    # Returns {"gateway": 8080, "dns": 5353, "dashboard": 8443} if free,
    # or auto-incremented ports if any are taken.
"""


import logging
import os
import socket
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger("agentshroud.tools.port_manager")


# Default ports for AgentShroud services
DEFAULT_PORTS = {
    "gateway": 8080,
    "dns": 5353,
    "dashboard": 8443,
    "websocket": 8081,
    "metrics": 9090,
}

# Range to search within when auto-detecting
PORT_SEARCH_RANGE = 100  # Will try up to +100 from base


@dataclass
class PortAssignment:
    """Record of a port assignment decision."""

    service: str
    requested: int
    assigned: int
    was_available: bool
    reason: str = ""


@dataclass
class PortResolution:
    """Result of resolving all ports for an instance."""

    assignments: dict[str, PortAssignment] = field(default_factory=dict)
    offset_applied: int = 0
    conflicts_found: int = 0

    @property
    def ports(self) -> dict[str, int]:
        """Get the final port mapping."""
        return {name: a.assigned for name, a in self.assignments.items()}

    @property
    def has_conflicts(self) -> bool:
        return self.conflicts_found > 0

    def summary(self) -> str:
        lines = []
        for name, a in self.assignments.items():
            status = "✓" if a.was_available else f"⚠ conflict → {a.assigned}"
            lines.append(f"  {name}: {a.requested} {status}")
        return "\n".join(lines)


class PortManager:
    """Detect port conflicts and auto-assign available ports."""

    def __init__(self, host: str = "0.0.0.0"):
        self.host = host
        self._offset = int(os.environ.get("AGENTSHROUD_PORT_OFFSET", "0"))

    @staticmethod
    def is_port_available(port: int, host: str = "0.0.0.0") -> bool:
        """Check if a TCP port is available for binding.

        Tries to bind briefly. Returns True if successful.
        Also checks UDP for DNS port.
        """
        # TCP check
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.settimeout(0.5)
                s.bind((host, port))
                # Also try connecting to see if something is listening
            # Double-check by trying to connect (catches TIME_WAIT etc.)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host if host != "0.0.0.0" else "127.0.0.1", port))
                if result == 0:
                    # Something is actually listening
                    return False
        except OSError:
            return False

        return True

    @staticmethod
    def is_port_available_udp(port: int, host: str = "0.0.0.0") -> bool:
        """Check if a UDP port is available (used for DNS)."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(0.5)
                s.bind((host, port))
            return True
        except OSError:
            return False

    def find_available_port(
        self,
        base: int,
        host: str = "0.0.0.0",
        check_udp: bool = False,
        exclude: Optional[set[int]] = None,
    ) -> int:
        """Find next available port starting from base.

        Args:
            base: Starting port number
            host: Host to check binding on
            check_udp: Also check UDP availability (for DNS)
            exclude: Set of ports already assigned in this resolution
        """
        exclude = exclude or set()
        for offset in range(PORT_SEARCH_RANGE):
            candidate = base + offset
            if candidate in exclude:
                continue
            if candidate > 65535:
                break
            tcp_ok = self.is_port_available(candidate, host)
            udp_ok = True
            if check_udp:
                udp_ok = self.is_port_available_udp(candidate, host)
            if tcp_ok and udp_ok:
                return candidate

        raise RuntimeError(f"No available port found in range {base}-{base + PORT_SEARCH_RANGE}")

    def resolve_ports(
        self, requested: Optional[dict[str, int]] = None, auto_resolve: bool = True
    ) -> PortResolution:
        """Resolve all ports, detecting conflicts and auto-assigning if needed.

        Args:
            requested: Map of service name → desired port. Defaults to DEFAULT_PORTS.
            auto_resolve: If True, auto-find available ports on conflict.
                         If False, just report conflicts.

        Returns:
            PortResolution with final assignments and conflict info.
        """
        ports = dict(requested or DEFAULT_PORTS)
        result = PortResolution(offset_applied=self._offset)
        assigned_ports: set[int] = set()

        # Apply manual offset first
        if self._offset:
            logger.info("Applying port offset: +%d", self._offset)
            ports = {k: v + self._offset for k, v in ports.items()}

        for service, port in ports.items():
            check_udp = service == "dns"
            available = self.is_port_available(port, self.host)
            if check_udp:
                available = available and self.is_port_available_udp(port, self.host)

            # Also check we haven't already assigned this port
            if port in assigned_ports:
                available = False

            if available:
                assignment = PortAssignment(
                    service=service,
                    requested=port,
                    assigned=port,
                    was_available=True,
                )
                assigned_ports.add(port)
            elif auto_resolve:
                new_port = self.find_available_port(
                    port, self.host, check_udp=check_udp, exclude=assigned_ports
                )
                assignment = PortAssignment(
                    service=service,
                    requested=port,
                    assigned=new_port,
                    was_available=False,
                    reason=f"port {port} in use, reassigned to {new_port}",
                )
                assigned_ports.add(new_port)
                result.conflicts_found += 1
                logger.warning(
                    "Port conflict: %s wanted %d, assigned %d",
                    service,
                    port,
                    new_port,
                )
            else:
                assignment = PortAssignment(
                    service=service,
                    requested=port,
                    assigned=port,
                    was_available=False,
                    reason=f"port {port} in use",
                )
                result.conflicts_found += 1
                logger.error("Port conflict: %s port %d is in use", service, port)

            result.assignments[service] = assignment

        if result.conflicts_found:
            logger.info(
                "Port resolution: %d conflict(s) resolved\n%s",
                result.conflicts_found,
                result.summary(),
            )
        else:
            logger.info("All ports available:\n%s", result.summary())

        return result

    def generate_compose_ports(self, resolution: PortResolution) -> dict[str, str]:
        """Generate docker-compose port mapping strings from resolution.

        Returns dict like {"gateway": "8081:8080", "dns": "5354:53/udp"}
        where external port is the resolved one and internal stays fixed.
        """
        internal_ports = {
            "gateway": 8080,
            "dns": 53,
            "dashboard": 8443,
            "websocket": 8081,
            "metrics": 9090,
        }
        mappings = {}
        for service, assignment in resolution.assignments.items():
            internal = internal_ports.get(service, assignment.assigned)
            if service == "dns":
                mappings[service] = f"{assignment.assigned}:{internal}/udp"
            else:
                mappings[service] = f"{assignment.assigned}:{internal}"
        return mappings


def check_and_report(host: str = "0.0.0.0") -> PortResolution:
    """Quick check: are the default ports available? Log and return result."""
    pm = PortManager(host=host)
    return pm.resolve_ports()


if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    host = sys.argv[1] if len(sys.argv) > 1 else "0.0.0.0"
    result = check_and_report(host)
    if result.has_conflicts:
        pm = PortManager(host=host)
        for svc, mapping in pm.generate_compose_ports(result).items():
            logging.info("  %s: %s", svc, mapping)
