a---
title: Full System Flowchart
type: index
tags: [#type/index, #status/active]
related: ["[[Architecture Overview]]", "[[Data Flow]]", "[[Startup Flow Diagram]]"]
status: active
last_reviewed: 2026-03-09
---

# Full System Flowchart

```mermaid
flowchart TD

    subgraph ENV["Environment Variables"]
        E1["TELEGRAM_API_BASE_URL\nhttp://gateway:8080/telegram-api"]
        E2["ANTHROPIC_BASE_URL\nhttp://gateway:8080"]
        E3["HTTP_PROXY\nhttp://gateway:8181"]
        E4["GATEWAY_AUTH_TOKEN_FILE\n/run/secrets/gateway_password"]
        E5["AGENTSHROUD_MODE\nenforce"]
        E6["PROXY_ALLOWED_NETWORKS\n172.11.0.0/16,172.12.0.0/16"]
    end

    subgraph EXTERNAL["External Services"]
        TG_API[("api.telegram.org")]
        ANTHRO[("api.anthropic.com")]
        MCP_HOST[("host.docker.internal:8200\nmac-messages-mcp")]
        SSH_HOSTS[("marvin / trillian\nraspberrypi :22")]
    end

    subgraph BOT_CONTAINER["agentshroud-bot (Node.js 22 / OpenClaw)"]
        direction TB
        OPENCLAW["OpenClaw Agent\nclaude-3-5-sonnet"]
        GRAMMY["grammY Telegram SDK\n(patched: TELEGRAM_API_BASE_URL)"]
        ANTHRO_SDK["Anthropic SDK\n(ANTHROPIC_BASE_URL)"]
        DL["downloadAndSaveTelegramFile\n(patched: TELEGRAM_API_BASE_URL)"]

        E1 --> GRAMMY
        E1 --> DL
        E2 --> ANTHRO_SDK
        E3 --> GRAMMY

        OPENCLAW --> GRAMMY
        OPENCLAW --> ANTHRO_SDK
        OPENCLAW --> DL
    end

    subgraph GW_CONTAINER["agentshroud-gateway (Python 3.13 / FastAPI)"]
        direction TB

        subgraph STARTUP["Startup Sequence (lifespan.py)"]
            CFG["load_config()\nagentshroud.yaml"]
            PII_INIT["PIISanitizer\npresidio + spaCy"]
            LEDGER["DataLedger\nSQLite /app/data/ledger.db"]
            ROUTER["MultiAgentRouter\ndefault_url=bot:18789"]
            APPROVAL_INIT["EnhancedApprovalQueue\nSQLite approvals.db"]
            PIPELINE_INIT["SecurityPipeline\n11 components wired"]

            CFG --> PII_INIT
            PII_INIT --> LEDGER
            LEDGER --> ROUTER
            ROUTER --> APPROVAL_INIT
            APPROVAL_INIT --> PIPELINE_INIT
        end

        subgraph PROXY_LAYER["Proxy Layer"]
            TG_PROXY["TelegramAPIProxy\n/telegram-api/"]
            LLM_PROXY["LLMProxy\n/v1/"]
            CONNECT_PROXY["HTTP CONNECT Proxy\n:8181 allowlist"]
            DNS_FWD["DNS Forwarder\n:5353 + blocklist"]
            MCP_PROXY["MCPProxy\n/mcp/"]
            SSH_PROXY["SSHProxy\n/ssh/"]
        end

        subgraph PIPELINE["Security Pipeline (pipeline.py)"]
            direction LR
            HC["1.1 HeuristicClassifier"]
            PG["1. PromptGuard\nscore ≥0.8 → BLOCK"]
            PII_S["2. PIISanitizer\nredact SSN/CC/phone"]
            TRUST["3. TrustManager"]
            CANARY["5. CanaryTripwire"]
            ENC["6. EncodingDetector"]
            EGRESS["5. EgressFilter\ndomain allowlist"]
            AUDIT["AuditChain\nSHA-256 hash chain"]

            HC --> PG --> PII_S --> TRUST --> CANARY --> ENC --> EGRESS --> AUDIT
        end

        subgraph STORES["Data Stores"]
            AUDIT_DB[("audit.db")]
            LEDGER_DB[("ledger.db")]
            APPROVAL_DB[("approvals.db")]
            DRIFT_DB[("drift.db")]
            ALERT_LOG[("/tmp/security/alerts\nalerts.jsonl")]
        end

        subgraph P3_SECURITY["P3 Security Modules"]
            KILLSWITCH["KillSwitchMonitor"]
            DRIFT_DET["DriftDetector"]
            MEM_INT["MemoryIntegrityMonitor\nSHA-256 baselines"]
            CLAMAV["ClamAV Scanner"]
            TRIVY["Trivy Scanner"]
            FALCO["Falco Monitor"]
            WAZUH["Wazuh Client"]
        end

        TG_PROXY --> PIPELINE
        LLM_PROXY --> PIPELINE
        PIPELINE --> AUDIT_DB
        PIPELINE --> LEDGER_DB
    end

    subgraph NETWORKS["Docker Networks"]
        NET_INT["agentshroud-internal\n172.10.0.0/16 ← internet"]
        NET_ISO["agentshroud-isolated\n172.11.0.0/16 ← no internet"]
        NET_CON["agentshroud-console\n172.12.0.0/16"]
    end

    %% Bot → Gateway connections
    GRAMMY -->|"http://gateway:8080/telegram-api"| TG_PROXY
    DL -->|"http://gateway:8080/telegram-api/file/"| TG_PROXY
    ANTHRO_SDK -->|"http://gateway:8080/v1/"| LLM_PROXY
    OPENCLAW -->|"HTTP CONNECT :8181"| CONNECT_PROXY

    %% Gateway → External
    TG_PROXY -->|"HTTPS"| TG_API
    LLM_PROXY -->|"HTTPS"| ANTHRO
    CONNECT_PROXY -->|"allowlisted domains"| TG_API
    MCP_PROXY --> MCP_HOST
    SSH_PROXY --> SSH_HOSTS

    %% Network memberships
    GW_CONTAINER -.->|"member"| NET_INT
    GW_CONTAINER -.->|"member"| NET_ISO
    BOT_CONTAINER -.->|"member"| NET_ISO
    BOT_CONTAINER -.->|"member"| NET_CON

    %% Error paths
    PIPELINE -->|"BLOCK"| SYNTH["Synthetic Error\nResponse"]:::error
    PG -->|"score ≥ 0.8"| BLOCK_MSG["403 Blocked"]:::error
    EGRESS -->|"denied domain"| DENY_MSG["Egress Denied"]:::error

    %% Styles
    classDef error fill:#ff6b6b,color:#fff
    classDef critical fill:#ffd93d,color:#000
    classDef external fill:#6bcfff,color:#000

    class TG_API,ANTHRO,MCP_HOST,SSH_HOSTS external
    class PIPELINE_INIT,PG,EGRESS critical
    class SYNTH,BLOCK_MSG,DENY_MSG error
```

## Legend

| Color | Meaning |
|-------|---------|
| Yellow | Critical security components |
| Blue | External services |
| Red | Error/block paths |
| White | Normal operation |

## Key Flows

1. **Telegram message in:** User → `api.telegram.org` → Gateway TelegramAPIProxy → Pipeline (inbound) → Bot `/webhook`
2. **LLM call:** Bot Anthropic SDK → Gateway LLMProxy → `api.anthropic.com` → Streaming filter → Pipeline (outbound) → Bot
3. **Telegram message out:** Bot grammY → Gateway TelegramAPIProxy → Pipeline (outbound) → `api.telegram.org`
4. **File download:** Bot `downloadAndSaveTelegramFile` → Gateway TelegramAPIProxy `/telegram-api/file/` → `api.telegram.org/file/` → Bot
5. **Other HTTP:** Bot → CONNECT proxy `:8181` → allowlist check → destination (if allowed)
