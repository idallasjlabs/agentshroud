---
title: pipeline.py
type: module
file_path: gateway/proxy/pipeline.py
tags: [proxy, security-pipeline, audit, pii, prompt-injection, canary, egress]
related: [[mcp_proxy.py]], [[mcp_audit.py]], [[forwarder.py]]
status: documented
---

# pipeline.py

## Purpose
Implements the central `SecurityPipeline` that every message — inbound and outbound — must pass through before forwarding. Wires together all security guards into a deterministic, ordered sequence with a tamper-evident SHA-256 hash chain audit ledger.

## Responsibilities
- Route inbound messages through: prompt injection scan → PII sanitization → trust check → approval queue check → audit → forward
- Route outbound responses through: XML block stripping → PII sanitization → outbound info filter → encoding bypass detection → canary tripwire → egress URL check → audit → return
- Maintain a SHA-256 hash chain (`AuditChain`) of every processed message
- Enforce fail-closed policy: refuses to start if `pii_sanitizer` is absent
- Emit CRITICAL-level log warnings for each missing recommended guard
- Accumulate per-direction statistics for operational monitoring

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `PipelineAction` | Enum | FORWARD, BLOCK, or QUEUE_APPROVAL outcome |
| `PipelineResult` | Dataclass | Full result of pipeline processing — action, sanitized message, audit info, all findings |
| `AuditChainEntry` | Dataclass | One node in the SHA-256 linked hash chain |
| `AuditChain` | Class | Append-only tamper-evident ledger using SHA-256 chaining |
| `SecurityPipeline` | Class | Orchestrates all guards for inbound and outbound messages |

## Function Details

### AuditChain.append(content, direction, metadata)
**Purpose:** Append a new entry to the hash chain, linking it to the previous entry.
**Parameters:** `content` (str) — raw message text; `direction` (str) — flow label; `metadata` (dict) — extra context.
**Returns:** `AuditChainEntry` with computed `chain_hash` = SHA-256(prev_hash + content_hash + direction + timestamp).

### AuditChain.verify_chain()
**Purpose:** Walk the entire chain and validate every hash link.
**Parameters:** None.
**Returns:** `(bool, str)` — validity flag and descriptive message.

### SecurityPipeline.process_inbound(message, agent_id, action, source, metadata)
**Purpose:** Run a user/agent message through the full inbound security sequence.
**Parameters:** `message` (str), `agent_id` (str), `action` (str) — the MCP or API action being attempted, `source` (str), `metadata` (dict).
**Returns:** `PipelineResult`. Blocks and short-circuits at first failure (injection → trust → approval).

### SecurityPipeline.process_outbound(response, agent_id, destination_urls, metadata, user_trust_level, source)
**Purpose:** Run an LLM or tool response through the full outbound security sequence.
**Parameters:** `response` (str), `agent_id` (str), `destination_urls` (list[str]) — checked against egress filter, `user_trust_level` (str), `source` (str).
**Returns:** `PipelineResult`. Blocks at canary tripwire or egress denial; all other guards redact and continue.

### SecurityPipeline.get_stats()
**Purpose:** Return cumulative pipeline counters including audit chain health.
**Returns:** Dict with inbound/outbound totals, block counts, redaction counts, and `audit_chain_valid`.

### SecurityPipeline.verify_audit_chain()
**Purpose:** Expose chain integrity check for external health endpoints.
**Returns:** `(bool, str)` delegating to `AuditChain.verify_chain()`.

## Configuration / Environment Variables
- No direct environment variables; all guards are injected at construction time
- `prompt_block_threshold` (float, default 0.8) — score above which a prompt injection finding causes an immediate block
- `approval_actions` (list[str], default: execute_command, delete_file, admin_action, install_package) — action names that trigger the approval queue

## Guards (Fail Behavior)

| Guard | Required | Missing Behavior |
|-------|----------|-----------------|
| `pii_sanitizer` | Yes | Raises `RuntimeError` at startup (fail-closed) |
| `prompt_guard` | No | CRITICAL log; injection scanning skipped |
| `egress_filter` | No | CRITICAL log; egress check skipped |
| `outbound_filter` | No | CRITICAL log; info disclosure check skipped |
| `canary_tripwire` | No | CRITICAL log; canary detection skipped |
| `encoding_detector` | No | CRITICAL log; encoding bypass detection skipped |

## Related
- [[Architecture Overview]]
- [[Data Flow]]
- [[mcp_proxy.py]]
- [[mcp_audit.py]]
- [[forwarder.py]]
