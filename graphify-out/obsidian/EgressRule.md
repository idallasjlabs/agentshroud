---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "EgressApprovalQueue"
location: "L98"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressApprovalQueue
---

# EgressRule

## Connections
- [[dot-_check_existing_rule()]] - `references` [EXTRACTED]
- [[dot-_load_rules()]] - `calls` [EXTRACTED]
- [[dot-add_rule()]] - `calls` [EXTRACTED]
- [[dot-approve()]] - `calls` [EXTRACTED]
- [[dot-deny()]] - `calls` [EXTRACTED]
- [[dot-preload_permanent_rules()]] - `calls` [EXTRACTED]
- [[EgressApprovalQueue]] - `shares_data_with` [EXTRACTED]
- [[EgressScope]] - `references` [EXTRACTED]
- [[Represents an egress allowdeny rule.]] - `rationale_for` [EXTRACTED]
- [[egress_approval.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressApprovalQueue
