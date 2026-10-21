---
type: community
members: 56
---

# test_main_endpoints.py

**Members:** 56 nodes

## Members
- [[dot-setup_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Main Endpoints Integration Tests - P1 Middleware Wiring Tests for main.py…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Receive structured security alerts from gateway-internal scripts. Called by…]] - rationale - gateway/ingest_api/main.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test mcpproxy endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test approval queue endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAlertsLocalhostEnforcement]] - code - gateway/tests/test_main_endpoints.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[auth_dep()]] - code - gateway/ingest_api/main.py
- [[health_check_detail's per-bot inventory must key the Docker lookup by each…]] - rationale - gateway/tests/test_main_endpoints.py
- [[receive_security_alert()]] - code - gateway/ingest_api/main.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_main_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_main_endpoints.py (2)]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py (2)]]
- 2 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py (3)]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy()]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_GatewayEmailService]]

## Top bridge nodes
- [[test_main_endpoints.py]] - degree 21, connects to 7 communities
- [[auth_dep()]] - degree 14, connects to 6 communities
- [[receive_security_alert()]] - degree 6, connects to 2 communities
- [[dot-test_alerts_accepted_from_localhost()]] - degree 4, connects to 1 community
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - degree 2, connects to 1 community
