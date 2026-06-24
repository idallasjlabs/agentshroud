# AgentShroud Phase Review — 2026-03-05

**Reviewer:** AgentShroud Bot (Claude Code)
**Branch:** `feat/v0.8.0-enforcement-hardening`
**Scope:** Full diff review `origin/main..HEAD` — v0.8.0 "Watchtower" enforcement hardening
**Files Changed:** 394 files (insertions across gateway, docker, scripts, tests, docs)

---

## 1. Changes in This Diff (Summary)

| Category | Key Changes |
|----------|-------------|
| **Enforcement defaults** | DNS filter, egress monitor, subagent monitor, killswitch all flipped from `monitor` → `enforce` mode |
| **Pipeline expansion** | ContextGuard, OutputCanary, EnhancedToolResultSanitizer wired into SecurityPipeline |
| **PromptGuard v2** | 20 new prompt injection patterns (43 total): LLaMA tokens, payload splitting, JSON/YAML injection, tool-call injection, multi-model confusion, authority escalation, encoding chains, completion attacks, constitutional bypass, persona chaining, multilingual (JP/KR/AR/HI/IT/NL/PT), and more |
| **Canary tripwire bridge** | New `TripwireResponse` dataclass + `scan_response()` for pipeline compatibility; `register_canary()` for runtime registration |
| **GitGuard** | New `scan_content()` method for in-memory scanning (middleware use) |
| **Route refactoring** | `main.py` routes split into `routes/forward.py`, `routes/health.py`, `routes/approval.py` etc.; lifespan extracted to `lifespan.py` |
| **Observatory mode API** | New `GET/PUT /api/mode` endpoints with auto-revert timer |
| **Config expansion** | `SecurityConfig` gains `dns_filter`, `subagent_monitor`, `egress_monitor`, `killswitch` module configs |
| **Docker hardening** | Pi-hole no exposed ports, Tailscale mesh VPN sidecar, proxy vars for bot, subnet change 172.20→172.21 |
| **RBAC config** | Owner ID moved from hardcoded string to `RBACConfig` class |
| **Test suite** | 2 new test files (`test_all_modules_enforce.py`, `test_e2e_watchtower.py`), expanded observatory mode tests, 20 new prompt guard pattern tests |

---

## 2. Findings

### 🔴 ERRORS (must fix)

#### E1: YAML indentation error in `docker-compose.pi.yml`

**File:** `docker/docker-compose.pi.yml`, lines 28-34
**Issue:** Proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`, `TELEGRAM_API_BASE_URL`) are indented at 4 spaces instead of 6, making them siblings of the `environment:` key rather than children. Docker Compose will fail to parse this file.

```yaml
# WRONG (4-space indent — parsed as service-level keys, not env vars):
    - HTTP_PROXY=http://gateway:8181
# CORRECT (6-space indent — inside environment block):
      - HTTP_PROXY=http://gateway:8181
```

#### E2: YAML indentation error in `docker-compose.trillian.yml`

**File:** `docker/docker-compose.trillian.yml`, lines 28-34
**Issue:** Same as E1 — identical indentation error for proxy environment variables.

---

### 🟡 WARNINGS (should fix)

#### W1: `if True: # keep indentation` anti-pattern in tests

**File:** `gateway/tests/test_main_endpoints.py`, 2 occurrences
**Issue:** After refactoring mock patches from `gateway.ingest_api.main` to `gateway.ingest_api.routes.forward`, the inner `with patch(...)` block was replaced with `if True:  # keep indentation` to avoid re-indenting code. This is a code smell — the `if True:` block serves no purpose and confuses readers.

**Fix:** Remove the `if True:` and un-indent the block contents, or merge the two mock patches into a single `with` statement (which the outer block already does via `, \`).

#### W2: Stale compose snapshot committed to tree

**File:** `docker/docker-compose.yml-latest-20260228-2044` (227 lines)
**Issue:** This appears to be an auto-generated backup/snapshot of the compose file. It contains older configuration (commented-out `HTTP_PROXY`, `TELEGRAM_BOT_TOKEN_FILE` still present in bot container). Stale configuration files in the repo can mislead operators.

**Fix:** Delete this file or move to a `docker/snapshots/` directory if historical records are needed.

#### W3: Empty test file placeholder

**File:** `gateway/tests/test_egress_filter.py`
**Issue:** File contains only a copyright header, docstring, and `from __future__ import annotations` — no actual tests. The egress filter module exists and has production code, but has zero test coverage from this file.

**Fix:** Track as test debt; add at least basic instantiation and enforce-mode tests before v0.8.0 release.

---

### 🟢 INFO (nice to have)

#### I1: Pipeline encoding detector API change

**File:** `gateway/proxy/pipeline.py`, lines 425-440
**Issue:** The pipeline changed from `encoding_detector.detect_and_decode(text, source)` to `encoding_detector.analyze(text)`. The new API returns `.layers` and `.cleaned_text` instead of `.decoded_segments` and `.fully_decoded_text`. This is a clean API migration. No issues found, but if any code outside the pipeline still calls the old API names, it will break at runtime.

#### I2: f-string in logger call

**File:** `gateway/proxy/pipeline.py`, lines 442-444
**Issue:** Uses f-string in `logger.info()` instead of `%s` formatting. While functional, lazy formatting (`logger.info("... %d methods ...", len(...))`) avoids string interpolation when the log level is disabled.

#### I3: Owner ID still hardcoded (improved)

**File:** `gateway/security/rbac_config.py`, line 42
**Issue:** `owner_user_id: str = "8096968754"` is still a hardcoded default in the dataclass. Better than the previous inline hardcoding in `webhook_receiver.py`, but ideally should be loaded from config/env. This was flagged in the 2026-03-04 review and has been partially addressed — the RBAC class is now the single source of truth, which is a good improvement.

#### I4: Copyright headers added consistently

Multiple test files received copyright headers. Good consistency improvement.

---

## 3. Security Analysis

### 3a. Enforcement Mode Flip — ✅ EXCELLENT

All core security modules now default to `enforce`:
- DNSFilter: `monitor` → `enforce`
- EgressMonitor: `monitor` → `enforce`
- SubagentMonitor: `monitor` → `enforce`
- KillSwitch: `dry_run=True` → `dry_run=False`
- SecurityModuleConfig: default `mode="enforce"`

The test suite (`test_all_modules_enforce.py`) explicitly validates all these defaults. The global `AGENTSHROUD_MODE=monitor` override correctly downgrades all modules. This is the core objective of v0.8.0 and it's implemented correctly.

### 3b. ContextGuard Pipeline Integration — ✅ GOOD

ContextGuard runs as Step 0 (before PromptGuard), which is correct — session-level injection should be caught before pattern matching. Repetition attacks are logged but not blocked (correct — they trigger on legitimate structured output). The fail-closed error handling is proper: ContextGuard exceptions block the message rather than allowing it through.

### 3c. Observatory Mode API — ✅ GOOD with note

The `PUT /api/mode` endpoint with auto-revert is well-designed:
- Clamped revert window (1–480 minutes)
- CRITICAL-level logging for non-enforce modes
- Cancels previous revert task on re-call
- Auth-required

**Note:** The revert task runs in-process (`asyncio.create_task`). If the gateway process restarts while in monitor/observatory mode, the revert task is lost and the mode reverts to default (`enforce`) anyway — so this is safe by design.

### 3d. 20 New Prompt Injection Patterns — ✅ GOOD

The new patterns cover important attack vectors:
- LLM-specific token injection (LLaMA, ChatML)
- Multi-model confusion
- Tool call/result injection
- Extended multilingual coverage (7 new languages)
- Encoding chain and whitespace obfuscation

All 20 new patterns have corresponding unit tests in `test_prompt_guard.py`. Benign-message false-positive tests are included.

### 3e. Docker Hardening — ✅ GOOD (minus YAML bugs)

- Pi-hole no longer exposes ports (admin via gateway proxy only)
- DNS upstream changed from Cloudflare (1.1.1.1) to Google (8.8.8.8) — acceptable
- Tailscale VPN sidecar for encrypted inter-container communication
- Subnet renumbered 172.20→172.21 consistently
- Bot container gets `HTTP_PROXY`/`HTTPS_PROXY` for egress routing

---

## 4. Test Coverage Assessment

| Area | Coverage | Notes |
|------|----------|-------|
| Enforce mode defaults | ✅ Excellent | `test_all_modules_enforce.py` — comprehensive |
| E2E pipeline | ✅ Good | `test_e2e_watchtower.py` — 10 scenarios |
| Prompt guard patterns | ✅ Good | All 20 new patterns tested + benign checks |
| ContextGuard pipeline wiring | ✅ Good | 6 unit tests in `test_pipeline_unit.py` |
| Observatory mode | ✅ Good | GET/PUT tests, auto-revert, clamping, logging |
| Canary tripwire bridge | ✅ Good | 5 new tests for `scan_response()` |
| Egress filter | ❌ Empty | Placeholder file only |
| Docker compose parsing | ⚠️ Missing | No CI validation of YAML correctness |

---

## 5. Errors & Warnings Summary

| Severity | Count | IDs |
|----------|:---:|-----|
| 🔴 Errors | 2 | E1, E2 (YAML indentation) |
| 🟡 Warnings | 3 | W1, W2, W3 |
| 🟢 Info | 4 | I1-I4 |

---

## 6. Verdict

**CONDITIONAL PASS.** The v0.8.0 enforcement hardening is comprehensive and well-tested. The two YAML indentation errors (E1, E2) must be fixed before merge — they will break `docker compose up` on Pi and Trillian hosts. The warnings are non-blocking but should be addressed for code hygiene.

### Fix Status

| ID | Status | Notes |
|----|--------|-------|
| E1 | ✅ Fixed | YAML indentation corrected in pi.yml (commit 2e5fa49) |
| E2 | ✅ Fixed | YAML indentation corrected in trillian.yml (commit 2e5fa49) |
| W1 | ✅ Fixed | Removed `if True:` blocks in test_main_endpoints.py (commit 2e5fa49) |
| W2 | ✅ Fixed | Deleted docker-compose.yml-latest-20260228-2044 (commit 2e5fa49) |
| W3 | ⬜ Deferred | Test debt — track for post-release |

---

## 7. Post-Fix Verification

**Test run:** 2193 passed, 0 failed, 1 warning (39.73s)
**Commit:** `2e5fa49` — `fix: peer review findings v0.8.0`
**Pushed:** `feat/v0.8.0-enforcement-hardening`

All errors and actionable warnings resolved. Branch is ready for merge.
