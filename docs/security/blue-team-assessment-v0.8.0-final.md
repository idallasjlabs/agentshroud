# AgentShroud v0.8.0 — Blue Team Security Assessment (Final)

**Date:** 2026-03-05
**Branch:** `feat/v0.8.0-enforcement-hardening`
**Assessor:** AgentShroud AI (automated blue team assessment)

---

## Prior Assessment (v0.8.0) — Status

| Finding | Severity | Status | Notes |
|---------|----------|--------|-------|
| C1: Hardcoded owner ID in middleware.py | CRITICAL | ✅ FIXED | Now uses `RBACConfig().owner_user_id` |
| C2: Hardcoded owner ID in webhook_receiver.py | CRITICAL | ✅ FIXED | Now uses `RBACConfig().owner_user_id` |
| C3: Bot token prefixes in chat history | CRITICAL | ⚠️ MANUAL | Requires Isaiah to rotate via @BotFather |
| H1: Telegram proxy middleware_manager None | HIGH | ✅ FIXED | Wired via `app_state` in request handler |
| H2: FileSandbox regex too broad | HIGH | ✅ FIXED | Regex removed; sandbox uses path matching |
| H3: Gateway password in config file | HIGH | ✅ FIXED | Uses `GATEWAY_AUTH_TOKEN_FILE` env var |
| M1: No rate limiting on security endpoints | MEDIUM | ⚠️ OPEN | Not yet implemented |
| M2: subprocess no resource limits | MEDIUM | ⚠️ OPEN | Timeout set but no cgroup limits |
| M3: Pi-hole password in secrets file | MEDIUM | ⚠️ OPEN | Expected for Docker secrets pattern |
| L1-L3 | LOW | ⚠️ OPEN | Informational, acceptable risk |

---

## New Findings

### CRITICAL — Must Fix Before Release

#### C4: Root Endpoint `/` Exposes System Metrics Without Authentication
**File:** `gateway/ingest_api/main.py:255`
**Description:** The root `/` endpoint is unauthenticated and returns an HTML dashboard showing:
- System uptime, version
- Ledger entry count, pending approval count
- PII engine mode
- Hardcoded Tailscale IP address (`100.90.175.83:8080`)
- Links to all management endpoints

**Risk:** Information disclosure enables reconnaissance. Attacker learns system posture, uptime, and network topology without credentials.
**Fix:** Add `auth: AuthRequired` dependency or redirect to a minimal landing page.

#### C5: `/status` Endpoint Exposes Security Posture Without Authentication
**File:** `gateway/ingest_api/routes/health.py:14`
**Description:** The `/status` health check returns:
- Observatory mode (enforce/monitor), module counts, canary status
- Egress approval counts, ledger stats
- Security summary with `modules_active`, `modules_enforcing` counts

**Risk:** Unauthenticated attacker learns whether security is in enforce or monitor mode, module counts, and blocking stats — enough to plan targeted attacks.
**Fix:** Split into minimal healthcheck (returns only `{"status":"healthy"}`) and detailed status behind auth.

### HIGH — Should Fix Before Release

#### H4: Docker Network `agentshroud-isolated` Not Actually Isolated
**File:** `docker/docker-compose.yml:253`
**Description:** The `agentshroud-isolated` network is configured with `internal: false`. This means containers on this network CAN reach the internet directly, bypassing the HTTP CONNECT proxy on the gateway. The bot's `HTTP_PROXY` env vars provide soft enforcement only — any process not respecting proxy env vars (e.g., low-level socket calls, DNS over non-standard ports) can bypass the proxy.
**Risk:** Proxy bypass allows unmonitored egress from the bot container.
**Fix:** Set `internal: true` on the isolated network. The gateway container on both networks acts as the sole egress path.

#### H5: `/dashboard/ws-token` Returns Master Auth Token to Browser
**File:** `gateway/ingest_api/routes/dashboard.py:157`
**Description:** The ws-token endpoint returns `app_state.config.auth_token` (the gateway master auth token) to authenticated browser sessions. If XSS occurs (despite CSP), the master token is exposed.
**Risk:** XSS → master token theft → full gateway control.
**Fix:** Generate a separate, short-lived WebSocket-only token (e.g., JWT with 5min expiry and `ws` audience) instead of returning the master auth token.

#### H6: Session Manager Path Traversal via Crafted User ID
**File:** `gateway/security/session_manager.py:148`
**Description:** `get_or_create_session()` uses `user_id` directly in path construction: `self.base_workspace / "users" / user_id`. No validation prevents path traversal characters (`../`, `/`, null bytes). While Telegram user IDs are numeric, the code accepts arbitrary strings.
**Risk:** A crafted user_id like `../../etc` could create directories outside the sandbox.
**Fix:** Validate user_id is alphanumeric or numeric only; resolve path and verify it's within base_workspace.

#### H7: Error Messages Disclose Internal Details
**Files:** Multiple endpoints in `gateway/ingest_api/main.py`
**Description:** Several endpoints return raw exception messages via `str(e)` in error responses:
- Lines 1866, 1927, 1949: `f"Error listing users: {str(e)}"`
- Lines 1991, 2065: `f"Error getting DNS stats: {str(e)}"`
- Lines 1799, 1821: Killswitch verification/status errors
**Risk:** Internal exception details (file paths, module names, stack info) disclosed to API consumers.
**Fix:** Return generic error messages; log details server-side only.

### MEDIUM — Fix Soon

#### M4: Pi-hole Auth Token Passed in URL Query String
**File:** `gateway/ingest_api/main.py:2031`
**Description:** The Pi-hole API token is appended as `&auth=<token>` in the URL query string. This token appears in Pi-hole access logs, browser history, and proxy logs.
**Risk:** Credential exposure in logs.
**Fix:** Use POST body or HTTP headers for Pi-hole authentication.

#### M5: LLM Proxy Endpoint `/v1/{path}` Has No Authentication
**File:** `gateway/ingest_api/main.py:2074`
**Description:** The Anthropic API proxy endpoint has no auth. While the bot needs unauthenticated access from the isolated network, any container on the Docker network can send arbitrary prompts through the Anthropic API (consuming credits and potentially exfiltrating data via prompt).
**Risk:** Unauthorized API usage from compromised containers on the network.
**Fix:** Add IP-based allowlist (only accept from bot container IP) or use a lightweight shared secret.

#### M6: Telegram API Proxy Passes Raw Bot Token Without Validation
**File:** `gateway/ingest_api/main.py:2138`
**Description:** The `/telegram-api/{path}` endpoint extracts `bot_token` from the URL path and forwards it directly to Telegram's API. There's no validation that the token matches the configured bot token. Any valid bot token passed through this endpoint will be proxied.
**Risk:** If an attacker obtains any Telegram bot token, they can use the gateway as an open proxy to Telegram's API.
**Fix:** Validate that the extracted bot token matches the configured token (loaded from Docker secret).

#### M7: Dockerfile Uses `curl | sh` for Trivy Installation
**Files:** `docker/Dockerfile.agentshroud:15`, `gateway/Dockerfile:41`
**Description:** Both Dockerfiles install Trivy via `curl -sfL ... | sh`. This is a supply chain risk — if the script or domain is compromised, arbitrary code executes during build.
**Fix:** Pin Trivy to a specific version and verify checksum, or use the official Trivy APT repository.

#### M8: Unpinned Base Images and `@latest` Tags
**File:** `docker/Dockerfile.agentshroud`
**Description:** Uses `openclaw@latest`, `bun@latest`, `playwright@latest`, `pihole/pihole:latest`. Unpinned versions mean builds are not reproducible and vulnerable to supply chain attacks.
**Risk:** A compromised upstream package could be pulled into production.
**Fix:** Pin all dependencies to specific versions with integrity hashes where possible.

### LOW — Informational

#### L4: CSP Allows `unsafe-inline` for Scripts and Styles
**File:** `gateway/ingest_api/routes/dashboard.py:120`
**Description:** Dashboard CSP includes `script-src 'unsafe-inline'` and `style-src 'unsafe-inline'`. This weakens XSS protection.
**Fix:** Use nonce-based CSP for scripts; extract styles to external file.

#### L5: WebSocket Token in Query String
**File:** `gateway/ingest_api/routes/approval.py:107`, `dashboard.py:170`
**Description:** WebSocket auth tokens are passed as query parameters (`?token=<token>`). These may appear in server access logs and referrer headers.
**Fix:** Use a ticket/nonce pattern: exchange a short-lived ticket for WS auth during the handshake.

#### L6: Auto-Refresh via JavaScript on Root Page
**File:** `gateway/ingest_api/main.py:335`
**Description:** Root page auto-refreshes every 30 seconds via `setTimeout`. Combined with no auth (C4), this means an open browser tab generates continuous unauthenticated requests.
**Fix:** Remove auto-refresh from unauthenticated pages, or add auth.

#### L7: Dead Code After Return in webhook_receiver.py
**File:** `gateway/proxy/webhook_receiver.py:80-86`
**Description:** There's a duplicate `self._stats` initialization block after `return False` in `_can_create_directory`. This code is unreachable.
**Fix:** Remove the dead code block.

#### L8: `python-jose` Dependency Has Known CVEs
**File:** `gateway/requirements.txt:24`
**Description:** `python-jose[cryptography]>=3.3.0` has known vulnerabilities (CVE-2024-33663, CVE-2024-33664). It appears unused in production code (may be test-only).
**Fix:** Remove if unused, or replace with `PyJWT` or `joserfc`.

---

## Summary

| Severity | Count | Auto-fixable | Manual |
|----------|-------|-------------|--------|
| CRITICAL | 2 | 2 | 0 |
| HIGH | 4 | 4 | 0 |
| MEDIUM | 5 | 3 | 2 (M7, M8 = build changes) |
| LOW | 5 | 3 | 2 (L4, L5 = design changes) |

---

## Fixes Applied

_Status will be updated after code fixes are applied._

| Finding | Fix Status | Details |
|---------|-----------|---------|
| C4 | ✅ FIXED | Added `auth: AuthRequired` to root endpoint; redacted Tailscale IP |
| C5 | ✅ FIXED | Split into minimal `/status` (unauth) and `/status/detail` (auth) |
| H4 | ✅ FIXED | Set `agentshroud-isolated` network to `internal: true` |
| H5 | ✅ FIXED | WS token endpoint now returns scoped, single-use, 5-min tokens |
| H6 | ✅ FIXED | Added alphanumeric validation + path containment check on user_id |
| H7 | ✅ FIXED | Replaced `str(e)` in error responses with generic messages |
| L7 | ✅ FIXED | Removed dead code block in webhook_receiver.py |

### Test Results
- **2193 passed**, 1 warning, 0 failures
- All existing tests continue to pass
- WS token test updated to validate new scoped token behavior
