---
title: config.py
type: module
file_path: /Users/ijefferson.admin/Development/agentshroud/gateway/ingest_api/config.py
tags: [#type/module, #status/critical]
related: ["[[agentshroud.yaml]]", "[[bot_config]]", "[[lifespan]]", "[[AGENTSHROUD_MODE]]"]
status: active
last_reviewed: 2026-03-09
---

# config.py — Configuration Loader

## Purpose

Loads `agentshroud.yaml` and returns a validated `GatewayConfig` Pydantic model. All gateway components read their configuration through this model — never directly from the YAML file.

## Key Pydantic Models

| Model | Description |
|-------|-------------|
| `GatewayConfig` | Root config model; all other models are fields |
| `PIIConfig` | PII engine, entities, min_confidence |
| `LedgerConfig` | SQLite backend, path, retention_days |
| `RouterConfig` | Multi-agent routing, default_url (validated — no external hosts) |
| `ApprovalQueueConfig` | Enabled, actions, timeout |
| `ChannelsConfig` | Email, Telegram, iMessage settings |
| `SecurityConfig` | Per-module mode (enforce/monitor) |
| `SecurityModuleConfig` | mode + optional action per module |
| `ToolRiskConfig` | Tool risk tiers (critical/high/medium/low) + classifications |
| `ToolRiskPolicy` | Per-tier: require_approval, timeout, notify_channels, owner_bypass |
| `AuditExportConfig` | CEF/JSON export, DB path, max records |
| `BotConfig` | Per-bot spec (imported from [[bot_config]]) |

## `load_config(config_path=None) → GatewayConfig`

### Config File Search Order

1. `config_path` argument (explicit)
2. `$AGENTSHROUD_CONFIG` env var
3. `./agentshroud.yaml` (CWD)
4. `../agentshroud.yaml` (one level up — for running from `gateway/`)
5. Raises `FileNotFoundError` if none found

### Auth Token Resolution Order

1. File at `$GATEWAY_AUTH_TOKEN_FILE`
2. `gateway.auth_token` in YAML
3. Generated random 32-byte hex token (logged, warns user to save it)

### Bot Config Backward Compatibility

If `bots:` section is absent from YAML:
```python
bot_configs["openclaw"] = BotConfig(
    id="openclaw", name="OpenClaw", runtime="node",
    hostname="agentshroud", port=18789,
    workspace_path="/home/node/.openclaw/workspace",
    ...
)
```
This allows pre-v0.8.0 configs to continue working.

### RouterConfig URL Validation

```python
# Rejects external hostnames (containing dots):
# "attacker.com" → ValueError
# Allows:
# "localhost", "127.0.0.1", "agentshroud", "gateway" (single-label Docker names)
```

This prevents SSRF via config injection.

## `get_module_mode(config, module_name) → str`

Returns `"monitor"` or `"enforce"` for a given module.

```python
# Global override:
if os.getenv("AGENTSHROUD_MODE", "enforce") == "monitor":
    return "monitor"
# Per-module from YAML security_modules section:
return config.security.{module_name}.mode
```

## `check_monitor_mode_warnings(config, logger)`

Logs a `WARNING` for every core module running in monitor mode. Called at startup after config load.

## Environment Variables Used

- [[AGENTSHROUD_CONFIG]] — explicit config file path
- `GATEWAY_AUTH_TOKEN_FILE` — Docker secret path for auth token
- [[AGENTSHROUD_MODE]] — global monitor override

## Failure Modes

| Cause | Error |
|-------|-------|
| No YAML file found | `FileNotFoundError` → gateway exits |
| YAML not a dict | `ValueError` → gateway exits |
| RouterConfig bad URL | `ValueError` during Pydantic validation |
| Bot hostname contains dot | `ValueError` during RouterConfig validation |
