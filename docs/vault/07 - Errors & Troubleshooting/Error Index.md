---
title: Error Index
type: reference
tags: [errors, troubleshooting, operations]
related: [Errors & Troubleshooting/Troubleshooting Matrix, Runbooks/Crash Recovery, Quick Reference]
status: documented
---

# Error Index

## HTTP Status Codes

| Code | Meaning | Common Cause |
|------|---------|-------------|
| 400 | Bad Request | Prompt injection detected, malformed request body |
| 401 | Unauthorized | Missing or invalid `Authorization: Bearer` token |
| 403 | Forbidden | Egress domain blocked, disallowed op:// path, rate limit |
| 404 | Not Found | Unknown endpoint |
| 408 | Request Timeout | Upstream service timeout |
| 422 | Unprocessable Entity | Pydantic validation failure on request body |
| 429 | Too Many Requests | Rate limit exceeded (per-client or per-tool) |
| 500 | Internal Server Error | Unhandled exception in gateway |
| 502 | Bad Gateway | Gateway cannot reach upstream service |
| 503 | Service Unavailable | Gateway starting up or in freeze mode |

---

## Startup Errors

See [[Errors & Troubleshooting/Startup Errors]] for detailed diagnosis.

| Error | Quick Cause |
|-------|-------------|
| `FileNotFoundError: No agentshroud.yaml found` | Config not mounted or missing |
| `spaCy model download failed` | No internet at build time → uses regex fallback |
| `ValueError: auth_token missing` | No token in config or secret file |
| Container health check failing | Gateway not responding on :8080 |
| Bot never healthy | Gateway was never healthy (bot waits for `service_healthy`) |

---

## Auth Errors

See [[Errors & Troubleshooting/Auth Errors]].

| Error | HTTP | Cause |
|-------|------|-------|
| `Invalid authentication credentials` | 401 | Token mismatch |
| `Authorization header missing` | 401 | No `Authorization: Bearer` header |
| `Token format invalid` | 401 | Not a Bearer token |

---

## PII Pipeline Errors

See [[Errors & Troubleshooting/PII Pipeline Errors]].

| Error | Cause |
|-------|-------|
| `PII redaction failed` | Presidio/spaCy engine error |
| `PII engine not initialized` | Gateway started before spaCy model loaded |
| Excessive false positives | `pii_min_confidence` too low (try 0.95) |
| Content blocked with false PII | Confidence threshold catching non-PII text |

---

## Egress Filter Errors

See [[Errors & Troubleshooting/Egress Filter Errors]].

| Error | HTTP | Cause |
|-------|------|-------|
| `Egress blocked: domain not in allowlist` | 403 | Domain not in `proxy.allowed_domains` |
| `RFC1918 address blocked` | 403 | Attempt to access private network |
| `Egress filter not initialized` | 500 | Filter failed to load allowlist |

---

## MCP Proxy Errors

See [[Errors & Troubleshooting/MCP Proxy Errors]].

| Error | HTTP | Cause |
|-------|------|-------|
| `MCP tool permission denied` | 403 | Tool requires `write` permission but only `read` granted |
| `MCP rate limit exceeded` | 429 | Tool called more than `rate_limit` times/minute |
| `MCP server unreachable` | 502 | MCP server at configured URL not responding |
| `Unknown MCP server` | 400 | Server name not in `mcp_proxy.servers` config |

---

## Prompt Injection Blocks

See [[Errors & Troubleshooting/Prompt Injection Blocks]].

| Error | HTTP | Cause |
|-------|------|-------|
| `Prompt injection detected` | 400 | Threat score exceeded threshold |
| `Suspicious tool result blocked` | 400 | Tool result contains injection signatures |

---

## Container Errors

See [[Errors & Troubleshooting/Container Errors]].

| Error | Cause |
|-------|-------|
| `exit code 137` | OOM kill — increase `mem_limit` |
| `exit code 139` | Segfault (rare — usually Node.js memory issue) |
| `Port already in use` | Another process using 8080/18790 |
| `read-only file system` | Attempted write to non-volume path |

---

## Related Notes

- [[Errors & Troubleshooting/Troubleshooting Matrix]] — Symptom → cause → fix
- [[Errors & Troubleshooting/Startup Errors]] — Startup-specific diagnosis
- [[Runbooks/Crash Recovery]] — Post-crash recovery steps
- [[Quick Reference]] — Common fixes cheat sheet
