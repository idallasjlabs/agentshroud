---
title: Network Topology
type: diagram
tags: [diagram, networking, docker]
related: [Containers & Services/networks, Architecture Overview, Configuration/docker-compose.yml]
status: documented
---

# Network Topology

## Container Network Diagram

```mermaid
graph TB
    subgraph Host["macOS Host / Server"]
        subgraph Localhost["Localhost (127.0.0.1)"]
            PORT_8080["Port :8080\nGateway API"]
            PORT_18790["Port :18790\nBot UI"]
        end

        subgraph InternalNet["agentshroud-internal\n172.20.0.0/16"]
            GW_INT["agentshroud-gateway\n172.20.x.x"]
        end

        subgraph IsolatedNet["agentshroud-isolated\n172.21.0.0/16"]
            GW_ISO["agentshroud-gateway\n172.21.x.x"]
            BOT["agentshroud-bot\n172.21.x.x"]
        end

        DOCKER_DNS["Docker DNS\nInternal hostname resolution"]
    end

    subgraph Tailscale["Tailscale Network\ntail240ea8.ts.net"]
        TS_GW["agentshroud\n(gateway)"]
        TS_PI["raspberrypi"]
        TS_MARVIN["marvin"]
        TS_TRILLIAN["trillian"]
    end

    subgraph Internet["Internet (Allowlisted Domains)"]
        ANTHROPIC["api.anthropic.com"]
        TELEGRAM["api.telegram.org"]
        GOOGLE["*.googleapis.com"]
        GITHUB["*.github.com"]
    end

    subgraph IOS["iOS Device"]
        SHORTCUTS["iOS Shortcuts"]
    end

    PORT_8080 <--> GW_INT
    PORT_18790 <--> BOT

    GW_INT <--> GW_ISO
    GW_ISO <--> BOT

    BOT -->|"All traffic\nvia gateway:8080"| GW_ISO
    GW_ISO -->|"Approved\ntraffic"| Internet

    TS_GW <-->|"Tailscale mesh"| TS_PI
    TS_GW <-->|"Tailscale mesh"| TS_MARVIN
    TS_GW <-->|"Tailscale mesh"| TS_TRILLIAN

    SHORTCUTS -->|"Tailscale :8080"| TS_GW
    GW_INT <-->|"Tailscale overlay"| TS_GW
```

---

## Hostname Resolution

| Hostname | Resolves To | Used By |
|----------|------------|---------|
| `gateway` | `172.21.x.x` (Docker DNS) | Bot container |
| `agentshroud` | `172.21.x.x` (Docker DNS) | Gateway (to reach bot) |
| `host.docker.internal` | `host-gateway` (macOS host) | Bot → MCP servers on host |
| `raspberrypi.tail240ea8.ts.net` | Tailscale IP | SSH proxy |
| `marvin.tail240ea8.ts.net` | Tailscale IP | SSH proxy |
| `trillian.tail240ea8.ts.net` | Tailscale IP | SSH proxy |

---

## Traffic Routing

| Traffic | Path |
|---------|------|
| Bot → LLM API | Bot → `http://gateway:8080` → Gateway → `api.anthropic.com` |
| Bot → Telegram | Bot → `http://gateway:8080/telegram-api` → Gateway → `api.telegram.org` |
| Bot → MCP tools | Bot → `http://gateway:8080` → Gateway → MCP server |
| Bot → SSH host | Bot → `http://gateway:8080/ssh-proxy` → Gateway → SSH host (Tailscale) |
| iOS Shortcuts → API | iPhone → Tailscale → `agentshroud.tail*:8080` → Gateway |
| Dashboard → WebSocket | Browser → `localhost:18790` → Bot → `localhost:8080/ws` |

---

## Network Security Notes

1. **agentshroud-isolated** network: Bot has no path to internet except through gateway
2. **agentshroud-internal** network: Gateway is accessible from localhost only (not LAN)
3. **RFC1918 blocking**: Gateway's egress filter blocks all private network destinations
4. **Port exposure**: Only `127.0.0.1:8080` and `127.0.0.1:18790` are exposed to host
5. **Tailscale**: Provides authenticated encrypted overlay for remote access and SSH

---

## Related Notes

- [[Containers & Services/networks]] — Docker network definitions
- [[Configuration/docker-compose.yml]] — Network configuration
- [[Architecture Overview]] — System component diagram
