---
source_file: "gateway/ingest_api/middleware.py"
type: "rationale"
community: ".process_request"
location: "L1079"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/process_request
---

# Check if user_id is the system owner via RBAC config (single source of truth).

## Connections
- [[dot-_is_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/process_request
