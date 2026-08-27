---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Community 53"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_53
---

# TestEnforceMode

## Connections
- [[.test_allowed_domain_passes()]] - `method` [EXTRACTED]
- [[.test_denied_domain_overrides_allow()]] - `method` [EXTRACTED]
- [[.test_port_not_allowed()]] - `method` [EXTRACTED]
- [[.test_unlisted_domain_blocked()]] - `method` [EXTRACTED]
- [[.test_wildcard_does_not_match_deep_subdomain()]] - `method` [EXTRACTED]
- [[.test_wildcard_matches_base_domain()]] - `method` [EXTRACTED]
- [[.test_wildcard_one_level()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilter in enforce mode should block unlisted destinations.]] - `rationale_for` [EXTRACTED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `semantically_similar_to` [INFERRED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_53