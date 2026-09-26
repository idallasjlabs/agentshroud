---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Production Safety Checklist (SKILL)"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Production_Safety_Checklist_SKILL
---

# Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row/32GB unbounded growth)

## Connections
- [[EgressFilter_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Production_Safety_Checklist_SKILL