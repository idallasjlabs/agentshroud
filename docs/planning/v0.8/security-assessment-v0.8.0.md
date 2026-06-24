# AgentShroud Security Assessment — v0.8.0

**Date:** 2026-03-07
**Branch:** `feat/v0.8.0-enforcement-hardening` (commit `c9f2103`)
**Auditor:** Claude Code (Primary LLM Agent)
**Methodology:** Blue-team code review, STRIDE-aligned analysis

---

## Executive Summary

AgentShroud's security architecture is **substantial and well-layered**: 50+ security modules, defense-in-depth middleware pipeline, Docker network isolation, non-root containers with seccomp profiles, constant-time auth, tamper-evident audit chains, and comprehensive test coverage (2,236 passing tests). The Phase 1–3 enforcement hardening objectives are largely met.

However, the audit uncovered **1 critical credential exposure**, several **unimplemented features marketed as complete**, and **input validation gaps at the API boundary** that undermine the defense-in-depth story.

---

## Scorecard: Are We Achieving Our Goal?

| Goal | Status | Grade |
|------|--------|-------|
| Bot-agnostic encapsulation (Phase 1+2) | Functional — BotConfig, dynamic hostname registration, config-driven routing | **A** |
| CORS port-awareness (Phase 3) | Complete — dynamic origin generation from configured port, localhost-only | **A** |
| Network isolation (Phase 3) | Complete — 3-network topology, bot on `internal: true`, proxy enforcement | **A** |
| Generic bot references (Phase 3) | Complete — `agentshroud-bot` container name, `agentshroud-*` networks | **A** |
| Prompt injection defense | Strong regex layer (43+ patterns, 20+ languages), but ML classifier is a stub | **B** |
| Egress filtering | Multi-layer (Docker network + HTTP CONNECT proxy + app-level filter + DNS blocklist) | **A** |
| Secret management | Strong architecture, but `history.env` committed with live credentials | **C** |
| Input validation at API boundary | Pydantic models lack `max_length` — OOM vector | **C** |
| Audit trail | Hash-chained, SQLite-backed, tamper-evident — but in-memory chain not persisted | **B+** |
| Test coverage | 2,236 passing, 5 stale Pi-hole tests — security modules well-covered | **A-** |

**Overall: B+** — Strong architecture with specific gaps that need closing before v1.0.

---

## Critical Findings

### CRITICAL-1: `history.env` committed to git with live Telegram credentials

**File:** `history.env` (tracked since commit `efc4b98`)
**Contents:** `TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, and personal phone number in cleartext.
**Impact:** Anyone with repo access has credentials to impersonate the Telegram integration.
**Remediation:**
1. Rotate the Telegram API hash immediately via https://my.telegram.org
2. Remove from git history with `git filter-repo` or BFG Repo-Cleaner
3. Add `history.env` to `.gitignore`

### CRITICAL-2: No request body size limits on API models

**File:** `gateway/ingest_api/models.py`
**Impact:** `ForwardRequest.content`, `EmailSendRequest.body`, and `SSHExecRequest.command` have no `max_length`. An attacker (or a compromised bot) can send multi-gigabyte payloads causing OOM, bypassing the ContextGuard's 50KB check which runs *after* the full body is already parsed into memory.
**Remediation:** Add `max_length` validators to all text fields in Pydantic models, and/or add a middleware-level request body size limit.

---

## High-Priority Gaps

### HIGH-1: ML injection classifier is entirely a stub

**File:** `gateway/security/ml_classifier.py`
**Status:** `_try_load_model()` is a placeholder. `_classify_ml()` falls back to a 6-signal heuristic. The DistilBERT model path is documented but never loads.
**Impact:** The uncertain-zone (score 0.3–0.8) classification relies on simple heuristics, not the ML model the architecture implies.
**Remediation:** Either implement the DistilBERT classifier or remove the ML claims from the architecture docs and rename to `HeuristicClassifier`.

### HIGH-2: Approval queue Telegram notifications unimplemented

**File:** `gateway/approval_queue/enhanced_queue.py:326`
**Status:** `# TODO: Implement Telegram notification` — just logs.
**Impact:** High-risk actions requiring approval (email sending, file deletion, external API calls) silently queue without notifying the operator.
**Remediation:** Wire the existing Telegram bot integration to send approval notifications.

### HIGH-3: Credential generation in key rotation is a placeholder

**File:** `gateway/security/key_rotation.py:271`
**Status:** Generates UUID-based tokens, not real credentials. Comment explicitly says "placeholder."
**Impact:** Automated key rotation produces non-functional credentials.
**Remediation:** Implement provider-specific credential generation (1Password, AWS IAM, etc.) or mark key rotation as experimental.

### HIGH-4: In-memory audit chain not persisted

**File:** `gateway/proxy/pipeline.py` — `AuditChain`
**Status:** The `SecurityPipeline`'s hash-chained audit trail lives in memory. The separate SQLite `AuditStore` is persisted but is a different chain.
**Impact:** On gateway restart, the tamper-evident chain is lost. Post-incident forensics has a gap.
**Remediation:** Flush `AuditChain` entries to the SQLite `AuditStore` or unify the two systems.

---

## Medium-Priority Gaps

| # | Finding | File | Detail |
|---|---------|------|--------|
| M-1 | No webhook signature validation | `gateway/proxy/webhook_receiver.py` | No `X-Telegram-Bot-Api-Secret-Token` header check. Mitigated by long-polling mode + network isolation, but the webhook path exists and is unprotected. |
| M-2 | No replay attack protection | Same | No nonce, timestamp validation, or deduplication on inbound webhooks. |
| M-3 | Pi-hole test suite is stale | `gateway/tests/test_pihole_integration.py` | 5 tests expect a Pi-hole container that was replaced by the in-process DNS blocklist (`dns_blocklist.py`). Tests should be rewritten or deleted. |
| M-4 | Router metadata/content-type matching stubbed | `gateway/ingest_api/router.py:123-128` | Priority 2 (metadata tags) and Priority 3 (content type) routing commented as "future enhancement." Only explicit routing and default fallback work. |
| M-5 | Rate limiter is in-memory only | `gateway/ingest_api/auth.py` | State lost on restart. Per-IP ineffective when gateway binds to `127.0.0.1` (all local traffic = same IP). No per-endpoint granularity. |
| M-6 | CEF audit export verification unimplemented | `gateway/security/audit_export.py:257` | Returns `{"verified": False, "message": "CEF verification not implemented yet"}`. |
| M-7 | `ForwardRequest.content_type` not validated | `gateway/ingest_api/models.py` | Accepts any string, not restricted to `{text, url, photo, file}`. |
| M-8 | Single-pass URL decode in input normalizer | `gateway/security/input_normalizer.py:54` | Double/triple URL encoding can bypass detection. |
| M-9 | `docker-compose.secure.yml` exposes port on `0.0.0.0` | `docker-compose.secure.yml:29` | Should be `127.0.0.1:8080:8080` like the production compose file. |
| M-10 | Egress filter log (10K entries) not persisted | `gateway/security/egress_filter.py` | Lost on restart. |

---

## Low-Priority / Informational

| # | Finding | Detail |
|---|---------|--------|
| L-1 | `docker` Python package unpinned | `requirements.txt` — should be range-pinned like other deps |
| L-2 | `python-multipart` has no upper bound | Floor only (`>=0.0.18`), no ceiling |
| L-3 | `agentshroud.yaml` prompt_guard in `observatory` mode | Should be `enforce` for production |
| L-4 | Personal phone numbers in `agentshroud.yaml` iMessage allowlist | Consider secrets-managed overlay for production |
| L-5 | `webhook_receiver.py` TODO for config-driven `owner_user_id` | Falls back to `RBACConfig` default |
| L-6 | `memory_integrity.py` modification detection is basic | 5-second heuristic for source attribution |
| L-7 | Prompt injection semantic paraphrasing bypass | Regex can't catch "the earlier guidance is no longer relevant" style attacks — needs the ML classifier (HIGH-1) |
| L-8 | No multimodal injection defense | No OCR-based detection for injection payloads in images |
| L-9 | Multilingual gaps | Thai, Vietnamese, Swahili, Amharic not covered in prompt guard |

---

## What's Working Well

These aspects are production-grade and should be preserved:

1. **Docker hardening** — SHA256-pinned base images, `cap_drop: ALL`, `no-new-privileges`, custom seccomp, read-only rootfs, setuid/setgid stripped, non-root users, resource limits
2. **Network topology** — 3-network isolation with bot on `internal: true`, all egress forced through gateway proxy
3. **Auth** — constant-time `hmac.compare_digest()`, Docker secrets (never env vars), auto-generated fallback tokens
4. **CORS** — port-aware, localhost-only, no wildcards, credentials only with specific origins
5. **Error handling** — global exception handler never leaks stack traces, request bodies never logged
6. **Security headers** — `nosniff`, `DENY`, `no-store`, CSP with per-request nonces
7. **Prompt injection** — 43+ patterns, 20+ languages, Unicode evasion detection, input normalization
8. **Egress** — 4-layer defense (Docker network + CONNECT proxy + app filter + DNS blocklist)
9. **IP allowlisting** — proxy endpoints restricted to isolated network subnets
10. **Test coverage** — 2,236 tests, every security module has dedicated test file

---

## Remediation Status (Post-v0.8.0)

All findings addressed in `feat/v0.8.0-enforcement-hardening`. See `docs/agentshroud-security-overview-v0.8.0.md` for before/after comparison and v0.9.0/v1.0.0 roadmap.
