---
title: sidecar.py
type: module
file_path: gateway/proxy/sidecar.py
tags: [proxy, sidecar, optional-scanning, best-effort, security-mode]
related: [[pipeline.py]], [[web_proxy.py]], [[http_proxy.py]]
status: documented
---

# sidecar.py

## Purpose
Implements an optional "sidecar" security mode where the agent runs normally but can voluntarily submit messages to the gateway's `POST /api/scan` endpoint for security screening. Unlike proxy mode, traffic is NOT forced through the scanner — this is best-effort only and does not guarantee all messages are scanned.

## Responsibilities
- Expose a `SidecarScanner.scan()` method that feeds a message through the `SecurityPipeline`
- Return the sanitized message along with the full security report to the caller
- Emit a persistent warning in every response that sidecar mode provides degraded protection
- Track basic statistics: total scans and blocked scan count
- Gracefully handle a missing pipeline (return original content with an error report)

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `ScanRequest` | Dataclass | Inbound scan request: content, agent_id, action, source |
| `ScanResponse` | Dataclass | Scan result: sanitized content, original content, security report dict, mode label, warning string |
| `SidecarScanner` | Class | Wraps `SecurityPipeline.process_inbound()` and provides stats; always emits `SIDECAR_WARNING` |
| `SIDECAR_WARNING` | Constant | Human-readable warning string included in every `ScanResponse` |

## Function Details

### SidecarScanner.scan(request)
**Purpose:** Pass a message through the inbound pipeline and return the sanitized result plus a full security report. If the pipeline is not configured, returns the original content with an error report.
**Parameters:** `request` (ScanRequest).
**Returns:** `ScanResponse` with `sanitized_content`, `security_report` (dict from `PipelineResult.to_dict()`), and `warning`.

### SidecarScanner.get_stats()
**Purpose:** Return operational statistics.
**Returns:** Dict with `mode="sidecar"`, warning text, `scans_total`, `scans_blocked`, `uptime_seconds`.

## Security Limitation Warning
```
SIDECAR MODE: Traffic can bypass this scanner.
For guaranteed security, use proxy mode (docker-compose.secure.yml).
```
This warning is embedded in every `ScanResponse` and `get_stats()` response. There is no way to suppress it.

## Configuration / Environment Variables
- `pipeline` — `SecurityPipeline` instance injected at construction; optional (scanner operates in degraded mode if absent)
- No environment variables; configuration is entirely through the constructor

## Related
- [[pipeline.py]]
- [[web_proxy.py]]
- [[http_proxy.py]]
