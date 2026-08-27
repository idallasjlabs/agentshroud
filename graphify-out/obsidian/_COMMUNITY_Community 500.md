---
type: community
members: 18
---

# Community 500

**Members:** 18 nodes

## Members
- [[.__init__()_157]] - code - gateway/tests/test_forward_routing.py
- [[._post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[.test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal app_state for owner-trust tests.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - rationale - gateway/tests/test_forward_routing.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id.]] - rationale - gateway/tests/test_forward_routing.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the         truste]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),         p]] - rationale - gateway/tests/test_forward_routing.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_trust_app_state()]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_500
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Community 167]]
- 3 edges to [[_COMMUNITY_Community 38]]
- 2 edges to [[_COMMUNITY_Community 754]]
- 1 edge to [[_COMMUNITY_Community 109]]

## Top bridge nodes
- [[_TrustCaptor]] - degree 13, connects to 3 communities
- [[TestOwnerTrustElevation]] - degree 10, connects to 3 communities
- [[_make_trust_app_state()]] - degree 6, connects to 3 communities