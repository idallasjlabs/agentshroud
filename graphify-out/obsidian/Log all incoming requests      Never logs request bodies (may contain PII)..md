---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "Ingest API & RBAC Core"
location: "L332"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Ingest_API__RBAC_Core
---

# Log all incoming requests      Never logs request bodies (may contain PII).

## Connections
- [[log_requests()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Ingest_API__RBAC_Core