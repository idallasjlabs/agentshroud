---
source_file: "gateway/security/audit_archive.py"
type: "rationale"
community: "Architecture Docs"
location: "L53"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Architecture_Docs
---

# Move audit_events older than cutoff_days into archive_path, then delete + VACUUM

## Connections
- [[archive_old_events()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Architecture_Docs