---
type: community
cohesion: 0.05
members: 62
---

# test_main_endpoints.py

**Cohesion:** 0.05 - loosely connected
**Members:** 62 nodes

## Members
- [[dot-_mock_websocket()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_accepted_from_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_backslash_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_connects_to_bridge_port_with_ws_scheme_and_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_dotdot_path_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_encoded_traversal_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mixed_case_encoded_rejected()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_proxy_returns_400_on_traversal_in_query()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_relays_text_and_bytes_both_directions()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_safe_path_passes()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_path_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_traversal_in_query_closes_without_connecting()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_upstream_connect_failure_closes_gracefully()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[A deadunreachable bridge must not raise out of the route -- it closes the…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Handler returns ok=True when called from 127.0.0.1.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Main Endpoints Integration Tests - P1 Middleware Wiring Tests for main.py…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Receive structured security alerts from gateway-internal scripts. Called by…]] - rationale - gateway/ingest_api/main.py
- [[Redirect bare hermes-dashboard to hermes-dashboard so assets resolve.]] - rationale - gateway/ingest_api/main.py
- [[Relay the Hermes dashboard's WebSocket channels (apiws, apipub) through the…]] - rationale - gateway/ingest_api/main.py
- [[Reverse-proxy the Hermes Agent dashboard through the gateway.]] - rationale - gateway/ingest_api/main.py
- [[Test mcpproxy endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAlertsLocalhostEnforcement]] - code - gateway/tests/test_main_endpoints.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardPathTraversal]] - code - gateway/tests/test_main_endpoints.py
- [[TestHermesDashboardWsProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[Upstream URL must be ws (not http) at the bridge port, with the client's…]] - rationale - gateway/tests/test_main_endpoints.py
- [[WebSocket relay for Slack Socket Mode inbound traffic. Bot connects here…]] - rationale - gateway/ingest_api/main.py
- [[_bot_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_client_to_upstream()]] - code - gateway/ingest_api/main.py
- [[_empty_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_one_frame_aiter()]] - code - gateway/tests/test_main_endpoints.py
- [[_upstream_to_bot()]] - code - gateway/ingest_api/main.py
- [[_upstream_to_client()]] - code - gateway/ingest_api/main.py
- [[asyncio_3]] - code
- [[health_check_detail's per-bot inventory must key the Docker lookup by each…]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_proxy must reject traversal sequences before forwarding.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_proxy raises HTTPException(400) for traversal in path.]] - rationale - gateway/tests/test_main_endpoints.py
- [[hermes_dashboard_root]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy (WebSocket relay)]] - code - gateway/ingest_api/main.py
- [[hermes_dashboard_ws_proxy WebSocket counterpart of hermes_dashboard_proxy.…]] - rationale - gateway/tests/test_main_endpoints.py
- [[receive_security_alert()]] - code - gateway/ingest_api/main.py
- [[slack_ws_relay()]] - code - gateway/ingest_api/main.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py
- [[websocket_8]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_main_endpointspy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 5 edges to [[_COMMUNITY_run-standalone.sh (Hermes docker run launcher)]]
- 4 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py_1]]
- 3 edges to [[_COMMUNITY_dot-_run_proxy()]]
- 1 edge to [[_COMMUNITY_TestForwardEndpoint]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py_2]]
- 1 edge to [[_COMMUNITY_TestGoogleAPIProxy]]
- 1 edge to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[test_main_endpoints.py]] - degree 21, connects to 8 communities
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - degree 16, connects to 4 communities
- [[hermes_dashboard_ws_proxy (WebSocket relay)]] - degree 14, connects to 2 communities
- [[receive_security_alert()]] - degree 6, connects to 2 communities
- [[hermes_dashboard_root]] - degree 4, connects to 2 communities
