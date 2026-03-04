---
title: Startup Flow Diagram
type: diagram
tags: [diagram, startup, sequence]
related: [Startup Sequence, Architecture Overview, Configuration/docker-compose.yml]
status: documented
---

# Startup Flow Diagram

```mermaid
sequenceDiagram
    participant DC as Docker Compose
    participant GW as Gateway Container
    participant PY as Python FastAPI App
    participant BOT as Bot Container
    participant SH as start-agentshroud.sh
    participant OC as OpenClaw Agent
    participant TG as Telegram

    DC->>GW: Create container<br/>Mount agentshroud.yaml, secrets
    activate GW
    GW->>PY: Start uvicorn
    activate PY

    Note over PY: Lifespan startup
    PY->>PY: load_config() → parse agentshroud.yaml
    PY->>PY: DataLedger.initialize() → SQLite WAL
    PY->>PY: PIISanitizer.initialize() → Presidio + spaCy
    Note over PY: ~10-30s for spaCy model load
    PY->>PY: PromptGuard.initialize()
    PY->>PY: EgressFilter.initialize()
    PY->>PY: MCPProxy.initialize()
    PY->>PY: EnhancedApprovalQueue.initialize()
    PY->>PY: MiddlewareManager.initialize()
    PY->>PY: KillSwitchMonitor.start()
    PY-->>GW: FastAPI app running on :8080

    loop Health check (every 30s)
        DC->>GW: python -c "urllib...urlopen('/status')"
        GW-->>DC: HTTP 200
    end
    DC->>DC: gateway = service_healthy

    DC->>BOT: Create container (gateway healthy)
    activate BOT
    BOT->>SH: Execute start-agentshroud.sh
    activate SH
    SH->>SH: Read /run/secrets/gateway_password
    SH->>SH: Export OPENCLAW_GATEWAY_PASSWORD + GATEWAY_AUTH_TOKEN
    SH->>SH: Read /run/secrets/telegram_bot_token
    SH->>GW: POST /credentials/op-proxy (Claude OAuth token, 5 retries)
    GW-->>SH: Claude OAuth token
    SH->>GW: POST /credentials/op-proxy (Brave API key, 5 retries)
    GW-->>SH: Brave API key
    SH->>SH: [Background] Load iCloud credentials
    SH->>SH: init-openclaw-config.sh (patch openclaw.json)
    SH->>OC: Start: openclaw gateway --bind lan
    activate OC
    OC->>OC: Load config from ~/.agentshroud/openclaw.json
    OC->>OC: Initialize MCP servers
    OC->>OC: Connect Telegram provider
    OC-->>SH: Listening on :18789

    loop Health polling (every 2s, max 60s)
        SH->>OC: curl http://localhost:18789/api/health
        OC-->>SH: {"status":"healthy"}
    end

    SH->>TG: POST sendMessage "🛡️ AgentShroud online"
    TG-->>SH: OK
    Note over BOT: System fully operational

    deactivate SH
    deactivate OC
    deactivate BOT
    deactivate PY
    deactivate GW
```

---

## Related Notes

- [[Startup Sequence]] — Numbered startup steps
- [[Shutdown & Recovery]] — Reverse sequence
- [[Containers & Services/agentshroud-gateway]] — Gateway container
- [[Containers & Services/agentshroud-bot]] — Bot container
