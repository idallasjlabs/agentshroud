---
source_file: "gateway/tests/test_audit_archive.py"
type: "rationale"
community: "purge_low_value_events()"
location: "L285"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/purge_low_value_events
---

# n_noisy events of (egress_filter, INFO); n_denies of (egress_filter, HIGH);

## Connections
- [[_make_mixed_live_db()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/purge_low_value_events