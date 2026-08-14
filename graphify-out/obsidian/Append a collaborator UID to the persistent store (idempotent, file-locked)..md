---
source_file: "gateway/security/rbac_config.py"
type: "rationale"
community: "Enhanced Approval Queue"
location: "L372"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Enhanced_Approval_Queue
---

# Append a collaborator UID to the persistent store (idempotent, file-locked).

## Connections
- [[persist_approved_collaborator()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Enhanced_Approval_Queue