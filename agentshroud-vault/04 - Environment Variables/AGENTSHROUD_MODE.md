---
title: AGENTSHROUD_MODE
type: env-var
tags: [#type/env-var, #status/optional]
required: false
default: "enforce"
related: ["[[config]]", "[[lifespan]]", "[[prompt_guard]]", "[[egress_filter]]", "[[sanitizer]]"]
status: active
last_reviewed: 2026-03-09
---

# AGENTSHROUD_MODE

## What It Controls

Global override for all security module modes. When set to `monitor`, ALL security modules switch to log-only (monitor) mode — no messages are blocked, no traffic is denied.

## Expected Format

String: `enforce` or `monitor`

```bash
AGENTSHROUD_MODE=monitor  # All modules log only, nothing blocked
AGENTSHROUD_MODE=enforce  # Default: all modules enforce
```

## Effect If Missing

Defaults to `enforce` — all security modules are active.

## Effect If Set to `monitor`

| Module | Normal (enforce) | Monitor mode |
|--------|-----------------|--------------|
| pii_sanitizer | Redacts PII | Logs PII found, no modification |
| prompt_guard | Blocks injection | Logs injection attempts |
| egress_filter | Blocks unauthorized domains | Logs only |
| mcp_proxy | Enforces permissions | Logs violations |
| dns_filter | Blocks tunneling | Logs only |
| killswitch | Live enforcement | Disabled |

> [!DANGER] Never use `AGENTSHROUD_MODE=monitor` in production. It disables all security enforcement. This is a debugging tool only.

## Where It Is Set

Not set in docker-compose.yml (intentionally absent — enforce is the default).

To enable monitor mode temporarily:
```bash
# Add to gateway environment in docker-compose.yml (temporarily):
- AGENTSHROUD_MODE=monitor
# Then restart:
docker compose -f docker/docker-compose.yml restart gateway
```

## How It Is Read

```python
# config.py get_module_mode():
if os.getenv("AGENTSHROUD_MODE", "enforce") == "monitor":
    return "monitor"
```

This function is called during [[lifespan]] for each module. The check happens at startup, not per-request — restart is required for the change to take effect.

## Used In

| Module | Effect |
|--------|--------|
| [[prompt_guard]] | `block_threshold=999.0`, `warn_threshold=999.0` (nothing blocks) |
| [[egress_filter]] | Returns `ALLOW` for all destinations |
| [[sanitizer]] | Logs PII but does not redact |
| [[lifespan]] | `get_module_mode()` called for all 8 modules at startup |
