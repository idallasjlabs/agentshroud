---
source_file: "docs/architecture/system-architecture.md"
type: "concept"
community: "AgentShroud (system, C4 context)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/AgentShroud_system_C4_context
---

# PII Sanitizer (Presidio + Regex)

## Connections
- [[Audit Ledger (SHA-256 hash only)]] - `calls` [EXTRACTED]
- [[Gateway (FastAPI)]] - `calls` [EXTRACTED]
- [[sanitizer.py (PII redaction, Presidioregex)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/AgentShroud_system_C4_context
