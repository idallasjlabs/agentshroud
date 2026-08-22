---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Egress Filter"
location: "L635"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Egress_Filter
---

# Port 465 on an un-allowlisted domain is still denied in enforce mode.

## Connections
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Egress_Filter