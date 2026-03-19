---
title: canary.py
type: module
file_path: gateway/security/canary.py
tags: [security, canary, verification, pipeline-health, audit-chain, pii]
related: ["[[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]", "[[Security Modules/encrypted_store.py|encrypted_store.py]]", "[[Data Flow]]"]
status: documented
---

# canary.py

## Purpose
Periodically verifies that the full security pipeline is functioning correctly by sending synthetic PII through the pipeline and asserting that it was scrubbed, audited, and that the proxy is healthy.

## Threat Model
Silent pipeline failure — the security stack appears to be running but is not actually scrubbing PII, maintaining the audit chain, or proxying traffic. Without active verification, a broken pipeline would be indistinguishable from a working one until a real incident occurred.

## Responsibilities
- Send a known synthetic PII payload (`000-00-0000`, `canary@test.agentshroud.local`, `555-000-0000`) through `SecurityPipeline.process_inbound()`
- Assert that the SSN canary value is absent from the sanitized output (PII stripping check)
- Assert that at least one entry exists in the audit chain (audit liveness check)
- Verify audit chain integrity via `pipeline.verify_audit_chain()`
- Perform a health check against the HTTP forwarder / proxy target
- Return a `CanaryResult` with per-check pass/fail status, overall verified status, timestamp, and duration in milliseconds

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `CANARY_SSN` | Constant | `"000-00-0000"` — synthetic SSN |
| `CANARY_EMAIL` | Constant | `"canary@test.agentshroud.local"` — synthetic email |
| `CANARY_PHONE` | Constant | `"555-000-0000"` — synthetic phone |
| `CANARY_MESSAGE` | Constant | Combined canary string sent through the pipeline |
| `CanaryCheck` | Dataclass | Individual check: name, passed, details |
| `CanaryResult` | Dataclass | Aggregated result: verified, checks dict, check_details list, timestamp, duration_ms |
| `run_canary()` | Async function | Entry point; runs all 4 checks and returns CanaryResult |

## Function Details

### run_canary(pipeline, forwarder)
**Purpose:** Execute the 4-check canary verification suite asynchronously.
**Parameters:**
- `pipeline` — `SecurityPipeline` instance (optional; checks are marked failed if None)
- `forwarder` — `HTTPForwarder` instance (optional; proxy check is skipped/passed if None)
**Returns:** `CanaryResult`
**Side effects:** Calls `pipeline.process_inbound()` which writes to the audit chain. Calls `forwarder.health_check()` which makes an outbound HTTP request.

### CanaryResult.to_dict()
**Purpose:** Serialize result to a plain dict for JSON logging or API response.
**Returns:** dict with keys: verified, checks, check_details, timestamp, duration_ms.

## Canary Checks

| Check Name | What It Verifies | Failure Condition |
|------------|-----------------|-------------------|
| `pii` | SSN scrubbed from sanitized output | `CANARY_SSN` present in `result.sanitized_message` |
| `audit` | Audit chain has at least one entry | `len(pipeline.audit_chain) == 0` |
| `chain` | Audit chain hash integrity | `pipeline.verify_audit_chain()` returns False |
| `proxy` | HTTP forwarder target is healthy | `forwarder.health_check()` returns False or raises |

`verified` in `CanaryResult` is True only if all checks pass.

## Mode: Enforce vs Monitor
Not applicable. The canary is a verification harness, not a policy enforcer. It always runs in full-check mode. If no forwarder is configured (e.g., in test environments), the proxy check is automatically marked as passed.

## Environment Variables
None. Dependencies (`pipeline`, `forwarder`) are passed as arguments.

## Operational Notes
- The canary agent_id is hardcoded as `"canary"`. Ensure this agent is registered (or excluded from trust checks) in the `TrustManager` if trust gating applies to the pipeline's `process_inbound()` path.
- `run_canary()` is `async`. It should be scheduled via the event loop (e.g., called from a background task or a cron-equivalent in the gateway's startup/health routines).
- Duration is measured in milliseconds using `time.time()` before/after the check suite.
- All canary PII values use clearly fake, reserved values (SSN 000-series, 555 phone prefix) to avoid any risk of false-positive matches against real data.

## Related
- [[Data Flow]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
- [[Security Modules/encrypted_store.py|encrypted_store.py]]
