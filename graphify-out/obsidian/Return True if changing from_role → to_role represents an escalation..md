---
source_file: "gateway/security/rbac.py"
type: "rationale"
community: "Approval & FastAPI Ingest"
location: "L353"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Approval__FastAPI_Ingest
---

# Return True if changing from_role → to_role represents an escalation.

## Connections
- [[.is_privilege_escalation()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Approval__FastAPI_Ingest