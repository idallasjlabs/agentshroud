---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Community 282"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_282
---

# Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row/32GB unbounded growth)

## Connections
- [[EgressFilter_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_282