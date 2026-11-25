---
source_file: "gateway/soc/event_adapter.py"
type: "code"
community: "Severity"
location: "L203"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Severity
---

# collect_recent_events()

## Connections
- [[Any_35]] - `references` [EXTRACTED]
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - `rationale_for` [EXTRACTED]
- [[SecurityEvent]] - `uses` [INFERRED]
- [[Severity]] - `uses` [INFERRED]
- [[_map_severity()]] - `calls` [EXTRACTED]
- [[event_adapter.py]] - `contains` [EXTRACTED]
- [[from_audit_chain_entry()]] - `calls` [EXTRACTED]
- [[get_egress_log()]] - `calls` [EXTRACTED]
- [[get_security_events()]] - `calls` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Severity
