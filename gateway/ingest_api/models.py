# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Pydantic models for AgentShroud Gateway API

Defines request and response schemas for all endpoints.
"""


from typing import Any, Optional

from pydantic import BaseModel, Field, field_validator

# === Request Models ===


class ForwardRequest(BaseModel):
    """Request to forward content through the gateway

    Received from iOS Shortcuts, browser extension, scripts, or direct API calls.
    """

    content: str = Field(..., description="The text/data being forwarded")
    source: str = Field(
        ...,
        description="Source of the content: shortcut, browser_extension, script, api",
    )
    content_type: str = Field(
        default="text", description="Type: text, url, photo, file"
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict, description="Optional routing hints and context"
    )
    route_to: Optional[str] = Field(
        default=None, description="Optional explicit target agent name"
    )
    user_id: Optional[str] = Field(
        default=None, description="Telegram/platform user ID for RBAC. Set by gateway for webhook requests."
    )

    @field_validator("content")
    @classmethod
    def content_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("content must not be empty")
        return v

    @field_validator("source")
    @classmethod
    def validate_source(cls, v: str) -> str:
        allowed = {"shortcut", "browser_extension", "script", "api", "telegram", "chat-console", "control-center"}
        if v not in allowed:
            raise ValueError(f"source must be one of {allowed}")
        return v


class ApprovalRequest(BaseModel):
    """Request for human approval of a sensitive action

    Submitted by an agent when attempting actions like email_sending, file_deletion, etc.
    """

    action_type: str = Field(..., description="Type of action requiring approval")
    description: str = Field(
        ..., description="Human-readable description of the action"
    )
    details: dict[str, Any] = Field(
        default_factory=dict, description="Action-specific payload"
    )
    agent_id: str = Field(
        default="openclaw-main", description="Agent requesting approval"
    )


class ApprovalDecision(BaseModel):
    """User's decision on a pending approval request"""

    request_id: str = Field(..., description="ID of the approval request")
    approved: bool = Field(..., description="Whether to approve or reject")
    reason: str = Field(default="", description="Optional reason for decision")


# === Response Models ===


class ForwardResponse(BaseModel):
    """Response after content is ingested, sanitized, and logged"""

    id: str = Field(..., description="Ledger entry UUID")
    sanitized: bool = Field(..., description="Whether PII was redacted")
    redactions: list[str] = Field(
        ..., description="Entity types redacted (e.g., ['US_SSN', 'EMAIL_ADDRESS'])"
    )
    redaction_count: int = Field(..., description="Total number of redactions made")
    content_hash: str = Field(..., description="SHA-256 hash of sanitized content")
    forwarded_to: str = Field(..., description="Target agent name")
    timestamp: str = Field(..., description="ISO 8601 timestamp")
    agent_response: Optional[str] = Field(
        None, description="Agent's response if available"
    )
    audit_entry_id: Optional[str] = Field(
        None, description="Pipeline audit chain entry ID"
    )
    audit_hash: Optional[str] = Field(
        None, description="SHA-256 hash chain entry for tamper-evident audit"
    )
    prompt_score: Optional[float] = Field(
        None, description="Prompt injection risk score (0.0–1.0)"
    )


class LedgerEntry(BaseModel):
    """Single entry from the data ledger"""

    id: str
    timestamp: str
    source: str
    content_hash: str
    sanitized: bool
    size: int
    redaction_count: int
    forwarded_to: str


class LedgerQueryResponse(BaseModel):
    """Paginated ledger query results"""

    entries: list[LedgerEntry]
    total: int
    page: int
    page_size: int


class StatusResponse(BaseModel):
    """Health check response"""

    status: str = Field(..., description="Service status: healthy, degraded, unhealthy")
    version: str = Field(..., description="Gateway version")
    uptime_seconds: float = Field(..., description="Uptime in seconds")
    ledger_entries: int = Field(..., description="Total entries in ledger")
    pending_approvals: int = Field(..., description="Pending approval requests")
    pii_engine: str = Field(..., description="PII detection engine: presidio or regex")
    config_loaded: bool = Field(..., description="Whether config loaded successfully")


class ApprovalQueueItem(BaseModel):
    """A pending approval request in the queue"""

    request_id: str
    action_type: str
    description: str
    details: dict[str, Any]
    agent_id: str
    submitted_at: str  # ISO 8601
    expires_at: str  # ISO 8601
    status: str  # pending, approved, rejected, expired


# === Internal/Utility Models ===


class RedactionDetail(BaseModel):
    """Individual redaction record"""

    entity_type: str
    start: int
    end: int
    score: float
    replacement: str


class RedactionResult(BaseModel):
    """Result of PII sanitization"""

    sanitized_content: str
    redactions: list[RedactionDetail]
    entity_types_found: list[str]


class AgentTarget(BaseModel):
    """Downstream OpenClaw agent target"""

    name: str
    url: str
    healthy: bool = False
    last_health_check: Optional[str] = None
    content_types: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


# === SSH Models ===


class SSHExecRequest(BaseModel):
    """Request to execute an SSH command"""

    host: str = Field(..., description="SSH host name from config")
    command: str = Field(..., description="Command to execute")
    timeout: Optional[int] = Field(default=None, description="Timeout in seconds")
    reason: str = Field(default="", description="Reason for execution")


class SSHExecResponse(BaseModel):
    """Response from SSH command execution"""

    request_id: str
    host: str
    command: str
    stdout: str
    stderr: str
    exit_code: int
    duration_seconds: float
    approved_by: str
    timestamp: str
    audit_id: str


# === Channel Ownership Models (P3) ===


class EmailSendRequest(BaseModel):
    """Request to send an email through the gateway (P3: channel ownership).

    The bot submits this to the gateway instead of calling Gmail directly.
    Gateway validates recipient, scans body for PII, and either approves or
    queues the send for human approval.
    """

    to: str = Field(..., description="Recipient email address")
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body text")
    agent_id: str = Field(default="openclaw-main", description="Requesting agent")

    @field_validator("subject")
    @classmethod
    def subject_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("subject must not be empty")
        return v

    @field_validator("body")
    @classmethod
    def body_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("body must not be empty")
        return v


class EmailSendResponse(BaseModel):
    """Response from POST /email/send."""

    status: str = Field(..., description="approved | queued | blocked")
    sanitized_body: Optional[str] = Field(None, description="Body after PII redaction")
    pii_redacted: bool = Field(False, description="Whether PII was removed from body")
    approval_id: Optional[str] = Field(None, description="Approval queue ID if queued")
    timestamp: str = Field(..., description="ISO 8601 timestamp")
