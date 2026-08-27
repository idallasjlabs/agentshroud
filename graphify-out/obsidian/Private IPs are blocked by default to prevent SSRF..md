---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Community 53"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_53
---

# Private IPs are blocked by default to prevent SSRF.

## Connections
- [[.test_private_ip_blocked_ssrf()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_53