---
type: community
members: 20
---

# _TrustCaptor

**Members:** 20 nodes

## Members
- [[dot-__init__()_219]] - code - gateway/tests/test_forward_routing.py
- [[dot-_post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()_8]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_6]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal app_state for owner-trust tests.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.…]] - rationale - gateway/tests/test_forward_routing.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id. The…]] - rationale - gateway/tests/test_forward_routing.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the trusted…]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),…]] - rationale - gateway/tests/test_forward_routing.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_trust_app_state()]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_TrustCaptor
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_forward_routing.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_app]]

## Top bridge nodes
- [[_make_trust_app_state()]] - degree 6, connects to 3 communities
- [[_TrustCaptor]] - degree 11, connects to 1 community
- [[TestOwnerTrustElevation]] - degree 8, connects to 1 community
- [[dot-_post_forward()]] - degree 8, connects to 1 community
