---
title: mcp_audit.py
type: module
file_path: gateway/proxy/mcp_audit.py
tags: [proxy, mcp, audit, hash-chain, tamper-evident, logging]
related: [[mcp_proxy.py]], [[mcp_inspector.py]], [[pipeline.py]]
status: documented
---

# mcp_audit.py

## Purpose
Provides a tamper-evident audit trail specifically for MCP tool calls and results. Each entry is linked into a SHA-256 hash chain, making any post-hoc modification detectable. Supports querying by agent, server, tool, and blocked/failed status.

## Responsibilities
- Log every MCP tool call and its result with full security metadata (PII redacted)
- Chain all entries using SHA-256 so that tampering with any entry breaks chain verification
- Track call start times for duration measurement of round-trips
- Provide query methods to filter the audit log by agent, server, tool, blocked, or failed state
- Generate summary reports of tool usage, error rates, and chain integrity

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `MCPAuditEntry` | Dataclass | Single audit record for a tool call or result, including chain hashes and security metadata |
| `MCPAuditTrail` | Class | Append-only hash chain for MCP tool call auditing; integrates start time tracking for duration |

## Function Details

### MCPAuditTrail.log_tool_call(agent_id, server_name, tool_name, parameters, findings_count, threat_level, blocked, block_reason, pii_redacted, call_id)
**Purpose:** Append an outgoing tool call to the audit chain. Computes content hash from `tool_call:server:tool:agent:timestamp` and chains it to the previous hash.
**Parameters:** Full call context including security findings and block disposition.
**Returns:** `MCPAuditEntry` with populated hash chain fields.

### MCPAuditTrail.log_tool_result(call_id, agent_id, server_name, tool_name, success, error_message, result_summary, findings_count, threat_level, pii_redacted)
**Purpose:** Append an incoming tool result to the audit chain. Calculates duration since `start_call()` was called for the matching call_id.
**Parameters:** Result disposition, truncated result summary (500 chars max), and security findings.
**Returns:** `MCPAuditEntry`.

### MCPAuditTrail.start_call(call_id)
**Purpose:** Record the wall-clock start time for a call so round-trip duration can be computed when the result arrives. Evicts stale entries (> 5 min old) when the pending map reaches `MAX_PENDING_CALLS` (1000).

### MCPAuditTrail.verify_chain()
**Purpose:** Walk the entire chain entry by entry, recomputing content and chain hashes and verifying all links.
**Returns:** `(bool, str)` — valid flag and diagnostic message.

### MCPAuditTrail.generate_report()
**Purpose:** Produce a summary dict with total entries, call/result counts, block rate, tool usage frequencies, average duration, chain validity, PII redaction count, unique agents, and unique servers.
**Returns:** Dict.

### Query Methods
| Method | Returns |
|--------|---------|
| `get_entries_for_agent(agent_id)` | All entries for a given agent |
| `get_entries_for_server(server_name)` | All entries for a given MCP server |
| `get_entries_for_tool(tool_name)` | All entries for a given tool name |
| `get_blocked_entries()` | All entries where `blocked=True` |
| `get_failed_entries()` | All tool_result entries where `success=False` |

## Hash Chain Structure
Each entry stores:
- `content_hash` = SHA-256(`{direction}:{server}:{tool}:{agent}:{timestamp}`)
- `previous_hash` = `chain_hash` of the preceding entry (genesis = "0" * 64)
- `chain_hash` = SHA-256(`{previous_hash}:{content_hash}:{direction}:{timestamp}`)

## Configuration / Environment Variables
- `MAX_PENDING_CALLS` = 1000 — maximum number of in-flight call start times before eviction

## Related
- [[mcp_proxy.py]]
- [[mcp_inspector.py]]
- [[pipeline.py]]
- [[mcp_config.py]]
