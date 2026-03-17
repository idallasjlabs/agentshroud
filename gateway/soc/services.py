# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC Service Manager — wraps container runtime engine to produce ServiceDescriptors."""
from __future__ import annotations

import logging
import time
from typing import Any, Dict, List, Optional

from .models import HealthStatus, ResourceUsage, ServiceDescriptor, ServiceStatus

logger = logging.getLogger("agentshroud.soc.services")

# Services the SOC knows about. This list can be extended.
_KNOWN_SERVICES = ["agentshroud-bot", "agentshroud-gateway"]


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
        """Return ServiceDescriptor for each known container."""
        engine = self._get_engine()
        descriptors: List[ServiceDescriptor] = []
        for name in _KNOWN_SERVICES:
            descriptors.append(self._describe_service(name, engine))
        return descriptors

    def get_service(self, name: str) -> Optional[ServiceDescriptor]:
        engine = self._get_engine()
        return self._describe_service(name, engine)

    def _describe_service(self, name: str, engine: Optional[Any]) -> ServiceDescriptor:
        if engine is None:
            return ServiceDescriptor(name=name, status=ServiceStatus.UNKNOWN)
        try:
            info = engine.inspect(name)
            if not info:
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

    async def get_logs(self, name: str, tail: int = 50) -> List[str]:
        engine = self._get_engine()
        if engine is None:
            return []
        try:
            raw = engine.logs(name, tail=tail)
            if isinstance(raw, (bytes, bytearray)):
                raw = raw.decode("utf-8", errors="replace")
            return raw.splitlines()[-tail:]
        except Exception as exc:
            logger.warning("get_logs(%s): %s", name, exc)
            return []
