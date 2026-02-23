# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Dashboard API endpoints for proxy status, alerts, SSH hosts, and logs.

These endpoints power the web dashboard and TUI panels.
"""

from __future__ import annotations

import asyncio
import logging
import socket
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Depends, Query

from .api import require_auth

logger = logging.getLogger("agentshroud.web.dashboard")

router = APIRouter(prefix="/api", tags=["dashboard"])


# ---------------------------------------------------------------------------
# Alert store (in-memory, other modules can push alerts here)
# ---------------------------------------------------------------------------

@dataclass
class Alert:
    timestamp: float
    severity: str  # critical, high, medium, low
    module: str
    message: str


class AlertStore:
    """Simple in-memory alert store. Thread-safe enough for single-process use."""

    def __init__(self) -> None:
        self._alerts: list[Alert] = []

    def push(self, severity: str, module: str, message: str) -> None:
        self._alerts.append(Alert(
            timestamp=time.time(),
            severity=severity,
            module=module,
            message=message,
        ))

    def summary(self) -> dict[str, int]:
        counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for a in self._alerts:
            if a.severity in counts:
                counts[a.severity] += 1
        counts["total"] = sum(counts.values())
        return counts

    def recent(self, n: int = 20) -> list[dict[str, Any]]:
        return [
            {
                "timestamp": datetime.fromtimestamp(a.timestamp, tz=timezone.utc).isoformat(),
                "severity": a.severity,
                "module": a.module,
                "message": a.message,
            }
            for a in self._alerts[-n:]
        ]


# Singleton — importable by other modules
alert_store = AlertStore()


# ---------------------------------------------------------------------------
# SSH host cache
# ---------------------------------------------------------------------------

_SSH_HOSTS = [
    {"name": "marvin", "host": "marvin"},
    {"name": "pi", "host": "pi"},
    {"name": "trillian", "host": "trillian"},
]

_ssh_cache: dict[str, dict[str, Any]] = {}
_SSH_CACHE_TTL = 60  # seconds


async def _check_host(name: str, host: str) -> dict[str, Any]:
    """TCP connect to port 22 to check if host is reachable."""
    now = datetime.now(timezone.utc)
    cached = _ssh_cache.get(name)
    if cached and (time.time() - cached["_checked_at"]) < _SSH_CACHE_TTL:
        return {k: v for k, v in cached.items() if not k.startswith("_")}

    status = "offline"
    try:
        loop = asyncio.get_running_loop()
        # Resolve host and TCP-connect to port 22 with 3s timeout
        fut = loop.run_in_executor(None, _tcp_check, host, 22, 3)
        reachable = await asyncio.wait_for(fut, timeout=5)
        if reachable:
            status = "online"
    except Exception:
        status = "offline"

    result = {
        "name": name,
        "host": host,
        "status": status,
        "last_check": now.isoformat(),
    }
    _ssh_cache[name] = {**result, "_checked_at": time.time()}
    return result


def _tcp_check(host: str, port: int, timeout: int) -> bool:
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        return True
    except OSError:
        return False


# ---------------------------------------------------------------------------
# In-memory log buffer
# ---------------------------------------------------------------------------

class LogBuffer:
    """Ring buffer for recent log/audit entries."""

    def __init__(self, max_size: int = 500) -> None:
        self._entries: list[dict[str, Any]] = []
        self._max_size = max_size

    def append(self, level: str, module: str, message: str) -> None:
        self._entries.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "module": module,
            "message": message,
        })
        if len(self._entries) > self._max_size:
            self._entries = self._entries[-self._max_size:]

    def tail(self, n: int = 20) -> list[dict[str, Any]]:
        n = max(1, min(n, 100))
        return self._entries[-n:]


# Singleton
log_buffer = LogBuffer()


# ---------------------------------------------------------------------------
# Logging handler that feeds log_buffer
# ---------------------------------------------------------------------------

class BufferHandler(logging.Handler):
    """Logging handler that pushes records into the LogBuffer."""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            log_buffer.append(
                level=record.levelname,
                module=record.name,
                message=self.format(record),
            )
        except Exception:
            pass


def install_log_handler() -> None:
    """Attach BufferHandler to the root agentshroud logger."""
    root = logging.getLogger("agentshroud")
    # Avoid duplicate handlers on reload
    if not any(isinstance(h, BufferHandler) for h in root.handlers):
        handler = BufferHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))
        root.addHandler(handler)


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("/proxy/status")
async def proxy_status(user: str = Depends(require_auth)) -> dict:
    """Proxy statistics (requests allowed/blocked/flagged)."""
    try:
        from ..ingest_api.main import app_state

        stats: dict[str, Any] = {"total_requests": 0, "allowed": 0, "blocked": 0, "flagged": 0, "uptime_seconds": 0}

        # Pull from SecurityPipeline if available
        if getattr(app_state, "pipeline", None) is not None:
            ps = app_state.pipeline.get_stats()
            stats["total_requests"] = ps.get("inbound_total", 0) + ps.get("outbound_total", 0)
            stats["blocked"] = ps.get("inbound_blocked", 0) + ps.get("outbound_blocked", 0)
            stats["flagged"] = ps.get("inbound_sanitized", 0) + ps.get("outbound_sanitized", 0)
            stats["allowed"] = stats["total_requests"] - stats["blocked"]

        # Pull from WebProxy if available (via http_proxy)
        if getattr(app_state, "http_proxy", None) is not None:
            wp = getattr(app_state.http_proxy, "web_proxy", None)
            if wp is not None and hasattr(wp, "_stats"):
                ws = wp._stats
                stats["total_requests"] += ws.get("total_requests", 0)
                stats["allowed"] += ws.get("allowed", 0)
                stats["blocked"] += ws.get("blocked", 0)

        if getattr(app_state, "start_time", None) is not None:
            stats["uptime_seconds"] = round(time.time() - app_state.start_time, 1)

        return stats
    except Exception as e:
        logger.warning("proxy_status error: %s", e)
        return {"total_requests": 0, "allowed": 0, "blocked": 0, "flagged": 0, "uptime_seconds": 0}


@router.get("/alerts/summary")
async def alerts_summary(user: str = Depends(require_auth)) -> dict:
    """Alert counts by severity."""
    return alert_store.summary()


@router.get("/ssh/hosts")
async def ssh_hosts(user: str = Depends(require_auth)) -> dict:
    """SSH host connectivity status."""
    tasks = [_check_host(h["name"], h["host"]) for h in _SSH_HOSTS]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    hosts = []
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            hosts.append({
                "name": _SSH_HOSTS[i]["name"],
                "host": _SSH_HOSTS[i]["host"],
                "status": "error",
                "last_check": datetime.now(timezone.utc).isoformat(),
            })
        else:
            hosts.append(r)
    return {"hosts": hosts}


@router.get("/logs/recent")
async def logs_recent(
    user: str = Depends(require_auth),
    tail: int = Query(default=20, ge=1, le=100),
) -> dict:
    """Recent security/audit log entries."""
    # First try audit chain entries from pipeline
    entries = log_buffer.tail(tail)

    # Also try to include audit chain entries
    try:
        from ..ingest_api.main import app_state
        if getattr(app_state, "pipeline", None) is not None:
            chain_entries = app_state.pipeline.audit_chain.entries
            for ce in chain_entries[-tail:]:
                entries.append({
                    "timestamp": datetime.fromtimestamp(ce.timestamp, tz=timezone.utc).isoformat(),
                    "level": "AUDIT",
                    "module": "audit_chain",
                    "message": f"[{ce.direction}] hash={ce.chain_hash[:16]}…",
                })
    except Exception:
        pass

    # Sort by timestamp descending, limit
    entries.sort(key=lambda e: e.get("timestamp", ""), reverse=True)
    return {"entries": entries[:tail]}
