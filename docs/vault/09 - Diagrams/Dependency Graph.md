---
title: Dependency Graph
type: diagram
tags: [diagram, dependencies, modules]
related: [Architecture Overview, Dependencies/All Dependencies]
status: documented
---

# Dependency Graph

## Gateway Module Dependencies

```mermaid
graph LR
    subgraph Entry["Entry Point"]
        MAIN["main.py"]
    end

    subgraph Core["Core Modules"]
        CONFIG["config.py"]
        AUTH["auth.py"]
        MDW["middleware.py"]
        SANIT["sanitizer.py"]
        LED["ledger.py"]
        ROUTER["router.py"]
        MODELS["models.py"]
        EVBUS["event_bus.py"]
    end

    subgraph Security["Security Modules"]
        PG["prompt_guard.py"]
        EG["egress_filter.py"]
        TM["trust_manager.py"]
        PN["input_normalizer.py"]
        AD["alert_dispatcher.py"]
        KS["killswitch_monitor.py"]
    end

    subgraph Proxy["Proxy Modules"]
        PIPE["pipeline.py"]
        MCP["mcp_proxy.py"]
        LLM["llm_proxy.py"]
        TG["telegram_proxy.py"]
        HTTP["http_proxy.py"]
        WEB["web_proxy.py"]
    end

    subgraph External["External Packages"]
        FASTAPI["fastapi"]
        PYDANTIC["pydantic"]
        PRESIDIO["presidio-analyzer"]
        SPACY["spacy"]
        AIOSQLITE["aiosqlite"]
        HTTPX["httpx"]
        YAML["pyyaml"]
    end

    MAIN --> CONFIG
    MAIN --> AUTH
    MAIN --> MDW
    MAIN --> SANIT
    MAIN --> LED
    MAIN --> ROUTER
    MAIN --> MODELS
    MAIN --> EVBUS
    MAIN --> PG
    MAIN --> EG
    MAIN --> TM
    MAIN --> PIPE
    MAIN --> MCP
    MAIN --> LLM
    MAIN --> TG
    MAIN --> HTTP
    MAIN --> WEB
    MAIN --> KS

    CONFIG --> PYDANTIC
    CONFIG --> YAML
    AUTH --> FASTAPI
    MDW --> PG
    MDW --> EG
    MDW --> PN
    MDW --> AD
    SANIT --> PRESIDIO
    SANIT --> SPACY
    LED --> AIOSQLITE
    PIPE --> PG
    PIPE --> EG
    PIPE --> TM
    LLM --> HTTPX
    TG --> HTTPX
    HTTP --> HTTPX
    WEB --> HTTPX
```

---

## Key Initialization Order (main.py lifespan)

```mermaid
graph TD
    A["1. load_config()"] --> B["2. DataLedger.initialize()"]
    B --> C["3. PIISanitizer.initialize()"]
    C --> D["4. PromptGuard.initialize()"]
    D --> E["5. EgressFilter.initialize()"]
    E --> F["6. MCPProxy.initialize()"]
    F --> G["7. EnhancedApprovalQueue.initialize()"]
    G --> H["8. MiddlewareManager.initialize()"]
    H --> I["9. KillSwitchMonitor.start()"]
    I --> J["10. FastAPI routes registered"]
    J --> K["Ready: /status returns 200"]
```

---

## Python Package Dependencies

```mermaid
graph LR
    GW["Gateway Application"]

    GW --> FASTAPI["fastapi\nUvicorn ASGI server"]
    GW --> PYDANTIC["pydantic v2\nData validation"]
    GW --> PRESIDIO["presidio-analyzer\nPII detection"]
    PRESIDIO --> SPACY["spacy\nen_core_web_sm model"]
    GW --> AIOSQLITE["aiosqlite\nAsync SQLite"]
    GW --> HTTPX["httpx\nAsync HTTP client"]
    GW --> JOSE["python-jose\nHMAC/JWT auth"]
    GW --> WS["websockets\nWebSocket server"]
    GW --> YAML["pyyaml\nConfig parsing"]
    GW --> PSUTIL["psutil\nResource monitoring"]
    GW --> DOCKER["docker\nContainer engine"]
```

---

## Related Notes

- [[Architecture Overview]] — System-level component view
- [[Dependencies/All Dependencies]] — Dependency details
- [[Gateway Core/main.py|main.py]] — Entry point that imports everything
