---
type: community
cohesion: 0.06
members: 47
---

# test_e2e_proxy.py

**Cohesion:** 0.06 - loosely connected
**Members:** 47 nodes

## Members
- [[dot-__init__()_169]] - code - gateway/proxy/forwarder.py
- [[dot-forward()_3]] - code - gateway/proxy/forwarder.py
- [[dot-get_stats()_16]] - code - gateway/proxy/forwarder.py
- [[dot-health_check()_4]] - code - gateway/proxy/forwarder.py
- [[dot-is_healthy()]] - code - gateway/proxy/forwarder.py
- [[dot-last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[dot-set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[dot-to_dict()_11]] - code - gateway/security/canary.py
- [[Any_66]] - code - gateway/proxy/forwarder.py
- [[Any_67]] - code - gateway/security/canary.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult_2]] - code - gateway/security/canary.py
- [[Check if the OpenClaw backend is healthy.]] - rationale - gateway/proxy/forwarder.py
- [[Configuration for the HTTP forwarder.]] - rationale - gateway/proxy/forwarder.py
- [[Forward a request to the OpenClaw backend.]] - rationale - gateway/proxy/forwarder.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[forwarder()_1]] - code - gateway/tests/test_e2e_proxy.py
- [[forwarder.py]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[run_canary()]] - code - gateway/security/canary.py
- [[test_canary.py]] - code - gateway/tests/test_canary.py
- [[test_canary_fails_without_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_message_contains_fake_pii()]] - code - gateway/tests/test_canary.py
- [[test_canary_passes_with_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_result_serialization()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_audit_chain()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_pii_stripping()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_forwarder_error_handling()]] - code - gateway/tests/test_e2e_proxy.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2e_proxypy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_EgressFilterConfig_2]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor_1]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_egress_filter.py_3]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_AgentTarget_1]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]

## Top bridge nodes
- [[test_canary.py]] - degree 21, connects to 7 communities
- [[run_canary()]] - degree 20, connects to 6 communities
- [[HTTPForwarder]] - degree 21, connects to 4 communities
- [[ForwarderConfig]] - degree 11, connects to 1 community
- [[test_forwarder_error_handling()]] - degree 5, connects to 1 community
