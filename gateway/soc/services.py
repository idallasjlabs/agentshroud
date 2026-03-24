# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC Service Manager — wraps container runtime engine to produce ServiceDescriptors."""
from __future__ import annotations

import http.client
import json as _json
import logging
import os
import socket
import time
from typing import Any, Dict, List, Optional

# Gateway process start time — used as uptime base for internal module services (CC-29)
_GATEWAY_START_TIME: float = time.time()

from .models import HealthStatus, ResourceUsage, ServiceDescriptor, ServiceStatus

logger = logging.getLogger("agentshroud.soc.services")

# Services the SOC knows about — core + security sidecar containers.
_DOCKER_SOCK = "/var/run/docker.sock"


def _inspect_via_socket(name: str) -> Optional[Dict[str, Any]]:
    """Query Docker daemon directly via Unix socket — no CLI needed."""
    try:
        class _UnixHTTP(http.client.HTTPConnection):
            def connect(self) -> None:
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.settimeout(3)
                self.sock.connect(_DOCKER_SOCK)

        conn = _UnixHTTP("localhost")
        conn.request("GET", f"/containers/{name}/json")
        resp = conn.getresponse()
        body = resp.read()
        if resp.status == 404:
            return {}  # container not found / stopped
        if resp.status != 200:
            return None
        return _json.loads(body)
    except Exception as exc:
        logger.debug("_inspect_via_socket(%s): %s", name, exc)
        return None


_KNOWN_SERVICES = [
    "agentshroud-bot",
    "agentshroud-gateway",
]


def _check_clamd() -> str:
    """Return 'running', 'stopped', or 'not_installed' for clamd (CC-01)."""
    import shutil
    if not shutil.which("clamd") and not os.path.exists("/usr/sbin/clamd"):
        return "not_installed"
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect("/tmp/clamd.ctl")
        s.close()
        return "running"
    except Exception:
        pass
    # Socket not ready yet — check if the clamd process is running (still initialising)
    try:
        for entry in os.listdir("/proc"):
            if not entry.isdigit():
                continue
            try:
                comm = open(f"/proc/{entry}/comm").read().strip()
                if comm in ("clamd", "clamd.exe"):
                    return "running"
            except Exception:
                continue
    except Exception:
        pass
    return "stopped"


def _check_fluent_bit() -> str:
    """Return 'running', 'stopped', or 'not_installed' for fluent-bit (CC-01)."""
    import shutil
    import os as _os
    _FB_FALLBACK = "/opt/fluent-bit/bin/fluent-bit"
    if (
        not shutil.which("fluent-bit")
        and not shutil.which("td-agent-bit")
        and not _os.path.exists(_FB_FALLBACK)
    ):
        return "not_installed"
    try:
        pid = int(open("/tmp/fluent-bit.pid").read().strip())
        _os.kill(pid, 0)
        return "running"
    except Exception:
        pass
    # Fallback: scan /proc for a running fluent-bit process
    try:
        for entry in _os.listdir("/proc"):
            if not entry.isdigit():
                continue
            comm_path = f"/proc/{entry}/comm"
            try:
                comm = open(comm_path).read().strip()
                if "fluent-bit" in comm or "td-agent-bit" in comm:
                    return "running"
            except Exception:
                continue
    except Exception:
        pass
    return "stopped"


def _check_wazuh_agent() -> str:
    """Return 'running', 'stopped', or 'not_installed' for wazuh-agentd (CC-01)."""
    import errno as _errno
    import os as _os
    import shutil
    if not shutil.which("wazuh-agentd") and not os.path.exists("/var/ossec/bin/wazuh-agentd"):
        return "not_installed"
    try:
        pid = int(open("/var/ossec/var/run/wazuh-agentd.pid").read().strip())
        _os.kill(pid, 0)
        return "running"
    except OSError as exc:
        if exc.errno == _errno.EPERM:
            return "running"  # process exists, owned by different user
    except Exception:
        pass
    # PID file missing — scan /proc for wazuh-agentd process directly
    try:
        for entry in _os.listdir("/proc"):
            if not entry.isdigit():
                continue
            try:
                comm = open(f"/proc/{entry}/comm").read().strip()
                if comm in ("wazuh-agentd",):
                    return "running"
            except Exception:
                continue
    except Exception:
        pass
    return "stopped"


def _check_openscap() -> str:
    """Return 'running', 'stopped', or 'not_installed' for openscap (CC-01)."""
    import shutil
    if not shutil.which("oscap"):
        return "not_installed"
    if os.path.exists("/usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml"):
        return "running"
    return "stopped"


# Internal gateway services — processes running inside the gateway container.
# (svc_name, app_state_attr, label, port, check_fn)
# check_fn: callable() -> bool overrides app_state attr lookup when not None.
_INTERNAL_SERVICE_ATTRS = [
    ("agentshroud-http-proxy",    "http_proxy",    "HTTP CONNECT Proxy",  8181, None),
    ("agentshroud-dns-forwarder", "dns_transport", "DNS Forwarder",       5353, None),
    ("agentshroud-mcp-proxy",     "mcp_proxy",     "MCP Proxy",           None, None),
    ("agentshroud-ssh-proxy",     "ssh_proxy",     "SSH Proxy",           None, None),
    ("agentshroud-egress-filter", "egress_filter", "Egress Filter",       None, None),
    ("agentshroud-pii-sanitizer", "sanitizer",     "PII Sanitizer",       None, None),
    ("agentshroud-clamav",        None,             "ClamAV",              None, _check_clamd),
    ("agentshroud-fluent-bit",    None,             "Fluent Bit",          2020, _check_fluent_bit),
    ("agentshroud-wazuh",         None,             "Wazuh Agent",         None, _check_wazuh_agent),
    ("agentshroud-openscap",      None,             "OpenSCAP",            None, _check_openscap),
]


def _engine_status_to_service_status(raw: str) -> ServiceStatus:
    mapping = {
        "running": ServiceStatus.RUNNING,
        "stopped": ServiceStatus.STOPPED,
        "paused": ServiceStatus.PAUSED,
        "restarting": ServiceStatus.RESTARTING,
        "exited": ServiceStatus.STOPPED,
        "dead": ServiceStatus.STOPPED,
        "created": ServiceStatus.STOPPED,
        "removing": ServiceStatus.STOPPED,
    }
    return mapping.get(str(raw).lower(), ServiceStatus.UNKNOWN)


def _engine_health_to_health(raw: str) -> HealthStatus:
    mapping = {
        "healthy": HealthStatus.HEALTHY,
        "unhealthy": HealthStatus.UNHEALTHY,
        "starting": HealthStatus.STARTING,
        "none": HealthStatus.UNKNOWN,
        "": HealthStatus.UNKNOWN,
    }
    return mapping.get(str(raw).lower(), HealthStatus.UNKNOWN)


class ServiceManager:
    """Thin wrapper around the container engine that produces ServiceDescriptors."""

    def __init__(self, engine: Optional[Any] = None):
        self._engine = engine

    def _get_engine(self) -> Optional[Any]:
        """Return the container engine from app_state if not injected."""
        if self._engine is not None:
            return self._engine
        try:
            from ..ingest_api.state import app_state
            from ..runtime.engine import get_engine
            return get_engine()
        except Exception:
            return None

    def list_services(self) -> List[ServiceDescriptor]:
        """Return ServiceDescriptor for each known container plus internal gateway services."""
        engine = self._get_engine()
        descriptors: List[ServiceDescriptor] = []
        for name in _KNOWN_SERVICES:
            descriptors.append(self._describe_service(name, engine))
        # Internal gateway services (running inside the gateway process)
        # CC-25: mark all as is_internal=True; CC-29: use gateway start time for uptime
        gateway_uptime = time.time() - _GATEWAY_START_TIME
        _status_map = {
            "running": ServiceStatus.RUNNING,
            "stopped": ServiceStatus.STOPPED,
            "not_installed": ServiceStatus.NOT_INSTALLED,
        }
        try:
            from ..ingest_api.state import app_state
            for svc_name, attr, label, port, check_fn in _INTERNAL_SERVICE_ATTRS:
                if check_fn is not None:
                    status_str = check_fn()  # now returns "running"/"stopped"/"not_installed"
                else:
                    obj = getattr(app_state, attr, None)
                    status_str = "running" if obj is not None else "stopped"
                svc_status = _status_map.get(status_str, ServiceStatus.UNKNOWN)
                running = svc_status == ServiceStatus.RUNNING
                ports = [f"{port}/tcp"] if port and running else []
                descriptors.append(ServiceDescriptor(
                    name=svc_name,
                    status=svc_status,
                    health=HealthStatus.HEALTHY if running else HealthStatus.UNKNOWN,
                    uptime_seconds=gateway_uptime if running else None,
                    ports=ports,
                    networks=["agentshroud-internal"],
                    version=None,
                    is_internal=True,  # CC-25
                ))
        except Exception as exc:
            logger.debug("list_services: internal service probe failed: %s", exc)
        return descriptors

    def get_service(self, name: str) -> Optional[ServiceDescriptor]:
        engine = self._get_engine()
        return self._describe_service(name, engine)

    def _describe_service(self, name: str, engine: Optional[Any]) -> ServiceDescriptor:
        info: Optional[Dict[str, Any]] = None
        if engine is not None:
            try:
                info = engine.inspect(name)
            except Exception as exc:
                logger.debug("_describe_service(%s): engine.inspect failed: %s", name, exc)
        if info is None:
            info = _inspect_via_socket(name)
        try:
            if info is None:
                return ServiceDescriptor(name=name, status=ServiceStatus.UNKNOWN)
            if not info:  # empty dict → container not found
                return ServiceDescriptor(name=name, status=ServiceStatus.STOPPED)
            state = info.get("State", {})
            status_raw = state.get("Status", "")
            health_raw = state.get("Health", {}).get("Status", "") if isinstance(state.get("Health"), dict) else ""
            started_at = state.get("StartedAt", "")
            restart_count = state.get("RestartCount", 0)
            image = info.get("Image", "")
            config = info.get("Config", {})
            labels = config.get("Labels", {}) if isinstance(config, dict) else {}
            version = labels.get("org.opencontainers.image.version") or labels.get("version")
            network_settings = info.get("NetworkSettings", {})
            ports_raw = network_settings.get("Ports", {}) if isinstance(network_settings, dict) else {}
            ports = [f"{k}:{v[0].get('HostPort', '')}" for k, v in ports_raw.items() if v]
            networks = list(network_settings.get("Networks", {}).keys()) if isinstance(network_settings, dict) else []
            # Uptime
            uptime: Optional[float] = None
            if started_at and started_at != "0001-01-01T00:00:00Z":
                try:
                    from datetime import datetime, timezone
                    started_dt = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
                    uptime = (datetime.now(timezone.utc) - started_dt).total_seconds()
                except Exception:
                    pass
            return ServiceDescriptor(
                name=name,
                container_id=info.get("Id", "")[:12],
                status=_engine_status_to_service_status(status_raw),
                health=_engine_health_to_health(health_raw),
                uptime_seconds=uptime,
                restart_count=restart_count,
                image=image[:64] if image else "",
                version=version,
                ports=ports[:4],
                networks=networks[:4],
            )
        except Exception as exc:
            logger.warning("_describe_service(%s): %s", name, exc)
            return ServiceDescriptor(name=name, status=ServiceStatus.UNKNOWN)

    async def start_service(self, name: str) -> bool:
        engine = self._get_engine()
        if engine is None:
            return False
        try:
            engine.start(name)
            return True
        except Exception as exc:
            logger.error("start_service(%s): %s", name, exc)
            return False

    async def stop_service(self, name: str) -> bool:
        engine = self._get_engine()
        if engine is None:
            return False
        try:
            engine.stop(name)
            return True
        except Exception as exc:
            logger.error("stop_service(%s): %s", name, exc)
            return False

    async def restart_service(self, name: str) -> bool:
        engine = self._get_engine()
        if engine is None:
            return False
        try:
            engine.restart(name)
            return True
        except Exception as exc:
            logger.error("restart_service(%s): %s", name, exc)
            return False

    async def update_service(self, name: str) -> bool:
        """Pull the latest image then restart the container."""
        engine = self._get_engine()
        if engine is None:
            return False
        try:
            # Pull latest image if engine supports it; fall through on failure.
            if hasattr(engine, "pull"):
                try:
                    engine.pull(name)
                except Exception as pull_exc:
                    logger.warning("update_service(%s): pull failed (%s), restarting anyway", name, pull_exc)
            engine.restart(name)
            return True
        except Exception as exc:
            logger.error("update_service(%s): %s", name, exc)
            return False

    def _logs_via_socket(self, name: str, tail: int = 50) -> List[str]:
        """Read container logs via Docker Unix socket — fallback when engine unavailable.

        The Docker logs API returns a multiplexed stream where each frame is:
          byte 0    : stream type (1=stdout, 2=stderr)
          bytes 1-3 : padding (zeroes)
          bytes 4-7 : payload size (big-endian uint32)
          bytes 8+  : payload
        """
        import struct
        try:
            class _UnixHTTP(http.client.HTTPConnection):
                def connect(self) -> None:
                    self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    self.sock.settimeout(5)
                    self.sock.connect(_DOCKER_SOCK)

            conn = _UnixHTTP("localhost")
            conn.request(
                "GET",
                f"/containers/{name}/logs?stdout=1&stderr=1&tail={tail}&follow=0&timestamps=0",
            )
            resp = conn.getresponse()
            if resp.status != 200:
                logger.debug("_logs_via_socket(%s): HTTP %d", name, resp.status)
                return []
            raw = resp.read()
            lines: List[str] = []
            offset = 0
            while offset + 8 <= len(raw):
                frame_size = struct.unpack(">I", raw[offset + 4 : offset + 8])[0]
                offset += 8
                if frame_size == 0:
                    continue
                if offset + frame_size > len(raw):
                    break
                payload = raw[offset : offset + frame_size]
                offset += frame_size
                line = payload.decode("utf-8", errors="replace").rstrip("\n")
                if line:
                    lines.extend(line.splitlines())
            return lines[-tail:]
        except Exception as exc:
            logger.debug("_logs_via_socket(%s): %s", name, exc)
            return []

    async def get_logs(self, name: str, tail: int = 50) -> List[str]:
        engine = self._get_engine()
        if engine is not None:
            try:
                raw = engine.logs(name, tail=tail)
                if isinstance(raw, (bytes, bytearray)):
                    raw = raw.decode("utf-8", errors="replace")
                return raw.splitlines()[-tail:]
            except Exception as exc:
                logger.warning("get_logs(%s): engine error (%s) — falling back to socket", name, exc)
        # Fallback: read directly via Docker Unix socket (always mounted in gateway)
        if os.path.exists(_DOCKER_SOCK):
            lines = self._logs_via_socket(name, tail=tail)
            if lines:
                return lines
            logger.debug("get_logs(%s): socket fallback returned no lines", name)
        else:
            logger.debug("get_logs(%s): Docker socket not available at %s", name, _DOCKER_SOCK)
        return []
