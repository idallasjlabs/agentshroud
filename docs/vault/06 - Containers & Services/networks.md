---
title: networks
type: infrastructure
tags: [networking, docker, isolation, security]
related: [Configuration/docker-compose.yml, Containers & Services/agentshroud-gateway, Containers & Services/agentshroud-bot]
status: documented
---

# Docker Networks

## Network Architecture

```
Internet
    │
    │ (egress filtering)
    │
agentshroud-internal (172.20.0.0/16)
    │
    ├── agentshroud-gateway ←── Host (localhost:8080)
    │
    └── connected to agentshroud-isolated

agentshroud-isolated (172.21.0.0/16)
    │
    ├── agentshroud-gateway (bridges both networks)
    └── agentshroud-bot (isolated — only connects to gateway)
```

## agentshroud-internal

| Property | Value |
|----------|-------|
| Driver | bridge |
| Subnet | 172.20.0.0/16 |
| Internal | false (host can access gateway) |
| Purpose | Allows localhost access to gateway API |

**Members:**
- `agentshroud-gateway` — accessible at `localhost:8080` from host

## agentshroud-isolated

| Property | Value |
|----------|-------|
| Driver | bridge |
| Subnet | 172.21.0.0/16 |
| Internal | false* |
| ICC | Enabled (inter-container communication) |
| Purpose | Bot ↔ gateway communication only |

**Members:**
- `agentshroud-gateway` — provides services on this network
- `agentshroud-bot` — routes all traffic through gateway

*`internal: false` note: Full network isolation (`internal: true`) breaks Docker Desktop's macOS port forwarding. Bot internet isolation is enforced at the application layer via `ANTHROPIC_BASE_URL` and `TELEGRAM_API_BASE_URL` routing. Full network-layer isolation via `HTTP_PROXY=http://gateway:8181` is planned for the final production phase.

## DNS Resolution

Within the `agentshroud-isolated` network:
- Bot accesses gateway as `gateway` (Docker embedded DNS)
- Gateway accesses bot as `agentshroud`

The bot uses `extra_hosts` for macOS host access:
```yaml
extra_hosts:
  - "host.docker.internal:host-gateway"
```

This allows MCP servers running on the macOS host to be reached as `host.docker.internal`.

## Related Notes

- [[Configuration/docker-compose.yml]] — Network definitions
- [[Containers & Services/agentshroud-gateway]] — Dual-network container
- [[Containers & Services/agentshroud-bot]] — Isolated-only container
- [[Architecture Overview]] — Full system diagram
