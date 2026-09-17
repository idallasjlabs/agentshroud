---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "EgressApprovalQueue"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressApprovalQueue
---

# egress_approval.py

## Connections
- [[ApprovalMode]] - `contains` [EXTRACTED]
- [[ApprovalResult]] - `contains` [EXTRACTED]
- [[EgressApprovalQueue]] - `contains` [EXTRACTED]
- [[EgressRequest]] - `contains` [EXTRACTED]
- [[EgressRule]] - `contains` [EXTRACTED]
- [[EgressScope]] - `contains` [EXTRACTED]
- [[Enum_3]] - `imports_from` [EXTRACTED]
- [[FR5 Restricted Data Flow]] - `references` [EXTRACTED]
- [[RiskLevel]] - `contains` [EXTRACTED]
- [[egress_config.py]] - `imports_from` [EXTRACTED]
- [[make_event()]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressApprovalQueue