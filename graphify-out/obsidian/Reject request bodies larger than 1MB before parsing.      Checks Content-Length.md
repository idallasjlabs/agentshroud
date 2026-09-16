---
source_file: "gateway/ingest_api/main.py"
type: "rationale"
community: "Ingest API & RBAC Core"
location: "L276"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Ingest_API__RBAC_Core
---

# Reject request bodies larger than 1MB before parsing.      Checks Content-Length

## Connections
- [[limit_request_body()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Ingest_API__RBAC_Core