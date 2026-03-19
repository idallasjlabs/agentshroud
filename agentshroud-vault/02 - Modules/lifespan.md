---
title: lifespan.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/ingest_api/lifespan.py
tags: [#type/module, #status/critical]
related: ["[[main]]", "[[config]]", "[[pipeline]]", "[[Startup Sequence]]", "[[Shutdown & Recovery]]"]
status: active
last_reviewed: 2026-03-09
---

# lifespan.py — Startup and Shutdown Orchestration

## Purpose

The FastAPI `lifespan` async context manager. Runs all startup initialization before the server accepts requests, and all cleanup on shutdown. This file is the "boot loader" of the gateway.

## Responsibilities

- Authenticate with 1Password (background thread, non-blocking)
- Load `agentshroud.yaml` configuration
- Initialize all security components in dependency order
- Wire components together (e.g., EgressFilter ← AuditStore)
- Start background services (HTTP CONNECT proxy, DNS forwarder, audit heartbeat)
- Clean shutdown of all components

## Key Function: `_read_secret(name, default="")`

Reads a Docker secret from `/run/secrets/<name>`. Used throughout startup to resolve tokens without requiring env vars.

```python
def _read_secret(name: str, default: str = "") -> str:
    return Path(f"/run/secrets/{name}").read_text().strip()
```

**Used for:** `telegram_bot_token`, `gateway_password`

## Initialization Order (Critical)

The order matters because of dependencies:

```
1. 1Password auth (background)
2. load_config()
3. PIISanitizer
4. DataLedger
5. MultiAgentRouter + register_bots()
6. AgentRegistry + IsolationVerifier
7. EnhancedApprovalQueue (needs: TELEGRAM_BOT_TOKEN, RBACConfig)
8. PromptGuard + HeuristicClassifier + TrustManager
9. EgressFilter (needs: config.bots for per-bot policies)
10. EgressTelegramNotifier → wired into EgressFilter
11. MiddlewareManager + set_config()
12. OutboundInfoFilter
13. PromptProtection
14. AuditStore → wired into EgressFilter (GAP-1)
15. SecurityPipeline (assembles all above)
16. LLMProxy (needs: pipeline)
17. UserSessionManager + CollaboratorActivityTracker
18. P3 infrastructure modules (AlertDispatcher, KillSwitch, etc.)
19. MCPProxy
20. SSHProxy (if ssh.enabled)
21. EventBus
22. HTTP CONNECT proxy (port 8181)
23. DNS forwarder + DNSBlocklist (port 5353)
24. AuditChain heartbeat task (60s interval)
```

## Important Wiring Details

### EgressFilter ← AuditStore (GAP-1)
```python
if app_state.egress_filter and app_state.audit_store:
    app_state.egress_filter._audit_store = app_state.audit_store
```
AuditStore must be initialized AFTER EgressFilter so it can be wired in. This is intentional.

### MemoryIntegrityMonitor Base Path
Uses `/app/data/memory-monitor/` (not bot workspace path). The bot's workspace is in the bot container — not accessible from gateway.

### TELEGRAM_BOT_TOKEN Resolution
```python
_tg_token = os.environ.get("TELEGRAM_BOT_TOKEN", "") or _read_secret("telegram_bot_token")
```
Env var checked first, then Docker secret file. The gateway does NOT have `TELEGRAM_BOT_TOKEN` as an env var by default — it comes from the secret file.

### PromptProtection Bot Hostname Filtering
```python
_bot_hostnames = [
    b.hostname for b in config.bots.values()
    if b.hostname and b.hostname.lower() != "agentshroud"
]
```
The product name "agentshroud" is excluded — it's public branding. Only internal service names (e.g., "openclaw", custom Docker hostnames) are filtered from outbound responses.

## Shutdown Block

```python
yield  # ← server runs here

# Shutdown:
await app_state.http_proxy.stop()
await app_state.approval_queue.close()
await app_state.audit_store.close()     # GAP-2: flush WAL
app_state.dns_blocklist.stop()          # GAP-6: cancel update task
await app_state.ledger.close()
```

## Environment Variables Used

- [[AGENTSHROUD_DATA_DIR]] — data directory (default: `/app/data`)
- [[AGENTSHROUD_MODE]] — global enforce/monitor override (via `get_module_mode()`)
- `GATEWAY_AUTH_TOKEN_FILE` — path to gateway secret
- `TELEGRAM_BOT_TOKEN` — Telegram token (secondary; primary is Docker secret)
- `OP_SESSION` — set dynamically after 1Password auth

## Config Files Read

- [[agentshroud.yaml]] via `load_config()`

## Failure Modes

| Step | Failure | Effect |
|------|---------|--------|
| `load_config()` | YAML missing or malformed | `raise` — gateway exits |
| `PIISanitizer` | spaCy model missing | `raise` — gateway exits |
| `DataLedger` | SQLite can't open (volume issue) | `raise` — gateway exits |
| `ApprovalQueue` | DB error | `raise` — gateway exits |
| `TrustManager` | SQLite error | `raise` — gateway exits |
| `EgressFilter` | Config error | `raise` — gateway exits |
| `HTTP CONNECT proxy` | Port 8181 in use | Warning, continues |
| `DNS forwarder` | Port 5353 in use | Warning, continues |
| P3 modules | Binary missing | Warning, module = None |
