---
title: Full System Flowchart
type: diagram
tags: [diagram, architecture, system]
related: [Architecture Overview, Data Flow, Diagrams/Security Pipeline Flow]
status: documented
---

# Full System Flowchart

![[Architecture Overview#Full System Diagram]]

## Complete System Diagram

```mermaid
flowchart TB
    subgraph Operator["Operator Interface"]
        DASH["Dashboard\n:18790"]
        IOS["iOS Shortcuts\nTailscale"]
        CLI["Management CLI\nREST API :8080"]
    end

    subgraph BotContainer["OpenClaw Bot Container"]
        direction TB
        OC["OpenClaw Agent\nNode.js 22"]
        MCP_WRAP["MCP Proxy Wrapper\nmcp-proxy-wrapper.js\nstdio ↔ HTTP"]
        OC --> MCP_WRAP
    end

    subgraph GWContainer["AgentShroud Gateway Container"]
        direction TB

        subgraph Ingestion["Request Ingestion"]
            AUTH["Auth\nShared Secret HMAC"]
            RATE["Rate Limiting"]
            LOG["Request Logging"]
        end

        subgraph Security["Security Pipeline"]
            NORM["Input Normalizer\nBase64 / Encoding"]
            PII["PII Sanitizer\nPresidio + spaCy\nSSN/CC/Email/Phone"]
            PG["Prompt Guard\nInjection Detection\nThreat Scoring"]
            EG["Egress Filter\nDomain Allowlist\nRFC1918 Block"]
            PIPE["Security Pipeline\nOrchestrator\npipeline.py"]
        end

        subgraph Proxies["Proxy Routing"]
            MCP_P["MCP Proxy\nmcp_proxy.py"]
            LLM_P["LLM Proxy\nllm_proxy.py"]
            TG_P["Telegram Proxy\ntelegram_proxy.py"]
            HTTP_P["HTTP CONNECT\nhttp_proxy.py :8181"]
            WEB_P["Web Proxy\nweb_proxy.py"]
        end

        subgraph Infrastructure["Infrastructure"]
            AQ["Approval Queue\nenhanced_queue.py"]
            LED["Audit Ledger\nSQLite hash chain"]
            WS["WebSocket\nDashboard feed"]
            OP_P["1Password\nOp-Proxy"]
            SSH_P["SSH Proxy\nssh_proxy/proxy.py"]
        end

        AUTH --> RATE --> LOG
        LOG --> NORM --> PII --> PG --> EG --> PIPE
        PIPE --> MCP_P
        PIPE --> LLM_P
        PIPE --> TG_P
        PIPE --> HTTP_P
        PIPE --> WEB_P
        MCP_P --> AQ
        LLM_P --> LED
        TG_P --> LED
        AQ --> WS
    end

    subgraph External["External Services (Allowlisted)"]
        ANTHROPIC["api.anthropic.com"]
        OPENAI["api.openai.com"]
        TELEGRAM["api.telegram.org"]
        GOOG["*.googleapis.com"]
        GH["*.github.com"]
        ICLOUD["imap/smtp.mail.me.com"]
    end

    subgraph Monitoring["Security Monitoring"]
        FALCO["Falco SIEM"]
        WAZUH["Wazuh"]
    end

    subgraph Hosts["SSH Hosts (Tailscale)"]
        PI["Raspberry Pi"]
        MARVIN["Marvin"]
        TRILLIAN["Trillian"]
    end

    MCP_WRAP -->|"HTTP :8080"| AUTH
    IOS -->|"Tailscale :8080"| AUTH
    CLI -->|"localhost :8080"| AUTH
    DASH <-->|"WebSocket"| WS

    LLM_P --> ANTHROPIC
    LLM_P --> OPENAI
    TG_P --> TELEGRAM
    HTTP_P --> GOOG
    HTTP_P --> GH
    HTTP_P --> ICLOUD
    SSH_P --> PI
    SSH_P --> MARVIN
    SSH_P --> TRILLIAN
    OP_P -.->|"1Password API"| External

    GWContainer -.->|"Alerts"| FALCO
    GWContainer -.->|"Events"| WAZUH
```

---

## Legend

| Symbol | Meaning |
|--------|---------|
| Solid arrow → | Normal request flow |
| Dashed arrow -.-> | Optional / monitoring flow |
| Box border (thick) | Container boundary |
| Subgraph | Logical grouping within container |

---

## Related Notes

- [[Architecture Overview]] — Narrative description of this diagram
- [[Data Flow]] — Step-by-step request trace
- [[Diagrams/Security Pipeline Flow]] — Security layer detail
- [[Diagrams/Network Topology]] — Network-focused view
