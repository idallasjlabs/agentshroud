---
title: Startup Sequence
type: process
tags: [#type/process, #status/critical]
related: ["[[lifespan]]", "[[config]]", "[[Architecture Overview]]", "[[Gateway Startup Failure]]"]
status: active
last_reviewed: 2026-03-09
---

# Startup Sequence

Cold boot to fully operational. The gateway must be healthy before the bot starts.

## Container Dependency Order

```
docker compose up -d
    │
    ├── 1. agentshroud-gateway starts
    │       └── healthcheck: python -c "urllib.request.urlopen('http://127.0.0.1:8080/status')"
    │               └── passes → condition: service_healthy
    │
    └── 2. agentshroud-bot starts (depends_on: gateway service_healthy)
```

---

## Gateway Startup Sequence (lifespan.py)

> [!NOTE] Step 1: 1Password Authentication (background thread)
> **Triggered by:** Startup, if `/run/secrets/1password_bot_email` exists and is non-empty
> **Module:** [[lifespan]] `_op_authenticate()`
> **Produces:** `OP_SESSION` env var set in process
> **Failure behavior:** Warning logged; op-proxy will be unavailable but startup continues

> [!NOTE] Step 2: Configuration Load
> **Triggered by:** Always
> **Module:** [[config]] `load_config()`
> **Needs:** `agentshroud.yaml` at `/app/agentshroud.yaml` or env `AGENTSHROUD_CONFIG`
> **Produces:** `app_state.config` (GatewayConfig Pydantic model)
> [!DANGER] If this step fails: `FileNotFoundError` or `ValueError` — gateway exits immediately. Check `docker logs agentshroud-gateway`. See [[Gateway Startup Failure]].

> [!NOTE] Step 3: PII Sanitizer Init
> **Module:** [[sanitizer]] `PIISanitizer`
> **Needs:** `config.pii` (engine=presidio, entities, min_confidence)
> **Produces:** `app_state.sanitizer`
> **Note:** Presidio logs language warnings (es/it/pl skipped) — benign
> [!DANGER] If this step fails: Gateway exits. Usually caused by missing spaCy model. Rebuild image.

> [!NOTE] Step 4: Data Ledger Init
> **Module:** [[ledger]] `DataLedger`
> **Needs:** SQLite at `/app/data/ledger.db` (gateway-data volume)
> **Produces:** `app_state.ledger`
> [!DANGER] If this step fails: Gateway exits. Check volume mount: `docker volume inspect agentshroud_gateway-data`

> [!NOTE] Step 5: Multi-Agent Router Init
> **Module:** [[router]] `MultiAgentRouter`
> **Needs:** `config.router`, `config.bots` (from `agentshroud.yaml bots:` section)
> **Produces:** `app_state.router`
> **Computes:** `default_url` from default bot's `hostname:port`

> [!NOTE] Step 6: Agent Registry Init
> **Module:** `agent_isolation.AgentRegistry`
> **Needs:** `config.bots`
> **Produces:** `app_state.agent_registry`
> **Also:** Runs `IsolationVerifier.verify_shared_nothing()` — logs warnings for isolation violations

> [!NOTE] Step 7: Approval Queue Init
> **Module:** `approval_queue.enhanced_queue.EnhancedApprovalQueue`
> **Needs:** `TELEGRAM_BOT_TOKEN` (env or `/run/secrets/telegram_bot_token`), `RBACConfig().owner_user_id`
> **Produces:** `app_state.approval_queue`
> **DB:** `/app/data/agentshroud_approvals.db` (or `$AGENTSHROUD_DATA_DIR`)
> [!DANGER] If this step fails: Gateway exits.

> [!NOTE] Step 8: Security Components Init
> Initialized in order (each can be skipped with warning if optional):
> - `PromptGuard` — prompt injection scorer (thresholds from config mode)
> - `HeuristicClassifier` — ML-free injection heuristics
> - `TrustManager` — agent trust scoring (SQLite), default agent elevated to STANDARD
> - `EgressFilter` — per-bot domain allowlist enforcement
> - `EgressTelegramNotifier` — Telegram alerts for egress events
> - `MiddlewareManager` — tool result PII scan, log sanitizer, context guard
> - `OutboundInfoFilter` — blocks information disclosure in bot responses
> - `PromptProtection` — blocks system prompt / architecture disclosure

> [!NOTE] Step 9: AuditStore Init
> **Module:** `security.audit_store.AuditStore`
> **DB:** `/app/data/audit.db`
> **Also wires:** AuditStore into EgressFilter (egress events persist to DB)

> [!NOTE] Step 10: Security Pipeline Assembly
> **Module:** [[pipeline]] `SecurityPipeline`
> **Wires together:** PromptGuard, PIISanitizer, TrustManager, EgressFilter, ApprovalQueue, OutboundFilter, ContextGuard, CanaryTripwire, EncodingDetector, OutputCanary, EnhancedToolSanitizer, AuditStore, PromptProtection, HeuristicClassifier
> **Produces:** `app_state.pipeline`

> [!NOTE] Step 11: LLM Proxy Init
> **Module:** [[llm_proxy]] `LLMProxy`
> **Wires:** pipeline, middleware_manager, sanitizer
> **Produces:** `app_state.llm_proxy`

> [!NOTE] Step 12: Session Manager + Collaborator Tracker Init
> - `UserSessionManager` — per-user session isolation (workspace: `/app/data/sessions`)
> - `CollaboratorActivityTracker` — logs collaborator Telegram activity

> [!NOTE] Step 13: P3 Infrastructure Security Modules
> Initialized but non-fatal if binaries missing:
> - `AlertDispatcher` — routes findings to `/tmp/security/alerts/alerts.jsonl`
> - `KillSwitchMonitor` — heartbeat + anomaly detection
> - `DriftDetector` — config change baseline
> - `MemoryIntegrityMonitor` — SHA-256 baselines at `/app/data/memory-monitor/`
> - `MemoryLifecycleManager` — PII+injection scanning on memory writes
> - `HealthReport` — module aggregator
> - `EncryptedStore` — AES-256-GCM ledger encryption
> - `Canary` — integrity checks on 3 critical files
> - `ClamAV` — antivirus (requires `clamscan` binary)
> - `Trivy` — container vulnerability scanner (requires `trivy` binary)
> - `Falco` monitor — reads `/tmp/security/falco` alert files
> - `Wazuh` client — reads `/tmp/security/wazuh` alert files
> - `NetworkValidator`

> [!NOTE] Step 14: MCP Proxy Init
> **Module:** `proxy.mcp_proxy.MCPProxy`
> **Config:** `agentshroud.yaml mcp_proxy:` section
> **Enforce mode:** enables PII scan, injection scan, audit logging

> [!NOTE] Step 15: SSH Proxy Init
> **Module:** `ssh_proxy.proxy.SSHProxy`
> **Needs:** `agentshroud.yaml ssh.enabled: true` + SSH key volume mounted at `/var/agentshroud-ssh`

> [!NOTE] Step 16: HTTP CONNECT Proxy Start
> **Module:** `proxy.http_proxy.HTTPConnectProxy`
> **Port:** 8181
> **Domain allowlist:** from `agentshroud.yaml proxy.allowed_domains`

> [!NOTE] Step 17: DNS Forwarder Start
> **Module:** `proxy.dns_forwarder`, `proxy.dns_blocklist.DNSBlocklist`
> **Port:** 5353
> **Blocklist:** downloads adlists on first run, updates periodically

> [!NOTE] Step 18: Audit Chain Heartbeat
> **Task:** asyncio background task, runs every 60 seconds
> **Action:** calls `pipeline.verify_audit_chain()` — logs CRITICAL if tampered

> [!NOTE] Step 19: Ready
> Logs: `AgentShroud Gateway ready at 127.0.0.1:8080`
> Bot container starts (depends_on: gateway healthy)

---

## Bot Startup Sequence

1. `docker-entrypoint.sh` → `start-agentshroud.sh` (entrypoint in Dockerfile)
2. Reads `OPENCLAW_GATEWAY_PASSWORD_FILE` → sets `OPENCLAW_GATEWAY_PASSWORD`
3. Reads `TELEGRAM_BOT_TOKEN_FILE` → sets `TELEGRAM_BOT_TOKEN`
4. Runs `init-config.sh` — writes `openclaw.json` if not present
5. Runs `apply-patches.js` — patches model, tool list, workspace path
6. Starts OpenClaw CLI (`openclaw start`)
7. OpenClaw connects to Telegram via `getUpdates` long-poll
8. Sends startup Telegram notification via gateway (`X-AgentShroud-System: 1` bypasses content filter)

> [!DANGER] If bot startup fails at step 2/3: Secret files missing. Check `docker/secrets/*.txt` files.
> [!DANGER] If bot startup fails at step 6: OpenClaw config corrupt. Check `docker volume inspect agentshroud_agentshroud-config`
