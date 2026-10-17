---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "EgressFilterConfig (2)"
location: "L111"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressFilterConfig_2
---

# TestIPRules

## Connections
- [[dot-test_allowed_cidr()]] - `method` [EXTRACTED]
- [[dot-test_allowed_ip()]] - `method` [EXTRACTED]
- [[dot-test_ipv4_mapped_ipv6_blocked()]] - `method` [EXTRACTED]
- [[dot-test_localhost_hostname_blocked()]] - `method` [EXTRACTED]
- [[dot-test_private_ip_allowed_if_in_policy_allowlist()]] - `method` [EXTRACTED]
- [[dot-test_private_ip_blocked_ssrf()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_2]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[IP allowlist and private-IP SSRF protection.]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressFilterConfig_2
