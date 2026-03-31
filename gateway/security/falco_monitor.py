# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Falco runtime security monitoring integration.

Reads Falco alerts from shared volume and parses JSON format.
"""


import asyncio
import hashlib
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
    "Container Shell",
    "Unexpected Outbound",
    "Privilege Escalation",
    "Secret File Access",
    "Crypto Mining",
    "File Access Outside Workspace",
]


def configure_rules(bot_names: list[str]) -> None:
    """Extend AGENTSHROUD_RULES with bot-specific name prefixes.

    Called at gateway startup after bots are loaded from config so that
    Falco alerts prefixed with the registered bot name (e.g. "OpenClaw")
    are captured by is_agentshroud_rule() without hardcoding them here.

    Args:
        bot_names: List of BotConfig.name values to add as rule prefixes.
    """
    global AGENTSHROUD_RULES
    for name in bot_names:
        if name and name not in AGENTSHROUD_RULES:
            AGENTSHROUD_RULES.append(name)
            logger.info("Falco rule prefix registered: %s", name)


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


class FalcoAlertWatcher:
    """Tail Falco alert files and trigger progressive lockdown on CRITICAL alerts.

    Runs as an async background task.  Each alert is deduplicated by content
    hash so a single event is only acted on once per gateway lifetime.

    Fail mode: if Falco alert directory does not exist, the watcher no-ops
    gracefully — Falco is unavailable in many dev environments (no eBPF).
    """

    _POLL_INTERVAL_SECS = 30

    def __init__(
        self,
        alert_dir: Path = DEFAULT_ALERT_DIR,
        progressive_lockdown=None,
        audit_store=None,
    ) -> None:
        self.alert_dir = Path(alert_dir)
        self.progressive_lockdown = progressive_lockdown
        self.audit_store = audit_store
        self._seen: set[str] = set()
        self._running = False

    async def run(self) -> None:
        """Poll Falco alert files until stopped."""
        self._running = True
        logger.info("FalcoAlertWatcher started, monitoring: %s", self.alert_dir)
        while self._running:
            try:
                await self._process_new_alerts()
            except Exception as exc:
                logger.error("FalcoAlertWatcher poll error: %s", exc)
            await asyncio.sleep(self._POLL_INTERVAL_SECS)

    def stop(self) -> None:
        self._running = False

    async def _process_new_alerts(self) -> None:
        if not self.alert_dir.exists():
            return
        for alert_file in sorted(self.alert_dir.glob("*.json")):
            try:
                content = alert_file.read_text()
            except OSError:
                continue
            for line in content.strip().splitlines():
                if not line.strip():
                    continue
                alert_key = hashlib.sha256(line.encode()).hexdigest()[:16]
                if alert_key in self._seen:
                    continue
                self._seen.add(alert_key)
                try:
                    raw = json.loads(line)
                    alert = parse_alert(raw)
                    if alert and alert.get("severity") == "CRITICAL":
                        await self._handle_critical(alert)
                except json.JSONDecodeError:
                    continue

    async def _handle_critical(self, alert: dict[str, Any]) -> None:
        container_name = alert.get("container_name", "")
        agent_id = container_name or "unknown"
        rule = alert.get("rule", "unknown")
        summary = f"Falco CRITICAL: {rule} in container={container_name or 'unknown'}"
        logger.critical("FalcoAlertWatcher enforcement: %s", summary)

        if self.progressive_lockdown is not None:
            try:
                self.progressive_lockdown.record_block(agent_id, reason=summary)
            except Exception as exc:
                logger.error("FalcoAlertWatcher lockdown record_block failed: %s", exc)

        if self.audit_store is not None:
            try:
                await self.audit_store.log_event(
                    event_type="falco_enforcement",
                    severity="CRITICAL",
                    details={"rule": rule, "container": container_name, "alert": alert},
                    source_module="falco_monitor.watcher",
                )
            except Exception as exc:
                logger.error("FalcoAlertWatcher audit log failed: %s", exc)


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
