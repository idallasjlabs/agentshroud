# AgentShroud v0.8.0 — Blue Team Security Assessment
**Date:** 2026-03-05
**Assessor:** AgentShroud AI (self-assessment)

## Findings

### CRITICAL — Must Fix Before Release

#### C1: Hardcoded Owner User ID in middleware.py:94
```python
owner_user_id = "8096968754"
```
Should use `RBACConfig().owner_user_id` — RBAC is the single source of truth.
**File:** `gateway/ingest_api/middleware.py:94`

#### C2: Hardcoded Owner User ID in webhook_receiver.py:45
```python
owner_user_id = "8096968754"  # Isaiah - owner
```
Same fix — use RBACConfig.
**File:** `gateway/proxy/webhook_receiver.py:45`

#### C3: Bot Tokens Partially Exposed in Chat History
Production token prefix `8481143014:AAE5` and Marvin token prefix `8736289266:AAGV` were printed during debugging.
**Fix:** Rotate both tokens via @BotFather (manual — Isaiah only).

### HIGH — Should Fix

#### H1: Telegram Proxy middleware_manager Never Initialized
The `_telegram_proxy` in main.py has `middleware_manager=None`. This means:
- Inbound messages are NOT scanned by the security pipeline
- PII sanitization is NOT applied to proxied messages
- The entire security stack is bypassed for Telegram traffic
**Fix:** Wire `middleware_manager` during lifespan initialization.

#### H2: FileSandbox _extract_file_paths Regex Too Broad
Pattern `r'/[a-zA-Z0-9_./\-]+'` matches any string starting with `/`.
This causes false positive blocks on conversational messages containing paths.
**Fix:** Tighten regex to only match filesystem-operation contexts, not plain text.

#### H3: Gateway Password Still in auth.token
While `auth.password` was removed from config, `auth.token` still stores the password in plaintext in the config file. The env var approach should replace both.
**Impact:** Config file leaks gateway credentials if read by unauthorized process.

### MEDIUM — Recommended

#### M1: No Rate Limiting on Security Endpoints
`/manage/mode`, `/manage/egress/*`, `/approve/*` have no rate limiting.
An attacker with access could spam mode changes or approval decisions.
**Fix:** Add rate limiter middleware for management endpoints.

#### M2: subprocess Calls Use Lists (Good) but No Resource Limits
`subprocess.run` calls for 1Password (`timeout=90`) and SSH could consume resources.
**Fix:** Add `ulimit` or cgroup constraints in production.

#### M3: Pi-hole Web Password in Secrets File
Pi-hole admin password stored in plaintext file at `docker/secrets/pihole_password.txt`.
**Fix:** Rotate after initial setup, or generate at runtime.

### LOW — Informational

#### L1: State Dir is a Symlink
`/home/node/.openclaw` → `/home/node/.agentshroud` — extra trust boundary.
**Impact:** Minimal, but symlink attacks possible if filesystem permissions are weak.

#### L2: Browser Control Enabled
OpenClaw browser control is enabled. In a multi-user scenario this is a risk.
**Impact:** Low for single-operator model.

#### L3: Memory Index Not Built
`0 files indexed` — memory search won't work until rebuilt.
**Fix:** Run memory index rebuild.

## Summary
| Severity | Count | Fixed | Remaining |
|----------|-------|-------|-----------|
| Critical | 3 | 0 | 3 (2 code, 1 manual) |
| High | 3 | 0 | 3 |
| Medium | 3 | 0 | 3 |
| Low | 3 | 0 | 3 |

## Remediation Plan
1. Fix C1, C2 (hardcoded IDs) — code change
2. Fix H1 (middleware wiring) — code change
3. Fix H2 (regex) — code change
4. C3 (token rotation) — Isaiah manual step
5. H3, M1-M3 — lower priority, can be v0.8.1
