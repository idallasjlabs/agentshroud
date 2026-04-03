# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Sidecar Mode — optional security scanning without mandatory proxying.

WARNING: In sidecar mode, traffic CAN bypass the security pipeline.
This provides "best effort" scanning for users who want to add security
without full proxy mode. For guaranteed protection, use proxy mode.

Exposes POST /api/scan endpoint that accepts a message, runs the
security pipeline, and returns the sanitized message + security report.
"""


import logging
import time
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger("agentshroud.proxy.sidecar")

SIDECAR_WARNING = (
    "SIDECAR MODE: Traffic can bypass this scanner. "
    "For guaranteed security, use proxy mode (docker-compose.secure.yml)."
)


@dataclass
class ScanRequest:
    """Request to scan a message."""

    content: str
    agent_id: str = "default"
    action: str = "send_message"
    source: str = "sidecar"


@dataclass
class ScanResponse:
    """Response from sidecar scan."""

    sanitized_content: str
    original_content: str
    security_report: dict[str, Any] = field(default_factory=dict)
    mode: str = "sidecar"
    warning: str = SIDECAR_WARNING


class SidecarScanner:
    """Sidecar security scanner — reduced security, traffic can bypass.

    This is for users who run OpenClaw normally but want optional security
    scanning. It does NOT guarantee all traffic is scanned.
    """

    def __init__(self, pipeline=None):
        self.pipeline = pipeline
        self._scans_total = 0
        self._scans_blocked = 0
        self._started_at = time.time()

    async def scan(self, request: ScanRequest) -> ScanResponse:
        """Scan a message through the security pipeline."""
        self._scans_total += 1

        if not self.pipeline:
            return ScanResponse(
                sanitized_content=request.content,
                original_content=request.content,
                security_report={"error": "No pipeline configured"},
            )

        result = await self.pipeline.process_inbound(
            message=request.content,
            agent_id=request.agent_id,
            action=request.action,
            source=request.source,
        )

        if result.blocked:
            self._scans_blocked += 1

        return ScanResponse(
            sanitized_content=result.sanitized_message,
            original_content=request.content,
            security_report=result.to_dict(),
        )

    def get_stats(self) -> dict[str, Any]:
        return {
            "mode": "sidecar",
            "warning": SIDECAR_WARNING,
            "scans_total": self._scans_total,
            "scans_blocked": self._scans_blocked,
            "uptime_seconds": time.time() - self._started_at,
        }
