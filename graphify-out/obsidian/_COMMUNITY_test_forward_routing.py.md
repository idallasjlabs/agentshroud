---
type: community
members: 37
---

# test_forward_routing.py

**Members:** 37 nodes

## Members
- [[dot-__init__()_138]] - code - gateway/tests/test_forward_routing.py
- [[dot-_post()]] - code - gateway/tests/test_forward_routing.py
- [[dot-_run_forward()]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()_4]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_agent_id_propagated_for_hermes()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_agent_id_propagated_for_openclaw()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_body_owner_id_with_matching_trusted_header_is_honored()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_body_owner_id_without_trusted_header_is_stripped()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_default_not_used_in_pipeline()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_forward_passes_user_id_in_metadata_to_process_inbound()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_non_owner_body_user_id_passes_through()]] - code - gateway/tests/test_forward_routing.py
- [[A non-owner user_id is not a spoof risk and must pass through unchanged (it…]] - rationale - gateway/tests/test_forward_routing.py
- [[Build a minimal mock app_state that returns a target with the given bot name.]] - rationale - gateway/tests/test_forward_routing.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Legitimate voice-gateway path owner ID in body + matching trusted header must…]] - rationale - gateway/tests/test_forward_routing.py
- [[Minimal pipeline mock that records which agent_id it was called with.]] - rationale - gateway/tests/test_forward_routing.py
- [[Owner ID claimed in the body with NO trusted header must not reach the pipeline…]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'hermes' as agent_id when routed to hermes.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'openclaw' as agent_id when routed to openclaw.]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression 'default' must never appear in agent_id when a named target is…]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression forward returned out_result.sanitized_message without checking…]] - rationale - gateway/tests/test_forward_routing.py
- [[TestAgentIdPropagatedFromTarget]] - code - gateway/tests/test_forward_routing.py
- [[TestOutboundBlockedNotDelivered]] - code - gateway/tests/test_forward_routing.py
- [[TestOwnerSpoofingViaForwardBody]] - code - gateway/tests/test_forward_routing.py
- [[Tests proving that agent_id=target.name (not default) flows into the security…]] - rationale - gateway/tests/test_forward_routing.py
- [[Verify that the resolved target.name is used as agent_id in pipeline calls.]] - rationale - gateway/tests/test_forward_routing.py
- [[WS-E SCRUM-7374 a body-supplied user_id must NOT grant owner identity to the…]] - rationale - gateway/tests/test_forward_routing.py
- [[_BlockedOutboundPipeline]] - code - gateway/tests/test_forward_routing.py
- [[_PipelineCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_mock_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[_passthrough_block_credentials()]] - code - gateway/tests/test_forward_routing.py
- [[process_inbound must receive metadata={'user_id' ...} from forward so that…]] - rationale - gateway/tests/test_forward_routing.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_forward_routingpy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_AgentTarget]]
- 4 edges to [[_COMMUNITY_app]]
- 3 edges to [[_COMMUNITY_TestConfigValidation]]
- 3 edges to [[_COMMUNITY__TrustCaptor]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_ingest_apimodels.py]]

## Top bridge nodes
- [[test_forward_routing.py]] - degree 14, connects to 4 communities
- [[dot-test_blocked_outbound_replaced_with_policy_notice()]] - degree 6, connects to 3 communities
- [[TestAgentIdPropagatedFromTarget]] - degree 9, connects to 2 communities
- [[_make_mock_app_state()]] - degree 9, connects to 2 communities
- [[dot-test_agent_id_propagated_for_openclaw()]] - degree 6, connects to 2 communities
