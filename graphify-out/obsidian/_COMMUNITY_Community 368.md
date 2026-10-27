---
type: community
members: 27
---

# Community 368

**Members:** 27 nodes

## Members
- [[.__init__()_157]] - code - gateway/tests/test_forward_routing.py
- [[._post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[.test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[.test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[.test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal app_state for owner-trust tests.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression forward returned out_result.sanitized_message without checking]] - rationale - gateway/tests/test_forward_routing.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id.]] - rationale - gateway/tests/test_forward_routing.py
- [[TestOutboundBlockedNotDelivered]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the         truste]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),         p]] - rationale - gateway/tests/test_forward_routing.py
- [[_BlockedOutboundPipeline]] - code - gateway/tests/test_forward_routing.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_trust_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[forward-routing agent_id propagation into security pipeline]] - code - gateway/ingest_api/routes/forward.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_368
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 34]]
- 6 edges to [[_COMMUNITY_Community 325]]
- 5 edges to [[_COMMUNITY_Community 92]]
- 2 edges to [[_COMMUNITY_Community 37]]
- 1 edge to [[_COMMUNITY_Community 2154]]

## Top bridge nodes
- [[test_forward_routing.py]] - degree 13, connects to 4 communities
- [[_TrustCaptor]] - degree 13, connects to 3 communities
- [[TestOwnerTrustElevation]] - degree 10, connects to 2 communities
- [[_BlockedOutboundPipeline]] - degree 7, connects to 2 communities
- [[_make_trust_app_state()]] - degree 6, connects to 2 communities