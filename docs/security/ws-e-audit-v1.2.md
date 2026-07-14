<!--
Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
Patent Pending — U.S. Provisional Application No. 64/018,744
-->

# WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)

**Workstream:** WS-E — SCRUM-72 (blue-team re-run) · SCRUM-73 (red-team attack run) · SCRUM-74 (fix-or-accept closure)
**Branch audited:** `feat/scrum-72-74-ws-e-audit` (from `main`)
**Date:** 2026-07-14
**Method:** every claim grounded in real code (`file:line`), verified before assertion (repo No-Security-Theater rule). Findings are evidence-based; nothing invented.

---

## Executive Summary

The AgentShroud security pipeline is genuinely deep and well-instrumented: the inbound/outbound guard chain in `gateway/proxy/pipeline.py` is real, fail-closed on module error for non-owners, and the SHA-256 hash-chain audit ledger is tamper-evident with guaranteed persistence for block and owner-bypass events. Known-catalogued prompt-injection strings are correctly blocked. Subagent and delegation privilege escalation are properly floored/owner-gated.

However, the audit found **one HIGH-severity, cheaply-fixable hole that has been FIXED in this branch**, plus several genuine **FIX-RECOMMENDED** gaps where security code exists but is either unwired (dead code) or scanning only a subset. The central theme is an **identity-trust boundary weakness**: the pipeline's most powerful privilege — the *owner exemption* — keys off an attacker-controllable request field.

| Metric | Count |
|--------|-------|
| Blue-team defense layers reviewed | 18 |
| Red-team vectors tested | 12 (+1 sub-finding RT-9b) |
| Vectors fully blocked (evidence) | 4 (RT-3, RT-10, RT-11-if-configured, RT-12-partial) |
| Vectors exploitable / partially exploitable | 8 |
| Findings — **FIXED** (this branch, with test) | 1 |
| Findings — **FIX-RECOMMENDED** | 10 |
| Findings — **ACCEPTED** (risk-justified) | 2 |

**Headline finding (FIXED):** the `/forward` REST endpoint trusted a body-supplied `user_id` to grant the pipeline's owner exemption (bypass of PromptGuard/ContextGuard/injection scanners/PII + FULL outbound trust), with only a single shared Bearer token gating the endpoint. Any token holder could impersonate the owner. Fixed by requiring a trusted `X-AgentShroud-User-Id` header to corroborate an owner-ID claim — mirroring the existing `/mcp/proxy` defense. Three tests prove the block and preserve the legitimate voice-gateway path.

---

## Part 1 — Blue-Team Posture Review (SCRUM-72)

Defense layers reviewed, each with what it covers, gaps, and citation.

| # | Layer | File:line | Covers | Gap / note |
|---|-------|-----------|--------|------------|
| 1 | Pipeline required-guard fail-closed | `gateway/proxy/pipeline.py:406-415` | Refuses to start without `pii_sanitizer` | Only `pii_sanitizer` is *required*; other guards merely warn (`:420-438`) |
| 2 | ContextGuard (cross-turn injection) | `pipeline.py:468-517` | Session-level injection/repetition; fail-closed for non-owner on error (`:511-517`) | Owner exempt (`:478`), audited (`:484`) |
| 3 | ContextIntegrity scorer (C21) | `pipeline.py:523-582` | Rolling provenance score; <0.3 blocks non-owner | Owner exempt (`:532`) |
| 4 | PromptGuard inbound scan | `pipeline.py:586-617`; patterns `gateway/security/prompt_guard.py:72-578` | 43+ weighted regex rules, 20+ languages, threshold 0.8 | Pure regex — paraphrase/leetspeak/homoglyph evasions (see RT-1) |
| 5 | HeuristicClassifier (uncertain band) | `pipeline.py:621-659` | Secondary signal 0.3–0.8 only; never sole blocker | By design advisory |
| 6 | Inbound injection scan (CVE-2026-30741) | `pipeline.py:665-705` | ToolResultInjectionScanner ruleset on inbound | Encoded-injection only checks `rules[:6]` (see RT-2) |
| 7 | Inbound command-injection (CVE-2026-34425) | `pipeline.py:710-738` | XMLLeakFilter C32 shell-metachar patterns | — |
| 8 | PII sanitizer (Presidio 0.9 floor) | `pipeline.py:746-759`; config `gateway/ingest_api/config.py` | Redacts non-owner PII | Owner exempt (`:746`) |
| 9 | ClamAV inline scan | `pipeline.py:764-802` | base64 payload malware scan | **Fail-open** by design (`:778-780`); availability > detection |
| 10 | TrustManager action gate | `pipeline.py:805-822` | Per-agent trust level vs action | — |
| 11 | Approval queue | `pipeline.py:825-833`; email route `gateway/ingest_api/routes/forward.py:218` | Generic actions + dedicated `email_sending`/`imessage_sending` endpoints | Generic list differs from doc list (see RT-9) |
| 12 | Outbound PII + info filter + prompt-protection | `pipeline.py:869-968` | Outbound redaction, fabricated-notice block, disclosure risk | — |
| 13 | Encoding detector | `pipeline.py:971-989` | Multi-layer decode (base64/hex/url/rot13/homoglyph/zero-width) | **Outbound-only** — not run inbound (see RT-2) |
| 14 | Canary tripwire + OutputCanary | `pipeline.py:992-1025`, `1157-1209` | Canary-token exfil block; fail-closed non-owner (`:1196`) | — |
| 15 | KeyLeakDetector | `pipeline.py:1214-1258` | Redacts stored credential values; fail-closed non-owner | — |
| 16 | Egress filter + envelope signer | `pipeline.py:1273-1323` | Deny-listed URL block; HMAC attestation | Only runs when `destination_urls` passed (see RT-7) |
| 17 | Gateway auth (Bearer, constant-time) | `gateway/ingest_api/auth.py:89,140` | `hmac.compare_digest` — no timing attack | Single shared token; not bound to identity (see RT-6) |
| 18 | Audit hash-chain (FR6) | `pipeline.py:121-289` | SHA-256 chain, guaranteed persist on block/owner-bypass | Tamper-evident; verified `verify_chain` |

**Blue-team verdict:** the enforced pipeline is real and non-stub. The weaknesses are at the *edges*: (a) the identity that unlocks owner exemption, (b) inbound decode coverage, and (c) several modules that are constructed but never driven.

---

## Part 2 — Red-Team Attack Run (SCRUM-73)

12 vectors. For each: reproduction reasoning and BLOCKED / EXPLOITABLE with the guard `file:line`.

### RT-6 · Owner-identity spoofing via `/forward` body — **EXPLOITABLE → FIXED**

**Reproduction.** `/forward` (`gateway/ingest_api/routes/forward.py:327`) is gated only by `AuthRequired`, a single shared Bearer token compared at `auth.py:140` (`verify_token` → `hmac.compare_digest`). The token proves *possession*, not *identity* — `auth_check` returns `None` and binds no user (`auth.py:101,148-149`). Meanwhile `user_id` is a plain request-body field (`gateway/ingest_api/models.py:41-45`, default `None`). It flows unchecked into:
- middleware (`forward.py:365`), and
- pipeline metadata (`forward.py:418`),

where `is_owner` is computed as `str(user_id) == str(self._owner_user_id)` (`pipeline.py:460-461`). The owner ID is a static, public/guessable Telegram numeric ID (`gateway/security/rbac_config.py:63` = `"8096968754"`). Owner status then exempts ContextGuard (`pipeline.py:478`), ContextIntegrity (`:532`), PromptGuard (`:591`), inbound injection/cmd scanners (`:673`,`:714`), and PII redaction (`:746`), and elevates outbound trust to `FULL` (`forward.py:582`) — unmasking hostnames/ports.

An attacker holding the shared token sends `{"content":"…","source":"api","user_id":"8096968754"}` and is treated as owner across the pipeline. The in-code justification (`forward.py:574-576`, "trusted because /forward requires gateway auth … set by the authenticated bot, not by an untrusted end user") was **false**: the field is client-controlled and unbound from the token.

**Corroboration:** the same threat is *already defended* at `/mcp/proxy` via `_resolve_effective_agent_id` (`gateway/ingest_api/main.py:662-673`), which rejects body owner-impersonation unless a trusted `x-agentshroud-user-id` header is present. `/forward` had no equivalent guard — a clear inconsistency.

**Reachability:** gateway binds to `127.0.0.1` (`config.py:299`); surfaces are on Tailscale. Attacker needs the shared token AND loopback/Tailnet reach (leaked token, compromised bot container, or Tailnet insider). This bounds severity to HIGH (not internet-CRITICAL) but does not eliminate it.

**Disposition: FIXED (this branch).** `/forward` now drops an owner-ID claim unless the trusted `X-AgentShroud-User-Id` header matches (`gateway/ingest_api/routes/forward.py`, post-target-resolution block). The voice-gateway already sends this header (`voice_gateway/server.py:500`), and the Telegram webhook derives `user_id` from the authenticated payload (`gateway/proxy/webhook_receiver.py:138,175`), so no legitimate path breaks. Non-owner `user_id` values pass through unchanged (they grant no exemption).

**Integration proof:**
```
1. Entry point:  gateway/ingest_api/routes/forward.py:327  forward_content(request, req, auth)
2. Routing:      forward.py (post-resolve_target anti-spoof block) — owner-claim + trusted-header check
3. Handler:      request.user_id = None when owner claimed without matching X-AgentShroud-User-Id
4. Test:         gateway/tests/test_forward_routing.py
                   ::TestOwnerSpoofingViaForwardBody::test_body_owner_id_without_trusted_header_is_stripped
                   ::…::test_body_owner_id_with_matching_trusted_header_is_honored
                   ::…::test_non_owner_body_user_id_passes_through
                   ::TestOwnerTrustElevation::test_owner_id_without_trusted_header_does_not_elevate_trust
5. Evidence:     13 passed in 0.14s  (forward suite);  99 passed (pipeline+rbac+telegram+owner-pii suites)
```

### RT-1 · Prompt injection — **PARTIALLY BLOCKED**
Three catalogued strings all score ≥ 0.8 and BLOCK (`prompt_guard.py:74,102,159,401,494,505`). But PromptGuard is pure weighted regex (`prompt_guard.py:742-745`); paraphrase (synonyms not in the pattern list), leetspeak (`1gn0re`), and single-homoglyph substitution (Cyrillic `і`, only weight 0.5 at `:686`, below 0.8) evade it. `input_normalizer.normalize_input` (`:713`) does not fold homoglyphs/leet. **Disposition: FIX-RECOMMENDED** (add homoglyph+leet normalization; reuse `encoding_detector.HOMOGLYPHS`).

### RT-2 · Inbound encoding bypass — **EXPLOITABLE**
`EncodingDetector.analyze` runs outbound only (`pipeline.py:971`); there is no inbound decode step before PromptGuard. Inbound base64 is only handled by `PromptGuard._check_encoded_content`, which re-scans decoded text against **`_PATTERNS[:5]` only** (`prompt_guard.py:666,673`), and `ToolResultInjectionScanner._detect_encoded_injection` scans `rules[:6]` only (`tool_result_injection.py:197,212`). A base64-encoded payload matching a lower-ranked pattern (e.g. `authority_escalation`) decodes but is not matched. **Disposition: FIX-RECOMMENDED** (wire `EncodingDetector` inbound before Step 1; remove the top-N slice so decoded payloads hit the full ruleset).

### RT-3 · Cross-collaborator data access — **BLOCKED (isolation) / gated by RT-6**
Per-user memory keyed `users/{user_id}/bots/{bot_id}/MEMORY.md` (`gateway/security/session_manager.py:277-278`); `_validate_user_id` allows only `^[a-zA-Z0-9_-]+$` ≤64 chars (`:251-254`) plus resolved-path containment (`:293-298`) — path traversal BLOCKED. There is no cross-user read primitive; the only way to read B's memory is to *name* B's `user_id`, which loops back to RT-6 on the REST path. **Disposition: root cause = RT-6 (FIXED); isolation layer ACCEPTED (sound).**

### RT-4 · Cross-group access — **data BLOCKED / group tool-ACL UNWIRED**
Group memory membership is enforced (`gateway/security/shared_memory.py:180,240`; `session_manager.can_user_access_group` deny-by-default `:519-530`). But the per-group tool-permission layer is **dead code**: `rbac.check_group_permission` (`gateway/security/rbac.py:389`), `group_rbac.GroupRoleResolver`, and `tool_acl.can_use_tool_in_group_context` (`gateway/security/tool_acl.py:370`) have **zero non-test callers**. The "IEC 62443 FR3 SL3 enforced at every tool-call boundary" claim (`group_rbac.py:19`) does not run in production. **Disposition: FIX-RECOMMENDED** (wire into the tool-call path, or drop the claim per No-Security-Theater).

### RT-5 · Shared-memory write poisoning — **EXPLOITABLE**
`append_to_group_memory(group_id, content, author_id)` (`gateway/security/shared_memory.py:74-89`) performs **no membership/authorization check**; `author_id` is a free-form label in the timestamp header, not an authorization principal. `append_to_user_memory` (`:113`) likewise. Any caller reaching these writes arbitrary content into any group's shared memory, which is later merged into bot system context (`:204`) — a stored-prompt-injection / memory-poisoning vector. **Disposition: FIX-RECOMMENDED** (verify the authenticated caller is a member of `group_id` / is the target `user_id` before writing).

### RT-7 · Egress exfiltration — **BLOCKED in practice / pipeline hook is dead code + residual bypass**
The pipeline egress hook runs only when `destination_urls` is passed to `process_outbound` (`pipeline.py:1274`), and **no production caller passes it** (`forward.py:585-590`, `telegram_proxy.py:3603-3608`, `slack_proxy.py:191-199`, `webhook_receiver.py:224-227`) — so that step is dead code and outbound content bodies are never URL-scanned there. Real egress enforcement lives at the HTTP CONNECT proxy (`gateway/proxy/http_proxy.py:325` `egress_filter.check_async`, block → 403 at `:364-373`) and MCP proxy (`mcp_proxy.py:557,563`); the filter is **default-deny** in enforce mode (`egress_config.py:157,244`; `egress_filter.py:305-313`), blocks private/loopback IP-literals/SSRF (`egress_filter.py:217-224,458-480`), and denylists pastebin/webhook exfil targets (`egress_config.py:163-217`). Residual gaps: (a) `SYSTEM_BYPASS_DOMAINS` (`http_proxy.py:43-54`: `api.github.com`, Slack) **skip interactive approval** — a writable exfil channel; (b) `dns_filter.check_rebinding` (`dns_filter.py:195-224`) has **zero callers** — a name that passes the allowlist can re-resolve to a private IP at connect time with no re-check. **Disposition: FIX-RECOMMENDED** (delete or wire the dead pipeline hook per No-Security-Theater; reassess GitHub/Slack bypass; wire `check_rebinding`). Network isolation of bot containers is the effective boundary — the core exfil vector is not wide-open.

### RT-8 · Multi-bot lateral movement (trust ledger) — **EXPLOITABLE (inert)**
`CrossBotTrustLedger` (Module 27) propagation logic is real (`gateway/security/cross_bot_trust_ledger.py:192-308`) but **never driven** — it is assigned in the pipeline constructor (`pipeline.py:373`) yet `record_incident`/`register_peer` have **zero production callers**. A confirmed injection compromise on OpenClaw records zero cross-bot decay against Hermes. **Disposition: FIX-RECOMMENDED** (call `register_peer` at startup and `record_incident` from the inbound block path; add an integration test).

### RT-9 · Approval-queue bypass — **PARTIALLY EXPLOITABLE**
The pipeline approval gate is effectively **inert for normal traffic**: it fires only when `action in self.approval_actions` (`pipeline.py:825`) where the list is `["execute_command","delete_file","admin_action","install_package"]` (`:384-389`), but the primary inbound caller hard-codes `action="send_message"` (`forward.py:411`) — which never matches. Of the four CLAUDE.md-documented sensitive categories: `email_sending` IS gated by a dedicated route (`forward.py:213-228`, but only when the recipient is not allowlisted; allowlisted sends skip approval *and* PII redaction `forward.py:188-197`), `imessage_sending` at `main.py:696-717`, `skill_installation` via SkillGuard on the skills-reload path — but **`file_deletion` and `external_api_calls` have no human-in-the-loop approval route in the request pipeline** (only group-RBAC ACL denial in `group_rbac.py:38-41`, which is unwired per RT-4). **Disposition: FIX-RECOMMENDED** (unify the chokepoint; add real gates for `file_deletion`/`external_api_calls`; reconcile `approval_actions` with the documented list).

### RT-9b · Approval privilege-separation — **EXPLOITABLE**
The approval-decision route (`gateway/ingest_api/routes/approval.py:67-78`, `decide_approval`) is gated by the **same shared `auth_token`** used for agent submission (`approval.py:50`), with **no owner/role/RBAC check** on the decide route. A component holding the gateway token — including a compromised agent that can reach the gateway API — can approve its own pending request. Constant-time compare (`auth.py:140`) prevents forgery, and replay is blocked (already-decided/expired items rejected, `queue.py:146-153`), but submit-authority and approve-authority are not separated. **Disposition: FIX-RECOMMENDED** (require an owner/admin role, not the shared token, on the decide route).

### RT-10 · Subagent / delegation privilege escalation — **BLOCKED**
Subagent effective trust is floored: `min(parent_trust, parent_info.effective_trust)` (`gateway/security/subagent_monitor.py:93-95`); low-trust subagents are denied high-trust tools in enforce mode (`:129-142`). Delegation is owner-gated, self-delegation rejected, TTL-capped at 72h, auto-expiring (`gateway/security/delegation.py:47-51,137,145`). **Disposition: ACCEPTED (well-defended).**

### RT-11 · MCP-server compromise — **BLOCKED-if-configured / dormant-by-default**
`MCPPolicyEngine` is a real deny-by-default engine (`gateway/security/mcp_policy.py:307-380`), NFKC-normalized against homoglyph evasion, fail-closed (empty config = deny-all `:123,127`; REQUIRE_APPROVAL with no queue = DENY `:425-443`), and genuinely wired into `MCPProxy` before passthrough (`gateway/proxy/mcp_proxy.py:387-393`; entry `main.py:743`). BUT it is instantiated only when an `mcp_policy:` YAML section exists (`lifespan.py:1315-1316`; `config.py:580`), and **no such section ships in `agentshroud.yaml.example`** — so a stock deployment runs MCP with `policy_engine=None` and the gate disabled. **Disposition: FIX-RECOMMENDED** (ship a default deny-by-default `mcp_policy:` block in the example config).

### RT-12 · Skill supply-chain — **PARTIALLY BLOCKED**
`SkillGuard` is real, wired on both the HTTP deploy gate (`gateway/web/api.py:961-969`) and the bash sync gate (`scripts/sync-llm-settings.sh:171`), fail-closed on unreadable/oversized artefacts. BUT `recommendation` only **BLOCKs at CRITICAL** (`gateway/security/skill_guard.py:123-127`): a skill combining secret-file reads + data exfiltration + `shell=True` scores HIGH → FLAG → **deploys anyway**, relying on a human noticing the flag. Regex evasion (string-concat, `getattr`, non-Python payloads) is acknowledged in the module docstring (`:16-29`). **Disposition: FIX-RECOMMENDED** (block at HIGH for the exfil/secret/shell classes, or require approval for HIGH).

---

## Part 3 — Fix-or-Accept Closure (SCRUM-74)

Release gate: every finding has a disposition. Nothing ambiguous.

| ID | Finding | Severity | File:line | Disposition |
|----|---------|----------|-----------|-------------|
| RT-6 | Owner spoof via `/forward` body `user_id` | HIGH | `forward.py:418`, `pipeline.py:460-461`, `auth.py:140` | **FIXED** (trusted-header guard + 4 tests) |
| RT-1 | Prompt injection regex evasion (paraphrase/leet/homoglyph) | MEDIUM | `prompt_guard.py:686,713,742-745` | FIX-RECOMMENDED — add homoglyph+leet normalization to `input_normalizer` |
| RT-2 | Inbound encoding bypass (outbound-only decode; top-N slice) | HIGH | `pipeline.py:971`, `prompt_guard.py:666,673`, `tool_result_injection.py:197,212` | FIX-RECOMMENDED — wire EncodingDetector inbound; scan full ruleset |
| RT-4 | Group tool-ACL unwired (dead code) | MEDIUM | `rbac.py:389`, `tool_acl.py:370`, `group_rbac.py` | FIX-RECOMMENDED — wire into tool-call path or drop the claim |
| RT-5 | Shared-memory write has no ACL (poisoning) | HIGH | `shared_memory.py:74-89,113` | FIX-RECOMMENDED — enforce caller membership before write |
| RT-8 | Cross-bot trust ledger inert (Module 27 never driven) | MEDIUM | `pipeline.py:373`, `cross_bot_trust_ledger.py:192` (no callers) | FIX-RECOMMENDED — call `register_peer`+`record_incident`; add test |
| RT-11 | MCP policy engine dormant unless YAML authored | HIGH (deploy) | `lifespan.py:1315-1316`, `config.py:580`, `agentshroud.yaml.example` | FIX-RECOMMENDED — ship default deny-by-default `mcp_policy:` |
| RT-12 | SkillGuard blocks only at CRITICAL; HIGH flags-and-deploys | MEDIUM | `skill_guard.py:123-127`, `web/api.py:970-975` | FIX-RECOMMENDED — block/queue-approve at HIGH |
| RT-7 | Pipeline egress hook dead code; GitHub/Slack approval-bypass; `check_rebinding` unwired | MEDIUM | `pipeline.py:1274`, `http_proxy.py:43-54`, `dns_filter.py:195-224` | FIX-RECOMMENDED — wire/delete hook; reassess bypass; wire rebinding |
| RT-9 | Pipeline approval gate inert for normal traffic; `file_deletion`/`external_api_calls` ungated | MEDIUM | `pipeline.py:384-389,825`, `forward.py:411` | FIX-RECOMMENDED — unify chokepoint; add missing gates |
| RT-9b | Approval decide route uses shared token (no priv-separation) | MEDIUM | `approval.py:67-78`, `auth.py:140` | FIX-RECOMMENDED — require owner/admin role on decide |
| RT-3 | Cross-collab isolation | — | `session_manager.py:251-298` | ACCEPTED — sound; root cause was RT-6 (fixed) |
| RT-10 | Subagent/delegation escalation | — | `subagent_monitor.py:93-142`, `delegation.py:47-51,137` | ACCEPTED — well-defended |

### IEC 62443 risk justification for ACCEPTED items
- **RT-3 (isolation):** FR2 (Use Control) / FR5 (Restricted Data Flow) SL2 satisfied — path-validated per-user namespacing with resolved-path containment. Residual reachability was RT-6, now closed.
- **RT-10 (subagent/delegation):** FR2 SL2 satisfied — least-privilege inheritance floor + owner-gated, TTL-bounded delegation. No escalation path reachable.

### Dead-code / unwired security modules surfaced (No-Security-Theater flags)
Confirmed constructed-but-never-called in the request path (per the repo's own Rule A):
`TokenValidator` (`middleware.py:214`; also `_decode_token` skips JWT signature verification, `token_validation.py:64-77`), `OAuthSecurityValidator` (`middleware.py:374`), `session_security.SessionManager` (`middleware.py:207`; strong nonce/fingerprint/replay controls never invoked), `CrossBotTrustLedger` (RT-8), group tool-ACL trio (RT-4). Recommend: wire them or stop counting them as active modules.

### MFA note
The task brief stated "MFA (just added)". An exhaustive search (`mfa|otp|totp|multi_factor|2fa|authenticator`) found **no MFA implementation** in `gateway/` — only a PII-redaction regex for OTP codes in message text (`gateway/ingest_api/sanitizer.py:46-47`) and a compliance description string (`gateway/security/scanner_integration.py:147`). There is no second factor to audit. The entire identity surface is the single shared token + (now header-corroborated) `user_id`. Recorded honestly as ACCEPTED-with-gap; MFA remains a genuine future control.

---

## Verification Steps

```bash
# Fix + regression proof (from repo root)
PY=/Users/ijefferson.admin/.conda/envs/gsdl/bin/python
$PY -m pytest gateway/tests/test_forward_routing.py -o addopts="" -q
#   -> 13 passed

$PY -m pytest gateway/tests/test_pipeline_unit.py \
              gateway/tests/test_email_owner_bypasses_pii.py \
              gateway/tests/test_rbac.py \
              gateway/tests/test_telegram_pipeline.py -o addopts="" -q
#   -> 99 passed

# Lint + format (changed files)
ruff check gateway/ingest_api/routes/forward.py gateway/tests/test_forward_routing.py   # All checks passed!
black --line-length 100 --check gateway/ingest_api/routes/forward.py gateway/tests/test_forward_routing.py

# Confirm the dead-code findings (should return empty / no production callers)
grep -rn "can_use_tool_in_group_context\|GroupRoleResolver(" gateway --include=*.py | grep -v test
grep -rn "record_incident\|register_peer" gateway/proxy gateway/ingest_api gateway/runtime --include=*.py | grep -v test
```

## Risk Callouts
- **RT-2 (inbound encoding)** and **RT-5 (memory write ACL)** are the two highest-value remaining items — both HIGH, both concrete injection/poisoning vectors. Recommend prioritizing next.
- **RT-11 (MCP dormant)** is a deployment-configuration risk: the gate exists but ships off. A one-line example-config addition closes it.
- The FIXED item (RT-6) removes the single most impactful privilege-escalation path; the same anti-spoof pattern should be audited on `/webhook/telegram` body `from.id` for defense-in-depth (currently mitigated by that endpoint being bot-internal).
