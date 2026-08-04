---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Egress Filter & Approval"
location: "L134"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Filter__Approval
---

# Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).

## Connections
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Filter__Approval
