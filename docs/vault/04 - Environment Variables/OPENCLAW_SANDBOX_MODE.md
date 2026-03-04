---
title: OPENCLAW_SANDBOX_MODE
type: env-var
tags: [security, isolation, sandbox, bot]
related: [Configuration/All Environment Variables, OPENCLAW_DISABLE_HOST_FILESYSTEM, Security Modules/agent_isolation.py]
status: documented
---

# OPENCLAW_SANDBOX_MODE

## Description

Sets the OpenClaw agent's sandbox enforcement level. Controls how strictly the agent is restricted from accessing system resources.

## Values

| Value | Effect |
|-------|--------|
| `strict` | Full sandbox: no host access, restricted tool set |
| `permissive` | Reduced restrictions (development only) |

## Production Setting

```
OPENCLAW_SANDBOX_MODE=strict
```

## Combination with Other Settings

For full isolation, use both:
```yaml
OPENCLAW_DISABLE_HOST_FILESYSTEM: "true"
OPENCLAW_SANDBOX_MODE: strict
```

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - OPENCLAW_SANDBOX_MODE=strict
```

## Related Notes

- [[OPENCLAW_DISABLE_HOST_FILESYSTEM]] — Companion filesystem restriction
- [[Security Modules/agent_isolation.py|agent_isolation.py]] — Agent isolation module
- [[Configuration/All Environment Variables]] — All env vars
