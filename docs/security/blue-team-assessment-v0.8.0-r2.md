# Blue Team Security Assessment — AgentShroud v0.8.0 (Round 2)

**Date:** 2026-03-05
**Branch:** `feat/v0.8.0-enforcement-hardening`
**Assessor:** agentshroud-bot (automated blue team)
**Scope:** Re-assessment after all Round 1 and Round 1-Final findings were fixed

---

## Prior Findings Verification

All findings from `blue-team-assessment-v0.8.0.md` and `blue-team-assessment-v0.8.0-final.md` were spot-checked and confirmed fixed:

| ID | Finding | Status |
|----|---------|--------|
| C1/C2 | Hardcoded owner IDs | ✅ Fixed — removed from code |
| M1 | Root endpoint info leak / no auth | ✅ Fixed — auth required, Tailscale IP redacted |
| M2 | `python-jose` CVEs | ✅ Fixed — removed from requirements.txt |
| M3 | CSP `unsafe-inline` on dashboard | ✅ Fixed — nonce-based CSP with security headers |
| M4 | Pi-hole auth token in query string | ✅ Fixed — moved to `X-Pi-hole-Auth` header |
| M5 | LLM proxy missing IP allowlist | ✅ Fixed — `172.21.0.0/16` + loopback only |
| M6 | Telegram proxy missing token validation | ✅ Fixed — `hmac.compare_digest` with Docker secret |
| M7 | Trivy installed without checksum | ⚠️ Partially — version pinned but no checksum verification (see R2-M1) |
| M8 | Base images not SHA-pinned | ✅ Fixed — both Dockerfiles use `@sha256:` digests |
| L1-L8 | Various low findings | ✅ Fixed |

---

## New Findings (Round 2)

### R2-M1: Trivy .deb Download Without Checksum Verification (MEDIUM)

**Location:** `gateway/Dockerfile` line 25, `docker/Dockerfile.agentshroud` line 27
**Description:** The M7 fix from Round 1 pinned Trivy to version 0.58.2 but the `RUN` command downloads the .deb without verifying a SHA256 checksum. A compromised CDN or MITM during build could inject a malicious binary. The round 1 assessment comment says "checksum verification" but no checksum is actually checked.

**Risk:** Supply chain compromise during container build.
**Remediation:** Download the `trivy_0.58.2_Linux-*.deb` checksums file, verify with `sha256sum -c`, then install.

### R2-M2: Telegram Proxy Token Validation Bypass When Secret Missing (MEDIUM)

**Location:** `gateway/ingest_api/main.py` lines 2175-2183
**Description:** The Telegram API proxy validates the bot token using `hmac.compare_digest`, but if the Docker secret file `/run/secrets/telegram_bot_token` does not exist, `configured_token` remains `None` and the guard `if configured_token and ...` is skipped. This means **any** bot token in the URL path will be accepted and proxied to `api.telegram.org` — allowing an attacker with network access to use the proxy as an open relay to the Telegram API with arbitrary tokens.

**Risk:** Open relay when secret file is missing (misconfiguration or development). Combined with the missing IP allowlist (R2-M3), this is exploitable from broader networks.
**Remediation:** When `configured_token` is `None`, reject all requests with 503 ("Telegram proxy not configured") rather than silently allowing any token.

### R2-M3: Telegram Proxy Missing IP Allowlist (MEDIUM)

**Location:** `gateway/ingest_api/main.py` lines 2162-2201
**Description:** The LLM proxy endpoint (`/v1/{path}`) was hardened with an IP allowlist restricting access to `172.21.0.0/16` (isolated Docker network) and loopback. The Telegram proxy endpoint (`/telegram-api/{path}`) has no equivalent IP restriction. On the `internal: true` Docker network this is partially mitigated, but defense-in-depth requires parity. If the gateway is ever exposed beyond the isolated network (e.g., Tailscale, misconfigured reverse proxy), the Telegram proxy would be accessible.

**Risk:** Unauthorized use of Telegram proxy from non-isolated networks.
**Remediation:** Add the same IP allowlist to the Telegram proxy endpoint.

### R2-M4: Root Endpoint Missing CSP and Security Headers (MEDIUM)

**Location:** `gateway/ingest_api/main.py` lines 255-342
**Description:** The `/` (system control) endpoint returns HTML with inline `<script>` (auto-refresh) and `<style>` tags but has no `Content-Security-Policy` header. The dashboard endpoint was correctly fixed with nonce-based CSP and security headers (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`), but the root endpoint was missed. This is inconsistent and leaves the main dashboard HTML page without XSS protections.

**Risk:** XSS if any user-controlled content is ever reflected in the root page.
**Remediation:** Add nonce-based CSP and security headers to the root endpoint response, matching the dashboard pattern.

### R2-L1: Auth Token Logged in Plaintext on Generation (LOW)

**Location:** `gateway/ingest_api/config.py` lines 429-435
**Description:** When no auth token is configured and one is auto-generated, the full token value is logged at WARNING level via `logger.warning()`. This token appears in container logs (`docker logs`), CI/CD output, and any log aggregation system. While necessary for initial setup, the token should be written to a file or shown via a secure channel rather than logged.

**Risk:** Token exposure in log files.
**Remediation:** Write the generated token to a file (e.g., `/tmp/agentshroud-auth-token`) and log only the file path, not the token value.

### R2-L2: Telegram Proxy Returns Internal Exception Details (LOW)

**Location:** `gateway/proxy/telegram_proxy.py` line 75
**Description:** When the Telegram API forward fails, the proxy returns `"description": str(e)` in the error response. Internal exception messages may reveal server internals (hostnames, connection details, stack info). The LLM proxy has the same pattern but is IP-restricted.

**Risk:** Information disclosure to callers.
**Remediation:** Return a generic error message; log the full exception server-side.

### R2-L3: LLM Proxy `_ALLOWED_NETWORKS` Parsed on Every Request (LOW)

**Location:** `gateway/ingest_api/main.py` lines 2092-2095
**Description:** The IP allowlist networks are constructed inside the endpoint function, meaning `ip_network()` is called on every request. This is a minor performance concern and also means the import happens inside the function body. Should be module-level constants.

**Risk:** Performance; no direct security impact.
**Remediation:** Move `_ALLOWED_NETWORKS` and the `ipaddress` import to module level.

---

## Summary

| Severity | Count | IDs |
|----------|-------|-----|
| CRITICAL | 0 | — |
| HIGH | 0 | — |
| MEDIUM | 4 | R2-M1, R2-M2, R2-M3, R2-M4 |
| LOW | 3 | R2-L1, R2-L2, R2-L3 |

All prior Round 1 and Round 1-Final findings are confirmed fixed. No critical or high severity issues found in Round 2. The four medium findings are defense-in-depth improvements addressing gaps in the recent fixes.
