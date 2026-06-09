---
title: main.py
type: module
file_path: gateway/ingest_api/main.py
tags: [fastapi, entrypoint, gateway-core, lifespan, endpoints, security-pipeline]
related: [Gateway Core/sanitizer.py, Gateway Core/ledger.py, Gateway Core/router.py, Gateway Core/auth.py, Gateway Core/middleware.py, Gateway Core/event_bus.py, Gateway Core/models.py, Architecture Overview, Data Flow]
status: documented
updated: 2026-06-09
---

# main.py

## Overview

Entry point for the AgentShroud™ Gateway FastAPI application. Wires all components together at startup, defines every HTTP and WebSocket endpoint, and implements the core content-forwarding pipeline:

```
Inbound → P1 Middleware → SecurityPipeline → MultiAgentRouter → Agent → DataLedger → Outbound filter
```

Responsibilities:
- Bootstrap all gateway components via `lifespan` (config, PII sanitizer, ledger, router, approval queue, security pipeline, session manager, P3 infrastructure modules)
- Define and serve all REST, WebSocket, and proxy endpoints
- Implement the 5-step `POST /forward` ingest pipeline
- Gate all protected endpoints with Bearer token auth via `AuthRequired`
- Apply runtime CORS, request-body size limit (1 MB), request logging, and security-header middleware
- Proxy Anthropic (`/v1/`), Google Gemini (`/v1beta/`), Ollama (`/api/`), Telegram Bot API (`/telegram-api/`), and Slack Web API (`/slack-api/`) calls through the security pipeline
- Intercept and audit MCP (Model Context Protocol) tool calls via `/mcp/proxy` and `/mcp/result`
- Serve Hermes Agent dashboard via reverse proxy at `/hermes-dashboard/`
- Provide SOC, RBAC, egress, quarantine, DNS, compliance, scanner, and killswitch management endpoints

## Lifespan / Startup

Initialization order in `gateway/ingest_api/lifespan.py::lifespan()`:

| Step | Component | Notes |
|------|-----------|-------|
| 1 | 1Password pre-warm | Background thread; no blocking |
| 2 | `GatewayConfig` | Load `agentshroud.yaml` |
| 3 | `PIISanitizer` | Mode from config; Presidio engine, 0.9 confidence floor |
| 4 | `DataLedger` | SQLite async audit trail |
| 5 | `MultiAgentRouter` | Registers all `bots:` from config |
| 6 | `AgentRegistry` + `IsolationVerifier` | Container isolation verification |
| 7 | `EnhancedApprovalQueue` | Approval queue + tool-risk config |
| 8 | `PromptGuard` | Injection detection |
| 9 | `HeuristicClassifier` | Heuristic threat scoring |
| 10 | `TrustManager` | Agent trust scoring (default agent elevated to STANDARD) |
| 11 | `EgressFilter` + `EgressApprovalQueue` | Domain allowlist + interactive egress approval |
| 12 | `SecurityPipeline` | Orchestrates P0 inbound/outbound checks |
| 13 | `MiddlewareManager` | P1 middleware (RBAC, session, file sandbox, etc.) |
| 14 | `MCPProxy` | MCP tool call interception |
| 15 | `HTTPConnectProxy` | TCP CONNECT proxy on port 8181 |
| 16 | `LLMProxy` | Anthropic/Google/Ollama reverse proxy |
| 17 | `TelegramAPIProxy` | Telegram Bot API reverse proxy |
| 18 | `SSHProxy` | SSH command proxy (if `ssh.enabled=True`) |
| 19 | P3 modules | `AlertDispatcher`, `KillSwitchMonitor`, `DriftDetector`, `EncryptedStore`, `KeyVault`, `CanaryRunner`, `ClamAVScanner`, `TrivyScanner`, `FalcoMonitor`, `WazuhClient`, `NetworkValidator`, `DNSBlocklist`, `AuditStore`, `HealthReport` |
| 20 | `EventBus` | In-process pub/sub; starts background flush task |
| 21 | `UserSessionManager` | Per-user session isolation |
| 22 | DNS forwarder | Background DNS-over-HTTPS forwarder |

On shutdown: cancels background tasks, closes ledger, stops proxies.

## Middleware (applied to all requests, outermost first)

| Middleware | Purpose |
|-----------|---------|
| `security_headers_middleware` | Adds `X-Content-Type-Options`, `X-Frame-Options`, `Cache-Control`, `Referrer-Policy`; catches Python 3.11 `BaseExceptionGroup` |
| `log_requests` | Logs method, path, status, duration; never logs bodies |
| `limit_request_body` | Rejects bodies > 1 MB (CVE-2026-32049 defense) |
| `cors_middleware` | Reads `config.cors_origins` at runtime; rejects preflight from unknown origins |

## Endpoints

Routes defined directly in `main.py` and in included routers. All protected routes require `Authorization: Bearer <token>` unless otherwise noted.

### Core / Root — main.py

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | Required | System Control live dashboard (HTML) — uptime, ledger stats, pending approvals |
| GET | `/proxy/status` | Required | HTTP CONNECT proxy traffic statistics |
| POST | `/credentials/op-proxy` | Required | 1Password credential proxy — resolves `op://` references against allowlist |
| POST | `/mcp/proxy` | Required | MCP tool call interception — injection/PII scan, permission check |
| POST | `/mcp/result` | Required | MCP tool result outbound audit — PII/credential scan, tamper-evident log |
| POST | `/webhook/telegram` | Required | Telegram inbound webhook (P3 channel ownership) |
| GET | `/ledger` | Required | Paginated ledger query (filters: source, since, until, forwarded_to) |
| GET | `/ledger/{entry_id}` | Required | Fetch single ledger entry |
| DELETE | `/ledger/{entry_id}` | Required | Delete ledger entry (right to erasure) |
| GET | `/agents` | Required | List agent targets with health status |
| POST | `/ssh/exec` | Required | SSH command execution with validation and approval gate |
| GET | `/ssh/hosts` | Required | List configured SSH host names |
| GET | `/ssh/history` | Required | SSH audit entries from ledger |
| GET | `/manage/modules` | Required | All security modules status (P0–P3) |
| POST | `/manage/scan/clamav` | Required | Trigger ClamAV antivirus scan (target param, default `/app`) |
| POST | `/manage/scan/trivy` | Required | Trigger Trivy vulnerability scan (target param, default `fs`) |
| POST | `/manage/scan/openscap` | Required | Run OpenSCAP XCCDF evaluation against container |
| POST | `/manage/scan/all` | Required | Run all available scanners (ClamAV + Trivy + OpenSCAP) |
| POST | `/manage/canary` | Required | Run canary integrity checks |
| GET | `/manage/health` | Required | Comprehensive security health report (module readiness) |
| GET | `/manage/security-report` | Required | Weighted security health score with per-tool grades and recommendations |
| POST | `/api/alerts` | None | Receive structured security alerts from internal scripts (localhost only) |
| GET | `/manage/scanners/summary` | Required | Normalized scanner state and latest results |
| GET | `/manage/scanners/history` | Required | Scanner result history (filterable by status) |
| GET | `/manage/falco/alerts` | Required | Recent Falco runtime security alerts with summary |
| GET | `/manage/wazuh/alerts` | Required | Recent Wazuh HIDS alerts with FIM and rootkit summary |
| GET | `/manage/egress/pending` | Required | Pending interactive egress approval requests with analytics |
| GET | `/manage/egress/log` | Required | Recent egress attempts for dashboard/SOC triage |
| POST | `/manage/egress/{request_id}/approve` | Required | Approve egress request (once/session/permanent) |
| POST | `/manage/egress/{request_id}/deny` | Required | Deny egress request (once/session/permanent) |
| GET | `/manage/egress/rules` | Required | Egress rules and emergency-block status |
| POST | `/manage/egress/rules` | Required | Add egress allow/deny rule |
| DELETE | `/manage/egress/rules` | Required | Remove egress rule by domain |
| GET | `/manage/egress/risk` | Required | Preview egress risk heuristic for domain/port |
| POST | `/manage/egress/emergency-block` | Required | Enable/disable emergency block-all for outbound egress |
| GET | `/manage/quarantine/blocked-messages` | Required | List quarantined blocked inbound messages |
| POST | `/manage/quarantine/blocked-messages/{message_id}/release` | Required | Release quarantined inbound message |
| POST | `/manage/quarantine/blocked-messages/{message_id}/discard` | Required | Discard quarantined inbound message after review |
| GET | `/manage/quarantine/blocked-outbound` | Required | List quarantined blocked outbound messages |
| POST | `/manage/quarantine/blocked-outbound/{message_id}/release` | Required | Release blocked outbound message |
| POST | `/manage/quarantine/blocked-outbound/{message_id}/discard` | Required | Discard blocked outbound message |
| GET | `/manage/quarantine/summary` | Required | Inbound/outbound quarantine state summary |
| GET | `/manage/soc/correlation` | Required | Cross-signal SOC correlation summary |
| GET | `/manage/soc/events` | Required | Recent security telemetry events (filterable by type/severity) |
| GET | `/manage/soc/report` | Required | Consolidated SOC report (correlation + events + quarantine + privacy + egress) |
| GET | `/manage/soc/export` | Required | Export tamper-evident audit events (formats: json, cef, json-ld) |
| GET | `/manage/privacy/policy` | Required | Private-data policy configuration and enforcement state |
| GET | `/manage/privacy/audit` | Required | Audit feed for private-data access policy violations |
| GET | `/manage/container-security` | Required | Full container security profile (12 checks: non-root, RO rootfs, caps, setuid, env secrets, memory/PID limits, Dockerfile misconfig, ClamAV, security modules, Docker secrets, health) |
| POST | `/manage/scan/cis-benchmark` | Required | CIS Docker Benchmark v1.6.0 container-level checks (13 checks) |
| POST | `/manage/deep-test` | Required | 37-test comprehensive security integration test suite |
| POST | `/manage/killswitch/verify` | Required | Run kill switch verification test (dry_run param) |
| GET | `/manage/killswitch/status` | Required | Kill switch monitor status and heartbeat history |
| GET | `/manage/rbac/users` | Required | List all users and roles (admin+ only) |
| PUT | `/manage/rbac/users/{target_user_id}` | Required | Set user role (owner only) |
| GET | `/manage/rbac/users/{user_id}/permissions` | Required | Get permissions summary for user (admin+ only) |
| GET | `/manage/rbac/my-permissions` | Required | Get permissions summary for current user |
| GET | `/manage/dns` | Required | DNS blocklist statistics |
| GET | `/manage/dns/blocked` | Required | Paginated list of blocked domains |
| POST | `/manage/dns/blocked` | Required | Add domain to local denylist |
| DELETE | `/manage/dns/blocked` | Required | Remove domain from local denylist |
| POST | `/manage/dns/refresh` | Required | Trigger immediate blocklist refresh from upstream adlists |
| GET | `/manage/compliance/soc2` | Required | SOC 2 Trust Service Criteria compliance coverage report |
| GET | `/llm-proxy/stats` | Required | LLM proxy statistics |
| GET/POST | `/v1/{path}` | IP allowlist only | Anthropic LLM API reverse proxy (streaming + non-streaming) |
| GET/POST | `/v1beta/{path}` | IP allowlist only | Google Gemini API reverse proxy |
| GET/POST | `/api/{path}` | IP allowlist only | Ollama native API reverse proxy |
| GET/POST/PUT/DELETE | `/telegram-api/{path}` | IP allowlist only | Telegram Bot API reverse proxy (multi-bot token registry) |
| GET/POST | `/slack-api/{path}` | IP allowlist only | Slack Web API reverse proxy through SecurityPipeline |
| GET/HEAD | `/hermes-dashboard` | None | Redirect to `/hermes-dashboard/` |
| ALL | `/hermes-dashboard/{path}` | None | Reverse-proxy Hermes Agent dashboard (port 9119; path-traversal blocked) |
| GET | `/soc` | None | Redirect to `/soc/v1/` (307) |
| GET | `/soc/` | None | Redirect to `/soc/v1/` (307) |

### Health Router — `gateway/ingest_api/routes/health.py` (no prefix)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/status` | None | Basic health check — returns `{"status": "ok"}` |
| GET | `/status/detail` | None | Detailed `StatusResponse` including module states |

### Forward Router — `gateway/ingest_api/routes/forward.py` (no prefix)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/forward` | Required | Main ingest endpoint — 5-step security pipeline → agent forwarding |
| POST | `/webhook/telegram` | Required | Telegram inbound webhook (duplicate declared here and main.py — router wins) |
| POST | `/email/send` | Required | Email send gateway — PII scan + recipient allowlist + approval queue |
| POST | `/email/send-owner` | Required | Send email directly to owner (owner-only shortcut) |

### Approval Router — `gateway/ingest_api/routes/approval.py` (no prefix)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/approve` | Required | Submit action for human approval |
| POST | `/approve/{request_id}/decide` | Required | Approve or reject a pending action |
| GET | `/approve/pending` | Required | List all pending approval requests |

### Dashboard Router — `gateway/ingest_api/routes/dashboard.py` (no prefix)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/collaborators` | Required | Collaborator data from bot workspace |
| GET | `/dashboard` | Cookie or Bearer | Activity dashboard HTML (sets session cookie on first auth) |
| GET | `/dashboard/stats` | Required | Dashboard JSON stats |
| GET | `/dashboard/ws-token` | Required | Issue short-lived single-use WebSocket token |

### Management API Router — `gateway/web/api.py` (prefix `/api`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/mode` | Bearer | Get current gateway mode |
| PUT | `/api/mode` | Bearer | Set gateway mode |
| GET | `/api/status` | Bearer | Extended gateway status |
| POST | `/api/services/{name}/start` | Bearer | Start a managed service |
| POST | `/api/services/{name}/stop` | Bearer | Stop a managed service |
| POST | `/api/services/{name}/restart` | Bearer | Restart a managed service |
| POST | `/api/killswitch/{mode}` | Bearer | Activate kill switch in specified mode |
| GET | `/api/config` | Bearer | Get current config |
| PUT | `/api/config` | Bearer | Update config |
| POST | `/api/config/import` | Bearer | Import config |
| GET | `/api/config/export` | Bearer | Export config |
| POST | `/api/rebuild` | Bearer | Rebuild gateway |
| GET | `/api/updates/bot/{bot_id}` | Bearer | Bot update status |
| POST | `/api/updates/bot/{bot_id}/upgrade` | Bearer | Upgrade bot |
| POST | `/api/updates/bot/{bot_id}/rollback` | Bearer | Roll back bot |
| GET | `/api/updates/openclaw` | Bearer | OpenClaw update status (legacy alias) |
| POST | `/api/updates/openclaw/upgrade` | Bearer | Upgrade OpenClaw (legacy alias) |
| POST | `/api/updates/openclaw/rollback` | Bearer | Roll back OpenClaw (legacy alias) |
| GET | `/api/updates/agentshroud` | Bearer | Gateway update status |
| POST | `/api/updates/agentshroud/upgrade` | Bearer | Upgrade gateway |
| POST | `/api/updates/agentshroud/rollback` | Bearer | Roll back gateway |
| GET | `/api/updates/history` | Bearer | Update history |
| GET | `/api/security/report` | Bearer | Security report |
| GET | `/api/logs` | Bearer | Recent log entries |

### Dashboard API Router — `gateway/web/dashboard_endpoints.py` (prefix `/api`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/proxy/status` | Bearer | HTTP proxy stats (duplicate of `/proxy/status` — dashboard version) |
| GET | `/api/alerts/summary` | Bearer | Alert summary for dashboard |
| GET | `/api/ssh/hosts` | Bearer | SSH hosts (dashboard version) |
| GET | `/api/logs/recent` | Bearer | Recent log lines |

### Management Dashboard Router — `gateway/web/management.py` (prefix `/manage`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/manage/` | Bearer | Management dashboard root (HTML) |
| GET | `/manage/dashboard` | Bearer | Management dashboard main page (HTML) |
| GET | `/manage/dashboard/approvals` | Bearer | Approvals dashboard page (HTML) |
| GET | `/manage/dashboard/modules` | Bearer | Security modules dashboard page (HTML) |
| GET | `/manage/dashboard/audit` | Bearer | Audit log dashboard page (HTML) |
| GET | `/manage/dashboard/ssh` | Bearer | SSH dashboard page (HTML) |
| GET | `/manage/dashboard/collaborators` | Bearer | Collaborators dashboard page (HTML) |
| GET | `/manage/dashboard/falco` | Bearer | Falco alerts dashboard page (HTML) |
| GET | `/manage/dashboard/wazuh` | Bearer | Wazuh HIDS dashboard page (HTML) |
| GET | `/manage/dashboard/security` | Bearer | Security overview dashboard page (HTML) |
| GET | `/manage/dashboard/killswitch` | Bearer | Kill switch dashboard page (HTML) |
| GET | `/manage/egress/allowlist` | Bearer | Get egress allowlist |
| PUT | `/manage/egress/allowlist` | Bearer | Update egress allowlist |
| GET | `/manage/credentials/status` | Bearer | Credential store status |
| POST | `/manage/credentials/rotate/{credential_id}` | Bearer | Rotate a credential |
| GET | `/manage/credentials/health` | Bearer | Credential health check |

### Version Router — `gateway/ingest_api/version_routes.py` (prefix `/api/v1/versions`)

All routes require gateway Bearer auth (wired via `dependencies=[Depends(auth_dep)]`).

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/v1/versions/current` | Required | Current gateway version |
| GET | `/api/v1/versions/history` | Required | Version history |
| GET | `/api/v1/versions/available` | Required | Available versions |
| POST | `/api/v1/versions/review` | Required | Review version changelog |
| POST | `/api/v1/versions/upgrade` | Required | Upgrade gateway version |
| POST | `/api/v1/versions/downgrade` | Required | Downgrade gateway version |
| POST | `/api/v1/versions/rollback` | Required | Roll back to previous version |

### SOC Router — `gateway/soc/router.py` (prefix `/soc/v1`)

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/soc/v1/auth/login` | SOC token | SOC login |
| POST | `/soc/v1/auth/ws-token` | SOC token | Issue SOC WebSocket token |
| GET | `/soc/v1/security/events` | SOC token | Security event feed |
| GET | `/soc/v1/security/alerts` | SOC token | Security alerts |
| GET | `/soc/v1/security/correlation` | SOC token | Cross-signal correlation |
| GET | `/soc/v1/security/risk` | SOC token | Risk assessment |
| GET | `/soc/v1/security/risk/summary` | SOC token | Risk summary |
| GET | `/soc/v1/security/audit/export` | SOC token | Audit export |
| POST | `/soc/v1/security/audit/verify` | SOC token | Audit chain verification |
| GET | `/soc/v1/egress/pending` | SOC token | Pending egress requests |
| GET | `/soc/v1/egress/rules` | SOC token | Egress rules |
| GET | `/soc/v1/egress/log` | SOC token | Egress log |
| POST | `/soc/v1/egress/{request_id}/approve` | SOC token | Approve egress |
| POST | `/soc/v1/egress/{request_id}/deny` | SOC token | Deny egress |
| POST | `/soc/v1/egress/rules/override` | SOC token | Override egress rule |
| DELETE | `/soc/v1/egress/rules/{domain}` | SOC token | Delete egress rule |
| GET | `/soc/v1/egress/history` | SOC token | Egress history |
| POST | `/soc/v1/egress/history/{entry_id}/revoke` | SOC token | Revoke egress history entry |
| POST | `/soc/v1/egress/emergency-block` | SOC token | Emergency egress block |
| GET | `/soc/v1/services` | SOC token | Managed service list |
| GET | `/soc/v1/services/{name}/logs` | SOC token | Service logs |
| POST | `/soc/v1/services/{name}/start` | SOC token | Start service |
| POST | `/soc/v1/services/{name}/stop` | SOC token | Stop service |
| POST | `/soc/v1/services/{name}/restart` | SOC token | Restart service |
| POST | `/soc/v1/services/{name}/update` | SOC token | Update service |
| POST | `/soc/v1/services/rebuild` | SOC token | Rebuild all services |
| POST | `/soc/v1/killswitch/freeze` | SOC token | Freeze gateway (kill switch) |
| POST | `/soc/v1/killswitch/shutdown` | SOC token | Shutdown gateway (kill switch) |
| POST | `/soc/v1/killswitch/disconnect` | SOC token | Disconnect gateway (kill switch) |
| GET | `/soc/v1/users` | SOC token | List SOC users |
| PUT | `/soc/v1/users/{user_id}/display-name` | SOC token | Update display name |
| POST | `/soc/v1/users/collaborator` | SOC token | Add collaborator |
| DELETE | `/soc/v1/users/{user_id}/collaborator` | SOC token | Remove collaborator |
| GET | `/soc/v1/collaborators/activity` | SOC token | Collaborator activity feed |
| PUT | `/soc/v1/users/{user_id}/role` | SOC token | Set user role |
| PUT | `/soc/v1/users/{user_id}/mode` | SOC token | Set user mode |
| GET | `/soc/v1/groups` | SOC token | List groups |
| GET | `/soc/v1/groups/{group_id}` | SOC token | Get group |
| POST | `/soc/v1/groups` | SOC token | Create group |
| DELETE | `/soc/v1/groups/{group_id}` | SOC token | Delete group |
| POST | `/soc/v1/groups/{group_id}/members` | SOC token | Add group member |
| DELETE | `/soc/v1/groups/{group_id}/members/{uid}` | SOC token | Remove group member |
| PUT | `/soc/v1/groups/{group_id}/name` | SOC token | Rename group |
| PUT | `/soc/v1/groups/{group_id}/mode` | SOC token | Set group mode |
| GET | `/soc/v1/delegation` | SOC token | List delegations |
| POST | `/soc/v1/delegation` | SOC token | Create delegation |
| DELETE | `/soc/v1/delegation/{delegatee_id}` | SOC token | Remove delegation |
| GET | `/soc/v1/tool-acl/{entity_id}` | SOC token | Get tool ACL for entity |
| GET | `/soc/v1/shared-memory/groups/{group_id}` | SOC token | Get shared memory for group |
| DELETE | `/soc/v1/shared-memory/groups/{group_id}` | SOC token | Clear shared memory for group |
| GET | `/soc/v1/privacy` | SOC token | Privacy policy state |
| GET | `/soc/v1/approvals/pending` | SOC token | Pending approvals |
| POST | `/soc/v1/approvals/{approval_id}/approve` | SOC token | Approve action |
| POST | `/soc/v1/approvals/{approval_id}/deny` | SOC token | Deny action |
| GET | `/soc/v1/health` | SOC token | SOC health check |
| GET | `/soc/v1/security/modules` | SOC token | Security module status |
| GET | `/soc/v1/modules` | SOC token | Module list (alias) |
| GET | `/soc/v1/llm/failover` | SOC token | LLM failover status |
| PUT | `/soc/v1/security/modules/{name}/mode` | SOC token | Set module mode |
| GET | `/soc/v1/bots` | SOC token | Bot registry |
| GET | `/soc/v1/config` | SOC token | Gateway config |
| PUT | `/soc/v1/config/log-level` | SOC token | Set log level |
| POST | `/soc/v1/config-integrity/acknowledge` | SOC token | Acknowledge config integrity alert |
| POST | `/soc/v1/scan/{scanner}` | SOC token | Run specific scanner |
| GET | `/soc/v1/scan/results` | SOC token | Scanner results |
| GET | `/soc/v1/scanners` | SOC token | Scanner status |
| GET | `/soc/v1/scanners/recent` | SOC token | Recent scanner output |
| GET | `/soc/v1/scorecard` | SOC token | Security scorecard |
| GET | `/soc/v1/sbom` | SOC token | Software Bill of Materials |
| GET | `/soc/v1/trivy` | SOC token | Trivy results |
| GET | `/soc/v1/agent-cves` | SOC token | Agent CVE report |
| POST | `/soc/v1/cve-report` | SOC token | Generate CVE report |
| GET | `/soc/v1/updates` | SOC token | Update status |
| POST | `/soc/v1/updates/gateway/upgrade` | SOC token | Upgrade gateway |
| POST | `/soc/v1/updates/bot/upgrade` | SOC token | Upgrade bot |
| POST | `/soc/v1/updates/hermes/upgrade` | SOC token | Upgrade Hermes |
| POST | `/soc/v1/updates/gateway/rollback` | SOC token | Roll back gateway |

## WebSocket Endpoints

| Path | Router | Auth | Description |
|------|--------|------|-------------|
| `/ws/activity` | `routes/dashboard.py` | WS token or Bearer | Real-time event feed from `EventBus`; sends `{"type":"ping"}` every 30 s; accepts `{"type":"authenticated"}` confirm on connect |
| `/ws/egress` | `routes/dashboard.py` | WS token or Bearer | Specialized egress/security dashboard event stream; emits egress-prefixed events |
| `/ws/approvals` | `routes/approval.py` | (open) | Real-time approval notifications; supports decision messages |
| `/slack-ws-relay` | `main.py` | Relay token `?t=` | Bridges bot Slack Socket Mode connection to real Slack WSS; inspects `events_api` frames for collaborator inbound activity |
| `/api/ws/logs` | `web/api.py` | Bearer | Streaming gateway log tail |
| `/api/ws/updates` | `web/api.py` | Bearer | Update progress notifications |
| `/manage/ws` | `soc/router.py` | SOC token | SOC real-time event WebSocket |

## Static Mounts

| Mount Point | Source Directory | Condition |
|-------------|-----------------|-----------|
| `/soc/static` | `gateway/soc/static/` | If directory exists |
| `/soc/branding` | `branding/logos/png/` | If directory exists |
| `/soc/favicons` | `branding/favicons/` | If directory exists |

## POST /forward — 5-Step Security Pipeline

```
Step 0: P1 Middleware (MiddlewareManager.process_request)
  → RBAC check
  → Session isolation enforcement
  → Memory security checks
  → Block on middleware failure (fail-closed)

Step 1: Security Pipeline (SecurityPipeline.process_inbound)
  → PromptGuard injection scan
  → PII sanitization (PIISanitizer, Presidio, 0.9 confidence floor)
  → TrustManager check
  → EgressFilter check
  → Tamper-evident audit chain entry
  → Block if pipeline flags content; queue if approval required

Step 2: Resolve routing target (MultiAgentRouter.resolve_target)

Step 3: Forward to agent (MultiAgentRouter.forward_to_agent)
  → HTTP POST to {target.url}/chat
  → Graceful degradation on ForwardError (content logged, not delivered)

Step 4: Record to ledger (DataLedger.record)
  → Hash both sanitized and original content
  → Emit forward/pii_detected events to EventBus

Step 5: Return ForwardResponse
  → If agent responded:
      → Outbound SecurityPipeline.process_outbound (XML filter, credential scan)
      → PIISanitizer.block_credentials (credential blocking for Telegram)
      → Log blocking event if credentials were blocked
```

## Key Dependencies — Modules Wired at Init

| Module | Tier | Source |
|--------|------|--------|
| `PIISanitizer` | P0 | `gateway/security/pii_sanitizer.py` |
| `PromptGuard` | P0 | `gateway/security/prompt_guard.py` |
| `TrustManager` | P0 | `gateway/security/trust_manager.py` |
| `EgressFilter` | P0 | `gateway/security/egress_filter.py` |
| `SecurityPipeline` | P0 | `gateway/proxy/pipeline.py` |
| `DataLedger` | P0 | `gateway/ingest_api/ledger.py` |
| `EnhancedApprovalQueue` | P0 | `gateway/approval_queue/` |
| `MultiAgentRouter` | P0 | `gateway/ingest_api/router.py` |
| `MiddlewareManager` | P1 | `gateway/ingest_api/middleware.py` |
| `UserSessionManager` | P1 | `gateway/security/session_manager.py` |
| `MCPProxy` | P1 | `gateway/proxy/mcp_proxy.py` |
| `EgressApprovalQueue` | P2 | `gateway/security/egress_approval.py` |
| `HTTPConnectProxy` | P2 | `gateway/proxy/http_proxy.py` |
| `LLMProxy` | P2 | `gateway/proxy/llm_proxy.py` |
| `TelegramAPIProxy` | P2 | `gateway/proxy/telegram_proxy.py` |
| `SlackAPIProxy` | P2 | `gateway/proxy/slack_proxy.py` |
| `SSHProxy` | P2 | `gateway/ssh_proxy/proxy.py` |
| `AlertDispatcher` | P3 | `gateway/security/alert_dispatcher.py` |
| `KillSwitchMonitor` | P3 | `gateway/security/killswitch_monitor.py` |
| `DriftDetector` | P3 | `gateway/security/drift_detector.py` |
| `EncryptedStore` | P3 | `gateway/security/encrypted_store.py` |
| `KeyVault` | P3 | `gateway/security/key_vault.py` |
| `CanaryRunner` | P3 | `gateway/security/canary.py` |
| `ClamAVScanner` | P3 | `gateway/security/clamav_scanner.py` |
| `TrivyScanner` | P3 | `gateway/security/trivy_scanner.py` |
| `FalcoMonitor` | P3 | `gateway/security/falco_monitor.py` |
| `WazuhClient` | P3 | `gateway/security/wazuh_client.py` |
| `NetworkValidator` | P3 | `gateway/security/network_validator.py` |
| `DNSBlocklist` | P3 | `gateway/security/dns_blocklist.py` |
| `AuditStore` | P3 | `gateway/security/audit_store.py` |
| `HealthReport` | P3 | `gateway/security/health_report.py` |
| `EventBus` | infra | `gateway/ingest_api/event_bus.py` |

## Environment Variables Used

| Variable | Purpose |
|----------|---------|
| `OP_SERVICE_ACCOUNT_TOKEN_FILE` | Path to 1Password service account token file |
| `OP_SERVICE_ACCOUNT_TOKEN` | 1Password service account token (loaded from file at startup) |
| `OP_SESSION` | Active 1Password CLI session token (set/refreshed by op-proxy handler) |
| `OPENCLAW_GATEWAY_PASSWORD` | Master secret for `EncryptedStore` (AES-256-GCM) |
| `AGENTSHROUD_GATEWAY_PASSWORD` | Alternate master secret for `EncryptedStore` |
| `GATEWAY_AUTH_TOKEN` | Fallback auth token for gateway Bearer auth |
| `PROXY_ALLOWED_NETWORKS` | Comma-separated CIDRs for LLM/Telegram/Slack proxy IP allowlist (default: `10.254.111.0/24,10.254.112.0/24,172.11.0.0/16` + `127.0.0.0/8`) |
| `HERMES_DASHBOARD_UPSTREAM` | Hermes dashboard upstream URL (default: `http://agentshroud-hermes:9119`) |

## Security Notes

- `_PROXY_ALLOWED_NETWORKS` restricts `/v1/`, `/v1beta/`, `/api/`, `/telegram-api/`, `/slack-api/` to the isolated Docker subnet plus loopback — not gateway Bearer auth
- `_ALLOWED_OP_PATHS` allowlist controls which `op://` references the gateway resolves; path traversal (`..`) is explicitly rejected
- `_is_imessage_recipient_allowed` checks iMessage recipients against `config.channels.imessage_allowed_recipients` before routing to MCP
- `_normalize_agent_identity` validates agent IDs to `[a-zA-Z0-9_-]{1,64}`; prevents injection via agent identity
- `_resolve_effective_agent_id` prevents body-level owner impersonation when `X-AgentShroud-User-Id` header is absent
- Request body hard-capped at 1 MB before Pydantic parsing (CVE-2026-32049 defense)
- Hermes dashboard proxy blocks path traversal patterns (`..`, `%2e%2e`, `%2f`, `%5c`) per CVE-2026-6829

## Known Issues / Notes

- `owner_user_id` is hard-coded in `lifespan.py` and `MiddlewareManager.__init__` — should be externalized to config
- The approval store path `/tmp/agentshroud_approvals.db` has a TODO to use the config-specified path
- `_EMAIL_ALLOWED_RECIPIENTS` is an empty list at module load — all email sends go to the approval queue unless populated via config
- Streaming responses from the LLM proxy pass through without outbound content filtering (TODO in code)
- The `serve_dashboard` endpoint uses `secure` cookie flag conditionally based on `X-Forwarded-Proto` — requires accurate proxy header from reverse proxy

## Related

- [[Gateway Core/sanitizer.py]]
- [[Gateway Core/ledger.py]]
- [[Gateway Core/router.py]]
- [[Gateway Core/auth.py]]
- [[Gateway Core/middleware.py]]
- [[Gateway Core/event_bus.py]]
- [[Gateway Core/models.py]]
- [[Gateway Core/version_routes.py]]
- [[Gateway Core/ssh_config.py]]
- [[Architecture Overview]]
- [[Data Flow]]
