# AgentShroud — Operations & Reliability Diagrams

> AgentShroud™ is a trademark of Isaiah Jefferson · All rights reserved

---

## 18. Runbook / Decision Tree — On-Call Logic

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
flowchart TD
    ALERT(["🚨 Alert / Issue Detected"])

    A1{"What is the symptom?"}

    %% Branch: Container down
    B1["Bot container not healthy\nor crash-looping"]
    B1A{"Check docker logs\nagentshroud-bot --tail 50"}
    B1B["Config invalid\n(mcpServers or\nduplicate key)"]
    B1C["Secret loading failed\n(op-proxy timeout)"]
    B1D["OOM / resource limit"]
    B1E["OpenClaw crash\n(Node.js error)"]

    B1B_FIX["Fix apply-patches.js\nRebuild image\ndocker compose build agentshroud\ndocker compose up -d agentshroud"]
    B1C_FIX["Check gateway health\ndocker ps | grep gateway\nCheck 1Password service account\nWait for op-proxy retry (2 min)"]
    B1D_FIX["Increase mem_limit in\ndocker-compose.yml\n(currently 4g)"]
    B1E_FIX["Check openclaw.json validity\nRun openclaw doctor --fix\nRestart container"]

    %% Branch: Context overflow
    B2["⚠️ Context limit exceeded\nBot resets mid-conversation"]
    B2A{"reserveTokensFloor set?"}
    B2B["Check openclaw.json:\nagents.defaults.compaction.\nreserveTokensFloor = 4000"]
    B2C["If session > 196K tokens:\nBot should auto-compact.\nIf reset persists: check logs\nfor compaction errors"]

    %% Branch: Gateway unhealthy
    B3["Gateway not healthy\n/status returns error"]
    B3A["Check gateway logs\ndocker logs agentshroud-gateway"]
    B3B["Check port 8080\ncurl http://localhost:8080/status"]
    B3C["Restart gateway\ndocker compose restart gateway"]

    %% Branch: Security alert
    B4["🔒 Security alert\n(blocked domain, HIGH MCP threat,\ncanary token triggered)"]
    B4A["Review gateway logs\nfor blocked_domain or\nThreatLevel.HIGH entries"]
    B4B{"Legitimate bot action?"}
    B4C["Update allowlist in\nagentshroud.yaml\nRestart containers"]
    B4D["Kill switch:\nGateway kill_switch_enabled=true\nAction: freeze/shutdown/disconnect"]

    %% Branch: Telegram down
    B5["Bot not responding\non Telegram"]
    B5A["Check Telegram provider\ndocker logs agentshroud-bot | grep telegram"]
    B5B["Check bot token\nopenclaw.json channels.telegram.botToken"]
    B5C["Restart bot container"]

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
    B2A -->|"Yes (4000)"| B2C

    B3 --> B3A --> B3B --> B3C

    B4 --> B4A --> B4B
    B4B -->|"Yes, add to allowlist"| B4C
    B4B -->|"No, potential attack"| B4D

    B5 --> B5A --> B5B --> B5C
```

---

## 19. Incident Response Flow — Severity & Escalation

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#161c27', 'primaryTextColor': '#e2e8f0', 'primaryBorderColor': '#1583f0', 'lineColor': '#3a7bd5', 'secondaryColor': '#0f1219', 'tertiaryColor': '#08090b', 'background': '#08090b', 'mainBkg': '#161c27', 'nodeBorder': '#1583f0', 'clusterBkg': '#0f1219', 'clusterBorder': '#232b3d', 'titleColor': '#4da2f4', 'edgeLabelBackground': '#0f1219', 'fontFamily': 'Inter, system-ui, sans-serif', 'fontSize': '14px'}}}%%
flowchart TD
    INCIDENT(["Incident detected"])

    SEV{"Assess severity"}

    subgraph P1["P1 — Critical (Respond immediately)"]
        P1_CRIT["Security breach\nCredential leak\nUnauthorized external action\nCanary token triggered"]
        P1_OWN["Owner: Isaiah Jefferson\nAction: Kill switch → freeze\nRevoke credentials\nReview all ledger entries\nRotate all secrets"]
    end

    subgraph P2["P2 — High (Respond within 1 hour)"]
        P2_HIGH["Bot in crash loop\n> 15 minutes down\nGateway unhealthy\nApproval queue not processing"]
        P2_OWN["Owner: Isaiah Jefferson\nAction: Check docker logs\nRestart containers\nRebuild image if needed"]
    end

    subgraph P3["P3 — Medium (Respond within 4 hours)"]
        P3_MED["Context resets (non-critical)\nOp-proxy retries\nCron job missed\nMCP threat MEDIUM logged"]
        P3_OWN["Owner: Isaiah Jefferson\nAction: Review logs\nApply config fix\nRestart at next opportunity"]
    end

    subgraph P4["P4 — Low (Resolve in next session)"]
        P4_LOW["Telegram notification\ndelivery delay\nTest email not received\nMinor config warning"]
        P4_OWN["Owner: Isaiah / Claude Code\nAction: Create fix branch\nPR and merge on schedule"]
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
    subgraph Instrumented["What Is Instrumented"]
        subgraph GW_MON["Gateway"]
            GW_HEALTH["GET /status\nHealth endpoint\n(Python urllib healthcheck)"]
            GW_LEDGER["GET /ledger\nAudit query API"]
            GW_LOGS["stdout/stderr\nstructured log lines\nLOG_LEVEL=INFO"]
            PROXY_STATS["HTTP CONNECT proxy stats\ntotal / allowed / blocked\nrecent connections (last 20)"]
            MCP_AUDIT_LOG["MCP audit log\nEvery tool call\nThreatLevel + findings"]
        end

        subgraph BOT_MON["Bot"]
            BOT_HEALTH["GET /api/health\nOpenClaw health endpoint\ncurl healthcheck (30s interval)"]
            BOT_LOGS["stdout/stderr\n[startup], [gateway], [telegram]\n[imessage], [delivery-recovery]"]
            CONTEXT_DIAG["[context-overflow-diag]\nSessionKey, tokens, attempts"]
            TG_NOTIF["Telegram notifications\n🛡️ Bot online\n🔴 Bot shutting down"]
        end
    end

    subgraph AlertThresholds["Alert Thresholds"]
        TH1["Health check: 3 retries × 10s timeout\nstart_period: 60s (bot), 10s (gateway)\nOn failure: Docker restarts container"]
        TH2["Context tokens: 200K hard limit\nCompaction triggers at 196K\n(reserveTokensFloor=4000)"]
        TH3["Approval queue timeout: 1 hour\nAuto-expires pending items"]
        TH4["Ledger retention: 90 days\nAuto-purge at expires_at"]
        TH5["Op-proxy retries: 6 attempts\nCascading: 5s,10s,15s,30s,60s\nTotal patience: ~2 minutes"]
    end

    subgraph MetricsDest["Where Metrics Land"]
        DOCKER_LOGS["Docker container logs\n(docker logs agentshroud-bot)\nPrimary observability surface"]
        SQLITE_AUDIT["ledger.db + approval_queue.db\nQueryable via GET /ledger"]
        TELEGRAM_CHAN["Telegram channel\nHuman-readable alerts\nStartup / shutdown events"]
    end

    subgraph Gaps["Observability Gaps (Future Work)"]
        GAP1["No centralised log aggregation\n(ELK / Loki planned)"]
        GAP2["No metrics export\n(Prometheus planned)"]
        GAP3["No uptime monitor\n(external pingcheck planned)"]
        GAP4["Zabbix: installed but not configured\nfor AgentShroud containers"]
    end

    Instrumented --> MetricsDest
    Instrumented --> AlertThresholds
```
