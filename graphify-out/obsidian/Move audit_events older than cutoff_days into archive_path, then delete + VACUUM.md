---
source_file: "gateway/security/audit_archive.py"
type: "rationale"
community: "AgentShroud Device Pairing Management"
location: "L53"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/AgentShroud_Device_Pairing_Management
---

# Move audit_events older than cutoff_days into archive_path, then delete + VACUUM

## Connections
- [[archive_old_events()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/AgentShroud_Device_Pairing_Management