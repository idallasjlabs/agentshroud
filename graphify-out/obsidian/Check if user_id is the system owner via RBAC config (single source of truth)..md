---
source_file: "gateway/ingest_api/middleware.py"
type: "rationale"
community: "Egress & RBAC Security Core"
location: "L1079"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress__RBAC_Security_Core
---

# Check if user_id is the system owner via RBAC config (single source of truth).

## Connections
- [[._is_owner()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress__RBAC_Security_Core