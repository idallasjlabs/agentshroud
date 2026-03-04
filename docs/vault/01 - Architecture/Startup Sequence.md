---
type: runbook
created: 2026-03-03
tags: [startup, operations, sequence]
related: [Architecture Overview, Shutdown & Recovery, Runbooks/First Time Setup, Configuration/docker-compose.yml]
---

# Startup Sequence

## Overview

AgentShroud uses a two-stage startup: the **gateway must be healthy** before the **bot container starts**. Docker Compose enforces this via `depends_on: condition: service_healthy`.

Total cold-start time: **~60-90 seconds** (Playwright browser installation may extend first-boot).

---

## Boot Sequence (Numbered)

### Stage 1: Gateway Container Startup

```
1. Docker creates agentshroud-gateway container
2. Mounts:
   - agentshroud.yaml (read-only)
   - gateway-data volume (SQLite ledger)
   - agentshroud-ssh volume (read-only)
   - Docker secrets: gateway_password, 1password_service_account
3. Sets environment:
   - GATEWAY_AUTH_TOKEN_FILE=/run/secrets/gateway_password
   - OP_SERVICE_ACCOUNT_TOKEN_FILE=/run/secrets/1password_service_account
4. Python 3.13 starts FastAPI application (gateway/ingest_api/main.py)
```

### Stage 2: Gateway Application Initialization (main.py lifespan)

```
5.  load_config() reads agentshroud.yaml
    - Searches: explicit path → $AGENTSHROUD_CONFIG → ./agentshroud.yaml → ../agentshroud.yaml
    - Generates random auth token if GATEWAY_AUTH_TOKEN_FILE is missing (logs warning)
    - Validates all Pydantic models (PIIConfig, LedgerConfig, RouterConfig, etc.)

6.  check_monitor_mode_warnings() — logs warnings if any core module is in monitor mode

7.  DataLedger.initialize()
    - Opens SQLite DB at gateway.data.path (default: ./data/ledger.db)
    - Creates tables if not exists
    - Applies retention policy (delete entries older than retention_days)

8.  PIISanitizer.initialize()
    - Loads Presidio AnalyzerEngine
    - Downloads spaCy en_core_web_lg model (first boot only — slow, ~200MB)
    - Validates entity list from config

9.  PromptGuard.initialize()
    - Loads prompt injection pattern database
    - Sets threat score thresholds

10. EgressFilter.initialize()
    - Loads domain allowlist from agentshroud.yaml proxy.allowed_domains
    - Compiles regex patterns for wildcard domains

11. MCPProxy.initialize()
    - Loads server configs from agentshroud.yaml mcp_proxy.servers
    - Sets per-tool permission levels and rate limits

12. EnhancedApprovalQueue.initialize()
    - Starts in-memory queue
    - Loads persistence store (approval_queue/store.py)
    - Activates for configured action types

13. MiddlewareManager.initialize()
    - Registers all middleware in order:
      a. RequestLoggingMiddleware
      b. AuthenticationMiddleware
      c. RateLimitingMiddleware
      d. SecurityHeadersMiddleware
      e. CORSMiddleware

14. KillSwitchMonitor starts background task
    - Polls killswitch state every 5 seconds

15. WebSocket dashboard handler registered (/ws)

16. Management API router mounted (/admin/*)

17. Gateway health endpoint becomes active (/status, /health)
```

### Stage 3: Health Check

```
18. Docker health check runs every 30s:
    python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()"

19. After 3 successful checks: gateway marked as healthy
    (start_period: 10s, interval: 30s, retries: 3)
```

### Stage 4: Bot Container Startup

```
20. Docker creates agentshroud-bot container (waits for gateway: service_healthy)
21. Mounts volumes: config, workspace, ssh, browsers
22. Docker secrets: gateway_password, telegram_bot_token

23. start-agentshroud.sh executes:
    a. Reads /run/secrets/gateway_password → exports OPENCLAW_GATEWAY_PASSWORD + GATEWAY_AUTH_TOKEN
    b. Reads /run/secrets/telegram_bot_token → exports TELEGRAM_BOT_TOKEN
    c. If GATEWAY_OP_PROXY_URL set: loads secrets via gateway op-proxy with retry:
       - Claude OAuth token (5 retries: 5s, 10s, 15s, 30s, 60s)
       - Brave Search API key (5 retries)
       - iCloud app password (background, non-blocking)
    d. Runs init-openclaw-config.sh:
       - Patches agentshroud/openclaw.json with SSH allowlist, agent settings
       - Runs apply-patches.js (idempotent config injection)
    e. Starts: openclaw gateway --allow-unconfigured --bind lan

24. OpenClaw agent starts on port 18789
    - MCP proxy wrapper (mcp-proxy-wrapper.js) intercepts all tool calls
    - All calls proxied to gateway:8080 for security inspection

25. Background: polls http://localhost:18789/api/health every 2s (up to 60s)
    - On ready: sends Telegram notification "🛡️ AgentShroud online"
```

### Stage 5: Fully Operational

```
26. Bot health check passes: curl -f http://localhost:18789/api/health
27. System is operational — both containers healthy
28. Operator can access dashboard at http://localhost:18790
```

---

## Startup Indicators

| Indicator | What It Means |
|-----------|---------------|
| Gateway logs: `Configuration loaded: bind=127.0.0.1:8080` | Config loaded successfully |
| Gateway logs: `spaCy model loaded` | PII engine ready |
| Gateway `/status` returns 200 | Gateway is healthy |
| Bot logs: `[startup] ✓ Loaded Gateway password` | Auth credential ready |
| Bot logs: `[startup] ✓ Loaded Claude OAuth token` | 1Password op-proxy working |
| Telegram: `🛡️ AgentShroud online` | Full startup complete |

---

## First-Boot Notes

- **spaCy model download** (`en_core_web_lg`, ~200MB) happens on first run; subsequent starts are fast
- **Playwright browsers** download to `agentshroud-browsers` volume on first use
- **SSH keys** are generated inside the bot container on first boot and stored in `agentshroud-ssh` volume

---

## Common Startup Failures

| Failure | Cause | Fix |
|---------|-------|-----|
| Gateway exits immediately | Missing `agentshroud.yaml` | Ensure config file exists at repo root |
| `FileNotFoundError: No agentshroud.yaml` | Config not mounted | Check volume mount in docker-compose.yml |
| `401 Unauthorized` from bot to gateway | Token mismatch | Verify `docker/secrets/gateway_password.txt` matches |
| spaCy download fails | No internet access at startup | Pre-pull image or configure offline model |
| Bot never reaches `service_healthy` | Gateway health check failing | Check gateway logs for Python errors |
| Telegram notification not sent | Bot token not loaded | Check `/run/secrets/telegram_bot_token` exists |

See [[Errors & Troubleshooting/Startup Errors]] for detailed diagnostics.

---

## Related Notes

- [[Shutdown & Recovery]] — Reverse of this sequence
- [[Configuration/docker-compose.yml]] — Container definitions
- [[Configuration/agentshroud.yaml]] — Config file that drives Step 5
- [[Runbooks/First Time Setup]] — Pre-requisites before first boot
- [[Runbooks/Health Checks]] — How to verify startup completion
