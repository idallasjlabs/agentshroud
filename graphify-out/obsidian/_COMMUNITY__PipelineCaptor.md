---
type: community
cohesion: 0.07
members: 49
---

# _PipelineCaptor

**Cohesion:** 0.07 - loosely connected
**Members:** 49 nodes

## Members
- [[dot-__init__()_16]] - code - gateway/tests/test_forward_routing.py
- [[dot-__init__()_17]] - code - gateway/tests/test_forward_routing.py
- [[dot-_post()]] - code - gateway/tests/test_forward_routing.py
- [[dot-_post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[dot-_run_forward()]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()_1]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_1]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_agent_id_propagated_for_hermes()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_agent_id_propagated_for_openclaw()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_body_owner_id_with_matching_trusted_header_is_honored()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_body_owner_id_without_trusted_header_is_stripped()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_default_not_used_in_pipeline()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_forward_passes_user_id_in_metadata_to_process_inbound()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_non_owner_body_user_id_passes_through()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[A non-owner user_id is not a spoof risk and must pass through unchanged]] - rationale - gateway/tests/test_forward_routing.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Build a minimal mock app_state that returns a target with the given bot name.]] - rationale - gateway/tests/test_forward_routing.py
- [[Legitimate voice-gateway path owner ID in body + matching trusted         heade]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal app_state for owner-trust tests.]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal pipeline mock that records which agent_id it was called with.]] - rationale - gateway/tests/test_forward_routing.py
- [[Owner ID claimed in the body with NO trusted header must not reach the         p]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'hermes' as agent_id when routed to hermes.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'openclaw' as agent_id when routed to openclaw.]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression 'default' must never appear in agent_id when a named target is resol]] - rationale - gateway/tests/test_forward_routing.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id.]] - rationale - gateway/tests/test_forward_routing.py
- [[TestAgentIdPropagatedFromTarget]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerSpoofingViaForwardBody]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[Verify that the resolved target.name is used as agent_id in pipeline calls.]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a body-supplied user_id must NOT grant owner identity     to t]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the         truste]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),         p]] - rationale - gateway/tests/test_forward_routing.py
- [[_PipelineCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_mock_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[_make_trust_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[forward-routing agent_id propagation into security pipeline]] - code - gateway/ingest_api/routes/forward.py
- [[process_inbound must receive metadata={'user_id' ...} from forward so that]] - rationale - gateway/tests/test_forward_routing.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_PipelineCaptor
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_ForwardRequest]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_forward.py]]

## Top bridge nodes
- [[test_forward_routing.py]] - degree 13, connects to 3 communities
- [[_PipelineCaptor]] - degree 16, connects to 2 communities
- [[_TrustCaptor]] - degree 13, connects to 2 communities
- [[TestOwnerTrustElevation]] - degree 10, connects to 2 communities
- [[_make_mock_app_state()]] - degree 9, connects to 2 communities
