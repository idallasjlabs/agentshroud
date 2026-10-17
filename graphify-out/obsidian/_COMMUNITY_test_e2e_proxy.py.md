---
type: community
members: 59
---

# test_e2e_proxy.py

**Members:** 59 nodes

## Members
- [[dot-__init__()_26]] - code - gateway/proxy/forwarder.py
- [[dot-forward()]] - code - gateway/proxy/forwarder.py
- [[dot-get_stats()_3]] - code - gateway/proxy/forwarder.py
- [[dot-health_check()]] - code - gateway/proxy/forwarder.py
- [[dot-is_healthy()]] - code - gateway/proxy/forwarder.py
- [[dot-last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[dot-set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[dot-to_dict()_3]] - code - gateway/security/canary.py
- [[Any_8]] - code - gateway/proxy/forwarder.py
- [[Any_9]] - code - gateway/security/canary.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
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
- [[canary-cron.sh embedded Python main()]] - code - scripts/canary-cron.sh
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[fail()]] - code - scripts/verify-proxy.sh
- [[forwarder()]] - code - gateway/tests/test_e2e_proxy.py
- [[forwarder.py]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[info()]] - code - scripts/verify-proxy.sh
- [[pass()]] - code - scripts/verify-proxy.sh
- [[run_bypass()]] - code - scripts/verify-proxy.sh
- [[run_canary()]] - code - scripts/verify-proxy.sh
- [[run_canary()_1]] - code - gateway/security/canary.py
- [[run_chain()]] - code - scripts/verify-proxy.sh
- [[run_full()]] - code - scripts/verify-proxy.sh
- [[run_quick()]] - code - scripts/verify-proxy.sh
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
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2e_proxypy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EgressFilterConfig (2)_1]]
- 8 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 8 edges to [[_COMMUNITY_AuditChain]]
- 5 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 5 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 1 edge to [[_COMMUNITY_egress_filter.py (5)]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)_1]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py (2)]]

## Top bridge nodes
- [[test_canary.py]] - degree 21, connects to 6 communities
- [[HTTPForwarder]] - degree 21, connects to 4 communities
- [[canary_pipeline()]] - degree 6, connects to 4 communities
- [[run_canary()_1]] - degree 20, connects to 3 communities
- [[run_canary()]] - degree 11, connects to 3 communities
