---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "EgressPolicy"
location: "L446"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressPolicy
---

# EgressFilter must call notifier when blocking an unknown domain.

## Connections
- [[test_egress_filter_notifies_on_deny()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressPolicy