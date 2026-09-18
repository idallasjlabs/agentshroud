---
source_file: "gateway/tests/test_audit_archive.py"
type: "rationale"
community: "archive_old_events()"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/archive_old_events
---

# events: list of (event_id, timestamp, prev_hash, entry_hash).

## Connections
- [[_make_live_db()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/archive_old_events