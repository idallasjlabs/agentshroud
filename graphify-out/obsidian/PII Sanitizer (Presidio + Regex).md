---
source_file: "docs/architecture/system-architecture.md"
type: "concept"
community: "Deployment Diagram (architecture)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Deployment_Diagram_architecture
---

# PII Sanitizer (Presidio + Regex)

## Connections
- [[Audit Ledger (SHA-256 hash only)]] - `calls` [EXTRACTED]
- [[Gateway (FastAPI)]] - `calls` [EXTRACTED]
- [[sanitizer.py (PII redaction, Presidioregex)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Deployment_Diagram_architecture