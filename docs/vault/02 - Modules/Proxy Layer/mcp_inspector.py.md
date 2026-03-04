---
title: mcp_inspector.py
type: module
file_path: gateway/proxy/mcp_inspector.py
tags: [proxy, mcp, inspection, prompt-injection, pii, security-scanning]
related: [[mcp_proxy.py]], [[mcp_permissions.py]], [[mcp_audit.py]]
status: documented
---

# mcp_inspector.py

## Purpose
Inspects MCP tool call parameters and tool results for security threats. Takes a log-and-allow approach for ambiguous cases — only HIGH-severity prompt injection causes a block in default mode; strict mode blocks all HIGH-severity findings including PII leaks.

## Responsibilities
- Scan tool call parameters recursively for prompt injection patterns, PII, suspicious encoding, and sensitive shell operations
- Scan tool results for PII and suspicious encoding (never block results, only redact)
- Redact HIGH-severity PII (SSN, credit card numbers) from both parameters and results
- Aggregate findings with threat level classification (NONE/LOW/MEDIUM/HIGH)
- Determine block/allow decision based on findings and strict mode setting
- Support recursive scanning of nested dicts and lists

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ThreatLevel` | Enum | NONE, LOW, MEDIUM, HIGH |
| `FindingType` | Enum | INJECTION, PII_LEAK, SUSPICIOUS_ENCODING, SENSITIVE_OP |
| `InspectionFinding` | Dataclass | Single finding: type, threat level, field path, description |
| `InspectionResult` | Dataclass | All findings plus sanitized params/result and block decision |
| `MCPInspector` | Class | Main inspection engine; `strict_mode` flag controls blocking sensitivity |

## Function Details

### MCPInspector.inspect_tool_call(tool_name, params, check_injection, check_pii, check_encoding, check_sensitive)
**Purpose:** Recursively scan all string values in `params` for security threats and produce sanitized parameters.
**Parameters:** `tool_name` (str), `params` (dict), and boolean flags for each check category.
**Returns:** `InspectionResult` with `blocked=True` if HIGH injection detected (or any HIGH in strict mode).

### MCPInspector.inspect_tool_result(tool_name, result_content, check_pii, check_encoding)
**Purpose:** Scan tool results for PII and encoding issues. Results are never blocked — only PII is redacted.
**Parameters:** `tool_name` (str), `result_content` (Any), and check flags.
**Returns:** `InspectionResult` with `blocked=False` always; `sanitized_result` has PII scrubbed.

### MCPInspector._scan_value(value, path, findings, ...)
**Purpose:** Recursive dispatcher — handles str, dict, list values; appends findings in-place.

### MCPInspector._scan_text(text, path, findings, ...)
**Purpose:** Apply all active pattern sets against a single string value. Appends findings to the shared list.

### MCPInspector._redact_pii(value)
**Purpose:** Recursively substitute SSNs with `REDACTED_SSN` and 16-digit credit card numbers with `REDACTED_CC`. Emails (LOW threat) are NOT redacted.
**Returns:** Copy of value with HIGH-severity PII replaced.

### MCPInspector._should_block(findings)
**Purpose:** Determine whether to block based on mode. Default mode: only HIGH injection blocks. Strict mode: any HIGH finding blocks.
**Returns:** `(bool, str)`.

## Detection Patterns

| Pattern Set | Threat Level | Examples |
|-------------|-------------|---------|
| `_INJECTION_HIGH` | HIGH | "ignore previous instructions", role override, fake system prompts, LLM control tokens |
| `_SENSITIVE_OP` | MEDIUM | `bash -c`, `rm -rf`, `curl http://`, `wget http://` |
| SSN | HIGH | `\d{3}-\d{2}-\d{4}` |
| Credit card | HIGH | 16-digit sequences |
| Email | LOW | Standard email regex |
| Large opaque blob | MEDIUM | String > 100 chars with no whitespace (possible base64) |
| Heavy URL encoding | MEDIUM | 10+ `%XX` sequences in a single value |

## Configuration / Environment Variables
- `strict_mode` (bool, default False) — when True, any HIGH finding (including PII) causes a block
- `_LARGE_BLOB_THRESHOLD` = 100 chars
- `_URL_ENCODING_COUNT_THRESHOLD` = 10 sequences

## Related
- [[mcp_proxy.py]]
- [[mcp_permissions.py]]
- [[mcp_audit.py]]
- [[pipeline.py]]
