---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L360"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Log privilege changes; emit WARNING for escalations (unusual patterns).

## Connections
- [[.audit_privilege_change()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy