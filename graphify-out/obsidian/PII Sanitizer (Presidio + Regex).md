---
source_file: "docs/architecture/system-architecture.md"
type: "concept"
community: "ADR-007: Zero-Config Security (docker-compose up = fully secured)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/ADR-007_Zero-Config_Security_docker-compose_up__fully_secured
---

# PII Sanitizer (Presidio + Regex)

## Connections
- [[Audit Ledger (SHA-256 hash only)]] - `calls` [EXTRACTED]
- [[Gateway (FastAPI)]] - `calls` [EXTRACTED]
- [[sanitizer.py (PII redaction, Presidioregex)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/ADR-007_Zero-Config_Security_docker-compose_up__fully_secured
