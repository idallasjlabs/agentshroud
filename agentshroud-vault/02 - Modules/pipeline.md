---
title: pipeline.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/proxy/pipeline.py
tags: [#type/module, #status/critical]
related: ["[[lifespan]]", "[[telegram_proxy]]", "[[llm_proxy]]", "[[egress_filter]]", "[[prompt_guard]]", "[[sanitizer]]"]
status: active
last_reviewed: 2026-03-09
---

# pipeline.py — Central Security Processing Chain

## Purpose

The `SecurityPipeline` is the central security processor. Every message (inbound from users and outbound from the LLM) passes through a chain of security guards. Results are tracked in a SHA-256 hash chain (`AuditChain`) for tamper-evident logging.

## Architecture

```
Inbound pipeline:
  HeuristicClassifier (0.3-0.8 uncertain zone) → step 1.1
  PromptGuard (injection detection) → step 1
  PIISanitizer → step 2
  TrustManager → step 3
  ContextGuard → step 4
  CanaryTripwire → step 5
  EncodingDetector → step 6
  ApprovalQueue → step 7
  AuditChain.append() → step 8

Outbound pipeline:
  PIISanitizer → step 1
  PromptProtection → step 1.55
  OutboundInfoFilter → step 2
  CanaryTripwire → step 3
  EncodingDetector → step 4
  EgressFilter → step 5
  EnhancedToolSanitizer → step 6
  AuditChain.append() → step 7
```

## Key Classes

### `PipelineResult`
Dataclass capturing full context of a message scan:
- `action` — `FORWARD`, `BLOCK`, or `QUEUE_APPROVAL`
- `blocked` / `block_reason`
- `prompt_score` + `prompt_patterns` — injection detection output
- `pii_redactions` + `pii_redaction_count`
- `trust_allowed` / `trust_level`
- `audit_entry_id` + `audit_hash`
- `canary_detections` / `encoding_detections`
- `info_filter_redactions`

### `AuditChain`
SHA-256 hash chain for tamper-evident logging:
- `GENESIS_HASH = "0" * 64`
- Each entry: `chain_hash = SHA-256(previous_hash + content_hash + direction + timestamp)`
- `verify_audit_chain()` — walks the full chain checking each link; returns `(valid, message)`
- Verified every 60 seconds by background heartbeat task
- BLOCK paths guaranteed to persist to SQLite AuditStore

### `SecurityPipeline`
Main class. Constructor accepts optional components; missing components are safely skipped.

```python
SecurityPipeline(
    prompt_guard=...,
    pii_sanitizer=...,
    trust_manager=...,
    egress_filter=...,
    approval_queue=...,
    outbound_filter=...,
    context_guard=...,
    canary_tripwire=...,
    encoding_detector=...,
    output_canary=...,
    enhanced_tool_sanitizer=...,
    audit_store=...,
    prompt_protection=...,
    heuristic_classifier=...,
)
```

## Methods

### `process_inbound(message, agent_id, user_id) → PipelineResult`

Runs the full inbound pipeline. Called for messages coming from users before forwarding to the bot.

| Step | Component | Block Threshold |
|------|-----------|----------------|
| 1.1 | HeuristicClassifier | score 0.3–0.8 = uncertain zone → warn |
| 1 | PromptGuard | score ≥ 0.8 → BLOCK |
| 2 | PIISanitizer | redacts PII from message |
| 3 | TrustManager | agent not authorized → BLOCK |
| 4 | ContextGuard | context boundary violation → BLOCK |
| 5 | CanaryTripwire | canary detected → BLOCK |
| 6 | EncodingDetector | obfuscation detected → warn |
| 7 | ApprovalQueue | dangerous action → QUEUE_APPROVAL |
| 8 | AuditChain | always appended |

### `process_outbound(message, agent_id, user_id) → PipelineResult`

Runs the full outbound pipeline. Called for LLM responses before sending to users.

| Step | Component | Block Threshold |
|------|-----------|----------------|
| 1 | PIISanitizer | redacts PII from response |
| 1.55 | PromptProtection | architecture disclosure → BLOCK |
| 2 | OutboundInfoFilter | info disclosure risk → REDACT |
| 3 | CanaryTripwire | canary in output → BLOCK |
| 4 | EncodingDetector | encoded exfiltration → BLOCK |
| 5 | EgressFilter | unauthorized domain → BLOCK |
| 6 | EnhancedToolSanitizer | tool result PII → REDACT |
| 7 | AuditChain | always appended; BLOCK = SQLite write |

### `verify_audit_chain() → (bool, str)`

Walks the full in-memory chain and verifies every hash link. Returns `(True, "Chain valid")` or `(False, "Tamper detected at entry N")`.

## AuditStore SQLite Persistence

BLOCK events are guaranteed to be written to SQLite via `AuditStore`:
```python
if result.blocked and self._audit_store:
    await self._audit_store.append(entry)
```

This ensures that even if the in-memory chain is cleared, all BLOCK decisions are durably recorded.

## Related Files

- [[lifespan]] — assembles and wires SecurityPipeline
- [[llm_proxy]] — calls `process_outbound()` on streaming LLM responses
- [[telegram_proxy]] — calls `process_inbound()` on Telegram messages
- [[egress_filter]] — one component in the outbound pipeline
- [[prompt_guard]] — one component in the inbound pipeline
