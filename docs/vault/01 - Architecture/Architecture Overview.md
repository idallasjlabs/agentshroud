---
type: architecture
created: 2026-03-03
tags: [architecture, components, diagram]
related: [System Overview, Data Flow, Startup Sequence, Containers & Services/agentshroud-gateway]
---

# Architecture Overview

## Summary

AgentShroud is a dual-container security architecture: an **OpenClaw bot container** (Node.js 22) and an **AgentShroud gateway container** (Python 3.13 / FastAPI). The bot container has no direct internet access; all outbound traffic routes through the gateway's security pipeline first.

---

## Full System Diagram

```mermaid
graph TB
    subgraph Host["macOS Host / Server"]
        subgraph BotNet["agentshroud-isolated network (172.21.0.0/16)"]
            BOT["OpenClaw Bot Container<br/>(Node.js 22)<br/>Port 18789"]
            MCP["MCP Proxy Wrapper<br/>(mcp-proxy-wrapper.js)<br/>stdio ↔ HTTP"]
            BOT --> MCP
        end

        subgraph GWNet["agentshroud-internal + agentshroud-isolated"]
            GW_AUTH["Auth Middleware<br/>(auth.py)"]
            GW_MDW["Security Middleware<br/>(middleware.py)"]
            GW_PII["PII Sanitizer<br/>(sanitizer.py)"]
            GW_PG["Prompt Guard<br/>(prompt_guard.py)"]
            GW_EG["Egress Filter<br/>(egress_filter.py)"]
            GW_MCP["MCP Proxy<br/>(mcp_proxy.py)"]
            GW_LLM["LLM Proxy<br/>(llm_proxy.py)"]
            GW_TG["Telegram Proxy<br/>(telegram_proxy.py)"]
            GW_HTTP["HTTP CONNECT Proxy<br/>(http_proxy.py, :8181)"]
            GW_AQ["Approval Queue<br/>(enhanced_queue.py)"]
            GW_LED["Ledger<br/>(ledger.py)"]
            GW_WS["WebSocket Dashboard<br/>(:18790)"]
            GW_API["Web Mgmt API<br/>(api.py)"]
        end

        OP["1Password CLI<br/>(op-proxy)"]
        SSH["SSH Proxy<br/>(ssh_proxy/proxy.py)"]
    end

    subgraph External["External Services (Allowlisted)"]
        ANTHROPIC["api.anthropic.com"]
        OPENAI["api.openai.com"]
        TELEGRAM["api.telegram.org"]
        GOOGLE["*.googleapis.com"]
        GITHUB["*.github.com"]
    end

    subgraph Monitoring["Security Monitoring"]
        FALCO["Falco SIEM"]
        WAZUH["Wazuh"]
    end

    subgraph Operator["Operator"]
        DASH["Dashboard Browser<br/>:18790"]
        IOS["iOS Shortcuts<br/>Tailscale"]
    end

    MCP -->|"HTTP :8080"| GW_AUTH
    GW_AUTH --> GW_MDW
    GW_MDW --> GW_PII
    GW_PII --> GW_PG
    GW_PG --> GW_EG
    GW_EG --> GW_MCP
    GW_EG --> GW_LLM
    GW_EG --> GW_TG
    GW_EG --> GW_HTTP

    GW_MCP -->|"inspect/audit"| GW_AQ
    GW_LLM --> GW_LED
    GW_TG --> GW_LED
    GW_HTTP --> GW_LED

    GW_LLM --> ANTHROPIC
    GW_LLM --> OPENAI
    GW_TG --> TELEGRAM
    GW_HTTP --> GOOGLE
    GW_HTTP --> GITHUB

    GW_AQ --> GW_WS
    GW_WS --> DASH
    DASH -->|"approve/deny"| GW_AQ

    GW_AUTH --> OP
    GW_MCP --> SSH

    GW_MDW --> FALCO
    GW_MDW --> WAZUH

    IOS -->|"Tailscale :8080"| GW_AUTH
```

---

## Container Architecture

### Gateway Container (`agentshroud-gateway`)

| Property | Value |
|----------|-------|
| Image | `gateway/Dockerfile` (Python 3.13, multi-stage) |
| Port exposed | `127.0.0.1:8080:8080` |
| Networks | `agentshroud-internal` + `agentshroud-isolated` |
| Memory limit | 1280 MB |
| CPU limit | 1.0 |
| PIDs limit | 100 |
| Root filesystem | Read-only |
| Security opts | `no-new-privileges`, seccomp profile |
| Capabilities | ALL dropped |

**Volumes:**
- `agentshroud.yaml` → `/app/agentshroud.yaml` (read-only)
- `gateway-data` → `/app/data` (ledger database)
- `agentshroud-ssh` → `/var/agentshroud-ssh` (read-only, SSH keys)
- `agentshroud-workspace` → `/data/bot-workspace` (read-only)

### Bot Container (`agentshroud-bot`)

| Property | Value |
|----------|-------|
| Image | `docker/Dockerfile.agentshroud` (Node.js 22) |
| Port exposed | `127.0.0.1:18790:18789` |
| Network | `agentshroud-isolated` only |
| Memory limit | 4 GB |
| CPU limit | 2.0 |
| PIDs limit | 512 |
| Root filesystem | Read-only |
| Security opts | `no-new-privileges`, seccomp profile |
| Capabilities | ALL dropped |

**Volumes:**
- `agentshroud-config` → `/home/node/.agentshroud` (config, API keys, memory)
- `agentshroud-workspace` → `/home/node/agentshroud/workspace` (agent work files)
- `agentshroud-ssh` → `/home/node/.ssh` (generated SSH keys)
- `agentshroud-browsers` → Playwright browser binaries

---

## Network Topology

```
agentshroud-internal (172.20.0.0/16)
  └── Gateway ← accessible from localhost (host machine)
  └── Operator dashboard, iOS Shortcuts via Tailscale

agentshroud-isolated (172.21.0.0/16)
  └── Bot container (NO direct internet — goes through gateway)
  └── Gateway (bridges both networks)
```

> **Note:** `internal: false` on `agentshroud-isolated` is a Docker Desktop compatibility
> workaround. Bot internet isolation is enforced at the application layer via
> `HTTP_PROXY=http://gateway:8181` and `ANTHROPIC_BASE_URL=http://gateway:8080`.

---

## Gateway Internal Layer Order

When a request arrives at the gateway, it passes through these layers **in order**:

1. `MiddlewareManager` — Auth, rate limiting, logging
2. `PIISanitizer` — Presidio/spaCy PII detection and redaction
3. `PromptGuard` — Prompt injection detection and threat scoring
4. `EgressFilter` — Domain/IP allowlist enforcement
5. `SecurityPipeline` — Orchestrates all security module checks
6. **Proxy routing:**
   - MCP calls → `MCPProxy`
   - LLM calls → `LLMProxy`
   - Telegram calls → `TelegramAPIProxy`
   - HTTP CONNECT → `HTTPConnectProxy` (port 8181)
   - Web content → `WebProxy`
7. `DataLedger` — SHA-256 hash-chained audit record
8. `ApprovalQueue` — Human-in-the-loop for risky actions

---

## Related Notes

- [[System Overview]] — Why this architecture was chosen
- [[Data Flow]] — Step-by-step request trace
- [[Startup Sequence]] — Boot order and initialization
- [[Containers & Services/agentshroud-gateway]] — Gateway container details
- [[Containers & Services/agentshroud-bot]] — Bot container details
- [[Containers & Services/networks]] — Network configuration details
- [[Diagrams/Full System Flowchart]] — Standalone diagram
