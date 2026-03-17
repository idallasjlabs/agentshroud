# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC event adapter — normalises heterogeneous event sources into SecurityEvent.

Maps:
  AuditChainEntry  → SecurityEvent
  PipelineResult   → SecurityEvent
  EgressAttempt    → SecurityEvent
  AnomalyAlert     → SecurityEvent
  dict (generic)   → SecurityEvent
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from .models import SecurityEvent, Severity

logger = logging.getLogger("agentshroud.soc.event_adapter")


def _map_severity(raw: Any) -> Severity:
    """Best-effort mapping of arbitrary severity strings to Severity enum."""
    if isinstance(raw, Severity):
        return raw
    s = str(raw).lower() if raw else "info"
    mapping = {
        "critical": Severity.CRITICAL,
        "high": Severity.HIGH,
        "medium": Severity.MEDIUM,
        "low": Severity.LOW,
        "info": Severity.INFO,
        "warning": Severity.MEDIUM,
        "warn": Severity.MEDIUM,
        "error": Severity.HIGH,
    }
    return mapping.get(s, Severity.INFO)


def from_audit_chain_entry(entry: Any) -> SecurityEvent:
    """Convert AuditChainEntry (from AuditStore) to SecurityEvent."""
    try:
        ts_raw = getattr(entry, "timestamp", None) or ""
        details = {}
        direction = getattr(entry, "direction", "unknown")
        block_reason = getattr(entry, "block_reason", "") or ""
        agent_id = getattr(entry, "agent_id", "") or ""
        user_id = getattr(entry, "user_id", None)
        action_taken = getattr(entry, "action_taken", "allowed") or "allowed"

        if block_reason:
            details["block_reason"] = block_reason
        if direction:
            details["direction"] = direction

        return SecurityEvent(
            event_type=direction or "audit_entry",
            severity=_map_severity(getattr(entry, "severity", "info")),
            timestamp=ts_raw or datetime.now(timezone.utc).isoformat(),
            source_module="audit_store",
            agent_id=str(agent_id),
            user_id=str(user_id) if user_id else None,
            action_taken=action_taken,
            summary=block_reason or direction or "Audit entry",
            details=details,
            chain_hash=getattr(entry, "chain_hash", None),
            prev_hash=getattr(entry, "prev_hash", None),
        )
    except Exception as exc:
        logger.warning("from_audit_chain_entry: %s", exc)
        return SecurityEvent(event_type="audit_entry", summary="Conversion error")


def from_pipeline_result(result: Any, user_id: Optional[str] = None) -> SecurityEvent:
    """Convert a PipelineResult to SecurityEvent."""
    try:
        blocked = getattr(result, "blocked", False)
        block_reason = getattr(result, "block_reason", "") or ""
        sanitized = getattr(result, "sanitized", False)
        action = "blocked" if blocked else ("sanitized" if sanitized else "allowed")
        severity = Severity.HIGH if blocked else (Severity.MEDIUM if sanitized else Severity.INFO)
        event_type = "inbound_blocked" if blocked else "inbound_allowed"
        return SecurityEvent(
            event_type=event_type,
            severity=severity,
            source_module="pipeline",
            user_id=str(user_id) if user_id else None,
            action_taken=action,
            summary=block_reason or event_type,
            details={"block_reason": block_reason, "sanitized": sanitized},
        )
    except Exception as exc:
        logger.warning("from_pipeline_result: %s", exc)
        return SecurityEvent(event_type="pipeline_result", summary="Conversion error")


def from_egress_attempt(attempt: Any) -> SecurityEvent:
    """Convert an EgressAttempt or egress dict to SecurityEvent."""
    try:
        if isinstance(attempt, dict):
            domain = attempt.get("domain", "")
            blocked = attempt.get("blocked", False)
            reason = attempt.get("reason", "")
            agent = attempt.get("agent_id", "")
        else:
            domain = getattr(attempt, "domain", "")
            blocked = getattr(attempt, "blocked", False)
            reason = getattr(attempt, "reason", "") or ""
            agent = getattr(attempt, "agent_id", "") or ""

        action = "blocked" if blocked else "allowed"
        severity = Severity.HIGH if blocked else Severity.INFO
        return SecurityEvent(
            event_type="egress_denied" if blocked else "egress_allowed",
            severity=severity,
            source_module="egress_filter",
            agent_id=str(agent),
            action_taken=action,
            summary=f"Egress to {domain}: {action}" + (f" ({reason})" if reason else ""),
            details={"domain": domain, "blocked": blocked, "reason": reason},
        )
    except Exception as exc:
        logger.warning("from_egress_attempt: %s", exc)
        return SecurityEvent(event_type="egress_attempt", summary="Conversion error")


def from_anomaly_alert(alert: Any) -> SecurityEvent:
    """Convert an AnomalyAlert (from EgressMonitor/SOCCorrelation) to SecurityEvent."""
    try:
        if isinstance(alert, dict):
            title = alert.get("title", "Anomaly")
            sev = alert.get("severity", "medium")
            details = alert.get("details", {})
        else:
            title = getattr(alert, "title", "Anomaly") or "Anomaly"
            sev = getattr(alert, "severity", "medium")
            details = getattr(alert, "details", {}) or {}

        return SecurityEvent(
            event_type="anomaly_detected",
            severity=_map_severity(sev),
            source_module="egress_monitor",
            action_taken="alerted",
            summary=title,
            details=dict(details),
        )
    except Exception as exc:
        logger.warning("from_anomaly_alert: %s", exc)
        return SecurityEvent(event_type="anomaly_alert", summary="Conversion error")


def from_dict(raw: Dict[str, Any]) -> SecurityEvent:
    """Best-effort conversion of arbitrary event dict to SecurityEvent."""
    try:
        return SecurityEvent(
            event_type=raw.get("event_type", raw.get("type", "unknown")),
            severity=_map_severity(raw.get("severity", "info")),
            timestamp=raw.get("timestamp", datetime.now(timezone.utc).isoformat()),
            source_module=raw.get("source_module", raw.get("source", "")),
            agent_id=str(raw.get("agent_id", "")),
            user_id=str(raw["user_id"]) if raw.get("user_id") else None,
            action_taken=raw.get("action_taken", "unknown"),
            summary=raw.get("summary", raw.get("message", "")),
            details={k: v for k, v in raw.items() if k not in {"event_type", "severity", "timestamp", "source_module", "agent_id", "user_id", "action_taken", "summary"}},
        )
    except Exception as exc:
        logger.warning("from_dict: %s", exc)
        return SecurityEvent(event_type="unknown", summary="Conversion error")


async def collect_recent_events(
    audit_store: Any,
    limit: int = 100,
    since_iso: Optional[str] = None,
    severity_filter: Optional[str] = None,
) -> List[SecurityEvent]:
    """Collect recent SecurityEvents from AuditStore (async-safe read)."""
    events: List[SecurityEvent] = []
    if audit_store is None:
        return events
    try:
        raw_entries = await audit_store.get_recent_entries(limit=limit)
        for entry in raw_entries:
            ev = from_audit_chain_entry(entry)
            if severity_filter:
                target_sev = _map_severity(severity_filter)
                sev_rank = {Severity.INFO: 0, Severity.LOW: 1, Severity.MEDIUM: 2, Severity.HIGH: 3, Severity.CRITICAL: 4}
                if sev_rank.get(ev.severity, 0) < sev_rank.get(target_sev, 0):
                    continue
            events.append(ev)
    except Exception as exc:
        logger.warning("collect_recent_events: %s", exc)
    return events
