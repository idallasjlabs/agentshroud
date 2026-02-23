# AgentShroud Phase Review — 2026-02-23

**Reviewer:** agentshroud-bot (automated security peer review)  
**Branches Reviewed:** 6 branches against `main`  
**Date:** 2026-02-23T14:25Z

---

## 1. Accomplishments This Phase

### p0/pipeline-wiring (4 commits)
- Wired core security pipeline into `main.py`: PromptGuard, TrustManager, EgressFilter, SecurityPipeline
- Added `psutil` dependency, test scaffolding for prompt guard
- Added ledger improvements and config changes
- **Files:** `main.py` (+31 lines), `config.py`, `ledger.py`, `models.py`, `test_prompt_guard.py`

### p1/middleware-modules (3 commits, builds on p0)
- Created `MiddlewareManager` class orchestrating 7 security modules: ContextGuard, MetadataGuard, LogSanitizer, EnvironmentGuard, GitGuard, FileSandbox, ResourceGuard
- Integrated middleware into the `/forward` endpoint with fail-closed error handling
- Made MCP proxy wrapper **fail-closed** (blocks tool calls when gateway unreachable)
- Wired LogSanitizer into Python logging handlers
- **Files:** `middleware.py` (210 lines, new), `main.py` (+94 lines), `mcp-proxy-wrapper.js` (updated), fail-closed patch

### p2/network-modules (3 commits)
- Integrated DNSFilter, NetworkValidator, EgressMonitor, BrowserSecurityGuard, OAuthSecurityValidator into `WebProxy`
- Added DNS check, browser reputation check, OAuth header flagging to request flow
- Added egress monitoring on response path
- 288-line integration test suite (`test_web_proxy_security.py`)
- **Files:** `web_proxy.py` (+123 lines), `test_web_proxy_security.py` (new, 288 lines)

### p3/infra-modules (0 commits)
- **No work done.** Branch is identical to `main`. No commits ahead.

### feature/web-control-center (2 commits)
- Full web dashboard at `/manage/` with 7 sub-pages: dashboard, approvals, modules, audit, SSH, collaborators, kill switch
- Static CSS, HTML template, FastAPI routes
- **Files:** `management.py` (+219 lines), `dashboard.html` (new), `agentshroud-dashboard.css` (new)

### feature/terminal-control-center (1 commit)
- Full terminal TUI dashboard using pure ANSI escape codes
- 7 screens: dashboard, approvals, kill switch, modules, log, SSH hosts, chat
- Gateway API integration with auth
- **Files:** `text_control_center.py` (+398 lines)

---

## 2. Security Value Audit

### ✅ Genuine Security Value

| Component | Verdict | Notes |
|-----------|---------|-------|
| **MCP Proxy Wrapper (fail-closed)** | ✅ **Real value** | Blocks tool calls when gateway unreachable. This is the correct posture for a security proxy. Major improvement from the original fail-open design. |
| **1Password op-proxy** | ✅ **Real value** | Keeps `OP_SERVICE_ACCOUNT_TOKEN` on gateway, not bot. Allowlist with glob patterns + path traversal rejection. Well-implemented credential isolation. |
| **Email/iMessage recipient allowlists** | ✅ **Real value** | Unknown recipients route to approval queue. Fail-closed when queue unavailable. Prevents unauthorized outbound communication. |
| **SecurityPipeline (prompt injection + PII + audit)** | ✅ **Real value** | Chains PromptGuard → PII sanitizer → EgressFilter → approval queue. Fail-closed on pipeline error. |
| **WebProxy SSRF blocking** | ✅ **Real value** | Hard blocks SSRF and denied domains before request proceeds. |
| **DNS Filter in WebProxy** | ✅ **Real value** | Fail-closed on DNS error. Blocks suspicious domains. |
| **Data Ledger audit trail** | ✅ **Real value** | Hash-chained tamper-evident logging. Records all forwards, SSH commands, security events. |

### ⚠️ Partial Value / Needs Hardening

| Component | Verdict | Notes |
|-----------|---------|-------|
| **MiddlewareManager** | ⚠️ **Fail-open on init** | Each guard is wrapped in try/except that sets it to `None`. If a guard fails to initialize, it's silently skipped during `process()` — e.g., `if self.context_guard:` simply bypasses the check. The final `except` block is fail-closed, but individual guard failures are **fail-open**. This is a significant gap. |
| **FileSandbox check in middleware** | ⚠️ **Naive string matching** | Checks for `/etc/`, `/var/`, `/root/` via `in` operator on message content. Trivially bypassed with encoding, path normalization, or simply not mentioning those paths. |
| **GitGuard in middleware** | ⚠️ **No-op** | The git guard block just logs "basic validation" and does nothing. Dead code placeholder. |
| **Browser security in WebProxy** | ⚠️ **Fail-closed is too aggressive** | Any exception in `check_url_reputation()` blocks the entire request. If the browser security module has a bug, all browser-UA traffic is blocked. |
| **WebProxy egress monitoring** | ⚠️ **Post-hoc only** | Egress monitor runs after response is received and doesn't block. Logging-only value — useful for forensics but not prevention. |

### 🚫 Security Theater

| Component | Verdict | Notes |
|-----------|---------|-------|
| **Web Control Center dashboard** | 🚫 **Theater** | Hardcoded values: "24/30 Active", "3 Online", "15 days uptime", "v1.2.3". No authentication on `/manage/` routes. Kill switch is `onclick="alert('Kill switch activated (demo)')"`. This provides zero security functionality and could mislead an operator into thinking they have operational visibility. |
| **Terminal TUI dashboard** | 🚫 **Theater** | Hardcoded log entries, hardcoded SSH host statuses, hardcoded stats (1,234 inbound, 12 blocked). Kill switch sends POST to non-existent `/kill` endpoint. `/modules` endpoint doesn't exist. Gives false impression of monitoring capability. |
| **p3/infra-modules branch** | 🚫 **Empty** | Zero commits. Branch exists but delivers nothing. |
| **Empty test files** | 🚫 **Theater** | `test_egress_filter.py` and `test_trust_manager.py` are 0-byte files. They inflate file counts in diffs but test nothing. |
| **OAuth security check** | 🚫 **Near-theater** | Simply flags any request that has an `Authorization` header with a low-severity finding. Every authenticated API call triggers this. No actual OAuth validation, token inspection, or scope checking. |

---

## 3. Remaining Work — Prioritized by Value

| Priority | Task | Why |
|----------|------|-----|
| **1** | **Fix MiddlewareManager fail-open on init** | If any guard fails to import/init, that entire security check is silently bypassed. Should fail-closed: if a critical guard can't initialize, the gateway should refuse to start (or at minimum block requests through that guard's path). |
| **2** | **Fix Python 3.10+ syntax** | All tests fail on Marvin (Python 3.9) due to `X \| None` union syntax in `ledger.py` and `config.py`. Use `Optional[X]` or add `from __future__ import annotations`. Zero test coverage until this is fixed. |
| **3** | **Implement actual FileSandbox path validation** | Current string-matching is trivially bypassed. Need proper path canonicalization and jail enforcement. |
| **4** | **Implement GitGuard logic** | Currently a no-op placeholder. Either implement or remove to avoid false sense of security. |
| **5** | **Add authentication to web dashboard** | `/manage/` routes have no auth. Anyone with network access can view (and eventually control) the gateway. |
| **6** | **Make dashboards read real data** | Both web and TUI dashboards show hardcoded fake data. Either wire to real APIs or remove to avoid misleading operators. |
| **7** | **Write actual tests for egress_filter and trust_manager** | Files exist but are empty. |
| **8** | **Implement p3/infra-modules** | Branch exists but has no work. DNS filter, network validator, etc. exist as code but aren't wired into infrastructure (Docker, CI, monitoring). |
| **9** | **Add integration tests that run against a live gateway** | Current test suite can't even import due to Python version issues. Need CI with correct Python version. |
| **10** | **Review browser security fail-closed aggressiveness** | A bug in `check_url_reputation()` blocks all browser traffic. Consider circuit-breaker pattern instead. |

---

## 4. Risks & Gaps

### Critical

1. **No working test suite.** All tests fail with `TypeError: unsupported operand type(s) for |` on Python 3.9. This means every security module is **untested in CI**. Any regression goes undetected.

2. **MiddlewareManager silent guard bypass.** If `ContextGuard` fails to import (e.g., missing dependency), the middleware silently skips context attack detection. An attacker who can cause an import error effectively disables a security layer.

3. **Dashboards show fake data.** If an operator relies on the web or TUI dashboard for situational awareness, they see fabricated metrics. This is worse than no dashboard — it creates false confidence.

### High

4. **No authentication on `/manage/` routes.** The web dashboard is served without any Bearer token or cookie check. All other sensitive endpoints require auth.

5. **FileSandbox path check is trivially bypassable.** Simple string `in` check on message content doesn't handle URL encoding, path traversal normalization, or indirect references.

6. **MCP proxy wrapper non-200 responses forward anyway.** Lines ~170: if gateway returns e.g., 500, the tool call is forwarded with just a stderr warning. Only 403 blocks. A gateway internal error results in unaudited pass-through.

### Medium

7. **CORS origin check uses `in` on list.** Not a vulnerability per se, but `origin in app_state.config.cors_origins` is O(n) and doesn't handle subdomains/wildcards. Could be a footgun if CORS origins list grows.

8. **Dashboard WS token endpoint returns raw auth token.** `/dashboard/ws-token` returns the gateway auth token in JSON for cookie-authenticated sessions. If the dashboard has any XSS, this token is exfiltrable.

9. **Rate limiter unbounded growth mitigation is best-effort.** The `MAX_TRACKED_DOMAINS` eviction deletes "stale" entries but under sustained diverse-domain attack, the cleanup may not keep up.

### Design Decisions to Reconsider

10. **30 security modules with many as stubs.** The repo lists 30+ security modules in `gateway/security/`, but many appear to be skeletal. Having many shallow modules creates maintenance burden and false coverage metrics. Consider consolidating into fewer, deeper modules.

---

## Summary

The core security pipeline (P0) and middleware integration (P1) deliver real value — particularly the fail-closed MCP proxy wrapper, 1Password credential isolation, and the SecurityPipeline chain. The network module integration (P2) adds meaningful DNS and SSRF protection.

However, the project is undermined by: **(a)** a completely broken test suite (Python 3.9 incompatibility), **(b)** fail-open guard initialization in MiddlewareManager, **(c)** two dashboards showing entirely fabricated data, and **(d)** an empty infrastructure branch (P3).

**Bottom line:** The security-critical code paths are mostly sound in design, but the lack of working tests and the fake dashboards are the two biggest risks. Fix the test suite first — everything else depends on being able to verify changes.
