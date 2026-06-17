---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Egress Filter & Approval"
location: "L468"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__Approval
---

# _make_deny_all_filter()

## Connections
- [[EgressFilter_2]] - `references` [EXTRACTED]
- [[EgressFilter_1]] - `calls` [EXTRACTED]
- [[EgressFilterConfig]] - `calls` [EXTRACTED]
- [[EgressPolicy]] - `calls` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]
- [[test_grant_timed_approval_allows_domain()]] - `calls` [EXTRACTED]
- [[test_grant_timed_approval_cleans_stale_entries()]] - `calls` [EXTRACTED]
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - `calls` [EXTRACTED]
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - `calls` [EXTRACTED]
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__Approval