# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC unified data models.

SecurityEvent, EgressRequest, ServiceDescriptor, ContributorRecord,
Alarm, AuditLogEntry — canonical types for /soc/v1/ API and WebSocket stream.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _new_uuid() -> str:
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ServiceStatus(str, Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    PAUSED = "paused"
    RESTARTING = "restarting"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"
    NOT_INSTALLED = "not_installed"


class HealthStatus(str, Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    STARTING = "starting"
    UNKNOWN = "unknown"


class UserRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    COLLABORATOR = "collaborator"
    VIEWER = "viewer"


class Platform(str, Enum):
    TELEGRAM = "telegram"
    SLACK = "slack"
    SYSTEM = "system"


class AlarmStatus(str, Enum):
    TRIGGERED = "triggered"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    ARCHIVED = "archived"


class AuditResult(str, Enum):
    SUCCESS = "success"
    DENIED = "denied"
    FAILED = "failed"
    CONFIRMATION_REQUIRED = "confirmation_required"


class SCLInterface(str, Enum):
    WEB = "web"
    CLI = "cli"
    CHAT = "chat"
    SYSTEM = "system"


class RiskLevel(str, Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class EgressStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    DENIED = "denied"
    EXPIRED = "expired"


# ---------------------------------------------------------------------------
# SecurityEvent — unified envelope replaces fragmented pipeline/egress models
# ---------------------------------------------------------------------------

class SecurityEvent(BaseModel):
    event_id: str = Field(default_factory=_new_uuid)
    event_type: str
    severity: Severity = Severity.INFO
    timestamp: str = Field(default_factory=_now_iso)
    source_module: str = ""
    agent_id: str = ""
    user_id: Optional[str] = None
    action_taken: str = "allowed"
    summary: str = ""
    details: Dict[str, Any] = Field(default_factory=dict)
    chain_hash: Optional[str] = None
    prev_hash: Optional[str] = None


# ---------------------------------------------------------------------------
# EgressRequest — pending approval item
# ---------------------------------------------------------------------------

class EgressRequest(BaseModel):
    request_id: str = Field(default_factory=_new_uuid)
    domain: str
    port: int = 443
    agent_id: str = ""
    tool_name: str = ""
    risk_level: RiskLevel = RiskLevel.YELLOW
    submitted_at: str = Field(default_factory=_now_iso)
    expires_at: Optional[str] = None
    status: EgressStatus = EgressStatus.PENDING
    decided_by: Optional[str] = None
    decided_at: Optional[str] = None


# ---------------------------------------------------------------------------
# ServiceDescriptor
# ---------------------------------------------------------------------------

class ResourceUsage(BaseModel):
    cpu_percent: Optional[float] = None
    memory_mb: Optional[float] = None
    memory_limit_mb: Optional[float] = None


class ServiceDescriptor(BaseModel):
    name: str
    container_id: Optional[str] = None
    status: ServiceStatus = ServiceStatus.UNKNOWN
    health: HealthStatus = HealthStatus.UNKNOWN
    uptime_seconds: Optional[float] = None
    restart_count: int = 0
    image: str = ""
    version: Optional[str] = None
    ports: List[str] = Field(default_factory=list)
    networks: List[str] = Field(default_factory=list)
    resource_usage: ResourceUsage = Field(default_factory=ResourceUsage)
    dependencies: List[str] = Field(default_factory=list)
    is_internal: bool = False  # True = in-process gateway module, not a Docker container


# ---------------------------------------------------------------------------
# ContributorRecord
# ---------------------------------------------------------------------------

class ContributorRecord(BaseModel):
    user_id: str
    platform: Platform = Platform.TELEGRAM
    display_name: str = ""
    role: UserRole = UserRole.VIEWER
    groups: List[str] = Field(default_factory=list)
    projects: List[str] = Field(default_factory=list)
    collab_mode: str = "local_only"
    added_at: str = Field(default_factory=_now_iso)
    added_by: str = "system"
    last_active: Optional[str] = None
    total_messages: int = 0
    blocks_received: int = 0
    lockdown_level: str = "normal"
    immunity_active: bool = False
    immunity_expires: Optional[str] = None


# ---------------------------------------------------------------------------
# Alarm
# ---------------------------------------------------------------------------

class Alarm(BaseModel):
    alarm_id: str = Field(default_factory=_new_uuid)
    title: str
    severity: Severity = Severity.MEDIUM
    source_module: str = ""
    triggered_at: str = Field(default_factory=_now_iso)
    acknowledged_at: Optional[str] = None
    acknowledged_by: Optional[str] = None
    resolved_at: Optional[str] = None
    resolved_by: Optional[str] = None
    status: AlarmStatus = AlarmStatus.TRIGGERED
    details: Dict[str, Any] = Field(default_factory=dict)
    related_events: List[str] = Field(default_factory=list)
    auto_action: Optional[str] = None


# ---------------------------------------------------------------------------
# AuditLogEntry — SCL operator action audit trail
# ---------------------------------------------------------------------------

class AuditLogEntry(BaseModel):
    entry_id: str = Field(default_factory=_new_uuid)
    timestamp: str = Field(default_factory=_now_iso)
    actor_id: str
    actor_role: str
    interface: SCLInterface = SCLInterface.SYSTEM
    command: str
    target: str = ""
    result: AuditResult = AuditResult.SUCCESS
    details: Dict[str, Any] = Field(default_factory=dict)
    ip_address: Optional[str] = None
    chain_hash: str = ""


# ---------------------------------------------------------------------------
# SCL API response envelope
# ---------------------------------------------------------------------------

class SCLError(BaseModel):
    error: bool = True
    code: str
    message: str
    details: Dict[str, Any] = Field(default_factory=dict)


class SCLConfirmationRequired(BaseModel):
    error: bool = True
    code: str = "CONFIRMATION_REQUIRED"
    message: str
    action: str
    target: str


# ---------------------------------------------------------------------------
# WebSocket event envelope
# ---------------------------------------------------------------------------

class WSEventType(str, Enum):
    SECURITY_EVENT = "security_event"
    EGRESS_EVENT = "egress_event"
    APPROVAL_EVENT = "approval_event"
    SERVICE_EVENT = "service_event"
    LOG_EVENT = "log_event"
    KEEPALIVE = "keepalive"


class WSEvent(BaseModel):
    type: WSEventType
    timestamp: str = Field(default_factory=_now_iso)
    severity: Severity = Severity.INFO
    summary: str = ""
    details: Dict[str, Any] = Field(default_factory=dict)
    source_module: str = ""
