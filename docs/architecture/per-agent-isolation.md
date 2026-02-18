# Per-Agent Container Isolation Architecture

## Overview

SecureClaw supports running multiple AI agents, each in its own isolated container.
This document describes the architecture for achieving shared-nothing isolation
between agents while routing requests through the central gateway.

## Design Principles

1. **Shared-Nothing**: No filesystem, network, or IPC sharing between agents
2. **Least Privilege**: Each container drops ALL capabilities, runs read-only
3. **Defense in Depth**: Network isolation + seccomp + capabilities + egress filtering
4. **Auditable**: Per-agent audit trails, all inter-agent communication logged

## Architecture

```
                    ┌─────────────┐
                    │   Gateway   │
                    │  (router)   │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────┴─────┐ ┌───┴───┐ ┌─────┴─────┐
        │  Agent A   │ │Agent B│ │  Agent C   │
        │ net: net-a │ │net-b  │ │  net: net-c│
        │ vol: vol-a │ │vol-b  │ │  vol: vol-c│
        └───────────┘ └───────┘ └───────────┘
```

## Container Configuration

Each agent container has:

- **Dedicated network**: Bridge network with `internal: true` (no direct internet)
- **Dedicated volume**: Isolated data volume, not shared with other agents
- **Read-only rootfs**: `read_only: true`
- **No new privileges**: `security_opt: [no-new-privileges:true]`
- **Seccomp profile**: Default or custom restrictive profile
- **Capabilities**: `cap_drop: [ALL]` — no Linux capabilities
- **Resource limits**: CPU and memory limits per container

## Docker Compose Template

```yaml
version: "3.8"

services:
  gateway:
    image: secureclaw/gateway:latest
    ports:
      - "8080:8080"
    networks:
      - gateway-net
    environment:
      AGENT_REGISTRY: /config/agents.json

  agent-alpha:
    image: secureclaw/agent:latest
    container_name: sc-agent-alpha
    networks:
      - net-alpha
      - gateway-net  # Only for gateway communication
    volumes:
      - vol-alpha:/data
    read_only: true
    security_opt:
      - no-new-privileges:true
      - seccomp:default
    cap_drop:
      - ALL
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512m

  agent-beta:
    image: secureclaw/agent:latest
    container_name: sc-agent-beta
    networks:
      - net-beta
      - gateway-net
    volumes:
      - vol-beta:/data
    read_only: true
    security_opt:
      - no-new-privileges:true
      - seccomp:default
    cap_drop:
      - ALL
    deploy:
      resources:
        limits:
          cpus: "1.0"
          memory: 512m

networks:
  gateway-net:
    driver: bridge
  net-alpha:
    driver: bridge
    internal: true
  net-beta:
    driver: bridge
    internal: true

volumes:
  vol-alpha:
    driver: local
  vol-beta:
    driver: local
```

## Request Routing

The gateway maintains an agent registry mapping `agent_id` to container endpoint:

1. Request arrives at gateway with `agent_id` header or path
2. Gateway looks up agent in registry
3. Request forwarded to agent's container via gateway network
4. Response returned through gateway
5. All requests logged in per-agent audit trail

## Per-Agent Audit Trails

Each agent has its own audit log, stored in its dedicated volume.
The gateway also maintains a global audit log of all routed requests.

## Security Verification

The `IsolationVerifier` class performs automated checks:

- Network isolation: no shared networks between agents
- Volume isolation: no shared volumes
- Security settings: read-only root, no-new-privileges, caps dropped
- Generates alerts for any violations

## Future Enhancements

- gVisor/Kata containers for stronger kernel isolation
- mTLS between gateway and agent containers
- Rate limiting per agent
- Automatic agent scaling
