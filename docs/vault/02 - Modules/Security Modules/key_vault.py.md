---
title: key_vault.py
type: module
file_path: gateway/security/key_vault.py
tags: [security, secrets, api-key-isolation, credential-management, leak-detection, audit]
related: [[log_sanitizer.py]], [[egress_monitor.py]], [[token_validation.py]]
status: documented
---

# key_vault.py

## Purpose
Provides in-process API key isolation for the gateway: stores API keys in gateway memory only (never forwarded to agent containers), enforces per-agent scope control, injects keys transparently into proxied requests, redacts key values from all output, and scans outbound content for accidental key leakage.

## Threat Model
Prevents agent containers from ever observing raw API key values, which would allow prompt injection or compromised agents to exfiltrate credentials. Addresses both targeted leakage (stored key found in outbound payload) and generic pattern-based leakage (regex patterns for OpenAI, GitHub, AWS, Slack tokens). Maintains a full audit trail of every key access, denial, rotation, and detected leak.

## Responsibilities
- Store named key entries with per-agent scope restrictions
- Enforce agent scope when returning key values
- Log every key access, denial, rotation, and deletion to an in-memory audit ledger
- Redact all known key values (current and previously rotated) from arbitrary text
- Inject the correct key into proxied HTTP request headers as a Bearer token
- Scan outbound content for both stored key values and generic API key patterns
- Detect and log key leakage events

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `KeyVault` | Class | Central in-memory key store with scope enforcement, redaction, and audit logging |
| `KeyInjector` | Class | Injects a named key into HTTP request headers for a specific agent |
| `KeyLeakDetector` | Class | Scans outbound text for stored key values and generic credential patterns |
| `KeyVaultConfig` | Dataclass | Configuration: `redact_in_logs`, `detect_leaks` flags |
| `KeyEntry` | Dataclass | Stored key: name, value, scopes, created_at, rotated_at |
| `KeyScope` | Dataclass | Associates a key name with a list of permitted agent IDs |
| `KeyAuditEvent` | Dataclass | Single audit log entry: timestamp, key_name, agent_id, action, details |
| `LeakScanResult` | Dataclass | Result of an outbound scan: `leak_detected` flag and `leaked_key_names` list |
| `GENERIC_KEY_PATTERNS` | Constant | Compiled regex patterns for OpenAI, GitHub, AWS, Slack key formats |

## Function Details

### KeyVault.store_key(name, value, scopes)
**Purpose:** Stores a named key in memory. `scopes` is a list of agent IDs or `["*"]` for unrestricted access.
**Parameters:** `name` (str), `value` (str), `scopes` (list[str] | None)
**Returns:** `None`

### KeyVault.get_key(name, agent_id)
**Purpose:** Returns the key value only if `agent_id` is in scope; logs an access or denial event.
**Parameters:** `name` (str), `agent_id` (str)
**Returns:** `str | None`

### KeyVault.rotate_key(name, new_value)
**Purpose:** Replaces a key value, retains the old value in a redaction list to catch post-rotation leaks, and logs the rotation event.
**Parameters:** `name` (str), `new_value` (str)
**Returns:** `None`; raises `KeyError` if the key does not exist

### KeyVault.redact(text)
**Purpose:** Replaces all occurrences of current and previously rotated key values in `text` with `[REDACTED]`. Applied to any output before logging or proxying.
**Parameters:** `text` (str)
**Returns:** Sanitized `str`

### KeyVault.get_audit_log()
**Purpose:** Returns a snapshot of all audit events recorded since instantiation.
**Returns:** `list[KeyAuditEvent]`

### KeyVault.check_value_match(text)
**Purpose:** Returns the names of any stored keys whose raw values appear in `text`.
**Parameters:** `text` (str)
**Returns:** `list[str]`

### KeyInjector.inject_for_request(url, headers, agent_id, key_name)
**Purpose:** Retrieves the named key for the requesting agent and adds an `Authorization: Bearer <key>` header if the agent is in scope.
**Parameters:** `url` (str), `headers` (dict), `agent_id` (str), `key_name` (str)
**Returns:** Updated headers `dict`

### KeyLeakDetector.scan_outbound(text)
**Purpose:** Checks outbound content first for stored key literal matches, then for generic API key regex patterns. Logs `leak_detected` audit events for any match.
**Parameters:** `text` (str)
**Returns:** `LeakScanResult`

## Configuration / Environment Variables
- No environment variables; the vault is configured programmatically via `KeyVaultConfig`
- `redact_in_logs` (default `True`) — controls whether redaction is applied
- `detect_leaks` (default `True`) — controls whether outbound scanning is active

## Generic Key Patterns Detected
- `sk-proj-*` and `sk-*` — OpenAI API keys
- `ghp_*` / `gho_*` — GitHub Personal Access Tokens
- `AKIA*` — AWS Access Key IDs
- `xoxb-*` — Slack Bot tokens

## Related
- [[log_sanitizer.py]]
- [[egress_monitor.py]]
- [[token_validation.py]]
