# ADR-009: Enforce-by-Default Security Philosophy

## Status
**Accepted** — March 2026

**Supersedes:** [ADR-002: Default-Allow Security Philosophy](ADR-002-default-allow-security-philosophy.md)

## Context

ADR-002 (December 2025) adopted a Default-Allow with Comprehensive Logging philosophy during
AgentShroud's initial design phase. This was appropriate for an early prototype: it preserved
agent functionality, minimized false positives, and allowed behavioral baselines to be established
before enforcing restrictions.

The v0.8.0 hardening cycle (February–March 2026) fundamentally changed this posture in response
to two findings:

1. **Steve Hay STPA-Sec Assessment (February 2026):** Found 0% effective enforcement against
   vanilla OpenClaw in a production-equivalent deployment. All 17 Unsafe Control Actions (UCAs)
   across 4 loss categories were reachable without triggering any active block.

2. **All 6 Tier-1 deployment blockers were closed** in v0.8.0, wiring the SecurityPipeline
   into the Telegram message path and setting all 65+ security modules to `mode: enforce`.

With the pipeline fully wired and all modules enforce-mode, the system no longer operates
Default-Allow. ADR-002 is now factually incorrect and represents a governance gap.

## Decision

AgentShroud adopts an **Enforce-by-Default** security philosophy effective v0.8.0:

- All security modules default to `mode: enforce` in `agentshroud.yaml`
- High-confidence threats are **blocked immediately** (no learning-phase pass-through)
- Suspicious activities queue for human approval **before** any action is taken
- `mode: monitor` is an **explicit opt-in** requiring named justification per module
- Owner messages are logged but pass through (operator exemption); all other identities
  are subject to full enforcement

### Policy Table

| Event | v0.7 (Default-Allow) | v0.8+ (Enforce-by-Default) |
|-------|----------------------|---------------------------|
| Prompt injection detected | Log + allow | Block immediately |
| PII in outbound response | Log | Redact and deliver sanitized |
| Canary value in response | Log | Block entire response |
| Credential pattern in output | Log | Replace with [REDACTED] |
| Egress to unknown domain | Log | Deny + Telegram alert |
| Tool call above risk tier | Queue (after attempt) | Queue (before attempt) |
| Unknown agent message | Allow with low trust | Block until trust established |

### Configuration

```yaml
# agentshroud.yaml — enforce-by-default baseline
security:
  prompt_guard:
    mode: enforce
  pii_sanitizer:
    mode: enforce
  egress_filter:
    mode: enforce
  outbound_filter:
    mode: enforce
  encoding_detector:
    mode: enforce
  canary_tripwire:
    mode: enforce
  # ...all other modules default to enforce
prompt_guard:
  mode: enforce
```

## Consequences

### Positive Consequences
- **Eliminates passive-observer weakness:** Threats are stopped, not logged and forwarded.
- **Closes the STPA-Sec gap:** Active blocking converts UCAs into controlled loss scenarios.
- **Governance alignment:** `mode: monitor` relaxations are now auditable exceptions.
- **Honest ADR state:** Documentation matches the deployed system.

### Negative Consequences
- **Increased false-positive risk:** Enforce mode may block legitimate agent actions.
  Mitigation: owner exemption ensures operator is never locked out; approval queue provides
  human-in-the-loop override for edge cases.
- **Reduced autonomy during tuning:** New patterns / domains require allowlist additions
  before they work. This is intentional — operator approval required.

### Migration from ADR-002

Operators upgrading from v0.7 to v0.8+ should:

1. Review `agentshroud.yaml` and confirm all modules are `mode: enforce`
2. Expand `proxy.allowed_domains` with any legitimate external endpoints the agent uses
3. Review approval queue thresholds — some previously auto-allowed actions now queue
4. Test with owner account first (owner exemption active) before enabling collaborator access

## Related

- ADR-001: Transparent Proxy Model (unchanged — enforcement is gateway-side, not agent-side)
- ADR-004: API Keys Never in Agent Container (unchanged — credential isolation)
- ADR-005: SHA-256 Hash Chain Audit Integrity (enhanced in v0.9.0: BLOCK events now await SQLite)
- ADR-008: Progressive Trust Levels (unchanged — trust model compatible with enforce-default)
