---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "EgressFilterConfig (2)"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressFilterConfig_2
---

# Private IPs are blocked by default to prevent SSRF.

## Connections
- [[dot-test_private_ip_blocked_ssrf()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressFilterConfig_2
