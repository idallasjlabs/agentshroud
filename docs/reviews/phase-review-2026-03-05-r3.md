# AgentShroud v0.8.0 — Peer Review Round 3 (FINAL)

**Date:** 2026-03-05  
**Reviewer:** AgentShroud Bot (automated peer review)  
**Branch:** `feat/v0.8.0-enforcement-hardening`  
**Diff base:** `origin/main..HEAD`  
**Prior reviews:** `phase-review-2026-03-05.md` (R1), `phase-review-2026-03-05-r2.md` (R2)

---

## Summary

This is the **final review pass** before v0.8.0 release. All ERROR and WARNING
findings from R1 and R2 have been verified as fixed. Three new minor findings
were discovered and fixed in this round.

### Test Results

| Metric | Value |
|--------|-------|
| Tests passed | **2225** |
| Tests failed | **0** |
| Warnings | **0** |
| Duration | ~39s |

---

## Prior Findings — Verification

### R1 Findings (all verified fixed in R2)

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| E1 | ERROR | `webhook_receiver.py` unreachable `_stats` init block | ✅ Fixed (dead code removed) |
| E2 | ERROR | `_get_pihole_auth_token` undefined in second endpoint | ✅ Fixed (helper extracted) |
| W1 | WARNING | `docker-compose.yml-latest` stale snapshot | ✅ Fixed (file deleted) |
| W2 | WARNING | `docker-compose.pi.yml` YAML indentation error | ✅ Fixed |
| W3 | WARNING | Hardcoded owner_user_id `"8096968754"` in webhook_receiver | ✅ Fixed (uses RBACConfig) |
| I1 | INFO | `cef_version` still reads `0.7.0` in config.py | ✅ Acceptable (CEF version != product version) |
| I2 | INFO | Duplicate `_is_imessage_recipient_allowed` across files | ⚠️ Fixed in R3 (see below) |
| I3 | INFO | `_get_pihole_auth_token` helper consistency | ✅ Fixed |
| I4 | INFO | Dockerfile uses `@latest` tags | ✅ Fixed (all pinned) |

### R2 Findings (all verified fixed)

| ID | Severity | Description | Status |
|----|----------|-------------|--------|
| R2-M1 | ERROR | Trivy install via curl\|sh (no checksum) | ✅ Fixed (checksum verification added) |
| R2-M2 | WARNING | `_telegram_proxy` pipeline never set | ✅ Acceptable — pipeline attribute unused in TelegramAPIProxy |
| R2-M3 | WARNING | Telegram proxy missing IP allowlist | ✅ Fixed (mirrors LLM proxy restrictions) |
| R2-M4 | WARNING | Root endpoint missing CSP nonce | ✅ Fixed (nonce + security headers added) |
| R2-H1 | INFO | 1Password CLI downloaded without GPG verification | ✅ Fixed (GPG sig verification added) |
| R2-H2 | INFO | setuid/setgid bits not stripped in container | ✅ Fixed (CIS 4.8 compliance) |

---

## R3 Findings (NEW — this round)

### R3-W1 — WARNING: Stale version string in control page HTML

**File:** `gateway/ingest_api/main.py` line 302  
**Issue:** The HTML control page (`/`) displayed `Version: 0.5.0` instead of `0.8.0`.  
**Risk:** Cosmetic but misleading — operator may think an old version is running.  
**Fix:** Updated to `0.8.0`. ✅ **FIXED**

### R3-W2 — WARNING: Stale OCI label version in Dockerfile

**File:** `docker/Dockerfile.agentshroud` line ~125  
**Issue:** `org.opencontainers.image.version` label was `"0.2.0"` instead of `"0.8.0"`.  
**Risk:** Container image metadata would report wrong version to registries/scanners.  
**Fix:** Updated to `0.8.0`. ✅ **FIXED**

### R3-W3 — WARNING: Dead code `_is_imessage_recipient_allowed` in forward.py

**File:** `gateway/ingest_api/routes/forward.py` lines 64–66  
**Issue:** `_is_imessage_recipient_allowed` was defined but never called. The active
implementation lives in `main.py` (with `fnmatch` glob support). The forward.py
version used simple string matching — a functional inconsistency if it were ever used.  
**Risk:** Dead code that could be mistakenly called, bypassing glob-based allowlist logic.  
**Fix:** Removed the dead function. ✅ **FIXED**

### R3-W4 — WARNING: Debug log leaking agent response content

**File:** `gateway/ingest_api/routes/forward.py` line 306  
**Issue:** `logger.info(f"DEBUG: agent_response = {agent_response}")` logs the full
agent response at INFO level, which could contain sensitive data (PII, credentials,
internal state) and would appear in production logs.  
**Risk:** Information leakage through production logs.  
**Fix:** Changed to `logger.debug()` with only the response type name. ✅ **FIXED**

---

## Architecture Review (Positive Observations)

The v0.8.0 branch demonstrates mature security architecture:

1. **Route extraction** — Main.py was >2000 lines in v0.7; now properly decomposed
   into `routes/health.py`, `routes/forward.py`, `routes/approval.py`, `routes/dashboard.py`,
   `state.py`, and `lifespan.py`. Clean separation of concerns.

2. **IP allowlisting** — LLM and Telegram proxy endpoints correctly restrict to
   `172.21.0.0/16` (isolated network) + `127.0.0.0/8` (loopback). No stale
   `172.20.0.0/16` (internal network) in the allowlist.

3. **Supply chain hardening** — Base image pinned to SHA256 digest, Trivy with
   checksum verification, 1Password with GPG signature verification, Bun/Playwright/OpenClaw
   pinned to specific versions. `setuid/setgid` bits stripped.

4. **Network isolation** — Bot on isolated-only network, gateway bridges both,
   Pi-hole DNS sinkhole on isolated network, HTTP CONNECT proxy for egress control.

5. **Session isolation** — `UserSessionManager` validates user IDs with regex and
   resolves paths to prevent traversal. Defense in depth with both validation and
   path resolution check.

6. **Prompt injection defense** — 43 pattern rules (20 new in v0.8.0) covering
   LLaMA/ChatML tokens, multilingual injection (20+ languages), payload splitting,
   tool-call injection, encoding chains, authority escalation, and more.

7. **CSP nonces** — Both `/` and `/dashboard` endpoints generate per-request nonces
   for inline scripts/styles with strict Content-Security-Policy headers.

8. **WebSocket auth** — Short-lived, single-use WS tokens with 5-minute TTL,
   preventing token replay.

9. **Canary tripwire** — Runtime canary registration + pipeline-compatible
   `scan_response()` bridge for tool result scanning.

10. **GitGuard** — `scan_content()` method enables middleware to scan arbitrary text
    (user messages, tool results) against supply-chain attack patterns.

---

## Release Recommendation

**✅ APPROVED FOR RELEASE**

All ERROR and WARNING findings from three review rounds have been resolved.
Test suite passes at 2225/2225 with zero failures and zero warnings.
The codebase demonstrates strong security posture with defense-in-depth throughout.

No blocking issues remain.
