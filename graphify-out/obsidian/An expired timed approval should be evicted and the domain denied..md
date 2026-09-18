---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "EgressPolicy"
location: "L543"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressPolicy
---

# An expired timed approval should be evicted and the domain denied.

## Connections
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressPolicy