# AgentShroud — Operations & Reliability Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 18. Runbook / Decision Tree — On-Call Logic

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
flowchart TD
    ALERT(["🚨 Alert Detected"])

    A1{"What is the symptom?"}

    B1["Bot Container\nCrash-Looping"]
    B1A{"Inspect\nContainer Logs"}
    B1B["Config Invalid\n(mcpServers / duplicate key)"]
    B1C["Secret Load Failed\n(op-proxy timeout)"]
    B1D["OOM / Resource Limit"]
    B1E["OpenClaw Crash\n(Node.js error)"]

    B1B_FIX["Fix Config Script\n→ Rebuild & Restart"]
    B1C_FIX["Verify Gateway Health\n& 1Password Account\n(~2 min retry)"]
    B1D_FIX["Raise mem_limit\nin docker-compose.yml"]
    B1E_FIX["Validate Config\n→ Run Doctor → Restart"]

    B2["⚠️ Context Limit Exceeded\nBot Resets Mid-Conversation"]
    B2A{"reserveTokensFloor\nset to 4000?"}
    B2B["Set compaction\nreserveTokensFloor = 4000"]
    B2C["Session > 196K tokens\nConfirm auto-compact\nor review compaction logs"]

    B3["Gateway Unhealthy\n/status Returns Error"]
    B3A["Inspect\nGateway Logs"]
    B3B["Probe /status\non Port 8080"]
    B3C["Restart\nGateway"]

    B4["🔒 Security Alert\n(Blocked domain · HIGH threat\nor canary token triggered)"]
    B4A["Review Logs for\nblocked_domain &\nThreatLevel.HIGH"]
    B4B{"Legitimate\nBot Action?"}
    B4C["Add to Allowlist\n→ Restart"]
    B4D["Activate Kill Switch\nFreeze / Disconnect"]

    B5["Bot Not Responding\non Telegram"]
    B5A["Inspect\nTelegram Logs"]
    B5B["Verify Bot Token\nin Config"]
    B5C["Restart\nBot Container"]

    ALERT --> A1
    A1 -->|"Container crash loop"| B1
    A1 -->|"Context resets"| B2
    A1 -->|"Gateway error"| B3
    A1 -->|"Security alert"| B4
    A1 -->|"No Telegram response"| B5

    B1 --> B1A
    B1A -->|"Config invalid"| B1B --> B1B_FIX
    B1A -->|"op-proxy failed"| B1C --> B1C_FIX
    B1A -->|"OOMKilled"| B1D --> B1D_FIX
    B1A -->|"Node.js error"| B1E --> B1E_FIX

    B2 --> B2A
    B2A -->|"No / missing"| B2B
    B2A -->|"Yes"| B2C

    B3 --> B3A --> B3B --> B3C

    B4 --> B4A --> B4B
    B4B -->|"Yes → allowlist"| B4C
    B4B -->|"No → attack"| B4D

    B5 --> B5A --> B5B --> B5C
```

---

## 19. Incident Response Flow — Severity & Escalation

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
flowchart TD
    INCIDENT(["Incident Detected"])

    SEV{"Assess Severity"}

    subgraph P1["P1 — Critical  ·  Respond Immediately"]
        P1_CRIT["Security Breach\nCredential Leak\nUnauthorized External Action\nCanary Token Triggered"]
        P1_OWN["Owner: Isaiah Jefferson\n→ Kill Switch & Freeze\n→ Revoke & Rotate Secrets\n→ Audit Full Ledger"]
    end

    subgraph P2["P2 — High  ·  Respond Within 1 Hour"]
        P2_HIGH["Bot Crash Loop > 15 min\nGateway Unhealthy\nApproval Queue Stalled"]
        P2_OWN["Owner: Isaiah Jefferson\n→ Check Logs\n→ Restart / Rebuild"]
    end

    subgraph P3["P3 — Medium  ·  Respond Within 4 Hours"]
        P3_MED["Context Resets (non-critical)\nOp-proxy Retries\nCron Job Missed\nMCP Threat MEDIUM"]
        P3_OWN["Owner: Isaiah Jefferson\n→ Review Logs\n→ Apply Config Fix"]
    end

    subgraph P4["P4 — Low  ·  Resolve Next Session"]
        P4_LOW["Telegram Delivery Delay\nTest Email Not Received\nMinor Config Warning"]
        P4_OWN["Owner: Isaiah / Claude Code\n→ Fix Branch → PR\n→ Merge on Schedule"]
    end

    INCIDENT --> SEV
    SEV -->|"Credentials / security"| P1
    SEV -->|"Service down"| P2
    SEV -->|"Degraded performance"| P3
    SEV -->|"Minor anomaly"| P4

    P1 --> P1_OWN
    P2 --> P2_OWN
    P3 --> P3_OWN
    P4 --> P4_OWN
```

---

## 20. Monitoring & Observability Map

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
graph TB
    subgraph Instrumented["Instrumented Components"]
        subgraph GW_MON["Gateway"]
            GW_HEALTH["GET /status\nHealth Endpoint"]
            GW_LEDGER["GET /ledger\nAudit Query API"]
            GW_LOGS["stdout/stderr\nLOG_LEVEL=INFO"]
            PROXY_STATS["HTTP CONNECT Stats\nAllowed / Blocked / Recent"]
            MCP_AUDIT_LOG["MCP Audit Log\nEvery Call + ThreatLevel"]
        end

        subgraph BOT_MON["Bot"]
            BOT_HEALTH["GET /api/health\n30s Interval"]
            BOT_LOGS["stdout/stderr\n[startup][gateway][telegram]\n[imessage][delivery-recovery]"]
            CONTEXT_DIAG["Context Overflow Diag\nSession · Tokens · Attempts"]
            TG_NOTIF["Telegram Notifications\n🛡️ Bot online  🔴 Shutting down"]
        end
    end

    subgraph AlertThresholds["Alert Thresholds"]
        TH1["Healthcheck: 3 × 10s\nstart_period 60s bot / 10s gw\nFail → Docker restarts"]
        TH2["Tokens: 200K hard limit\nCompaction at 196K\n(reserveTokensFloor=4000)"]
        TH3["Queue Timeout: 1 hour\nAuto-expires pending items"]
        TH4["Ledger: 90-day TTL\nAuto-purge on expiry"]
        TH5["Op-proxy: 6 retries\n5s→10s→15s→30s→60s\n(~2 min total)"]
    end

    subgraph MetricsDest["Where Metrics Land"]
        DOCKER_LOGS["docker logs agentshroud-bot\nPrimary Observability Surface"]
        SQLITE_AUDIT["ledger.db + approval_queue.db\nQueryable via GET /ledger"]
        TELEGRAM_CHAN["Telegram Channel\nHuman-readable Alerts\nStartup / Shutdown Events"]
    end

    subgraph Gaps["Observability Gaps (Future Work)"]
        GAP1["No Log Aggregation\n(Loki planned)"]
        GAP2["No Metrics Export\n(Prometheus planned)"]
        GAP3["No Uptime Monitor\n(planned)"]
        GAP4["Zabbix: Installed\nnot yet configured"]
    end

    Instrumented --> MetricsDest
    Instrumented --> AlertThresholds
```
