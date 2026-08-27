---
type: community
members: 31
---

# Community 167

**Members:** 31 nodes

## Members
- [[.__init__()_156]] - code - gateway/tests/test_forward_routing.py
- [[._post()]] - code - gateway/tests/test_forward_routing.py
- [[._run_forward()]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_5]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_5]] - code - gateway/tests/test_forward_routing.py
- [[.test_agent_id_propagated_for_hermes()]] - code - gateway/tests/test_forward_routing.py
- [[.test_agent_id_propagated_for_openclaw()]] - code - gateway/tests/test_forward_routing.py
- [[.test_body_owner_id_with_matching_trusted_header_is_honored()]] - code - gateway/tests/test_forward_routing.py
- [[.test_body_owner_id_without_trusted_header_is_stripped()]] - code - gateway/tests/test_forward_routing.py
- [[.test_default_not_used_in_pipeline()]] - code - gateway/tests/test_forward_routing.py
- [[.test_forward_passes_user_id_in_metadata_to_process_inbound()]] - code - gateway/tests/test_forward_routing.py
- [[.test_non_owner_body_user_id_passes_through()]] - code - gateway/tests/test_forward_routing.py
- [[A non-owner user_id is not a spoof risk and must pass through unchanged]] - rationale - gateway/tests/test_forward_routing.py
- [[Build a minimal mock app_state that returns a target with the given bot name.]] - rationale - gateway/tests/test_forward_routing.py
- [[Legitimate voice-gateway path owner ID in body + matching trusted         heade]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal pipeline mock that records which agent_id it was called with.]] - rationale - gateway/tests/test_forward_routing.py
- [[Owner ID claimed in the body with NO trusted header must not reach the         p]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'hermes' as agent_id when routed to hermes.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'openclaw' as agent_id when routed to openclaw.]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression 'default' must never appear in agent_id when a named target is resol]] - rationale - gateway/tests/test_forward_routing.py
- [[TestAgentIdPropagatedFromTarget]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerSpoofingViaForwardBody]] - code - gateway/tests/test_forward_routing.py
- [[Verify that the resolved target.name is used as agent_id in pipeline calls.]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a body-supplied user_id must NOT grant owner identity     to t]] - rationale - gateway/tests/test_forward_routing.py
- [[_PipelineCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_mock_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[forward-routing agent_id propagation into security pipeline]] - code - gateway/ingest_api/routes/forward.py
- [[process_inbound must receive metadata={'user_id' ...} from forward so that]] - rationale - gateway/tests/test_forward_routing.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_167
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 38]]
- 5 edges to [[_COMMUNITY_Community 754]]
- 5 edges to [[_COMMUNITY_Community 500]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 35]]
- 1 edge to [[_COMMUNITY_Community 109]]

## Top bridge nodes
- [[test_forward_routing.py]] - degree 13, connects to 4 communities
- [[_PipelineCaptor]] - degree 16, connects to 2 communities
- [[_make_mock_app_state()]] - degree 9, connects to 2 communities
- [[TestAgentIdPropagatedFromTarget]] - degree 9, connects to 2 communities
- [[TestOwnerSpoofingViaForwardBody]] - degree 8, connects to 2 communities