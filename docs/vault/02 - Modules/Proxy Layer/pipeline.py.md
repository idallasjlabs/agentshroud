---
source: "gateway/proxy/pipeline.py"
module: pipeline
layer: proxy
created: 2026-06-09
updated: 2026-06-10
tags: [proxy, pipeline, security, audit-chain, pii, prompt-guard, egress, canary, clamav, context-integrity, envelope-signing]
type: module-doc
status: production
coverage: "≥94%"
related: [[mcp_proxy.py]], [[mcp_audit.py]], [[forwarder.py]]
---

# pipeline.py — Security Pipeline

## Overview

`gateway/proxy/pipeline.py` is the central message-routing and security enforcement
layer for AgentShroud. Every message — inbound from an AI agent or human, and outbound
from a downstream system or LLM — passes through `SecurityPipeline` before it reaches
its destination. The pipeline chains together up to 20 security guards in a deterministic
order, terminates early on any block decision, and records every event in a SHA-256
tamper-evident `AuditChain`.

The pipeline separates concerns cleanly:
- **Inbound path** (`process_inbound`) — validates, sanitizes, and authorizes messages
  arriving at the proxy from agents or users.
- **Outbound path** (`process_outbound`) — sanitizes and inspects responses leaving the
  proxy toward end users or downstream systems.

Both paths converge on a single `PipelineResult` dataclass and a single `AuditChain`
instance, producing a unified audit ledger for the session.

---

## Pipeline Stages

### Inbound (`process_inbound`)

Steps run in strict order. A BLOCK at any step returns immediately; subsequent steps
are skipped.

| Step | Guard | Class / Module | Block Condition | Owner Exemption |
|------|-------|----------------|-----------------|-----------------|
| 0 | **ContextGuard** | `gateway/security/context_guard.py` | `critical` or `high` severity cross-turn injection. Repetition attacks are logged only, never blocked. | Yes — owner messages are allowed through with an INFO log |
| 0.5 | **ContextIntegrityScorer** | `gateway/security/context_integrity.py` | C21 — scores session segment provenance 0.0–1.0. Score < 0.3 blocks (lockdown threshold); 0.3 ≤ score < 0.6 warns and forwards. Requires `context_guard` to supply segments. Fail-closed for non-owners on scorer error. Audit label: `inbound_integrity_blocked`. | Yes |
| 1 | **PromptGuard** | `gateway/security/prompt_guard.py` | `scan.blocked == True` OR `scan.score >= prompt_block_threshold` (default 0.8) | Yes |
| 1.1 | **HeuristicClassifier** | `gateway/security/heuristic_classifier.py` | Secondary signal only when PromptGuard score is in the uncertain zone (0.3–0.8). Blocks on `is_injection == True`. Never the sole blocking signal. | Yes |
| 1.5 | **InboundInjectionScanner** | `gateway/security/tool_result_injection.py` (reused) | CVE-2026-30741 — applies 12-rule ToolResultInjectionScanner pattern set (encoded injection + unicode obfuscation) to inbound messages. Blocks on `InjectionAction.STRIP`; warns on `InjectionAction.WARN`. | Yes |
| 1.6 | **C32InboundScan** | `gateway/security/xml_leak_filter.py` (reused) | CVE-2026-34425 — applies XMLLeakFilter C32 shell metacharacter patterns to inbound messages. Blocks when `filter_applied == True`. | Yes |
| 2 | **PIISanitizer** | `gateway/security/pii_sanitizer.py` | Redacts PII (Presidio, 0.9 confidence minimum). Does not block; mutates `sanitized_message`. This guard is **required** — pipeline raises `RuntimeError` at startup without it. | N/A — sanitization runs for all users |
| 2.5 | **ClamAV Scanner** | `clamav_scanner` callable | Decodes base64 chunks ≥ 256 bytes and scans with clamd. Blocks on malware signature match. **Fail-open**: clamd unavailability logs CRITICAL and allows through. | No — malware is blocked regardless of identity |
| 3 | **TrustManager** | `gateway/security/trust_manager.py` | `is_action_allowed(agent_id, action) == False` | No — trust is enforced by agent tier, not ownership |
| 4 | **ApprovalQueue** | `gateway/approval_queue/` | `action in approval_actions` — routes to human approval instead of forwarding. Default actions: `execute_command`, `delete_file`, `admin_action`, `install_package`. | No |
| 5 | **Audit + Forward** | `AuditChain.append()` | Terminal step — appends to chain and sets `action = FORWARD`. | N/A |

### Outbound (`process_outbound`)

| Step | Guard | Class / Module | Block Condition |
|------|-------|----------------|-----------------|
| 0 | **XML Block Stripper** | `pii_sanitizer.filter_xml_blocks()` | Never blocks — strips Claude internal XML tags from response text before any other guard runs. |
| 1 | **PIISanitizer** | `gateway/security/pii_sanitizer.py` | Redacts PII. Does not block; mutates `sanitized_message`. |
| 1.5 | **OutboundInfoFilter** | `gateway/security/outbound_info_filter.py` | Redacts information disclosure matches by category and trust level. If `pattern_name == "fabricated_security_notice"` → escalates to full BLOCK with clean fallback response (`"I'm sorry, I wasn't able to process that request."`). |
| 1.55 | **PromptProtection** | `gateway/security/prompt_protection.py` | System prompt / architecture disclosure prevention. Redacts matches; blocks if `risk_score > 100` for non-owners. Owner (`user_trust_level == "FULL"` or matching `owner_user_id`) is always exempt. |
| 1.6 | **EncodingDetector** | `gateway/security/encoding_detector.py` | Detects encoding bypass attempts (base64, unicode, etc.) in outbound content. Does not block — normalizes to `cleaned_text` for downstream guards to evaluate on decoded content. |
| 1.7 | **CanaryTripwire** | `gateway/security/canary_tripwire.py` | Final defense. Blocks entire response (no redaction) when tripwire is triggered (`is_blocked == True`). Uses `append_block()` for guaranteed SQLite persistence. |
| 1.75 | **EnhancedToolResultSanitizer** | `gateway/security/enhanced_tool_sanitizer.py` | Strips exfiltration and leak patterns from outbound content. Fail-closed for non-owners: if the module raises an exception, the response is blocked. |
| 1.76 | **PromptGuard (tool-result scan)** | `gateway/security/prompt_guard.py` | CVE-2026-31045 — scans outbound content as a tool result for indirect prompt injection embedded in web pages, file reads, and API responses. Blocks on `scan_tool_result(...).blocked == True`. |
| 1.8 | **OutputCanary** | `gateway/security/output_canary.py` | Checks for leaked canary tokens in outbound responses. Blocks on `risk_level in ("high", "critical")`. Fail-closed for non-owners on module crash. |
| 1.9 | **OutputSchemaEnforcer** | `gateway/security/output_schema_enforcer.py` | C25 — validates response schema; redacts violations via `schema_result.sanitized_output`. Does not block. |
| 2 | **EgressFilter** | `gateway/security/egress_filter.py` | Checks each `destination_url` against allow/deny rules. Blocks on `action == "deny"`. Supports both sync (`check`) and async (`check_async`) interfaces. |
| 2.5 | **EnvelopeSigner** | `gateway/security/instruction_envelope.py` | C46 — HMAC-SHA256 attestation of the final sanitized response. Tool results (`metadata["tool_name"]` present) are signed via `wrap_tool_result()`; all others via `sign(issuer="agent:<agent_id>")`. **Never blocks** — signing failure logs ERROR and delivery proceeds. `envelope_id` / `envelope_signature` / `envelope_timestamp` are written into the final audit entry metadata. |
| 3 | **Audit + Return** | `AuditChain.append()` | Terminal step — appends to chain and sets `action = FORWARD`. |

> **Signing key:** `EnvelopeSigner` sources its key from `AGENTSHROUD_ENVELOPE_SIGNING_KEY`;
> without it a random 32-byte key is generated and **rotates on every restart**, which
> invalidates verification of envelopes signed before the restart. Set the env var in
> production for stable attestation.

---

## Key Classes

### `PipelineAction` (Enum)

Three possible routing decisions produced by the pipeline:

| Value | Meaning |
|-------|---------|
| `FORWARD` | Message passes all guards; forward to destination |
| `BLOCK` | Message rejected; do not forward |
| `QUEUE_APPROVAL` | Message held for human review before forwarding |

---

### `PipelineResult` (Dataclass)

All fields populated by a single pipeline run. The `to_dict()` method serializes to
JSON for logging and API responses.

| Field | Type | Description |
|-------|------|-------------|
| `original_message` | `str` | Raw message before any pipeline processing |
| `sanitized_message` | `str` | Message after all sanitization steps |
| `action` | `PipelineAction` | Final routing decision |
| `blocked` | `bool` | True if message was blocked at any step |
| `block_reason` | `str` | Human-readable description of the block trigger |
| `prompt_score` | `float` | PromptGuard injection score (0.0–1.0) |
| `prompt_patterns` | `list[str]` | Matched injection pattern names |
| `pii_redactions` | `list[str]` | PII entity types redacted (e.g. `["EMAIL", "PHONE_NUMBER"]`) |
| `pii_redaction_count` | `int` | Count of individual PII redactions applied |
| `trust_allowed` | `bool` | Whether TrustManager permitted the requested action |
| `trust_level` | `Optional[int]` | Numeric trust tier for the agent (from TrustManager) |
| `audit_entry_id` | `str` | UUID of the AuditChain entry for this message |
| `audit_hash` | `str` | SHA-256 chain hash at the time of audit entry |
| `queued_for_approval` | `bool` | True if routed to the approval queue |
| `approval_id` | `str` | ID of the approval queue item (if queued) |
| `direction` | `str` | `"inbound"` or `"outbound"` |
| `timestamp` | `float` | Unix timestamp when pipeline processing began |
| `processing_time_ms` | `float` | Wall-clock time in milliseconds for the full pipeline run |
| `info_filter_redactions` | `list[str]` | Information disclosure categories redacted by OutboundInfoFilter |
| `info_filter_redaction_count` | `int` | Count of OutboundInfoFilter redactions |
| `info_disclosure_risk` | `str` | Risk level from OutboundInfoFilter (`"low"`, `"medium"`, `"high"`) |
| `canary_detections` | `list[str]` | Detection descriptions from CanaryTripwire |
| `canary_blocked` | `bool` | True if CanaryTripwire or OutputCanary triggered a block |
| `encoding_detections` | `list[str]` | Encoding methods detected by EncodingDetector (e.g. `["base64", "unicode_escape"]`) |
| `encoding_decoded_segments` | `int` | Number of encoded segments decoded and replaced |
| `integrity_score` | `float` | C21 context integrity score (0.0–1.0). `-1.0` means not scored (scorer or context_guard absent). |
| `integrity_factors` | `list[str]` | Score component breakdown from ContextIntegrityScorer (e.g. `["system_prompt_hmac_valid:+0.3"]`) |
| `envelope_id` | `str` | C46 — UUID of the signed instruction envelope (outbound only; empty if signer absent or signing failed) |
| `envelope_signature` | `str` | C46 — hex HMAC-SHA256 signature of the final sanitized response |

---

### `AuditChain`

SHA-256 tamper-evident hash chain for audit logging. One instance is shared across
both inbound and outbound paths within a single `SecurityPipeline`.

**Chain hash formula:**
```
chain_hash = SHA-256("{previous_hash}:{content_hash}:{direction}:{timestamp}")
```

| Member | Description |
|--------|-------------|
| `GENESIS_HASH` | `"0" * 64` — the initial previous-hash for the first entry |
| `append(content, direction, metadata, _skip_task)` | Adds a chain entry. Persists to SQLite via `loop.create_task()` (fire-and-forget). Used for non-critical events (FORWARD, QUEUE_APPROVAL). |
| `append_block(content, direction, metadata)` | **Async. Guaranteed SQLite persistence.** Awaits the audit store write directly. Used exclusively for BLOCK events. |
| `verify_chain()` | Walks all entries, recomputes each `chain_hash`, returns `(bool, error_message)`. |
| `entries` | Read-only copy of the in-memory `list[AuditChainEntry]`. |
| `last_hash` | The most recent `chain_hash` — used as `previous_hash` for the next entry. |
| `__len__` | Number of entries in the chain. |

**`AuditChainEntry` fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | `str` | UUID for this entry |
| `timestamp` | `float` | Unix timestamp at append time |
| `direction` | `str` | Event label (e.g. `"inbound_blocked"`, `"outbound_canary_blocked"`, `"outbound"`) |
| `content_hash` | `str` | SHA-256 of the raw content string |
| `previous_hash` | `str` | Chain hash of the preceding entry (or `GENESIS_HASH`) |
| `chain_hash` | `str` | SHA-256 of the combined chain input string |
| `metadata` | `dict` | Arbitrary key-value context (agent_id, malware signatures, canary methods, etc.) |

---

### `SecurityPipeline`

Central orchestrator. One instance per gateway process, constructed at startup with
all guards injected.

**Constructor parameters (all keyword):**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pii_sanitizer` | guard | **Required** | Presidio-backed PII sanitizer. `RuntimeError` raised if absent. |
| `prompt_guard` | guard | Recommended | PromptGuard injection scanner; also used at outbound Step 1.76 |
| `trust_manager` | guard | Recommended | TrustManager for agent action authorization |
| `egress_filter` | guard | Recommended | Egress URL allow/deny filter |
| `outbound_filter` | guard | Recommended | OutboundInfoFilter for information disclosure |
| `canary_tripwire` | guard | Recommended | CanaryTripwire final defense |
| `encoding_detector` | guard | Recommended | EncodingDetector for bypass attempt normalization |
| `context_guard` | guard | Recommended | ContextGuard for cross-turn injection analysis |
| `clamav_scanner` | `async callable` | Recommended | `async (bytes) -> dict` wrapping clamd |
| `approval_queue` | object | Optional | Approval queue client |
| `heuristic_classifier` | guard | Optional | Secondary injection classifier (uncertain-zone signal) |
| `output_canary` | guard | Optional | OutputCanary for leaked token detection |
| `enhanced_tool_sanitizer` | guard | Optional | EnhancedToolResultSanitizer for exfil pattern stripping |
| `prompt_protection` | guard | Optional | PromptProtection for system prompt / architecture disclosure |
| `tool_result_injection_scanner` | guard | Optional | CVE-2026-30741 inbound injection scanner |
| `xml_leak_filter` | guard | Optional | CVE-2026-34425 inbound command injection scanner |
| `output_schema_enforcer` | guard | Optional | C25 schema enforcement |
| `context_integrity_scorer` | guard | Recommended | C21 — inbound Step 0.5 session integrity scoring (requires `context_guard`) |
| `envelope_signer` | guard | Recommended | C46 — outbound Step 2.5 response attestation |
| `prompt_block_threshold` | `float` | Optional | PromptGuard block score threshold (default: `0.8`) |
| `approval_actions` | `list[str]` | Optional | Actions that route to the approval queue (default: `execute_command`, `delete_file`, `admin_action`, `install_package`) |
| `audit_store` | object | Optional | SQLite AuditStore for persistent audit logging |

**Key public methods:**

| Method | Signature | Description |
|--------|-----------|-------------|
| `process_inbound` | `async (message, agent_id, action, source, metadata, skip_context_guard) -> PipelineResult` | Run the full inbound pipeline |
| `process_outbound` | `async (response, agent_id, destination_urls, metadata, user_trust_level, source) -> PipelineResult` | Run the full outbound pipeline |
| `get_stats` | `() -> dict` | Current pipeline counters plus live audit chain length and validity |
| `verify_audit_chain` | `() -> tuple[bool, str]` | Delegate to `AuditChain.verify_chain()` |
| `set_global_mode` | `(mode: str) -> None` | Switch all supporting guards between `"monitor"` and `"enforce"` modes |

---

## CVE Mitigations

| CVE | Pipeline Step | Guard | Mechanism |
|-----|---------------|-------|-----------|
| CVE-2026-30741 | Inbound Step 1.5 | `tool_result_injection_scanner` | Applies the ToolResultInjectionScanner 12-rule pattern set (encoded injection + unicode obfuscation) to all inbound messages, closing the asymmetry where only tool results were previously scanned |
| CVE-2026-34425 | Inbound Step 1.6 | `xml_leak_filter` (C32 patterns) | Applies XMLLeakFilter shell metacharacter patterns inbound so piped/subshell constructs are caught on the way in, not only on outbound |
| CVE-2026-31045 | Outbound Step 1.76 | `prompt_guard.scan_tool_result()` | Scans outbound content as a tool result for indirect prompt injection embedded in web pages, file reads, and API responses |

---

## Configuration

### Guard Presence and Startup Behavior

| Guard | Required | Absent Behavior |
|-------|----------|-----------------|
| `pii_sanitizer` | Yes | `RuntimeError` at startup — pipeline will not start (fail-closed) |
| `context_guard` | Recommended | `CRITICAL` log at startup; cross-turn injection scanning skipped |
| `prompt_guard` | Recommended | `CRITICAL` log; injection scanning and tool-result scan skipped |
| `egress_filter` | Recommended | `CRITICAL` log; egress URL check skipped |
| `outbound_filter` | Recommended | `CRITICAL` log; information disclosure filtering skipped |
| `canary_tripwire` | Recommended | `CRITICAL` log; canary final defense skipped |
| `encoding_detector` | Recommended | `CRITICAL` log; encoding bypass normalization skipped |
| `clamav_scanner` | Recommended | `CRITICAL` log; malware scanning of base64 payloads skipped |
| `context_integrity_scorer` | Recommended | `CRITICAL` log; session integrity scoring skipped |
| `envelope_signer` | Recommended | `CRITICAL` log; outbound response attestation skipped |

### Key Thresholds

| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt_block_threshold` | `0.8` | PromptGuard score at or above which inbound messages are blocked |
| HeuristicClassifier activation zone | score in `[0.3, 0.8]` | Score range where HeuristicClassifier is consulted as a secondary signal |
| PromptProtection block threshold | `100` (risk score) | OutboundInfoFilter risk score above which PromptProtection blocks the outbound response |
| ClamAV minimum chunk size | 256 bytes (decoded) | Base64 payloads that decode to fewer than 256 bytes are not submitted to clamd |
| Presidio confidence minimum | `0.9` | Set in PIISanitizer — do not lower per AgentShroud hard constraint |

### Owner Exemption

The pipeline reads `RBACConfig().owner_user_id` at startup (stored as `_owner_user_id`).
At runtime, `metadata["user_id"]` is compared to this value string-to-string. When a match
is found:

- **Inbound:** ContextGuard, PromptGuard, HeuristicClassifier, InboundInjectionScanner,
  and C32InboundScan allow the message through with an INFO log (reason and guard name
  always recorded).
- **Outbound:** PromptProtection skips scanning when `user_trust_level == "FULL"` or
  `metadata["user_id"]` matches the owner. EnhancedToolResultSanitizer and OutputCanary
  skip the fail-closed crash path for owner requests.
- **Not exempted:** ClamAV (malware blocked regardless of identity) and TrustManager
  (trust is enforced by agent tier, not ownership).

### Monitor vs. Enforce Mode

`set_global_mode(mode)` switches the pipeline globally. The switch is lossless — original
thresholds are saved on the first switch to `"monitor"` and restored exactly on return to
`"enforce"`.

| Mode | Effect on PromptGuard | Effect on Other Guards |
|------|-----------------------|------------------------|
| `"monitor"` | `block_threshold` and `warn_threshold` raised to `999.0` (effectively disabled) | `set_mode("monitor")` called on `pii_sanitizer`, `prompt_guard`, `egress_filter` if they support the method |
| `"enforce"` | Thresholds restored from `_pg_orig_block_threshold` / `_pg_orig_warn_threshold` (fallback: `0.8` / `0.4`) | `set_mode("enforce")` called on supporting guards |

---

## Important Behaviors

### Fail-Open ClamAV

ClamAV scanning is intentionally fail-open. If clamd is unavailable or returns an
`"error"` key in the response dict, the pipeline logs at `CRITICAL` level and allows
the message through rather than blocking it. The rationale — documented in the source
at `gateway/proxy/pipeline.py:578` — is that availability takes precedence over ClamAV
detection for inline message scanning. ClamAV is a defense-in-depth layer, not the
primary gate. Malformed base64 chunks and individual scan errors are also silently
skipped (`except Exception: pass`) to avoid disrupting the pipeline on bad input.

### Owner Exemption — Logging Guarantee

Owner messages that would otherwise be blocked are always logged at INFO level with
the phrase `"— allowing"` and the original block reason included. The exemption is
never silent — the log record is always created so the bypass is auditable even though
no `AuditChain` block entry is written.

### `AuditChain.append_block()` — Guaranteed Persistence Guarantee

Block events use `append_block()` (async, awaited directly) rather than the
fire-and-forget `append()`. This ensures security-critical block events are never
silently lost under load. The implementation:

1. Calls `append(..., _skip_task=True)` first — creates the in-memory chain entry and
   advances `_last_hash` so the hash chain stays consistent even if the DB write fails.
2. Then awaits `audit_store.log_event(...)` directly with `severity="CRITICAL"`.
3. On `audit_store` failure, logs `ERROR` and returns the in-memory entry — the chain
   is intact even if persistence failed.

Non-block events (FORWARD, QUEUE_APPROVAL) use `append()` with `loop.create_task()` —
best-effort persistence that does not add latency to the response path.

### Early Return on Block

Any guard that sets `result.blocked = True` immediately computes `processing_time_ms`
and returns the `PipelineResult`. No subsequent guard in the same pipeline direction
is invoked. The `direction` label on the `AuditChainEntry` encodes which guard triggered
the block (e.g. `"inbound_context_blocked"`, `"inbound_clamav_blocked"`,
`"outbound_canary_blocked"`), making post-incident forensics unambiguous without
additional metadata queries.

### Stats Counter

`SecurityPipeline._stats` accumulates counters for the lifetime of the process:

| Counter | Incremented By |
|---------|----------------|
| `inbound_total` | Every `process_inbound` call |
| `inbound_blocked` | Any inbound BLOCK decision |
| `inbound_sanitized` | Inbound PII redaction occurred |
| `inbound_queued` | Inbound QUEUE_APPROVAL decision |
| `outbound_total` | Every `process_outbound` call |
| `outbound_sanitized` | Outbound PII redaction occurred |
| `outbound_blocked` | Any outbound BLOCK decision |
| `outbound_info_filtered` | OutboundInfoFilter matched patterns |
| `canary_blocked` | CanaryTripwire or OutputCanary triggered a block |
| `encoding_detected` | EncodingDetector found encoded segments |
| `pii_redactions_total` | Cumulative PII redaction count (inbound + outbound) |
| `info_redactions_total` | Cumulative OutboundInfoFilter redaction count |

`get_stats()` appends `audit_chain_length` and `audit_chain_valid` (live chain
integrity re-verification) to these counters before returning.

---

## Related

- [[Architecture Overview]]
- [[Data Flow]]
- [[mcp_proxy.py]]
- [[mcp_audit.py]]
- [[forwarder.py]]
