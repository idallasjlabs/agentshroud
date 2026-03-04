---
title: main.py
type: module
file_path: gateway/ingest_api/main.py
tags: [fastapi, entrypoint, gateway-core, lifespan, endpoints, security-pipeline]
related: [Gateway Core/sanitizer.py, Gateway Core/ledger.py, Gateway Core/router.py, Gateway Core/auth.py, Gateway Core/middleware.py, Gateway Core/event_bus.py, Gateway Core/models.py, Architecture Overview, Data Flow]
status: documented
---

# main.py

## Purpose
The entry point for the AgentShroud gateway API. Wires all components together at startup, defines all HTTP and WebSocket endpoints, and implements the core content forwarding pipeline: middleware security checks → injection scan → PII sanitization → routing → ledger recording → outbound filtering.

## Responsibilities
- Bootstrap all gateway components in `lifespan` (config, PII sanitizer, ledger, router, approval queue, security pipeline, session manager, P3 infrastructure modules)
- Define and serve all REST API endpoints and WebSocket endpoints
- Implement the 5-step `POST /forward` pipeline: middleware → pipeline → routing → agent forwarding → ledger
- Gate all protected endpoints with Bearer token authentication via `AuthRequired`
- Run custom CORS middleware that reads origin allowlist from config at runtime
- Proxy 1Password credential reads via `POST /credentials/op-proxy` (credential isolation)
- Proxy all Anthropic LLM API calls via `GET|POST /v1/{path}` (LLM proxy)
- Proxy all Telegram Bot API calls via `GET|POST /telegram-api/{path}` (Telegram proxy)
- Intercept and audit MCP tool calls via `POST /mcp/proxy` and `POST /mcp/result`
- Enforce email recipient allowlist via `POST /email/send`
- Enforce iMessage recipient allowlist via MCP proxy for the `mac-messages` server
- Serve real-time activity dashboard via WebSocket `/ws/activity`
- Expose SSH command execution with approval gate via `POST /ssh/exec`

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `AppState` | class | Container for all application-wide singleton state |
| `app_state` | module instance | Global `AppState` singleton |
| `lifespan` | async context manager | FastAPI lifespan: startup initialization and graceful shutdown |
| `app` | `FastAPI` | The FastAPI application instance (version 0.5.0) |
| `auth_dep` | async function | Gateway-level authentication dependency |
| `AuthRequired` | type alias | `Annotated[None, Depends(auth_dep)]` for endpoint signatures |
| `OpProxyRequest` | class | Request body for `POST /credentials/op-proxy` |
| `MCPProxyRequest` | class | Request body for `POST /mcp/proxy` |
| `MCPResultRequest` | class | Request body for `POST /mcp/result` |
| `_is_op_reference_allowed` | function | Validates `op://` references against the allowed paths allowlist |
| `_is_email_recipient_allowed` | function | Checks email address against `_EMAIL_ALLOWED_RECIPIENTS` |
| `_is_imessage_recipient_allowed` | function | Checks iMessage recipient against config allowlist |

## Endpoints

### Public (No Auth)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | System Control live dashboard (HTML) |
| GET | `/status` | Health check — returns `StatusResponse` |
| GET | `/v1/{path}` | LLM API reverse proxy (Anthropic) — no gateway auth; uses upstream API key |
| GET/POST | `/telegram-api/{path}` | Telegram Bot API reverse proxy — no gateway auth |

### Protected (Bearer Auth Required)
| Method | Path | Description |
|--------|------|-------------|
| POST | `/forward` | Main ingest endpoint — 5-step security pipeline |
| GET | `/ledger` | Paginated ledger query |
| GET | `/ledger/{entry_id}` | Fetch single ledger entry |
| DELETE | `/ledger/{entry_id}` | Delete ledger entry (right to erasure) |
| GET | `/agents` | List agent targets with health status |
| POST | `/approve` | Submit action for human approval |
| POST | `/approve/{request_id}/decide` | Approve or reject a pending action |
| GET | `/approve/pending` | List all pending approval requests |
| POST | `/mcp/proxy` | MCP tool call interception and security inspection |
| POST | `/mcp/result` | MCP tool result outbound audit |
| POST | `/webhook/telegram` | Telegram inbound webhook (P3 channel ownership) |
| POST | `/email/send` | Email send gateway with PII scan and recipient allowlist |
| POST | `/credentials/op-proxy` | 1Password credential proxy (P2 credential isolation) |
| GET | `/proxy/status` | HTTP CONNECT proxy traffic statistics |
| GET | `/llm-proxy/stats` | LLM proxy statistics |
| GET | `/telegram-proxy/stats` | Telegram proxy statistics |
| POST | `/ssh/exec` | SSH command execution with validation and approval |
| GET | `/ssh/hosts` | List configured SSH host names |
| GET | `/ssh/history` | SSH audit entries from ledger |
| GET | `/manage/modules` | Security module status (all tiers) |
| POST | `/manage/scan/clamav` | Trigger ClamAV antivirus scan |
| POST | `/manage/scan/trivy` | Trigger Trivy vulnerability scan |
| POST | `/manage/canary` | Run canary integrity checks |
| GET | `/manage/health` | Comprehensive security health report |
| GET | `/manage/container-security` | Full container security profile (9+ checks) |
| GET | `/collaborators` | Collaborator data from bot workspace |
| GET | `/dashboard` | Activity dashboard HTML (cookie or token auth) |
| GET | `/dashboard/stats` | Dashboard JSON stats |
| GET | `/dashboard/ws-token` | WS token for cookie-authenticated dashboard sessions |

### WebSocket Endpoints
| Path | Description |
|------|-------------|
| `/ws/approvals` | Real-time approval notifications; supports decision messages |
| `/ws/activity` | Real-time event feed from `EventBus`; pings every 30s |

## POST /forward — 5-Step Pipeline

```
Step 0: P1 Middleware (MiddlewareManager.process_request)
  → RBAC check
  → Session isolation enforcement
  → Memory security checks
  → Block on middleware failure (fail-closed)

Step 1: Security Pipeline (SecurityPipeline.process_inbound)
  → PromptGuard injection scan
  → PII sanitization (PIISanitizer)
  → TrustManager check
  → EgressFilter check
  → Tamper-evident audit chain entry
  → Block if pipeline flags content; queue if approval required

Step 2: Resolve routing target (MultiAgentRouter.resolve_target)

Step 3: Forward to agent (MultiAgentRouter.forward_to_agent)
  → HTTP POST to {target.url}/chat
  → Graceful degradation on ForwardError (content logged but not delivered)

Step 4: Record to ledger (DataLedger.record)
  → Hash both sanitized and original content
  → Emit forward/pii_detected events to EventBus

Step 5: Return ForwardResponse
  → If agent responded:
      → Outbound SecurityPipeline.process_outbound (XML filter, credential scan)
      → PIISanitizer.block_credentials (credential blocking for Telegram)
      → Log blocking event if credentials were blocked
```

## AppState Fields

| Field | Type | Notes |
|-------|------|-------|
| `config` | `GatewayConfig` | Loaded from `agentshroud.yaml` |
| `sanitizer` | `PIISanitizer` | PII detection engine |
| `ledger` | `DataLedger` | SQLite audit trail |
| `router` | `MultiAgentRouter` | Agent routing |
| `approval_queue` | `EnhancedApprovalQueue` | Human approval workflow |
| `prompt_guard` | `PromptGuard` | Injection detection |
| `trust_manager` | `TrustManager` | Agent trust scoring |
| `egress_filter` | `EgressFilter` | Outbound domain allowlist |
| `mcp_proxy` | `MCPProxy` | MCP tool call interception |
| `pipeline` | `SecurityPipeline` | Orchestrates all inbound/outbound security checks |
| `session_manager` | `UserSessionManager` | Per-user session isolation |
| `event_bus` | `EventBus` | In-process pub/sub |
| `http_proxy` | `HTTPConnectProxy` | HTTP CONNECT proxy on port 8181 |
| `middleware_manager` | `MiddlewareManager` | P1 middleware orchestrator |
| `outbound_filter` | `OutboundInfoFilter` | Outbound information filtering |
| `telegram_proxy` | `TelegramAPIProxy` | Telegram API reverse proxy |
| `llm_proxy` | `LLMProxy` | Anthropic LLM API reverse proxy |
| `ssh_proxy` | `SSHProxy` | SSH command proxy |
| P3 modules | various | `alert_dispatcher`, `killswitch_monitor`, `drift_detector`, `encrypted_store`, `key_vault`, `canary_runner`, `clamav_scanner`, `trivy_scanner`, `falco_monitor`, `wazuh_client`, `network_validator`, `encoding_detector`, `canary_tripwire` |

## Environment Variables Used

| Variable | Purpose |
|----------|---------|
| `OP_SERVICE_ACCOUNT_TOKEN_FILE` | Path to file containing 1Password service account token |
| `OP_SERVICE_ACCOUNT_TOKEN` | 1Password service account token (loaded from file at startup if not set) |
| `OPENCLAW_GATEWAY_PASSWORD` | Master secret for `EncryptedStore` (AES-256-GCM) |
| `GATEWAY_AUTH_TOKEN` | Fallback master secret for `EncryptedStore` |

## Config Keys Read
- `config.bind` / `config.port` — bind address and port for startup log
- `config.log_level` — Python logging level set on startup
- `config.cors_origins` — list of allowed CORS origins
- `config.auth_token` — Bearer token for all protected endpoints
- `config.pii` — `PIIConfig` passed to `PIISanitizer`
- `config.ledger` — `LedgerConfig` passed to `DataLedger`
- `config.router` — `RouterConfig` passed to `MultiAgentRouter`
- `config.approval_queue` — approval queue config
- `config.tool_risk` — tool risk enforcement config
- `config.ssh` — `SSHConfig` (enables SSH proxy if `ssh.enabled=True`)
- `config.security` — security module modes
- `config.proxy_allowed_domains` — domain allowlist for HTTP CONNECT proxy and EgressFilter
- `config.mcp_proxy_data` — MCP proxy server registry
- `config.channels.imessage_allowed_recipients` — iMessage recipient allowlist

## Credential Isolation (op-proxy)
The `_ALLOWED_OP_PATHS` list controls which `op://` references the gateway will resolve on behalf of the bot:
```python
_ALLOWED_OP_PATHS = [
    "op://Agent Shroud Bot Credentials/*/*",
]
```
Path traversal attempts (containing `..`) are explicitly rejected before allowlist matching.

## Known Issues / Notes
- `owner_user_id = "8096968754"` is hard-coded in the lifespan and in `MiddlewareManager.__init__` — this is the Telegram owner user ID and should be externalized to config.
- The approval store path `/tmp/agentshroud_approvals.db` is hard-coded with a TODO to use the config path.
- `DEBUG: agent_response = {agent_response}` log at line 1435 is a debug artifact that should be removed or gated behind `DEBUG` level.
- The `TrustManager` default agent is programmatically elevated to `STANDARD` (score=200) via raw SQL after initialization — this bypasses the standard trust API.
- `_EMAIL_ALLOWED_RECIPIENTS` is an empty list at module load time — all email sends go to the approval queue unless this is populated.
- `email/send` calls `sanitizer.sanitize()` without `await` at line 1144 — this is a bug if `sanitize` is async (it is). Will raise a coroutine warning.
- Streaming responses from the LLM proxy pass through without outbound filtering (TODO comment in code).
- The `serve_dashboard` endpoint sets cookies with `httponly=True` and `samesite="strict"` but uses `secure` conditionally based on forwarded headers — this is correct for reverse proxy deployments but requires the proxy to set `X-Forwarded-Proto` accurately.
- The container security profile (`/manage/container-security`) reads `/proc/self/status` and runs `find /` and `clamscan` — these are potentially slow operations on large filesystems.
- `WebSocket /ws/activity` uses a 30-second `asyncio.wait_for` timeout and sends a `{"type": "ping"}` to keep connections alive — clients must handle these ping messages.

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
