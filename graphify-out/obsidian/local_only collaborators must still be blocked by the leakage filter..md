---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "rationale"
community: "check_upstream_cves"
location: "L9550"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/check_upstream_cves
---

# local_only collaborators must still be blocked by the leakage filter.

## Connections
- [[.test_default_collab_outbound_still_blocked_by_leakage_filter()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/check_upstream_cves