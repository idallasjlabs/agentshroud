# Blue Team Security Assessment — AgentShroud v0.8.0 Round 2

**Date:** 2026-03-05  
**Branch:** `feat/v0.8.0-enforcement-hardening`  
**Assessor:** AgentShroud Bot (automated blue team)  
**Scope:** Fresh clean-slate assessment after Round 1 remediation  

---

## Executive Summary

Round 2 assessment finds the codebase significantly improved after Round 1 fixes.
The major issues from Round 1 (hardcoded owner IDs, python-jose CVEs, Pi-hole auth
token in query strings, missing IP allowlists, missing CSP) are all properly
remediated. However, this fresh assessment uncovered **1 CRITICAL**, **2 HIGH**,
**3 MEDIUM**, and **3 LOW** new findings.

| Severity | Count | Status |
|----------|-------|--------|
| CRITICAL | 1     | ⚠️ Must Fix |
| HIGH     | 2     | ⚠️ Should Fix |
| MEDIUM   | 3     | ℹ️ Fix Soon |
| LOW      | 3     | ℹ️ Informational |

---

## CRITICAL Findings

### R2-C1: RBAC Management Endpoints Missing Authentication

**Severity:** CRITICAL  
**Location:** `gateway/ingest_api/main.py` lines 1833–1950  
**Endpoints affected:**
- `GET /manage/rbac/users` (line 1833)
- `PUT /manage/rbac/users/{target_user_id}/role` (line 1871)
- `GET /manage/rbac/users/{user_id}/permissions` (line 1904)
- `GET /manage/rbac/me` (line 1932)

**Issue:** All four RBAC management endpoints lack the `auth: AuthRequired` dependency
that protects every other management endpoint. They rely solely on a client-supplied
`X-User-ID` header for identity — trivially spoofable.

**Impact:** An unauthenticated attacker with network access to the gateway can:
1. Enumerate all users and their roles (`GET /manage/rbac/users`)
2. Escalate any user to OWNER by setting `X-User-ID` to the owner's ID and calling
   `PUT /manage/rbac/users/{target}/role?role=owner`
3. Read permissions of any user

**Proof of concept:**
```bash
curl -H "X-User-ID: 8096968754" \
  http://127.0.0.1:8080/manage/rbac/users
```

**Fix:** Add `auth: AuthRequired` to all four endpoint signatures.

---

## HIGH Findings

### R2-H1: 1Password CLI Download Without Checksum Verification (Bot Dockerfile)

**Severity:** HIGH  
**Location:** `docker/Dockerfile.agentshroud` lines ~34-39

**Issue:** The 1Password CLI binary is downloaded via `curl` and installed without
any GPG signature or SHA256 checksum verification. Unlike the gateway Dockerfile
which installs 1Password via the signed apt repository, the bot Dockerfile
downloads a raw zip file:

```dockerfile
RUN ARCH=$(dpkg --print-architecture) && \
    curl -L -o /tmp/op.zip "https://cache.agilebits.com/dist/1P/op2/pkg/v2.32.0/op_linux_${ARCH}_v2.32.0.zip" && \
    unzip -q /tmp/op.zip -d /tmp/ && \
    mv /tmp/op /usr/local/bin/op && ...
```

**Impact:** A supply chain attacker who compromises the CDN or performs MITM
could inject a malicious binary that has access to all 1Password secrets.

**Fix:** Verify the GPG signature (`op.sig`) against AgileBits' public key, or
add SHA256 checksum verification for both architectures.

### R2-H2: Bot Dockerfile Missing setuid/setgid Bit Stripping (CIS 4.8)

**Severity:** HIGH  
**Location:** `docker/Dockerfile.agentshroud`

**Issue:** The gateway Dockerfile correctly strips setuid/setgid bits before
switching to non-root user:
```dockerfile
RUN find / -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true
```

The bot Dockerfile does NOT have this step. Any setuid binary in the base image
or installed packages (e.g., `gosu`, `su`, `mount`) could be exploited for
privilege escalation within the container.

**Fix:** Add the same `find / -perm /6000 ...` step before `USER node`.

---

## MEDIUM Findings

### R2-M1: Missing `aiohttp` in `requirements.txt`

**Severity:** MEDIUM  
**Location:** `gateway/requirements.txt`, `gateway/ingest_api/main.py` lines 1978, 2029

**Issue:** The Pi-hole DNS management endpoints (`/manage/dns`, `/manage/dns/blocklist`)
use `import aiohttp` at runtime, but `aiohttp` is not listed in `requirements.txt`.
This means:
1. Fresh installs will fail at runtime when these endpoints are called
2. The dependency is implicitly satisfied in Docker by another package pulling it in,
   but this is fragile

**Fix:** Add `aiohttp>=3.9.0,<4.0.0` to `requirements.txt`.

### R2-M2: WebSocket Endpoints in `web/api.py` Use Full Auth Token (Not Scoped)

**Severity:** MEDIUM  
**Location:** `gateway/web/api.py` lines 771-825 (`ws_logs`, `ws_updates`)

**Issue:** The `/api/ws/logs` and `/api/ws/updates` WebSocket endpoints accept the
full gateway auth token as a query parameter. Unlike the dashboard's `/ws/activity`
endpoint which uses scoped single-use WS tokens (`ws_*` prefix), these endpoints
directly compare against the master `config.auth_token`.

WebSocket tokens in query parameters appear in server logs, browser history, and
referrer headers. Using the full auth token here means token exposure from WS
connection logs could compromise all API authentication.

The dashboard correctly implemented scoped WS tokens (per Round 1 fix), but the
management API WebSocket endpoints were not updated to match.

**Fix:** Migrate `/api/ws/logs` and `/api/ws/updates` to use the same scoped
WS token pattern as `/ws/activity`.

### R2-M3: Trivy Downloads Without Checksum Verification (Both Dockerfiles)

**Severity:** MEDIUM  
**Location:** `gateway/Dockerfile` line 50, `docker/Dockerfile.agentshroud` line 27

**Issue:** Both Dockerfiles download the Trivy `.deb` package via curl without
SHA256 checksum verification:
```dockerfile
curl -sSfL -o /tmp/trivy.deb "https://github.com/.../trivy_${TRIVY_VERSION}_Linux-${ARCH}.deb"
dpkg -i /tmp/trivy.deb
```

While the version is pinned (good), there's no integrity check on the downloaded
binary. A GitHub CDN compromise or MITM could inject a malicious scanner binary.

**Fix:** Add SHA256 checksum verification for both architectures.

---

## LOW Findings

### R2-L1: No Global Security Headers Middleware for API Responses

**Severity:** LOW  
**Location:** `gateway/ingest_api/main.py`

**Issue:** Security headers (`X-Content-Type-Options`, `X-Frame-Options`,
`Cache-Control: no-store`) are only set on the dashboard HTML response. API
responses lack these headers. While the gateway binds to localhost only, adding
basic security headers to all responses is defense-in-depth best practice.

### R2-L2: WebSocket Connection Leak in `web/api.py`

**Severity:** LOW  
**Location:** `gateway/web/api.py` lines 767-799

**Issue:** The `active_websockets` list in `ws_logs` only cleans up on
`WebSocketDisconnect`. If the connection fails with a different exception
(e.g., `ConnectionResetError`), the stale WebSocket reference remains in the
list indefinitely, causing a memory leak and potential errors when iterating.

**Fix:** Use a `finally` block for cleanup.

### R2-L3: OCI Image Version Labels Outdated

**Severity:** LOW  
**Location:** `gateway/Dockerfile` (label says 0.7.0), `docker/Dockerfile.agentshroud` (label says 0.2.0)

**Issue:** The `org.opencontainers.image.version` labels are outdated —
gateway says "0.7.0" and bot says "0.2.0" while the actual version is 0.8.0.
This causes confusion when inspecting running containers.

---

## Verification of Round 1 Fixes

All Round 1 critical/high/medium/low findings were verified as properly fixed:

| R1 ID | Finding | Status |
|-------|---------|--------|
| C1 | Hardcoded owner Telegram ID in middleware | ✅ Fixed — resolved dynamically via RBACConfig |
| C2 | Hardcoded owner ID in session_manager | ✅ Fixed — loaded from RBACConfig |
| H1 | python-jose CVE dependency | ✅ Fixed — removed from requirements.txt |
| H2 | Pi-hole auth token in URL query string | ✅ Fixed — uses X-Pi-hole-Auth header |
| H3 | No IP allowlist on LLM proxy | ✅ Fixed — 172.21.0.0/16 + 127.0.0.0/8 only |
| H4 | No bot token validation on Telegram proxy | ✅ Fixed — hmac.compare_digest check |
| M1 | No CSP on dashboard | ✅ Fixed — nonce-based CSP implemented |
| M2 | WebSocket full token exposure (dashboard) | ✅ Fixed — scoped single-use ws_ tokens |
| M3 | Trivy version not pinned | ✅ Fixed — pinned to 0.58.2 |
| M4 | Docker base images not pinned | ✅ Fixed — SHA256 digests used |
| L1-L4 | Various low severity | ✅ All fixed |

---

## Recommendations

1. **Immediate (CRITICAL):** Add `auth: AuthRequired` to all RBAC endpoints
2. **Before release (HIGH):** Add checksum verification for 1Password CLI download; add setuid stripping to bot Dockerfile
3. **Soon (MEDIUM):** Add aiohttp to requirements.txt; migrate management WS endpoints to scoped tokens; add Trivy checksums
4. **Backlog (LOW):** Add global security headers middleware; fix WS cleanup; update OCI labels
