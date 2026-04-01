# AgentShroud — Infrastructure & Network Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 4. Infrastructure Diagram — Hosting & Servers

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
graph TB
    subgraph Internet["Internet (External Services)"]
        OAI["OpenAI API"]
        ANTH["Anthropic API"]
        TG["Telegram API"]
        GH["GitHub"]
        OP["1Password Cloud"]
        BRAVE["Brave Search API"]
    end

    subgraph Tailscale["Tailscale Overlay  ·  tail240ea8.ts.net"]
        MARVIN["marvin\n100.90.175.83"]
        PI["raspberrypi\n100.107.248.66\nagentshroud-bot user"]
        TRILLIAN["trillian\n100.94.68.61"]
    end

    subgraph MacOS["macOS Host  ·  Development Machine"]
        direction TB

        subgraph DockerCompose["Docker Compose"]
            direction LR

            subgraph NetInternal["agentshroud-internal  ·  172.20.0.0/16"]
                GW["agentshroud-gateway\n:8080 REST API\n:8181 CONNECT Proxy\nPython 3.11 · 512 MB"]
            end

            subgraph NetIsolated["agentshroud-isolated  ·  172.21.0.0/16"]
                BOT["agentshroud-bot\n:18789 OpenClaw\n:18790 Web UI\nNode.js 22 · 4 GB"]
            end

            GW -.->|"shared network"| BOT
        end

        subgraph Volumes["Named Docker Volumes"]
            V1["agentshroud-config\n~/.agentshroud"]
            V2["agentshroud-workspace\n~/workspace"]
            V3["agentshroud-ssh\n~/.ssh"]
            V4["agentshroud-browsers\nPlaywright binaries"]
            V5["gateway-data\nledger.db"]
        end

        subgraph Secrets["Docker Secrets"]
            S1["gateway_password.txt"]
            S2["openai_api_key.txt"]
            S3["1password_service_account"]
            S4["1password_bot credentials"]
        end

        TAILSCALE_HOST["Tailscale Daemon\n(macOS host)"]
    end

    BOT -->|"HTTP_PROXY=gateway:8181"| GW
    GW -->|"Allowlisted domains only"| Internet
    BOT -->|"SSH via gateway proxy"| Tailscale
    MacOS -->|"MagicDNS (static IPs)"| Tailscale
```

---

## 5. Network Topology Diagram

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
graph LR
    subgraph Host["macOS Host"]
        TS["Tailscale\n(host daemon)"]
        DOCKER["Docker Desktop"]
    end

    subgraph Internal["agentshroud-internal\n172.20.0.0/16"]
        GW_INT["Gateway\n172.20.x.x\n:8080 :8181"]
    end

    subgraph Isolated["agentshroud-isolated\n172.21.0.0/16"]
        BOT_ISO["Bot\n172.21.x.x\n:18789"]
        GW_ISO["Gateway\n172.21.x.x\n(bridge)"]
    end

    LOCALHOST["localhost\n127.0.0.1"] -->|":8080"| GW_INT
    LOCALHOST -->|":18790"| BOT_ISO

    BOT_ISO -->|"HTTP CONNECT\nAll traffic"| GW_ISO
    GW_INT -->|"HTTPS 443\nAllowlisted domains only"| Internet(("Internet"))

    GW_INT -.->|"Blocked — RFC1918"| LAN(("LAN\n10.x / 172.16.x\n192.168.x"))

    TS -->|"WireGuard tunnel"| MARVIN["marvin\n100.90.175.83"]
    TS -->|"WireGuard tunnel"| PI["raspberrypi\n100.107.248.66"]
    TS -->|"WireGuard tunnel"| TRILLIAN["trillian\n100.94.68.61"]
```

---

## 6. Deployment Diagram — What Runs Where

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
graph TB
    subgraph GitHub["GitHub  ·  idallasjlabs/agentshroud"]
        REPO["Source code\nmain branch"]
        CI["GitHub Actions CI\ntest · lint · security-scan"]
        PR["Pull Requests\nfeat/* fix/* docs/*"]
    end

    subgraph MacOS["macOS Host"]
        CLONE["Local clone\n~/Development/agentshroud"]
        WORKTREES["Git Worktrees\n../agentshroud-worktrees/<branch>"]
        DC["Docker Compose\ndocker/docker-compose.yml"]

        subgraph Running["Running Containers"]
            GW_C["agentshroud-gateway\n(healthy)"]
            BOT_C["agentshroud-bot\n(healthy)"]
        end
    end

    DEV["Developer\n(Claude Code / Isaiah)"] -->|"git push"| PR
    PR -->|"squash merge"| REPO
    REPO -->|"triggers"| CI
    CI -->|"pytest ≥90%\nblack/isort/flake8\npip-audit"| CI

    REPO -->|"git pull"| CLONE
    CLONE -->|"docker compose build & up"| DC
    DC -->|"runs"| Running

    DEV -->|"creates worktree"| WORKTREES
    WORKTREES -->|"merges to main via PR"| REPO
```
