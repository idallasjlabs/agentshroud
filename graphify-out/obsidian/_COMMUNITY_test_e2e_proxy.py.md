---
type: community
members: 73
---

# test_e2e_proxy.py

**Members:** 73 nodes

## Members
- [[dot-__init__()_161]] - code - gateway/proxy/forwarder.py
- [[dot-forward()_2]] - code - gateway/proxy/forwarder.py
- [[dot-get_stats()_15]] - code - gateway/proxy/forwarder.py
- [[dot-health_check()_5]] - code - gateway/proxy/forwarder.py
- [[dot-is_healthy()]] - code - gateway/proxy/forwarder.py
- [[dot-last_forward_time()]] - code - gateway/proxy/forwarder.py
- [[dot-set_response_handler()]] - code - gateway/proxy/forwarder.py
- [[dot-to_dict()_9]] - code - gateway/security/canary.py
- [[Any_64]] - code - gateway/proxy/forwarder.py
- [[Any_65]] - code - gateway/security/canary.py
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
- [[Forward content → PII sanitized → ledger entry created → event bus fired.]] - rationale - gateway/tests/test_e2e.py
- [[Forward without auth returns 401403.]] - rationale - gateway/tests/test_e2e.py
- [[ForwardResult]] - code - gateway/proxy/forwarder.py
- [[ForwarderConfig]] - code - gateway/proxy/forwarder.py
- [[Forwards sanitized requests to the OpenClaw backend.      In production, uses ai]] - rationale - gateway/proxy/forwarder.py
- [[GET dashboard without auth returns 403.]] - rationale - gateway/tests/test_e2e.py
- [[GET dashboardstats returns JSON stats.]] - rationale - gateway/tests/test_e2e.py
- [[GET status returns service info.]] - rationale - gateway/tests/test_e2e.py
- [[HTTPForwarder]] - code - gateway/proxy/forwarder.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Result of forwarding a request.]] - rationale - gateway/proxy/forwarder.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[Set a mock response handler for testing.]] - rationale - gateway/proxy/forwarder.py
- [[Submit SSH command → approval queued.]] - rationale - gateway/tests/test_e2e.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[Verify forwarder handles errors gracefully.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[canary-cron.sh embedded Python main()]] - code - scripts/canary-cron.sh
- [[canary.py]] - code - gateway/security/canary.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[fail()_3]] - code - scripts/verify-proxy.sh
- [[forwarder()]] - code - gateway/tests/test_e2e_proxy.py
- [[forwarder.py]] - code - gateway/proxy/forwarder.py
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[info()_1]] - code - scripts/verify-proxy.sh
- [[pass()_2]] - code - scripts/verify-proxy.sh
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
- [[test_dashboard_requires_auth()_1]] - code - gateway/tests/test_e2e.py
- [[test_dashboard_stats_returns_json()]] - code - gateway/tests/test_e2e.py
- [[test_e2e.py]] - code - gateway/tests/test_e2e.py
- [[test_forward_pii_sanitized_and_ledger_entry()]] - code - gateway/tests/test_e2e.py
- [[test_forward_without_auth_rejected()]] - code - gateway/tests/test_e2e.py
- [[test_forwarder_error_handling()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_ssh_submit_queues_approval()]] - code - gateway/tests/test_e2e.py
- [[test_status_endpoint()]] - code - gateway/tests/test_e2e.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_e2e_proxypy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 8 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 8 edges to [[_COMMUNITY_PipelineAction]]
- 5 edges to [[_COMMUNITY_ContextSegment]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (2)]]
- 1 edge to [[_COMMUNITY_ForwardRequest (2)]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_test_dashboard.py]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (3)]]
- 1 edge to [[_COMMUNITY_egress_filter.py (5)]]

## Top bridge nodes
- [[test_e2e.py]] - degree 13, connects to 6 communities
- [[test_canary.py]] - degree 21, connects to 5 communities
- [[HTTPForwarder]] - degree 21, connects to 4 communities
- [[run_canary()_1]] - degree 20, connects to 4 communities
- [[canary_pipeline()]] - degree 6, connects to 4 communities
