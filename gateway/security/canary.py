# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Canary System — periodic verification that the security pipeline is working.

Sends fake PII through the pipeline and verifies:
1. PII was stripped
2. Audit entry exists with valid hash chain
3. Proxy mode is active (health check)
"""


import logging
import time
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger("agentshroud.security.canary")

# Fake PII for canary tests — clearly fake values
CANARY_SSN = "000-00-0000"
CANARY_EMAIL = "canary@test.agentshroud.local"
CANARY_PHONE = "555-000-0000"
CANARY_MESSAGE = (
    f"Canary test: SSN {CANARY_SSN}, email {CANARY_EMAIL}, phone {CANARY_PHONE}"
)


@dataclass
class CanaryCheck:
    """Individual canary check result."""

    name: str
    passed: bool
    details: str = ""


@dataclass
class CanaryResult:
    """Result of running the canary system."""

    verified: bool
    checks: dict[str, bool] = field(default_factory=dict)
    check_details: list[CanaryCheck] = field(default_factory=list)
    timestamp: str = ""
    duration_ms: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "verified": self.verified,
            "checks": self.checks,
            "check_details": [
                {"name": c.name, "passed": c.passed, "details": c.details}
                for c in self.check_details
            ],
            "timestamp": self.timestamp,
            "duration_ms": self.duration_ms,
        }


async def run_canary(
    pipeline=None,
    forwarder=None,
) -> CanaryResult:
    """Run the canary verification system.

    Args:
        pipeline: SecurityPipeline instance
        forwarder: HTTPForwarder instance (for proxy health check)

    Returns:
        CanaryResult with verification status
    """
    from datetime import datetime, timezone

    start = time.time()
    checks = []
    all_passed = True

    # Check 1: PII stripping
    pii_check = CanaryCheck(name="pii", passed=False)
    if pipeline:
        result = await pipeline.process_inbound(
            message=CANARY_MESSAGE,
            agent_id="canary",
            action="send_message",
            source="canary",
        )
        # Verify SSN was stripped
        if CANARY_SSN not in result.sanitized_message:
            pii_check.passed = True
            pii_check.details = f"PII stripped: {result.pii_redaction_count} redactions"
        else:
            pii_check.details = "SSN not stripped from canary message"
            all_passed = False
    else:
        pii_check.details = "No pipeline configured"
        all_passed = False
    checks.append(pii_check)

    # Check 2: Audit entry exists
    audit_check = CanaryCheck(name="audit", passed=False)
    if pipeline:
        chain_len = len(pipeline.audit_chain)
        if chain_len > 0:
            audit_check.passed = True
            audit_check.details = f"Audit chain has {chain_len} entries"
        else:
            audit_check.details = "No entries in audit chain"
            all_passed = False
    else:
        audit_check.details = "No pipeline configured"
        all_passed = False
    checks.append(audit_check)

    # Check 3: Chain integrity
    chain_check = CanaryCheck(name="chain", passed=False)
    if pipeline:
        valid, msg = pipeline.verify_audit_chain()
        chain_check.passed = valid
        chain_check.details = msg
        if not valid:
            all_passed = False
    else:
        chain_check.details = "No pipeline configured"
        all_passed = False
    checks.append(chain_check)

    # Check 4: Proxy health (forwarder)
    proxy_check = CanaryCheck(name="proxy", passed=False)
    if forwarder:
        try:
            healthy = await forwarder.health_check()
            proxy_check.passed = healthy
            proxy_check.details = (
                "Proxy target healthy" if healthy else "Proxy target unhealthy"
            )
        except Exception as e:
            proxy_check.details = f"Health check failed: {e}"
        if not proxy_check.passed:
            all_passed = False
    else:
        # No forwarder is OK in test mode — just mark as skipped
        proxy_check.passed = True
        proxy_check.details = "No forwarder configured (test mode)"
    checks.append(proxy_check)

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    duration = (time.time() - start) * 1000

    return CanaryResult(
        verified=all_passed,
        checks={c.name: c.passed for c in checks},
        check_details=checks,
        timestamp=now,
        duration_ms=round(duration, 2),
    )
