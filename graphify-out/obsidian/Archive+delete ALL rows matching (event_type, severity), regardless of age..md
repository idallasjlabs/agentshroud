---
source_file: "gateway/security/audit_archive.py"
type: "rationale"
community: "purge_low_value_events()"
location: "L159"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/purge_low_value_events
---

# Archive+delete ALL rows matching (event_type, severity), regardless of age.

## Connections
- [[purge_low_value_events()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/purge_low_value_events