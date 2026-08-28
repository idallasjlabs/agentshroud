---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Community 98"
location: "L134"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_98
---

# Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check).

## Connections
- [[.test_private_ip_allowed_if_in_policy_allowlist()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_98