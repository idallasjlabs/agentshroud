---
type: community
cohesion: 0.06
members: 44
---

# Module Group 92

**Cohesion:** 0.06 - loosely connected
**Members:** 44 nodes

## Members
- [[.__init__()_14]] - code - gateway/proxy/forwarder.py
- [[.forward()]] - code - gateway/proxy/forwarder.py
- [[.get_stats()_2]] - code - gateway/proxy/forwarder.py
- [[.health_check()_1]] - code - gateway/proxy/forwarder.py
- [[.is_healthy()]] - code - gateway/proxy/forwarder.py
- [[.last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[.set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[Any_10]] - code - gateway/proxy/forwarder.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail proxy check with unhealthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[Check if the OpenClaw backend is healthy.]] - rationale - gateway/proxy/forwarder.py
- [[Configuration for the HTTP forwarder.]] - rationale - gateway/proxy/forwarder.py
- [[Forward a request to the OpenClaw backend.]] - rationale - gateway/proxy/forwarder.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - rationale - gateway/proxy/forwarder.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[canary.py]] - code - gateway/security/canary.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[forwarder()]] - code - gateway/tests/test_e2e_proxy.py
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
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_92
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Sidecar Security Scanner]]
- 4 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 3 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 2 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 2 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]

## Top bridge nodes
- [[test_canary.py]] - degree 19, connects to 4 communities
- [[canary_pipeline()]] - degree 6, connects to 4 communities
- [[run_canary()]] - degree 14, connects to 2 communities
- [[HTTPForwarder]] - degree 17, connects to 1 community
- [[ForwarderConfig]] - degree 11, connects to 1 community
