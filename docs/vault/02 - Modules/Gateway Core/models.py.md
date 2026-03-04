---
title: models.py
type: module
file_path: gateway/ingest_api/models.py
tags: [pydantic, models, schema, api, gateway-core]
related: [Gateway Core/main.py, Gateway Core/sanitizer.py, Gateway Core/ledger.py, Gateway Core/router.py]
status: documented
---

# models.py

## Purpose
Defines all Pydantic v2 request, response, and internal data models for the AgentShroud gateway API. Acts as the single source of truth for the API schema.

## Responsibilities
- Define validated request models for content forwarding, approval workflow, SSH execution, and email sending
- Define response models for all API endpoints
- Define internal utility models used between modules (PII redaction records, agent targets)
- Enforce validation rules (non-empty fields, allowed source values) via `@field_validator`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ForwardRequest` | class | Inbound request to forward content through the gateway |
| `ApprovalRequest` | class | Agent submission for human approval of a sensitive action |
| `ApprovalDecision` | class | Human decision on a pending approval (approve/reject) |
| `ForwardResponse` | class | Response after ingestion, sanitization, and ledger recording |
| `LedgerEntry` | class | Single ledger record returned by query endpoints |
| `LedgerQueryResponse` | class | Paginated ledger query result |
| `StatusResponse` | class | Health check response with component status |
| `ApprovalQueueItem` | class | A pending approval request in the queue |
| `RedactionDetail` | class | Record of a single PII redaction (position, type, score) |
| `RedactionResult` | class | Full result from PII sanitization (content + all redactions) |
| `AgentTarget` | class | Downstream agent routing target (name, URL, health status) |
| `SSHExecRequest` | class | Request to execute a validated SSH command |
| `SSHExecResponse` | class | Result of SSH command execution with audit info |
| `EmailSendRequest` | class | P3 channel ownership — request to send an email via gateway |
| `EmailSendResponse` | class | Response from email send with PII redaction status |

## Model Details

### ForwardRequest
**Fields:**
- `content: str` — required, non-empty (validated)
- `source: str` — required, must be one of: `shortcut`, `browser_extension`, `script`, `api`, `telegram`, `chat-console`, `control-center`
- `content_type: str` — default `"text"`, one of: text, url, photo, file
- `metadata: dict[str, Any]` — optional routing hints
- `route_to: Optional[str]` — explicit target agent name
- `user_id: Optional[str]` — Telegram/platform user ID for RBAC

### ForwardResponse
**Fields:**
- `id: str` — ledger entry UUID
- `sanitized: bool`, `redactions: list[str]`, `redaction_count: int`
- `content_hash: str` — SHA-256 of sanitized content
- `forwarded_to: str`, `timestamp: str` (ISO 8601)
- `agent_response: Optional[str]` — agent's response text
- `audit_entry_id: Optional[str]`, `audit_hash: Optional[str]` — tamper-evident chain
- `prompt_score: Optional[float]` — prompt injection risk score (0.0–1.0)

### RedactionDetail
**Fields:** `entity_type`, `start`, `end`, `score`, `replacement`
Used internally by [[Gateway Core/sanitizer.py]] and returned in `RedactionResult`.

### AgentTarget
**Fields:** `name`, `url`, `healthy`, `last_health_check`, `content_types`, `tags`
Used by [[Gateway Core/router.py]] to track routing state.

### EmailSendRequest
**Fields:** `to`, `subject`, `body`, `agent_id`
Both `subject` and `body` validated non-empty.
**Response statuses:** `approved` | `queued` | `blocked`

### SSHExecRequest / SSHExecResponse
Request fields: `host`, `command`, `timeout`, `reason`
Response fields: `request_id`, `host`, `command`, `stdout`, `stderr`, `exit_code`, `duration_seconds`, `approved_by`, `timestamp`, `audit_id`

## Environment Variables Used
- None — models are pure Pydantic schemas with no environment access

## Config Keys Read
- None

## Imports From / Exports To
- Imports: `pydantic` (`BaseModel`, `Field`, `field_validator`)
- Exported to: [[Gateway Core/main.py]], [[Gateway Core/sanitizer.py]], [[Gateway Core/ledger.py]], [[Gateway Core/router.py]], [[Gateway Core/ssh_config.py]]

## Known Issues / Notes
- `ForwardRequest.validate_source` uses a hard-coded set of allowed sources. Adding new sources (e.g., a new client type) requires a code change here.
- `LedgerEntry` duplicates some fields that are also in the SQLite schema in [[Gateway Core/ledger.py]] — schema drift between the two is a risk.
- `ApprovalQueueItem.status` is a plain `str` (`pending`, `approved`, `rejected`, `expired`) without an Enum, so validation relies on the approval queue implementation.
- `EmailSendResponse.status` similarly uses free-form string values.

## Related
- [[Gateway Core/main.py]]
- [[Gateway Core/sanitizer.py]]
- [[Gateway Core/ledger.py]]
- [[Gateway Core/router.py]]
