# AgentShroud — Infrastructure & Network Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 4. Infrastructure Diagram — Hosting & Servers

```mermaid
graph TB
    subgraph Internet["Internet (External)"]
        OAI["OpenAI API\napi.openai.com"]
        ANTH["Anthropic API\napi.anthropic.com"]
        TG["Telegram API\napi.telegram.org"]
        GH["GitHub\ngithub.com"]
        OP["1Password\nmy.1password.com"]
        BRAVE["Brave Search\napi.search.brave.com"]
    end

    subgraph Tailscale["Tailscale Overlay Network (tail240ea8.ts.net)"]
        MARVIN["marvin\n100.90.175.83\nDevelopment node"]
        PI["raspberrypi\n100.107.248.66\nRaspberry Pi\nagentshroud-bot user"]
        TRILLIAN["trillian\n100.94.68.61\nDevelopment node"]
    end

    subgraph MacOS["macOS Host (Development Machine)"]
        direction TB

        subgraph DockerCompose["Docker Compose"]
            direction LR

            subgraph NetInternal["agentshroud-internal\n172.20.0.0/16 (bridge, external)"]
                GW["Gateway Container\nagentshroud-gateway\n:8080 → REST API\n:8181 → HTTP CONNECT proxy\nPython 3.11 / FastAPI\n512 MB / 1 CPU"]
            end

            subgraph NetIsolated["agentshroud-isolated\n172.21.0.0/16 (bridge, ICC enabled)"]
                BOT["Bot Container\nagentshroud-bot\n:18789 → OpenClaw gateway\n:18790 (host) → Web UI\nNode.js 22 / OpenClaw\n4 GB / 2 CPU"]
            end

            GW -.->|"shared network"| BOT
        end

        subgraph Volumes["Named Docker Volumes"]
            V1["agentshroud-config\n/home/node/.agentshroud"]
            V2["agentshroud-workspace\n/home/node/agentshroud/workspace"]
            V3["agentshroud-ssh\n/home/node/.ssh"]
            V4["agentshroud-browsers\nPlaywright binaries"]
            V5["gateway-data\n/app/data (ledger.db)"]
        end

        subgraph Secrets["Docker Secrets"]
            S1["gateway_password.txt"]
            S2["openai_api_key.txt"]
            S3["1password_service_account"]
            S4["1password_bot_email/password/key"]
        end

        HOST_GW["host.docker.internal\n(host-gateway)"]
        TAILSCALE_HOST["Tailscale daemon\n(runs on macOS host)"]
    end

    BOT -->|"HTTP_PROXY=http://gateway:8181\nAll outbound HTTPS"| GW
    GW -->|"allowlisted domains only"| Internet
    BOT -->|"SSH via gateway proxy"| Tailscale
    MacOS -->|"Tailscale MagicDNS\n(static IPs pinned in extra_hosts)"| Tailscale
```

---

## 5. Network Topology Diagram

```mermaid
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
    GW_INT -->|"HTTPS (port 443)\nAllowlisted only:\napi.openai.com\napi.anthropic.com\napi.telegram.org\n*.github.com\nimap.mail.me.com\nsmtp.mail.me.com"| Internet(("Internet"))

    GW_INT -.->|"Blocked by default\n(private RFC1918)"| LAN(("LAN\n192.168.x.x\n10.x.x.x\n172.16.x.x"))

    TS -->|"Encrypted tunnel\nWireGuard"| MARVIN["marvin\n100.90.175.83"]
    TS -->|"Encrypted tunnel"| PI["raspberrypi\n100.107.248.66"]
    TS -->|"Encrypted tunnel"| TRILLIAN["trillian\n100.94.68.61"]
```

---

## 6. Deployment Diagram — What Runs Where

```mermaid
graph TB
    subgraph GitHub["GitHub (idallasj/agentshroud)"]
        REPO["Source code\nmain branch"]
        CI["GitHub Actions CI\ntest + lint + security-scan"]
        PR["Pull Requests\nfeat/* fix/* docs/*"]
    end

    subgraph MacOS["macOS Host"]
        CLONE["Local clone\n/Development/agentshroud\n(main branch)"]
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
    CI -->|"pytest ≥90% coverage\nblack + isort + flake8\npip-audit"| CI

    REPO -->|"git pull"| CLONE
    CLONE -->|"docker compose build\n+ up -d"| DC
    DC -->|"runs"| Running

    DEV -->|"creates worktree\n../agentshroud-worktrees/<branch>"| WORKTREES
    WORKTREES -->|"merges to main via PR"| REPO
```
