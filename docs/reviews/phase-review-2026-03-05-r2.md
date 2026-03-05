# AgentShroud Phase Review — 2026-03-05 (Round 2)

**Reviewer:** AgentShroud Bot (Claude Code)
**Branch:** `feat/v0.8.0-enforcement-hardening`
**Scope:** Full diff review `origin/main..HEAD` — v0.8.0 "Watchtower" enforcement hardening (round 2)
**Prior Review:** `docs/reviews/phase-review-2026-03-05.md` (all E1/E2 errors + W1/W2 warnings fixed)
**Files Changed:** 394+ files across gateway, docker, scripts, tests, docs

---

## 1. Prior Review Verification

| ID | Finding | Status |
|----|---------|--------|
| E1 | YAML indentation in `docker-compose.pi.yml` | ✅ Fixed (commit 2e5fa49) |
| E2 | YAML indentation in `docker-compose.trillian.yml` | ✅ Fixed (commit 2e5fa49) |
| W1 | `if True:` anti-pattern in test_main_endpoints.py | ✅ Fixed (commit 2e5fa49) |
| W2 | Stale compose snapshot file | ✅ Fixed (deleted, commit 2e5fa49) |
| W3 | Empty `test_egress_filter.py` | ✅ Fixed — 300 lines of comprehensive tests added |

**All prior findings addressed.** W3 (originally deferred) was also resolved with a full test suite.

---

## 2. New Blue Team Changes Since Round 1

The blue team added significant hardening in commits after 2e5fa49:

| Change | Description |
|--------|-------------|
| **Route refactoring** | Approval, dashboard, health, and forward routes extracted to `routes/` package |
| **Scoped WS tokens** | Dashboard WS tokens are now short-lived (5min), single-use, prefixed `ws_` — no longer leak master auth token |
| **CSP nonce injection** | Dashboard HTML uses per-request nonce for script/style tags instead of `unsafe-inline` |
| **Security headers** | X-Content-Type-Options, X-Frame-Options, Referrer-Policy added to dashboard |
| **Bot token validation** | Telegram proxy validates bot token matches configured secret (M6) |
| **Pi-hole auth via header** | Auth sent via `X-Pi-hole-Auth` header instead of query string (M4) |
| **LLM API reverse proxy** | New `/v1/{path}` endpoint with IP allowlist for Docker network isolation (M5) |
| **Docker image pinning** | All base images pinned to SHA256 digests (M8) — node, python, pihole |
| **Trivy pinned** | Trivy scanner installed via versioned .deb instead of curl-pipe-bash (M7) |
| **Package pinning** | bun, openclaw, playwright pinned to specific versions |
| **Session path traversal** | `_validate_user_id()` + resolved path check in session_manager |
| **Error message sanitization** | Error responses no longer leak internal exception details |

---

## 3. Round 2 Findings

### 🔴 ERRORS (must fix)

#### E1: Tailscale sidecar on internal-only network cannot reach control plane

**File:** `docker/docker-compose.yml`, Tailscale service definition
**Issue:** The Tailscale container is assigned only to `agentshroud-isolated` network, which is `internal: true` (no external connectivity). Tailscale needs to reach its coordination server (`controlplane.tailscale.com`) to authenticate and establish mesh connections. On an internal-only Docker network, this is impossible — the sidecar will fail at startup.

**Fix:** Add `agentshroud-internal` network to the Tailscale service so it can reach external endpoints, while keeping `agentshroud-isolated` for mesh advertisement.

```yaml
networks:
  - agentshroud-internal   # External access for control plane
  - agentshroud-isolated   # Mesh route advertisement
```

---

### 🟡 WARNINGS (should fix)

#### W1: Duplicate `import time` in `dashboard.py`

**File:** `gateway/ingest_api/routes/dashboard.py`, lines 15 and 17
**Issue:** `import time` appears twice in the import block.

```python
import time      # line 15
import logging
import time      # line 17 — duplicate
```

#### W2: Redundant function-level `import threading` in `lifespan.py`

**File:** `gateway/ingest_api/lifespan.py`, line 66
**Issue:** `import threading` at line 66 inside a function, but `threading` is already imported at module level (line 8). Redundant.

#### W3: Redundant function-level `import fnmatch` in `main.py`

**File:** `gateway/ingest_api/main.py`, line 111
**Issue:** `import fnmatch` inside `_is_imessage_recipient_allowed()`, but `fnmatch` is already imported at module level (line 19). Redundant.

#### W4: Tailscale image not pinned to SHA256 digest

**File:** `docker/docker-compose.yml`, Tailscale service
**Issue:** `image: tailscale/tailscale:latest` is not pinned to a digest, inconsistent with the M8 fix that pinned all other images (node, python, pihole).

#### W5: Hardcoded owner ID fallback `'1234567890'` in `lifespan.py`

**File:** `gateway/ingest_api/lifespan.py`, line 239
**Issue:** `getattr(app_state.config, 'owner_user_id', '1234567890')` uses a bogus placeholder. The `webhook_receiver.py` was already fixed to use `RBACConfig().owner_user_id`. The lifespan should be consistent.

**Fix:** Use `RBACConfig().owner_user_id` as the fallback.

---

### 🟢 INFO (nice to have)

#### I1: Missing trailing newlines in route files

**Files:** `gateway/ingest_api/routes/approval.py`, `gateway/ingest_api/routes/dashboard.py`
**Issue:** Files do not end with a newline character. POSIX convention and many linters expect a trailing newline.

#### I2: Duplicated constants between `main.py` and `routes/forward.py`

**Files:** `gateway/ingest_api/main.py` lines 103-104, `gateway/ingest_api/routes/forward.py` lines 42-43
**Issue:** `_IMESSAGE_SERVER`, `_IMESSAGE_SEND_TOOL`, and `_is_imessage_recipient_allowed()` are defined in both files. After the route refactoring, the `main.py` versions appear to be dead code.

#### I3: `manage/dns/blocklist` reads pihole password inline

**File:** `gateway/ingest_api/main.py`, line 2033
**Issue:** The blocklist endpoint reads `/run/secrets/pihole_password` inline while the stats endpoint uses the new `_get_pihole_auth_token()` helper (line 1954). Inconsistent — the helper should be used in both places.

#### I4: `AppState` class missing dynamically-set attributes

**File:** `gateway/ingest_api/state.py`
**Issue:** Attributes `llm_proxy`, `observatory_mode`, `egress_approval_queue`, `forwarder`, `network_validator`, `encrypted_store`, `drift_detector`, `key_vault`, `alert_dispatcher` are all accessed via `getattr(app_state, ...)` but not declared in the `AppState` class. Adding `Optional[...]` type annotations would improve IDE support and documentation.

#### I5: Inline import on hot path in LLM proxy

**File:** `gateway/ingest_api/main.py`, line 2128
**Issue:** `from starlette.responses import StreamingResponse` is imported inside the `llm_api_proxy()` handler on every streaming response. Moving to top-level would be cleaner.

---

## 4. Security Analysis

### 4a. Blue Team Fixes — ✅ EXCELLENT

The blue team addressed all significant security concerns:

- **M4 (Pi-hole auth in URL):** Fixed — auth now via `X-Pi-hole-Auth` header
- **M5 (LLM proxy IP allowlist):** New — restricts to Docker network `172.21.0.0/16` + loopback
- **M6 (Telegram bot token validation):** New — validates token matches configured secret
- **M7 (Trivy curl|bash):** Fixed — pinned version .deb install
- **M8 (Image pinning):** Fixed — SHA256 digests for base images (except Tailscale)
- **L4 (CSP nonce):** New — per-request nonce replaces `unsafe-inline`
- **L5 (Scoped WS tokens):** New — 5-minute single-use tokens, no master token leak
- **H5 (Error sanitization):** Fixed — error responses no longer include `str(e)`
- **Session path traversal:** New — `_validate_user_id()` with regex + resolved path check
- **Dead code removal:** Removed unreachable `_stats` dict in `webhook_receiver.py`

### 4b. Remaining Risk: Tailscale Networking (E1)

The Tailscale sidecar cannot function on an internal-only network. This is a deployment blocker for the mTLS mesh feature, though it won't affect core gateway operation since Tailscale is opt-in.

### 4c. Test Coverage Improvements

- `test_egress_filter.py`: 300 lines, comprehensive enforce/monitor/IP/per-agent/URL parsing tests
- `test_security_fixes.py`: Updated to test scoped WS tokens (ws_ prefix)
- Mock patches updated for route refactoring (`lifespan.load_config`)

---

## 5. Summary

| Severity | Count | IDs |
|----------|:---:|-----|
| 🔴 Errors | 1 | E1 (Tailscale networking) |
| 🟡 Warnings | 5 | W1-W5 (duplicate imports, image pinning, hardcoded fallback) |
| 🟢 Info | 5 | I1-I5 (style, consistency) |

---

## 6. Verdict

**CONDITIONAL PASS.** The blue team hardening is thorough and well-executed. The critical security fixes (scoped WS tokens, CSP nonces, IP allowlists, image pinning, error sanitization, session path traversal) are all properly implemented.

The one error (E1: Tailscale on internal network) must be fixed — though it only affects the optional Tailscale mesh feature. Warnings are code hygiene items that should be cleaned up.

---

## 7. Fix Log

*(To be updated after fixes are applied)*
