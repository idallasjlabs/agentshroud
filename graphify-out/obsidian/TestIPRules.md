---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Egress Filter & Approval"
location: "L111"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__Approval
---

# TestIPRules

## Connections
- [[.test_allowed_cidr()]] - `method` [EXTRACTED]
- [[.test_allowed_ip()]] - `method` [EXTRACTED]
- [[.test_ipv4_mapped_ipv6_blocked()]] - `method` [EXTRACTED]
- [[.test_localhost_hostname_blocked()]] - `method` [EXTRACTED]
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - `method` [EXTRACTED]
- [[.test_private_ip_blocked_ssrf()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[IP allowlist and private-IP SSRF protection.]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__Approval
