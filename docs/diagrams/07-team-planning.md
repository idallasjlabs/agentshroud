# AgentShroud — Team, Planning & Dependency Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 21. Agile Team Diagram — Structure & Roles

```mermaid
graph TB
    subgraph Owner["Product Owner / Architect"]
        ISAIAH["Isaiah Jefferson\nProduct Owner · Architect · Operator\nSecurity approvals · Credential mgmt"]
    end

    subgraph PrimaryDev["Primary Developer"]
        CLAUDE["Claude Code (claude-sonnet-4-6)\nLead Engineer\nFeatures · Bugs · Arch · PRs · Docs"]
    end

    subgraph SecondaryDev["Secondary Developer"]
        GEMINI["Gemini CLI\nTest Engineer\nTest augmentation · Safe refactors"]
    end

    subgraph TertiaryDev["Tertiary Developer"]
        CODEX["ChatGPT Codex\nQA / Support Engineer\nTest coverage · Validation scripts"]
    end

    subgraph Production["Production Agent"]
        BOT["AgentShroud Bot (@agentshroud_bot)\nAutonomous Agent · OpenClaw\nTelegram · iMessage · 8 Cron Jobs"]
    end

    ISAIAH -->|"Directs"| CLAUDE
    ISAIAH -->|"Approves actions"| BOT
    ISAIAH -->|"Optionally directs"| GEMINI
    ISAIAH -->|"Optionally directs"| CODEX
    CLAUDE -->|"Deploys & configures"| BOT
    CLAUDE -->|"Delegates test work to"| GEMINI
    CLAUDE -->|"Delegates test work to"| CODEX
    GEMINI -.->|"Cannot direct\n(defer to Claude)"| CLAUDE
    CODEX -.->|"Cannot direct\n(defer to Claude)"| CLAUDE
```

---

## 22. Dependency Graph — Component Dependencies

Safe deployment order: components lower in the graph must be deployed first.

```mermaid
graph TB
    subgraph External["External Dependencies (no deploy needed)"]
        OP["1Password Cloud"]
        OAI["OpenAI API"]
        ANTH["Anthropic API"]
        TG_API["Telegram API"]
        TS["Tailscale Network"]
    end

    subgraph Secrets["Docker Secrets (must exist before containers start)"]
        SEC_GW["gateway_password.txt"]
        SEC_OAI["openai_api_key.txt"]
        SEC_OP["1password_service_account"]
        SEC_BOT["1password_bot credentials"]
    end

    subgraph Volumes["Docker Volumes (auto-created)"]
        VOL_CFG["agentshroud-config"]
        VOL_WS["agentshroud-workspace"]
        VOL_SSH["agentshroud-ssh"]
        VOL_GW["gateway-data"]
    end

    subgraph Images["Docker Images (must build before run)"]
        IMG_GW["docker-gateway\nPython 3.11 · gateway/Dockerfile"]
        IMG_BOT["docker-agentshroud\nNode.js 22 · docker/Dockerfile.agentshroud"]
    end

    subgraph Containers["Containers (startup order)"]
        GW_C["agentshroud-gateway\n(starts first)"]
        BOT_C["agentshroud-bot\n(starts after gateway healthy)"]
    end

    OP --> SEC_OP
    SEC_GW --> GW_C
    SEC_OAI --> BOT_C
    SEC_OP --> GW_C
    SEC_BOT --> BOT_C

    VOL_CFG --> BOT_C
    VOL_WS --> BOT_C
    VOL_SSH --> BOT_C
    VOL_GW --> GW_C

    IMG_GW --> GW_C
    IMG_BOT --> BOT_C

    GW_C -->|"service_healthy\n(healthcheck: /status)"| BOT_C

    BOT_C -->|"All outbound via"| GW_C
    BOT_C -->|"op-proxy via"| GW_C
    GW_C -->|"reads secrets from"| OP
    GW_C -->|"proxies to"| OAI
    GW_C -->|"proxies to"| ANTH
    GW_C -->|"proxies to"| TG_API
    BOT_C -->|"SSH via gateway"| TS
```

---

## 23. Roadmap / Timeline — Development Phases

```mermaid
gantt
    title AgentShroud Development Roadmap — 2026
    dateFormat  YYYY-MM-DD
    axisFormat  %b %d

    section Phase 1 — Foundation
    Gateway API + Ledger           :done,    p1a, 2026-02-01, 2026-02-10
    Bot Container + Telegram       :done,    p1b, 2026-02-01, 2026-02-10
    HMAC Auth + PII Sanitizer      :done,    p1c, 2026-02-05, 2026-02-12

    section Phase 2 — Security Core
    HTTP CONNECT Proxy             :done,    p2a, 2026-02-10, 2026-02-16
    MCP Proxy Inspector            :done,    p2b, 2026-02-10, 2026-02-16
    Approval Queue                 :done,    p2c, 2026-02-12, 2026-02-16
    SSH Proxy                      :done,    p2d, 2026-02-14, 2026-02-18

    section Phase 3 — Credential Isolation
    Op-Proxy (gateway holds keys)  :done,    p3a, 2026-02-15, 2026-02-20
    1Password service account      :done,    p3b, 2026-02-16, 2026-02-20
    Cascading retry + startup      :done,    p3c, 2026-02-18, 2026-02-22

    section Phase 4 — Channels
    iMessage MCP integration       :done,    p4a, 2026-02-18, 2026-02-22
    iCloud Email (replace Gmail)   :done,    p4b, 2026-02-22, 2026-02-24
    Telegram startup notification  :done,    p4c, 2026-02-20, 2026-02-22

    section Phase 5 — Stability
    Context limit fix (Patch 4)    :done,    p5a, 2026-02-23, 2026-02-24
    MCP key crash fix (Patch 3)    :done,    p5b, 2026-02-23, 2026-02-24
    Documentation & Diagrams       :active,  p5c, 2026-02-24, 2026-02-26

    section Phase 6 — Observability
    Tailscale config & serve       :         p6a, 2026-02-26, 2026-03-05
    Prometheus + Grafana           :         p6b, 2026-03-01, 2026-03-10
    Log aggregation (Loki)         :         p6c, 2026-03-05, 2026-03-15

    section Phase 7 — Enterprise Hardening
    IEC 62443 policy docs          :         p7a, 2026-03-10, 2026-03-20
    Multi-tenant isolation         :         p7b, 2026-03-15, 2026-04-01
    External contributor access    :         p7c, 2026-03-20, 2026-04-10
```
