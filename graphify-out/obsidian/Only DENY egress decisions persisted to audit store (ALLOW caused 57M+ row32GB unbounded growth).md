---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Egress Filter (security)"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Filter_security
---

# Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row/32GB unbounded growth)

## Connections
- [[EgressFilter_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Filter_security