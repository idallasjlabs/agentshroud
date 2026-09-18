---
source_file: "docs/architecture/system-architecture.md"
type: "concept"
community: "ADR-001: Transparent Proxy Decision"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/ADR-001_Transparent_Proxy_Decision
---

# PII Sanitizer (Presidio + Regex)

## Connections
- [[Audit Ledger (SHA-256 hash only)]] - `calls` [EXTRACTED]
- [[Gateway (FastAPI)]] - `calls` [EXTRACTED]
- [[sanitizer.py (PII redaction, Presidioregex)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/ADR-001_Transparent_Proxy_Decision