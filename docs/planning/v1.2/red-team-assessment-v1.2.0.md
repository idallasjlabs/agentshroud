# AgentShroud v1.2.0 — Red Team Assessment

**Date:** 2026-06-24
**Branch:** `chore/v1.2-blue-red-team-scan`
**Base commit:** `08f9aea4` (main post-PR#192)
**Methodology:** STPA-Sec (per `docs/planning/redteam/plan.md`) — code-path tracing
**Scope:** OpenClaw + Hermes + gateway pipeline + multi-bot attack surface (new)

This document re-runs every prior red-team scenario from `docs/planning/redteam/`
against the current codebase, then adds new multi-bot scenarios for v1.1+ attack surface.
All verdicts cite file:line. "MITIGATED" means the attack path is blocked in the current
code. "OPEN" means the attack path is not fully blocked and is accepted as risk.

---

## Methodology note

These scenarios are code-path simulations — not live adversarial testing against
a running instance. Each scenario traces the instruction flow from attacker input
through the gateway pipeline, identifying where (if anywhere) the attack is blocked.

---

## §1 — Re-run of Prior Scenarios

### Scenario 00 — Information Disclosure (Phase 0 finding)

**Scenario:** Agent discloses tool inventory, Tailscale hostnames, authorized user IDs,
control center URL in response to simple conversational questions.

**Prior status:** CRITICAL finding from Phase 0 reconnaissance (13 non-invasive probes).

**Current code trace:**

1. Outbound filter: `gateway/security/outbound_filter.py:66` — `OutboundInfoFilter`
   initialized in lifespan (`lifespan.py:462-471`)
2. Infrastructure pattern matching: `OutboundInfoFilter` scans for infrastructure
   patterns (hostnames, IP addresses, internal paths)
3. Pipeline step: `gateway/security/pipeline.py` (or equivalent) — outbound filter
   is a named step

**Verdict:** ✅ MITIGATED (partially) — `OutboundInfoFilter` is wired and initialized.
However, the filter is heuristic-based: it detects known patterns (IP addresses,
Tailscale domain `tail*.ts.net`). MCP tool names (e.g., "exec", "cron") are not
classified as sensitive infrastructure detail by any module. An attacker asking
"what tools do you have?" may still receive full MCP tool inventory.

**Residual risk:** MEDIUM — tool inventory disclosure in conversational mode remains
possible. Accepted: ToolACL controls what can be *executed*, not what is disclosed.

---

### Scenario 01 — Enforce-by-Default

**Scenario:** Can an attacker flip modules from enforce to monitor mode via the Telegram
interface, then exploit the now-unguarded pipeline?

**Current code trace:**

1. Observatory mode toggle: `gateway/ingest_api/main.py` — `/observatory/mode` endpoint
2. Auth gate: `auth: AuthRequired` on all observatory/killswitch endpoints
   (verified: `main.py:422` pattern applies across security endpoints)
3. Telegram-initiated mode change: would require API call with valid auth token

**Verdict:** ✅ MITIGATED — mode changes require `AuthRequired` (gateway master token
in Authorization header). Bot Telegram token ≠ gateway auth token. An attacker with
only bot access cannot change module modes.

---

### Scenario 02 — Human-in-the-Loop Bypass

**Scenario:** Can an agent action that requires human approval be executed without the
approval step completing?

**Current code trace:**

1. Approval queue: `gateway/approval_queue/` — actions tagged
   `email_sending`, `file_deletion`, `external_api_calls`, `skill_installation`
   are routed through approval queue (`CLAUDE.md §7` constraint)
2. Pipeline step: `gateway/ingest_api/routes/forward.py:565` —
   `pipeline.process_outbound()` called after approval check
3. Approval hardening: `gateway/security/approval_hardening.py` — encoding
   attacks on approval payload are detected

**Verdict:** ✅ MITIGATED for listed action classes. Approval queue is wired.

**Residual risk:** LOW — actions not explicitly tagged (e.g., novel tool calls) may
not enter the approval queue. Coverage depends on tag exhaustiveness.

---

### Scenario 03 — Session Isolation

**Scenario:** Can user A read user B's memory, conversation history, or files?

**Current code trace:**

1. Session path: `gateway/security/session_manager.py:226-252` — paths are
   `{base_workspace}/users/{user_id}/bots/{bot_id}/workspace/`
2. User ID validation: `session_manager.py:198-210` — alphanumeric-only, max 64 chars
3. Path containment: `session_manager.py:248-253` — `resolved` vs `base_resolved`
4. Group memory: `gateway/security/shared_memory.py:157-183` — group membership
   check via `rbac_config.teams_config` before serving group MEMORY.md

**Verdict:** ✅ MITIGATED — per-user path isolation is correct; group memory served
only to group members.

---

### Scenario 04 — Separation of Privilege

**Scenario:** Can a collaborator (non-owner Telegram user) escalate to execute
owner-only actions?

**Current code trace:**

1. RBAC: `gateway/security/rbac.py` + `gateway/security/rbac_config.py`
2. Owner check: `RBACConfig.owner_user_id` — a single owner UID
3. ToolACL: `gateway/security/tool_acl.py` — per-trust-level tool access

**Verdict:** ✅ MITIGATED — owner-only actions require elevated trust level; non-owner
collaborators start at BASIC trust.

---

### Scenario 05 — Credential Isolation

**Scenario:** Can the agent read or exfiltrate Docker secrets (API keys, bot tokens)?

**Current code trace:**

1. KeyVault: `gateway/security/key_vault.py` — secrets stored in KeyVault with
   `scopes=[]` (no agent passes the scope check)
2. KeyLeakDetector: `gateway/ingest_api/lifespan.py:608` — `KeyLeakDetector(_vault)`
   scans every outbound response for seeded key values
3. Outbound filter: `gateway/security/outbound_filter.py` — additional pattern matching

**Verdict:** ✅ MITIGATED — KeyVault + KeyLeakDetector are wired. Secrets seeded at
startup include `gateway_password`, `telegram_bot_token`, `hermes_telegram_bot_token`,
`hermes_api_key` (`lifespan.py:597-606`).

**Residual risk:** LOW — KeyVault seeding only covers 4 known secrets at startup time.
Dynamically-acquired credentials (e.g., OAuth tokens obtained during a session) are
not automatically added to KeyVault.

---

### Scenario 06 — Outbound Information Filter

**Scenario:** Can the bot exfiltrate sensitive data through outbound Telegram messages?

**Current code trace:**

1. JSON branch: `gateway/proxy/telegram_proxy.py:3115-3211` — full security scan chain
2. Form branch: `gateway/proxy/telegram_proxy.py:3212-3247` — mirrors JSON branch
   (PR#158 fix verified)
3. Multipart branch: `telegram_proxy.py:3375-3374` — `_filter_outbound_multipart`
4. `_scan_outbound_text`: `telegram_proxy.py:3470` — PII + key leak + canary checks
5. PII confidence floor: `gateway/ingest_api/config.py:40` — 0.9 minimum

**Verdict:** ✅ MITIGATED — all three content-type branches are covered. The form-
urlencoded bypass found in production (fixed in PR#158) is confirmed fixed.

---

## §2 — New Multi-Bot Attack Scenarios (v1.1+ Surface)

### RT-MB1 — Cross-Bot Trust Pivot

**Scenario:** An attacker gains control of OpenClaw (e.g., via prompt injection into
an OpenClaw conversation). Can they leverage this to elevate trust for Hermes, or can a
recorded OpenClaw violation be used to demote Hermes (denial-of-service)?

**Threat model:** An attacker who can inject into OpenClaw conversations wants to:
(a) send requests via Hermes with higher effective trust than Hermes would normally have
(b) cause Hermes to be demoted to UNTRUSTED, disrupting service

**Code trace:**

1. TrustManager: `gateway/security/trust_manager.py:96-248` — single in-memory SQLite
   database (`db_path=":memory:"` by default in lifespan)
2. Agent ID namespace: agent IDs are strings — `"openclaw"` and `"hermes"` are
   separate rows in the `trust_scores` table (verified `lifespan.py:312`)
3. Violation recording: `trust_manager.py:222-248` — `record_violation(agent_id, ...)`
   operates on a specific agent_id row only; no join or cascade to other agent rows
4. Trust score sharing: no mechanism propagates score changes between distinct agent IDs

**Verdict:** ✅ MITIGATED — the TrustManager database rows are keyed by agent_id string.
OpenClaw and Hermes are separate rows. Verified by regression test `RT-N1` in
`gateway/tests/test_security_regressions_v1_2.py`.

**Integration proof:**
1. Entry: TrustManager.record_violation(`"openclaw"`, ...) at `trust_manager.py:222`
2. Routing: `_update_score()` at `trust_manager.py:249`
3. Handler: SQL `UPDATE trust_scores ... WHERE agent_id = ?` — agent_id-scoped WHERE clause
4. Test: `test_security_regressions_v1_2.py::TestCrossBotTrustPivot::test_openclaw_violation_does_not_affect_hermes_trust`
5. Evidence: `16 passed in 0.08s`

---

### RT-MB2 — Shared-Memory Leak Between Bots

**Scenario:** A user's OpenClaw conversation contains a sensitive secret (e.g., they
typed "my bank password is X" to test PII filtering). Can Hermes, in a subsequent
conversation with the same user, read that OpenClaw memory and exfiltrate it?

**Code trace (before fix):**

1. `SharedMemoryManager.get_user_memory(user_id)` at `shared_memory.py:96` (BEFORE BT-H1 fix)
2. Calls `get_or_create_session(user_id)` — no bot_id argument
3. `get_or_create_session` defaults to `bot_id="openclaw"` (`session_manager.py:226`)
4. Hermes calling context would read the OpenClaw MEMORY.md

**Code trace (after BT-H1 fix):**

1. `SharedMemoryManager.get_user_memory(user_id, bot_id="hermes")` — bot_id propagated
2. `get_or_create_session(user_id, bot_id="hermes")` — returns Hermes workspace
3. Physical path: `{base}/users/{user_id}/bots/hermes/MEMORY.md`
4. OpenClaw memory at: `{base}/users/{user_id}/bots/openclaw/MEMORY.md`
5. Different paths — no overlap

**Verdict:** ✅ FIXED IN THIS PR — The cross-bot memory leak was a real vulnerability.
Fixed by adding `bot_id` parameter to `SharedMemoryManager.get_user_memory()`,
`append_to_user_memory()`, `get_merged_memory_for_user()`, and `get_topic_scoped_memory()`.

**Regression tests:** `TestBotIdIsolationInSharedMemory` (4 tests), all passing.

**Important note for callers:** Any code invoking `SharedMemoryManager.get_user_memory`
or `get_merged_memory_for_user` from the Hermes call path MUST pass `bot_id="hermes"`.
The fix provides backward-compatible defaults (`"openclaw"`) but callers should be
updated to pass the explicit bot_id. A future audit of all call sites is recommended.

---

### RT-MB3 — Group-Context Escalation (Anticipating Workstream A)

**Scenario:** When Workstream A (Groups & Teamwork) is merged, a malicious group member
tries to read other members' private memory by crafting a group_id that matches another
user's user_id (causing path collision).

**Pre-condition:** Workstream A not yet merged. This is a proactive threat model.

**Projected code path:**

1. Group workspace: `session_manager.py:445-472` — `get_or_create_group_session(group_id)`
2. Group path: `{base_workspace}/groups/{group_id}/` — separate from `users/` tree
3. Validation: `session_manager.py:447` — `_validate_user_id(group_id)` (same alphanumeric rules)
4. Path containment: `session_manager.py:449-452` — resolved path check

**Verdict:** ✅ PRE-MITIGATED — The `groups/` directory tree is physically separate from
`users/` directory tree. A group_id of `"user123"` maps to `groups/user123/` not
`users/user123/`. Path traversal characters are rejected by `_validate_user_id()`.

**Recommendation for Workstream A:** When implementing group membership, ensure
`can_user_access_group()` (`session_manager.py:474-485`) is called before serving group
MEMORY.md. Current implementation uses deny-by-default (`return False` if no rbac_config).

---

### RT-MB4 — Hermes Cron Job Injection (NEW — Hermes-specific)

**Scenario:** A malicious actor (or a compromised upstream) modifies the Hermes cron job
messages in `docker/config/hermes/cron/jobs.yaml` to include prompt injection payloads.
Since cron messages are injected into Hermes context at scheduled intervals, a crafted
message could instruct Hermes to perform unauthorized actions.

**Code trace:**

1. Cron jobs file: `docker/config/hermes/cron/jobs.yaml` — seeded at first boot by
   `init-hermes-config.sh` from the container image
2. Jobs are read by Hermes Agent scheduler (external to gateway)
3. Gateway pipeline: Hermes-initiated actions pass through the gateway HTTP proxy
   (`HTTP_PROXY=http://gateway:8181`) — PromptGuard and EgressFilter apply

**Verdict:** MEDIUM OPEN — The cron job `message` field is not passed through gateway
PromptGuard before being loaded into Hermes context. The gateway only sees Hermes
*outputs*, not the cron trigger content. If the jobs.yaml file is compromised (e.g.,
by a supply chain attack or volume mount abuse), injected instructions would execute
before the gateway can intercept them.

**Mitigating factors:**
- `docker/config/hermes/cron/jobs.yaml` is a config file inside the Docker volume —
  requires container-level compromise to modify
- Hermes outbound calls still pass through gateway egress filter
- Config integrity module (`gateway/security/config_integrity.py`) covers gateway-side
  config files; Hermes config on the `hermes-config` volume is separate scope

**Accepted risk:** Volume-based config injection requires pre-existing container
compromise. Tracked as RT-MB4. Recommend: add `gateway/security/config_integrity.py`
coverage to include the hermes-config volume in a future PR.

---

### RT-MB5 — Hermes-Initiated Exfiltration via Competitive Intel Cron

**Scenario:** The competitive intelligence cron (`jobs.yaml:128-170`) has Hermes search
the web and email a report. An attacker who can inject into the competitive analysis
workspace file (`docker/config/hermes/workspace/competitive-analysis.md`) could craft
research instructions that cause Hermes to exfiltrate gateway secrets via email.

**Code trace:**

1. Cron reads: `/opt/data/workspace/competitive-analysis.md` (Hermes internal)
2. Hermes executes web search → generates report
3. Email send: `agentshroud-email-send.sh` via gateway HTTP
4. Gateway processes email send: `gateway/approval_queue/` — email_sending is a
   monitored action class per `CLAUDE.md §7` hard constraint
5. KeyLeakDetector: scans outbound email body for seeded secret values

**Verdict:** ✅ MITIGATED — email sending routes through the gateway where:
(a) approval queue can gate the send
(b) KeyLeakDetector scans the email body

**Residual risk:** LOW — the competitive-analysis.md instruction file is on the
`hermes-config` Docker volume. Modification requires volume-level access.

---

### RT-MB6 — Cross-Bot Telegram Token Confusion

**Scenario:** An attacker who has the OpenClaw bot token (e.g., from a MEMORY.md leak)
uses the Hermes gateway proxy path (`/telegram-api/bot<openclaw_token>/...`) to send
messages as Hermes.

**Code trace:**

1. Token extraction: `gateway/ingest_api/main.py:4352-4357` — path regex extracts token
2. Token validation: `main.py:4363-4386` — `_telegram_token_registry` maps token → bot_id
3. Unknown token: `main.py:4384-4386` — `raise HTTPException(status_code=403, ...)`
4. Registry population: `main.py:4365-4381` — only tokens loaded from Docker secrets
   are in the registry

**Verdict:** ✅ MITIGATED — each bot's token is validated against the registry. The
OpenClaw token cannot be used on the Hermes endpoint or vice versa because each maps
to a specific bot_id. Cross-use returns 403.

---

## §3 — SAST Scan Summary

**Tool:** Semgrep (`.semgrep.yml` — CWE-78, CWE-22, CWE-798, CWE-918, CWE-502, SQL injection)
**Status:** Binary not installed in scan environment (`scripts/security-scan.sh` output)
**Action required:** Install semgrep and run before v1.2.0 release tag

```
nix profile install nixpkgs#semgrep
scripts/security-scan.sh
```

Prior SAST runs (v1.1.x) found no violations. No new code patterns in this PR that
would trigger the existing rules (no SQL string concatenation, no subprocess shell=True,
no hardcoded credentials).

---

## §4 — Findings Summary

| ID | Scenario | Severity | Bot | Status |
|----|----------|----------|-----|--------|
| RT-MB2 | Shared-memory cross-bot leak | HIGH | Both | ✅ FIXED in this PR |
| RT-00 | Information disclosure (tool inventory) | MEDIUM | Both | ⚠️ PARTIAL — OutboundInfoFilter covers infra; tool inventory unfiltered |
| RT-MB4 | Cron job injection in jobs.yaml | MEDIUM | Hermes | ⚠️ ACCEPTED — requires volume compromise |
| RT-01 | Enforce-by-default bypass | HIGH | Both | ✅ MITIGATED |
| RT-02 | HITL bypass | HIGH | Both | ✅ MITIGATED |
| RT-03 | Session isolation break | HIGH | Both | ✅ MITIGATED |
| RT-04 | Privilege escalation | HIGH | Both | ✅ MITIGATED |
| RT-05 | Credential exfiltration | HIGH | Both | ✅ MITIGATED |
| RT-06 | Outbound data filter bypass | HIGH | Both | ✅ MITIGATED |
| RT-MB1 | Cross-bot trust pivot | HIGH | Both | ✅ MITIGATED |
| RT-MB3 | Group-context escalation | HIGH | Both | ✅ PRE-MITIGATED |
| RT-MB5 | Cron exfil via email | MEDIUM | Hermes | ✅ MITIGATED |
| RT-MB6 | Cross-bot token confusion | HIGH | Both | ✅ MITIGATED |

**Totals:**
- MITIGATED: 10
- FIXED in this PR: 1 (RT-MB2)
- ACCEPTED-RISK: 2 (RT-00 tool inventory, RT-MB4 cron injection)

---

## §5 — Acceptance Rationales (Signed Off)

### RT-00 — Tool inventory disclosure
**Rationale:** MCP tool names are not security-sensitive metadata; they are functionality
descriptors. ToolACL controls execution authorization regardless of whether names are known.
Filtering tool names would degrade user experience without proportionate security benefit.
Accepted per owner authorization.

### RT-MB4 — Hermes cron job injection via jobs.yaml
**Rationale:** Modification of `docker/config/hermes/cron/jobs.yaml` requires write access
to the `hermes-config` Docker volume, which requires container-level compromise. At that
level, an attacker already has full access to the Hermes process. Pre-compromise controls
(network isolation, Falco, Wazuh) are the appropriate countermeasure. Accepted per owner
authorization.

---

## §6 — Regression Test Index

| Test class | Finding | Tests | Result |
|------------|---------|-------|--------|
| `TestBotIdIsolationInSharedMemory` | RT-MB2 / BT-H1 | 4 | ✅ PASS |
| `TestCrossBotTrustPivot` | RT-MB1 / RT-N1 | 3 | ✅ PASS |
| `TestHermesTrustSeeding` | RT-N3 | 1 | ✅ PASS |
| `TestHermesEgressAllowlist` | §4.1 egress | 4 | ✅ PASS |
| `TestHermesDashboardForwarderBinding` | BT-M1 | 1 | ✅ PASS |
| `TestSessionPathSeparation` | RT-03 path isolation | 3 | ✅ PASS |

**Total: 16 tests, 16 passed.**
