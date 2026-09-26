---
source_file: "gateway/security/audit_store.py"
type: "rationale"
community: "load_config()"
location: "L298"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/load_config
---

# Return the most recent audit entries (alias for query_events with limit).

## Connections
- [[.get_recent_entries()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/load_config