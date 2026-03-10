# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC correlation helpers.

Builds a compact cross-signal security view by correlating:
- egress denials/attempts
- quarantined blocked messages
- Wazuh and Falco alerts
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from collections import Counter
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlparse


@dataclass
class CorrelationSummary:
    risk_score: int
    severity: str
    egress_denied: int
    egress_allowed: int
    quarantined_messages: int
    quarantined_outbound_messages: int
    wazuh_alerts: int
    falco_alerts: int
    private_data_policy_violations: int
    private_data_redactions: int
    top_denied_destinations: list[dict[str, Any]]
    top_policy_violators: list[dict[str, Any]]
    egress_trend: dict[str, int]
    scanner_findings: dict[str, Any]
    scanner_recent_critical_events: int
    correlated_findings: list[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_correlation_summary(app_state, limit: int = 200) -> CorrelationSummary:
    now = datetime.now(timezone.utc)
    correlated: list[dict[str, Any]] = []

    egress_denied = 0
    egress_allowed = 0
    denied_destinations: Counter[str] = Counter()
    denied_agents: Counter[str] = Counter()
    egress_log = []
    if getattr(app_state, "egress_filter", None):
        egress_log = app_state.egress_filter.get_log(limit=limit)
        for a in egress_log:
            if a.action.value == "deny":
                egress_denied += 1
                dest = a.destination
                if "://" in dest:
                    parsed = urlparse(dest)
                    dest = parsed.hostname or dest
                denied_destinations[dest] += 1
                denied_agents[a.agent_id] += 1
            else:
                egress_allowed += 1

    quarantine = getattr(app_state, "blocked_message_quarantine", []) or []
    quarantined_messages = len(quarantine[-limit:])
    outbound_quarantine = getattr(app_state, "blocked_outbound_quarantine", []) or []
    quarantined_outbound_messages = len(outbound_quarantine[-limit:])

    wazuh_alerts = 0
    if getattr(app_state, "wazuh_client", None):
        try:
            alerts = app_state.wazuh_client.read_alerts()
            wazuh_alerts = len(alerts[-limit:])
        except Exception:
            wazuh_alerts = 0

    falco_alerts = 0
    if getattr(app_state, "falco_monitor", None):
        try:
            alerts = app_state.falco_monitor.read_alerts()
            falco_alerts = len(alerts[-limit:])
        except Exception:
            falco_alerts = 0

    private_data_policy_violations = 0
    private_data_redactions = 0
    if getattr(app_state, "mcp_proxy", None):
        perms = getattr(app_state.mcp_proxy, "permissions", None)
        if perms and hasattr(perms, "get_private_access_summary"):
            private_summary = perms.get_private_access_summary(limit=limit)
            private_data_policy_violations = private_summary.get("total", 0)
            by_agent = private_summary.get("by_agent", {})
            for agent_id, count in by_agent.items():
                denied_agents[agent_id] += int(count)
            if hasattr(perms, "get_private_redaction_summary"):
                private_data_redactions = int(
                    perms.get_private_redaction_summary(limit=limit).get("total_redactions", 0)
                )

    egress_trend = {
        "denied": egress_denied,
        "allowed": egress_allowed,
        "pending": 0,
    }
    queue = getattr(app_state, "egress_approval_queue", None)
    if queue and hasattr(queue, "_pending_requests"):
        try:
            egress_trend["pending"] = len(queue._pending_requests)  # read-only dashboard metric
        except Exception:
            egress_trend["pending"] = 0

    scanner_results = getattr(app_state, "scanner_results", {}) or {}
    scanner_history = list(getattr(app_state, "scanner_result_history", []) or [])
    scanner_findings = {
        "critical": 0,
        "high": 0,
        "findings": 0,
        "scanners": {},
    }
    for scanner_name, scanner_data in scanner_results.items():
        if not isinstance(scanner_data, dict):
            continue
        summary = scanner_data.get("summary", {}) or {}
        critical = int(summary.get("critical", 0) or 0)
        high = int(summary.get("high", 0) or 0)
        findings = int(summary.get("findings", 0) or 0)
        scanner_findings["critical"] += critical
        scanner_findings["high"] += high
        scanner_findings["findings"] += findings
        scanner_findings["scanners"][scanner_name] = summary
    scanner_recent_critical_events = sum(
        1
        for item in scanner_history[-limit:]
        if str((item.get("summary") or {}).get("status", "")).lower() == "critical"
    )

    # Correlation rules (simple, deterministic)
    if egress_denied >= 3 and quarantined_messages >= 3:
        correlated.append(
            {
                "type": "possible_data_exfiltration_campaign",
                "confidence": "high",
                "details": "Multiple egress denials plus blocked/quarantined inbound prompts",
            }
        )
    if quarantined_outbound_messages >= 1:
        correlated.append(
            {
                "type": "outbound_content_blocking_active",
                "confidence": "medium",
                "details": f"Blocked outbound messages quarantined: {quarantined_outbound_messages}",
            }
        )
    if egress_denied >= 1 and (wazuh_alerts > 0 or falco_alerts > 0):
        correlated.append(
            {
                "type": "network_plus_host_signal_overlap",
                "confidence": "medium",
                "details": "Egress denials observed alongside host-level security alerts",
            }
        )
    if private_data_policy_violations >= 1:
        correlated.append(
            {
                "type": "private_data_access_attempts",
                "confidence": "high" if private_data_policy_violations >= 3 else "medium",
                "details": f"Blocked admin-private access attempts: {private_data_policy_violations}",
            }
        )
    if private_data_redactions >= 1:
        correlated.append(
            {
                "type": "private_data_redacted_from_results",
                "confidence": "medium",
                "details": f"Admin-private data redactions applied: {private_data_redactions}",
            }
        )
    if scanner_findings["critical"] > 0:
        correlated.append(
            {
                "type": "critical_scanner_findings",
                "confidence": "high",
                "details": f"Critical findings from scanners: {scanner_findings['critical']}",
            }
        )
    if scanner_recent_critical_events >= 3:
        correlated.append(
            {
                "type": "repeated_critical_scanner_events",
                "confidence": "high",
                "details": f"Recent critical scanner events: {scanner_recent_critical_events}",
            }
        )
    elif scanner_findings["high"] > 0:
        correlated.append(
            {
                "type": "high_scanner_findings",
                "confidence": "medium",
                "details": f"High findings from scanners: {scanner_findings['high']}",
            }
        )

    risk_score = min(
        100,
        egress_denied * 8
        + quarantined_messages * 3
        + quarantined_outbound_messages * 4
        + wazuh_alerts * 2
        + falco_alerts * 2
        + private_data_policy_violations * 10
        + private_data_redactions * 2
        + scanner_findings["critical"] * 12
        + scanner_findings["high"] * 6
        + scanner_recent_critical_events * 3
        + len(correlated) * 15,
    )
    if risk_score >= 70:
        severity = "critical"
    elif risk_score >= 40:
        severity = "high"
    elif risk_score >= 20:
        severity = "medium"
    else:
        severity = "low"

    correlated.append(
        {
            "type": "generated_at",
            "timestamp": now.isoformat(),
        }
    )

    return CorrelationSummary(
        risk_score=risk_score,
        severity=severity,
        egress_denied=egress_denied,
        egress_allowed=egress_allowed,
        quarantined_messages=quarantined_messages,
        quarantined_outbound_messages=quarantined_outbound_messages,
        wazuh_alerts=wazuh_alerts,
        falco_alerts=falco_alerts,
        private_data_policy_violations=private_data_policy_violations,
        private_data_redactions=private_data_redactions,
        top_denied_destinations=[
            {"destination": dest, "count": count}
            for dest, count in denied_destinations.most_common(5)
        ],
        top_policy_violators=[
            {"agent_id": agent_id, "count": count}
            for agent_id, count in denied_agents.most_common(5)
        ],
        egress_trend=egress_trend,
        scanner_findings=scanner_findings,
        scanner_recent_critical_events=scanner_recent_critical_events,
        correlated_findings=correlated,
    )
