# SSH Capability — Architecture Document

## Overview

The SSH proxy module provides **controlled remote command execution** through the AgentShroud Gateway. Instead of granting agents or automation direct SSH access to hosts, all commands flow through the Gateway API, which enforces validation, approval workflows, and audit logging before any command reaches the target.

**Why it exists:**

- Prevents unrestricted shell access from AI agents or automation scripts
- Enforces allow/deny lists and injection detection on every command
- Routes sensitive commands through a human approval queue
- Creates a tamper-evident audit trail with PII sanitization

## Architecture

```
┌──────────┐     ┌───────────────────────────────────────────────┐     ┌─────────────┐
│          │     │              AgentShroud Gateway               │     │             │
│  Client  │────▶│                                               │────▶│ Target Host │
│  (API)   │ POST│  ┌────────────┐  ┌──────────────┐            │ SSH │ (e.g. Pi)   │
│          │◀────│  │  Command   │─▶│  Approval    │            │◀────│             │
│          │     │  │ Validation │  │  Queue       │            │     │             │
└──────────┘     │  └────────────┘  └──────┬───────┘            │     └─────────────┘
                 │       │                 │                     │
                 │       │ auto-approve    │ approved            │
                 │       ▼                 ▼                     │
                 │  ┌─────────────────────────┐  ┌───────────┐  │
                 │  │      SSHProxy           │─▶│  Ledger   │  │
                 │  │  (asyncio subprocess)   │  │  + PII    │  │
                 │  └─────────────────────────┘  │  Sanitize │  │
                 │                               └───────────┘  │
                 └───────────────────────────────────────────────┘
```

## Request Flow

### Auto-Approved Commands

Commands that exactly match `auto_approve_commands` skip the approval queue:

1. Client sends `POST /ssh/exec` with host, command, and auth token
2. Gateway validates: injection check → global deny list → host deny list → host allow list
3. Command matches an auto-approve entry → execute immediately
4. SSHProxy runs the command via `asyncio.create_subprocess_exec`
5. Output is returned; command is PII-sanitized and recorded in the ledger

### Approval-Required Commands

Commands that pass validation but aren't auto-approved:

1. Steps 1–2 same as above
2. Command is not auto-approved and `require_approval` is `true`
3. Gateway returns **HTTP 202** with a `request_id` and `pending_approval` status
4. Request enters the approval queue; human reviews via dashboard or API
5. On approval, the command executes and result is recorded
6. On rejection or expiry, the command is never executed

### Denied Commands

Commands that fail validation never reach the approval queue:

1. Validation detects injection, deny-list match, or allow-list miss
2. Gateway returns **HTTP 403** with the denial reason
3. The denied attempt is PII-sanitized and recorded in the ledger

## Security Layers

| Layer | Purpose | Implementation |
|-------|---------|----------------|
| **Injection Detection** | Block shell metacharacters (`; \| & \` $()` etc.) | Regex pattern in `INJECTION_PATTERNS` and executed directly without a shell (via `asyncio.create_subprocess_exec`) |
| **Global Deny List** | Block catastrophic commands across all hosts | `global_denied_commands` in config |
| **Per-Host Deny List** | Block host-specific dangerous commands | `denied_commands` per host |
| **Per-Host Allow List** | Whitelist-only mode when non-empty | `allowed_commands` per host |
| **Approval Queue** | Human review for non-auto-approved commands | Configurable via `require_approval` |
| **PII Sanitization** | Strip sensitive data from audit logs | Presidio engine on commands before ledger storage |
| **Host Key Verification** | Prevent MITM attacks | `StrictHostKeyChecking=accept-new` (TOFU) with optional `known_hosts_file` |
| **Timeout Enforcement** | Prevent runaway commands | `max_session_seconds` per host; process killed on expiry |

## Components

### `SSHProxy` (`gateway/ssh_proxy/proxy.py`)

Core execution engine:

- **`validate_command(host, command)`** — Runs all validation checks. Returns `(bool, reason)`.
- **`is_auto_approved(host, command)`** — Checks exact match against auto-approve list.
- **`execute(host, command, timeout)`** — Builds SSH arguments, spawns subprocess, enforces timeout. Returns `SSHResult`.

### `SSHConfig` / `SSHHostConfig` (`gateway/ingest_api/ssh_config.py`)

Pydantic configuration models:

- **`SSHConfig`** — Top-level: `enabled`, `require_approval`, `global_denied_commands`, `hosts` dict.
- **`SSHHostConfig`** — Per-host: connection details, allow/deny/auto-approve lists, timeout, key path.

### API Endpoints (`gateway/ingest_api/main.py`)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ssh/exec` | POST | Execute a command (with validation + approval flow) |
| `/ssh/hosts` | GET | List configured host names |
| `/ssh/history` | GET | Query SSH audit entries from the ledger (paginated) |

### Request/Response Models (`gateway/ingest_api/models.py`)

- **`SSHExecRequest`** — `host`, `command`, `timeout`, `reason`
- **`SSHExecResponse`** — Full result including `stdout`, `stderr`, `exit_code`, `duration_seconds`, `approved_by`, `audit_id`
