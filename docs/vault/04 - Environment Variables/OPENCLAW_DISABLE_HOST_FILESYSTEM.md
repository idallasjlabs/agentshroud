---
title: OPENCLAW_DISABLE_HOST_FILESYSTEM
type: env-var
tags: [security, isolation, bot]
related: [Configuration/All Environment Variables, Security Modules/agent_isolation.py, Configuration/docker-compose.yml]
status: documented
---

# OPENCLAW_DISABLE_HOST_FILESYSTEM

## Description

Instructs the OpenClaw agent to disable all host filesystem access. When set to `true`, the agent cannot read or write files on the container's filesystem outside of its designated workspace volume.

## Value

```
OPENCLAW_DISABLE_HOST_FILESYSTEM=true
```

## Effect

- Agent's file tools (`read_file`, `write_file`, `list_dir`) operate only within `/home/node/agentshroud/workspace`
- Direct filesystem traversal outside workspace is blocked
- Combined with `OPENCLAW_SANDBOX_MODE=strict` for full isolation

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - OPENCLAW_DISABLE_HOST_FILESYSTEM=true
  - OPENCLAW_SANDBOX_MODE=strict
```

## Related Notes

- [[OPENCLAW_SANDBOX_MODE]] — Companion setting
- [[Security Modules/agent_isolation.py|agent_isolation.py]] — Agent isolation enforcement
- [[Configuration/All Environment Variables]] — All env vars
