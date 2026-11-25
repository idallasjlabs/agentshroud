---
type: community
members: 50
---

# test_canary.py

**Members:** 50 nodes

## Members
- [[dot-__init__()_223]] - code - gateway/proxy/forwarder.py
- [[dot-forward()_3]] - code - gateway/proxy/forwarder.py
- [[dot-get_stats()_19]] - code - gateway/proxy/forwarder.py
- [[dot-health_check()_5]] - code - gateway/proxy/forwarder.py
- [[dot-set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[dot-to_dict()_14]] - code - gateway/security/canary.py
- [[Any_84]] - code
- [[Any_85]] - code
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail proxy check with unhealthy forwarder.]] - rationale - gateway/tests/test_canary.py
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
- [[Forwards sanitized requests to the OpenClaw backend. In production, uses…]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system. Args pipeline SecurityPipeline instance…]] - rationale - gateway/security/canary.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Tests for the canary verification system.]] - rationale - gateway/tests/test_canary.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[asyncio_85]] - code
- [[canary.py_2]] - code - gateway/security/canary.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[fixture_136]] - code
- [[forwarder.py_2]] - code - gateway/proxy/forwarder.py
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
TABLE source_file, type FROM #community/test_canarypy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 4 edges to [[_COMMUNITY_PIISanitizer]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]
- 1 edge to [[_COMMUNITY_TrustLevel]]

## Top bridge nodes
- [[test_canary.py]] - degree 27, connects to 7 communities
- [[canary_pipeline()]] - degree 7, connects to 4 communities
- [[run_canary()]] - degree 15, connects to 3 communities
- [[HTTPForwarder]] - degree 13, connects to 1 community
- [[ForwarderConfig]] - degree 9, connects to 1 community
