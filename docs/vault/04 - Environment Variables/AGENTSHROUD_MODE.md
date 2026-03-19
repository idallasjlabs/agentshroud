---
title: AGENTSHROUD_MODE
type: env-var
tags: [security, configuration, enforcement]
related: [Gateway Core/config.py, Configuration/agentshroud.yaml, Configuration/All Environment Variables]
status: documented
---

# AGENTSHROUD_MODE

## Description

Global override for security module enforcement. When set to `monitor`, all security modules log threats but do NOT block them. This disables the security gateway's enforcement capability.

## Values

| Value | Effect |
|-------|--------|
| `enforce` (default) | All modules in enforce mode — threats are blocked |
| `monitor` | All modules in monitor mode — threats are logged only |

## Behavior

The `get_module_mode()` function in `config.py` checks this variable first, overriding the per-module `mode` setting in `agentshroud.yaml`:

```python
def get_module_mode(config, module_name):
    permissive = os.getenv("AGENTSHROUD_MODE", "enforce") == "monitor"
    if permissive:
        return "monitor"   # Global override wins
    return config.security.<module>.mode  # Otherwise use per-module config
```

## Affected Modules

- `pii_sanitizer` — PII detected but not redacted
- `prompt_guard` — Injections detected but not blocked
- `egress_filter` — Blocked domains still allowed through
- `mcp_proxy` — Permission violations logged but not enforced

## Startup Warnings

If any core module is in monitor mode, the gateway logs:
```
SECURITY: Module pii_sanitizer is in MONITOR mode.
Threats will be logged but NOT blocked.
Set mode: enforce or remove AGENTSHROUD_MODE=monitor for production.
```

## Usage

```bash
# Development: disable enforcement temporarily
export AGENTSHROUD_MODE=monitor
docker compose restart agentshroud-gateway

# Production: return to enforcement (default)
unset AGENTSHROUD_MODE
docker compose restart agentshroud-gateway
```

> **Warning:** `monitor` mode should NEVER be used in production. It allows PII leakage, prompt injection, and egress to blocked domains.

## Related Notes

- [[Gateway Core/config.py|config.py]] — `get_module_mode()` implementation
- [[Configuration/agentshroud.yaml]] — Per-module mode configuration
- [[Configuration/All Environment Variables]] — All env vars
