# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Wazuh HIDS integration.

Reads Wazuh alerts from shared volume for file integrity monitoring
and rootkit detection.
"""


import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_ALERT_DIR = Path("/var/ossec/logs/alerts")
DEFAULT_LOG_DIR = Path("/var/log/security/wazuh")

# Wazuh rule level to severity mapping
LEVEL_MAP = {
    range(0, 4): "LOW",
    range(4, 7): "LOW",
    range(7, 10): "MEDIUM",
    range(10, 13): "HIGH",
    range(13, 16): "CRITICAL",
}

# File integrity monitoring rule IDs
FIM_RULE_IDS = {
    550: "file_integrity_added",
    551: "file_integrity_deleted",
    553: "file_integrity_modified",
    554: "file_integrity_attributes_changed",
}

# Rootkit detection rule IDs
ROOTKIT_RULE_IDS = {
    510: "rootkit_trojan",
    512: "rootkit_hidden_file",
    513: "rootkit_hidden_process",
    514: "rootkit_hidden_port",
}


def level_to_severity(level: int) -> str:
    """Map Wazuh alert level to severity string.

    Args:
        level: Wazuh alert level (0-15).

    Returns:
        Severity string.
    """
    for level_range, severity in LEVEL_MAP.items():
        if level in level_range:
            return severity
    return "MEDIUM"


def read_alerts(
    alert_dir: Path = DEFAULT_ALERT_DIR,
    since: datetime | None = None,
) -> list[dict[str, Any]]:
    """Read Wazuh alerts from the alert directory.

    Args:
        alert_dir: Directory containing Wazuh alert files.
        since: Only return alerts after this timestamp.

    Returns:
        List of parsed alert dicts.
    """
    alerts: list[dict[str, Any]] = []

    if not alert_dir.exists():
        logger.warning("Wazuh alert directory not found: %s", alert_dir)
        return alerts

    for alert_file in sorted(alert_dir.glob("alerts*.json")):
        try:
            content = alert_file.read_text()
            for line in content.strip().splitlines():
                if not line.strip():
                    continue
                try:
                    raw = json.loads(line)
                    parsed = parse_alert(raw)
                    if parsed:
                        alerts.append(parsed)
                except json.JSONDecodeError:
                    continue
        except OSError as e:
            logger.warning("Failed to read alert file %s: %s", alert_file, e)

    if since:
        since_str = since.isoformat()
        alerts = [a for a in alerts if a.get("timestamp", "") >= since_str]

    return alerts


def parse_alert(raw: dict[str, Any]) -> dict[str, Any] | None:
    """Parse a single Wazuh alert.

    Args:
        raw: Raw Wazuh alert JSON.

    Returns:
        Parsed alert dict or None if invalid.
    """
    if not raw:
        return None

    rule = raw.get("rule", {})
    rule_id = int(rule.get("id", 0))
    level = int(rule.get("level", 0))
    severity = level_to_severity(level)

    alert_type = "general"
    if rule_id in FIM_RULE_IDS:
        alert_type = FIM_RULE_IDS[rule_id]
    elif rule_id in ROOTKIT_RULE_IDS:
        alert_type = ROOTKIT_RULE_IDS[rule_id]

    syscheck = raw.get("syscheck", {})

    return {
        "timestamp": raw.get("timestamp", datetime.now(timezone.utc).isoformat()),
        "rule_id": rule_id,
        "rule_description": rule.get("description", ""),
        "level": level,
        "severity": severity,
        "alert_type": alert_type,
        "agent": raw.get("agent", {}).get("name", ""),
        "file_path": syscheck.get("path", ""),
        "file_event": syscheck.get("event", ""),
        "file_md5_before": syscheck.get("md5_before", ""),
        "file_md5_after": syscheck.get("md5_after", ""),
        "raw": raw,
    }


def get_fim_events(alerts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter alerts to file integrity monitoring events only.

    Args:
        alerts: List of parsed alerts.

    Returns:
        FIM events only.
    """
    fim_types = set(FIM_RULE_IDS.values())
    return [a for a in alerts if a.get("alert_type") in fim_types]


def get_rootkit_events(alerts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Filter alerts to rootkit detection events only.

    Args:
        alerts: List of parsed alerts.

    Returns:
        Rootkit events only.
    """
    rootkit_types = set(ROOTKIT_RULE_IDS.values())
    return [a for a in alerts if a.get("alert_type") in rootkit_types]


def generate_summary(alerts: list[dict[str, Any]]) -> dict[str, Any]:
    """Generate a summary dict suitable for the health report.

    Args:
        alerts: List of parsed Wazuh alerts.

    Returns:
        Summary dict.
    """
    fim_events = get_fim_events(alerts)
    rootkit_events = get_rootkit_events(alerts)

    severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for alert in alerts:
        sev = alert.get("severity", "MEDIUM")
        if sev in severity_counts:
            severity_counts[sev] += 1

    critical = severity_counts["CRITICAL"]
    high = severity_counts["HIGH"]

    if critical > 0 or len(rootkit_events) > 0:
        status = "critical"
    elif high > 0:
        status = "warning"
    elif len(alerts) > 0:
        status = "info"
    else:
        status = "clean"

    # Files modified
    modified_files = list(
        {
            a["file_path"]
            for a in fim_events
            if a.get("file_path") and a.get("alert_type") == "file_integrity_modified"
        }
    )

    return {
        "tool": "wazuh",
        "status": status,
        "findings": len(alerts),
        "critical": critical,
        "high": high,
        "medium": severity_counts["MEDIUM"],
        "low": severity_counts["LOW"],
        "fim_events": len(fim_events),
        "rootkit_events": len(rootkit_events),
        "modified_files": modified_files[:20],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
