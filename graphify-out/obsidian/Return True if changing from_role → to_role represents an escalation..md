---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "ingest_api/main.py"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/ingest_api/mainpy
---

# Return True if changing from_role → to_role represents an escalation.

## Connections
- [[.is_privilege_escalation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/ingest_api/mainpy