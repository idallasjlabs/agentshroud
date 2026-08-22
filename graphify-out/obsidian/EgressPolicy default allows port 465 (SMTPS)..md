---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Egress Filter"
location: "L588"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Filter
---

# EgressPolicy default allows port 465 (SMTPS).

## Connections
- [[.test_default_policy_allows_imaps()]] - `rationale_for` [EXTRACTED]
- [[.test_default_policy_allows_smtps()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Filter