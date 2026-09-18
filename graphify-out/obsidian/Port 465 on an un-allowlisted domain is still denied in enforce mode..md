---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "EgressPolicy"
location: "L635"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressPolicy
---

# Port 465 on an un-allowlisted domain is still denied in enforce mode.

## Connections
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressPolicy