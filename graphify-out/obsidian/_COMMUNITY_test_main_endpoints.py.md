---
type: community
cohesion: 0.03
members: 83
---

# test_main_endpoints.py

**Cohesion:** 0.03 - loosely connected
**Members:** 83 nodes

## Members
- [[dot-_mock_websocket()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-setup_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_connects_to_bridge_port_with_ws_scheme_and_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_relays_text_and_bytes_both_directions()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_path_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_query_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_upstream_connect_failure_closes_gracefully()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[A deadunreachable bridge must not raise out of the route -- it closes the…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Main Endpoints Integration Tests - P1 Middleware Wiring Tests for main.py…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Receive structured security alerts from gateway-internal scripts. Called by…]] - rationale - gateway/ingest_api/main.py
- [[Relay the Hermes dashboard's WebSocket channels (apiws, apipub) through the…]] - rationale - gateway/ingest_api/main.py
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
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardWsProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[Upstream URL must be ws (not http) at the bridge port, with the client's…]] - rationale - gateway/tests/test_main_endpoints.py
- [[WebSocket relay for Slack Socket Mode inbound traffic. Bot connects here…]] - rationale - gateway/ingest_api/main.py
- [[_bot_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_client_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_empty_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_one_frame_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_upstream_to_bot()]] - code - gateway/ingest_api/main.py
- [[_upstream_to_client()]] - code - gateway/ingest_api/main.py
- [[asyncio]] - code
- [[auth_dep()]] - code - gateway/ingest_api/main.py
- [[health_check_detail's per-bot inventory must key the Docker lookup by each…]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in query string.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_ws_proxy()]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy WebSocket counterpart of hermes_dashboard_proxy.…]] - rationale - gateway/tests/test_main_endpoints.py
- [[receive_security_alert()]] - code - gateway/ingest_api/main.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py
- [[websocket_4]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_main_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 5 edges to [[_COMMUNITY_Request]]
- 2 edges to [[_COMMUNITY_forward.py]]
- 2 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 1 edge to [[_COMMUNITY_TestForwardEndpoint]]
- 1 edge to [[_COMMUNITY_TestGoogleAPIProxy]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_GatewayEmailService]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[auth_dep()]] - degree 14, connects to 6 communities
- [[test_main_endpoints.py]] - degree 20, connects to 5 communities
- [[asyncio]] - degree 11, connects to 2 communities
- [[receive_security_alert()]] - degree 6, connects to 2 communities
- [[hermes_dashboard_ws_proxy()]] - degree 11, connects to 1 community
