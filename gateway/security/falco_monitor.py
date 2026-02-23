# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Falco runtime security monitoring integration.

Reads Falco alerts from shared volume and parses JSON format.
"""
from __future__ import annotations


import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_ALERT_DIR = Path("/var/log/falco")
DEFAULT_LOG_DIR = Path("/var/log/security/falco")

# Falco priority mapping to our severity levels
PRIORITY_MAP = {
    "Emergency": "CRITICAL",
    "Alert": "CRITICAL",
    "Critical": "CRITICAL",
    "Error": "HIGH",
    "Warning": "MEDIUM",
    "Notice": "LOW",
    "Informational": "LOW",
    "Debug": "LOW",
}

# AgentShroud-specific rule prefixes
AGENTSHROUD_RULES = [
    "AgentShroud",
    "OpenClaw",
    "Container Shell",
    "Unexpected Outbound",
    "Privilege Escalation",
    "Secret File Access",
    "Crypto Mining",
    "File Access Outside Workspace",
]


def read_alerts(
    alert_dir: Path = DEFAULT_ALERT_DIR,
    since: datetime | None = None,
    agentshroud_only: bool = False,
) -> list[dict[str, Any]]:
    """Read Falco alerts from the alert directory.

    Args:
        alert_dir: Directory containing Falco alert files.
        since: Only return alerts after this timestamp.
        agentshroud_only: Filter to AgentShroud-specific rules only.

    Returns:
        List of parsed alert dicts.
    """
    alerts: list[dict[str, Any]] = []

    if not alert_dir.exists():
        logger.warning("Falco alert directory not found: %s", alert_dir)
        return alerts

    for alert_file in sorted(alert_dir.glob("*.json")):
        try:
            content = alert_file.read_text()
            for line in content.strip().splitlines():
                if not line.strip():
                    continue
                try:
                    alert = json.loads(line)
                    parsed = parse_alert(alert)
                    if parsed:
                        alerts.append(parsed)
                except json.JSONDecodeError:
                    continue
        except OSError as e:
            logger.warning("Failed to read alert file %s: %s", alert_file, e)

    # Filter by time
    if since:
        since_str = since.isoformat()
        alerts = [a for a in alerts if a.get("timestamp", "") >= since_str]

    # Filter AgentShroud rules
    if agentshroud_only:
        alerts = [a for a in alerts if is_agentshroud_rule(a.get("rule", ""))]

    return alerts


def parse_alert(raw: dict[str, Any]) -> dict[str, Any] | None:
    """Parse a single Falco alert.

    Args:
        raw: Raw Falco alert JSON.

    Returns:
        Parsed alert dict or None if invalid.
    """
    if not raw:
        return None

    priority = raw.get("priority", "Unknown")
    severity = PRIORITY_MAP.get(priority, "MEDIUM")

    return {
        "timestamp": raw.get("time", datetime.now(timezone.utc).isoformat()),
        "rule": raw.get("rule", "unknown"),
        "severity": severity,
        "priority": priority,
        "output": raw.get("output", ""),
        "source": raw.get("source", "syscall"),
        "hostname": raw.get("hostname", ""),
        "container_id": raw.get("output_fields", {}).get("container.id", ""),
        "container_name": raw.get("output_fields", {}).get("container.name", ""),
        "process": raw.get("output_fields", {}).get("proc.name", ""),
        "raw": raw,
    }


def is_agentshroud_rule(rule_name: str) -> bool:
    """Check if a rule is AgentShroud-specific.

    Args:
        rule_name: Falco rule name.

    Returns:
        True if rule matches AgentShroud patterns.
    """
    return any(rule_name.startswith(prefix) for prefix in AGENTSHROUD_RULES)


def categorize_alerts(alerts: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Categorize alerts by severity.

    Args:
        alerts: List of parsed alerts.

    Returns:
        Dict mapping severity to list of alerts.
    """
    categories: dict[str, list[dict[str, Any]]] = {
        "CRITICAL": [],
        "HIGH": [],
        "MEDIUM": [],
        "LOW": [],
    }
    for alert in alerts:
        sev = alert.get("severity", "MEDIUM")
        if sev in categories:
            categories[sev].append(alert)
        else:
            categories["MEDIUM"].append(alert)
    return categories


def generate_summary(alerts: list[dict[str, Any]]) -> dict[str, Any]:
    """Generate a summary dict suitable for the health report.

    Args:
        alerts: List of parsed Falco alerts.

    Returns:
        Summary dict.
    """
    categories = categorize_alerts(alerts)

    critical = len(categories["CRITICAL"])
    high = len(categories["HIGH"])

    if critical > 0:
        status = "critical"
    elif high > 0:
        status = "warning"
    elif len(alerts) > 0:
        status = "info"
    else:
        status = "clean"

    # Top rules by frequency
    rule_counts: dict[str, int] = {}
    for alert in alerts:
        rule = alert.get("rule", "unknown")
        rule_counts[rule] = rule_counts.get(rule, 0) + 1
    top_rules = sorted(rule_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "tool": "falco",
        "status": status,
        "findings": len(alerts),
        "critical": critical,
        "high": high,
        "medium": len(categories["MEDIUM"]),
        "low": len(categories["LOW"]),
        "top_rules": [{"rule": r, "count": c} for r, c in top_rules],
        "agentshroud_alerts": len(
            [a for a in alerts if is_agentshroud_rule(a.get("rule", ""))]
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
