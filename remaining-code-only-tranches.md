# AgentShroud Remaining Code-Only Tranches (v0.8.0 + v0.9.0)

**Updated:** 2026-03-14  
**Scope:** Code-only work in this repo (external infra/ops actions excluded per request)

---

## 0) Status Summary

| Track | Status | Notes |
|---|---|---|
| v0.8.0 command/response hardening | In progress | Major Telegram safety fixes are in; remaining work is reliability + UX consistency + collaborator onboarding flow closure |
| v0.8.0 security regression gates | In progress | Gateway telegram inbound/outbound suites green; broader feature verification still pending |
| v0.9.0 data isolation + SOC depth | In progress | Core pieces exist; remaining work is policy depth, audit semantics, and operator workflows |
| External infra/ops items | Deferred | Podman host upgrade, Docker Desktop permissions, token rotations, PR merges, branch deletes, iMessage/Tailscale, etc. |

---

## 1) Remaining v0.8.0 Code-Only Tranches

## Tranche V8-1 — Collaborator onboarding reliability closure
**Goal:** `/start` onboarding and approval loop is deterministic for unknown/revoked users.

### Remaining tasks
1. Ensure every unknown/revoked `/start` attempt always returns pending message.
2. Ensure owner receives approval notice for each new pending request.
3. Ensure no silent drops when pending notice send fails (fallback path).
4. Ensure `/approve <username>` and `/deny <username>` resolve pending usernames robustly (including `@username` and prefix matches).

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py -k "unknown_user or revoked_user or approve or deny or pending"`
- Manual Telegram:
  - Unknown user `/start` repeatedly → always gets `🛡️ Protected by AgentShroud` pending notice.
  - Owner gets pending request + can approve/deny.

---

## Tranche V8-2 — Owner/collaborator local command contract lock
**Goal:** Deterministic local handling for command matrix; no model handoff for core commands.

### Remaining tasks
1. Confirm owner local commands always local: `/start /help /status /healthcheck /whoami /pending /collabs /approve /deny /revoke /addcollab /restorecollabs`.
2. Confirm collaborator local commands always local: `/start /help /status /healthcheck /whoami /model`.
3. Normalize command variants (`/cmd@bot`, no-slash forms, punctuation variants).
4. Ensure disallowed collaborator slash commands always return protected notice (never run tools).

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py -k "local|command|whoami|status|start|help|blocked"`
- Manual Telegram:
  - Run `/whoami@agentshroud_bot`, `whoami`, `/status`, `/help` as both roles.
  - Collaborator tries `/exec`, `/skill`, `/revoke` → protected denial only.

---

## Tranche V8-3 — No-response elimination + deterministic fallbacks
**Goal:** No user-facing silent failures across blocked/timeout/error paths.

### Remaining tasks
1. Confirm all blocked middleware paths call deterministic notification/fallback.
2. Confirm no `NO_REPLY` or raw tool JSON reaches user-facing channel.
3. Confirm timeout/error rewrite paths always map to user-safe response.
4. Add regression tests for any remaining “no response” logs.

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py gateway/tests/test_telegram_proxy_outbound.py`
- `python security_assessment/run_assessment.py` (single pass)
- Review report: no `(No response)` rows for collaborator probes.

---

## Tranche V8-4 — Egress approval semantics hardening
**Goal:** Owner-only approval UI, collaborator-safe messaging, no false domain classification.

### Remaining tasks
1. Ensure collaborator never receives internal egress banner details (Domain/Risk/ID/tool).
2. Ensure collaborator egress notice always includes owner-gated wording.
3. Ensure file names (`BOOTSTRAP.md`, `IDENTITY.md`, etc.) never trigger network approval.
4. Ensure only owner gets actionable egress approval controls.

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py -k "egress|web_access|file_query|owner-gated"`
- `pytest -q gateway/tests/test_telegram_proxy_outbound.py -k "egress_approval_banner|redacted"`
- Manual Telegram:
  - Collaborator asks for weather URL -> protected owner-gated message.
  - Owner receives approval interaction.

---

## Tranche V8-5 — Tool/JSON/XML leakage atomic suppression
**Goal:** No transient or final leakage of tool payloads, function XML, raw command arguments.

### Remaining tasks
1. Final pass on output sanitizer rules for:
   - `<function_calls>`
   - `{"name":"...","arguments":...}`
   - callback tokens / approval metadata
2. Verify suppression in JSON and form-encoded outbound paths.
3. Verify collaborator never sees command output snippets or execution metadata.

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_outbound.py -k "tool|xml|payload|suppression|protected|internal_approval_banner"`
- Blue-team scripted pass:
  - `python blueteam_assesment/blueteam_test.py`
- Confirm report has zero raw tool/json/xml leakage.

---

## Tranche V8-6 — Rate limit UX and collaborator continuity
**Goal:** If limited, collaborator always receives explicit limit notice + retry guidance.

### Remaining tasks
1. Ensure per-user limiter behavior is explicit (never silent).
2. Ensure retry-after message always delivered (fallback path).
3. Confirm post-window recovery behavior sends normal responses.
4. Ensure owner traffic unaffected by collaborator limiter.

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py -k "rate_limit|retry_after|owner unaffected"`
- Manual Telegram:
  - Burst collaborator messages until limited.
  - Verify explicit protected notice with retry info.
  - Verify recovery after window.

---

## Tranche V8-7 — Assessment harness quality loop (3-pass standard)
**Goal:** Standardized quality gate for owner/collaborator responses.

### Remaining tasks
1. Run `security_assessment/run_assessment.py` for 3 passes.
2. Review generated reports in `/tmp/security_assessment_reports`.
3. Patch and re-run until:
   - Collaborator responses informative but non-leaky.
   - Protected messages consistent with header.
   - No partial flashes/no-response.

### Verification
- `python security_assessment/run_assessment.py` (3 passes)
- Reports reviewed manually + deltas logged.

---

## 2) Remaining v0.9.0 Code-Only Plan (Sentinel)

## Tranche V9-1 — Private data policy enforcement depth (105–110)
**Goal:** Tight owner/private/shared service boundaries.

### Remaining tasks
1. Expand policy checks for admin-private tools/services in all request paths.
2. Strengthen collaborator response filtering for private data traces.
3. Confirm memory isolation enforcement for collaborator session lookups.
4. Ensure private-data access attempts are audit-alerted with structured reasons.
5. Finalize policy config defaults and test fixtures.

### Verification
- `pytest -q gateway/tests -k "private|isolation|memory|policy|collaborator"`
- `python security_assessment/run_assessment.py` private-data probes section.

---

## Tranche V9-2 — SOC correlation/reporting depth (111–116)
**Goal:** High-signal correlation between DNS/egress/audit/runtime events.

### Remaining tasks
1. Increase correlation linking across event types (same request/session/user).
2. Improve SOC/report endpoints with risk summaries and operator-ready fields.
3. Ensure incident automation hooks have deterministic tests.
4. Tighten false-positive/false-negative handling in SOC alert generation.

### Verification
- `pytest -q gateway/tests -k "soc|audit|correlation|incident|dashboard"`
- API smoke:
  - SOC/dashboard routes return structured correlated records.

---

## Tranche V9-3 — Security tool integration completeness (code-side only)
**Goal:** Trivy, OpenSCAP, Wazuh, ClamAV fully wired in code paths and surfaced in dashboard/reporting.

### Remaining tasks
1. Ensure scanner adapters are not stubs in runtime paths.
2. Ensure scan results normalize into unified event schema.
3. Ensure dashboard/security endpoints expose scanner states + recent findings.
4. Add deterministic tests for scanner error/fallback paths.

### Verification
- `pytest -q gateway/tests -k "trivy|openscap|wazuh|clamav|scanner"`
- Validate scanner sections in dashboard API responses.

---

## Tranche V9-4 — Collaborator policy model groundwork (roles/groups future-ready)
**Goal:** Prepare v1 permissions model without broad refactor now.

### Remaining tasks
1. Add explicit “owner-gated capability” language to collaborator capability responses.
2. Centralize collaborator-safe response templates for consistency.
3. Add hooks/flags for future per-group/per-user entitlements (no large schema migration in this tranche).

### Verification
- `pytest -q gateway/tests/test_telegram_proxy_inbound.py -k "safe_info|owner-gated|capability|protected"`
- Manual Telegram collaborator QA prompts.

---

## 3) Deferred (External / Non-Code-Only) Items

These remain intentionally deferred from this tracker:
- Host/runtime upgrades (Podman host version, Docker Desktop host perms).
- Tailscale/network host administration changes.
- Branch deletion/PR merge orchestration.
- Credential/token operational rotations outside code.
- iMessage activation + physical GUI sign-in flows.

---

## 4) Final Verification Gate (for tranche completion)

A tranche is complete only when all are true:
1. Targeted tests for touched behavior are green.
2. Full Telegram gateway suites are green:
   - `pytest -q gateway/tests/test_telegram_proxy_inbound.py gateway/tests/test_telegram_proxy_outbound.py`
3. No skipped tests in touched suites.
4. Manual Telegram sanity checks match expected role behavior.
5. Security assessment report has no silent collaborator responses for tested prompts.

---

## 5) Current Execution Order (from now)

1. **V8-1** onboarding reliability closure  
2. **V8-3** no-response elimination  
3. **V8-4** egress semantics hardening  
4. **V8-5** leak suppression atomicity  
5. **V8-6** rate-limit UX continuity  
6. **V8-7** 3-pass assessment loop  
7. **V9-1** private-data policy depth  
8. **V9-2** SOC correlation depth  
9. **V9-3** scanner integration completion  
10. **V9-4** owner-gated collaborator policy groundwork

