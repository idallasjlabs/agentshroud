---
source_file: "gateway/tests/test_audit_export.py"
type: "rationale"
community: "Community 254"
location: "L433"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_254
---

# Two stores sharing one SQLite file (e.g. two workers) must not fork the chain.

## Connections
- [[.test_concurrent_log_event_two_connections_keeps_linear_chain()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_254