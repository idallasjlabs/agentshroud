---
title: Security Pipeline Flow
type: diagram
tags: [diagram, security, pipeline]
related: [Data Flow, Architecture Overview, Proxy Layer/pipeline.py]
status: documented
---

# Security Pipeline Flow

## Overview

This diagram shows the security layers a request passes through in order. Each layer can either pass the request forward, block it (enforce mode), or log and pass (monitor mode).

```mermaid
flowchart TD
    REQ["Incoming Request\nfrom Bot or External Client"]

    AUTH{"Auth Check\nHMAC Bearer Token"}
    AUTH_FAIL["→ 401 Unauthorized"]

    RATE{"Rate Limit\nPer-client / Per-endpoint"}
    RATE_FAIL["→ 429 Too Many Requests"]

    NORM["Input Normalization\n• Base64 decode & inspect\n• Encoding normalization\n• Null byte stripping"]

    PII{"PII Detection\nPresidio + spaCy\nConfidence ≥ 0.9"}
    PII_ENFORCE["Redact PII\n→ <REDACTED_SSN> etc."]
    PII_BLOCK["→ 400 Blocked (if action=block)"]

    PG{"Prompt Guard\nPattern matching\nThreat scoring"}
    PG_FAIL["→ 400 Injection Blocked"]

    TRUST{"Trust Manager\nAgent trust score\nSession history"}
    TRUST_FAIL["→ 403 Trust Level Too Low"]

    EG{"Egress Filter\nDomain allowlist\nRFC1918 block"}
    EG_FAIL["→ 403 Egress Blocked"]

    PIPE["Security Pipeline\nOrchestrator\n• Context guard\n• Tool chain analysis\n• Outbound filter"]

    AQ{"Approval Queue\nRequires human review?"}
    AQ_WAIT["→ 202 Pending Approval\nWebSocket notification → dashboard"]

    PROXY["Route to Proxy\n(MCP / LLM / Telegram\nHTTP / Web / SSH)"]

    RESP_PII{"Scan Response\nfor PII"}
    RESP_REDACT["Redact PII\nin response"]

    LED["Audit Ledger\nSHA-256 hash chain\nSQLite storage"]

    RESP["Return Response\nto Bot"]

    REQ --> AUTH
    AUTH -->|Invalid| AUTH_FAIL
    AUTH -->|Valid| RATE
    RATE -->|Exceeded| RATE_FAIL
    RATE -->|OK| NORM
    NORM --> PII
    PII -->|PII found + mode=enforce + action=redact| PII_ENFORCE
    PII -->|PII found + mode=enforce + action=block| PII_BLOCK
    PII_ENFORCE --> PG
    PII -->|Clean / Monitor mode| PG
    PG -->|Injection detected + enforce| PG_FAIL
    PG -->|Clean| TRUST
    TRUST -->|Trust too low| TRUST_FAIL
    TRUST -->|OK| EG
    EG -->|Blocked + enforce| EG_FAIL
    EG -->|Allowed| PIPE
    PIPE --> AQ
    AQ -->|Needs approval| AQ_WAIT
    AQ -->|Auto-approved| PROXY
    PROXY --> RESP_PII
    RESP_PII -->|PII in response| RESP_REDACT
    RESP_REDACT --> LED
    RESP_PII -->|Clean| LED
    LED --> RESP

    style AUTH_FAIL fill:#ff6b6b,color:#fff
    style RATE_FAIL fill:#ff6b6b,color:#fff
    style PII_BLOCK fill:#ff6b6b,color:#fff
    style PG_FAIL fill:#ff6b6b,color:#fff
    style TRUST_FAIL fill:#ff6b6b,color:#fff
    style EG_FAIL fill:#ff6b6b,color:#fff
    style AQ_WAIT fill:#ffa500,color:#fff
    style PII_ENFORCE fill:#ffd700,color:#000
    style RESP_REDACT fill:#ffd700,color:#000
```

---

## Layer Reference

| Layer | File | Default Mode | Block Code |
|-------|------|-------------|-----------|
| Auth | `auth.py` | Always enforce | 401 |
| Rate Limit | `middleware.py` | Always enforce | 429 |
| Input Norm | `input_normalizer.py` | Always | N/A |
| PII Sanitizer | `sanitizer.py` | Enforce (redact) | N/A (redacts) |
| Prompt Guard | `prompt_guard.py` | Enforce | 400 |
| Trust Manager | `trust_manager.py` | Enforce | 403 |
| Egress Filter | `egress_filter.py` | Enforce | 403 |
| Security Pipeline | `pipeline.py` | Enforce | 400/403 |
| Approval Queue | `enhanced_queue.py` | Enforce | 202 (wait) |

---

## Monitor Mode

When `AGENTSHROUD_MODE=monitor` (or per-module `mode: monitor`):
- Red failure paths become logs
- Request passes through
- Security events are recorded but not enforced

---

## Related Notes

- [[Data Flow]] — Narrative sequence diagram
- [[Proxy Layer/pipeline.py|pipeline.py]] — Pipeline orchestrator
- [[Architecture Overview]] — System-level view
- [[Diagrams/Full System Flowchart]] — Complete system diagram
