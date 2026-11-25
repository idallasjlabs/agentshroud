---
source_file: "gateway/soc/event_adapter.py"
type: "code"
community: "Severity"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Severity
---

# from_audit_chain_entry()

## Connections
- [[dot-severity()]] - `indirect_call` [INFERRED]
- [[Any_35]] - `references` [EXTRACTED]
- [[Convert AuditEvent (from AuditStore) to SecurityEvent. AuditEvent fields…]] - `rationale_for` [EXTRACTED]
- [[SecurityEvent]] - `calls` [EXTRACTED]
- [[_map_severity()]] - `calls` [EXTRACTED]
- [[collect_recent_events()]] - `calls` [EXTRACTED]
- [[event_adapter.py]] - `contains` [EXTRACTED]
- [[timestamp()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Severity
