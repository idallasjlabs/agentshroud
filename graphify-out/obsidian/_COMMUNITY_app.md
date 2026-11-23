---
type: community
members: 73
---

# app

**Members:** 73 nodes

## Members
- [[dot-test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_alerts_rejected_from_non_localhost()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_email_send_routes_through_injectable_service()]] - code - gateway/tests/test_gateway_email_service.py
- [[dot-test_forward_middleware_error_handling()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[apialerts must reject non-localhost callers (S1 fix).]] - rationale - gateway/tests/test_main_endpoints.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Connection with correct token= query param is accepted and gets idle state.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with no token is rejected when auth is configured.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with wrong token= is closed (server returns no state frame).]] - rationale - gateway/tests/test_voice_gateway.py
- [[Create a test FastAPI app with version routes.]] - rationale - gateway/tests/test_version_routes.py
- [[External uptime monitors (e.g. UptimeRobot) probe with HEAD; a 405 makes a…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[No agent= param → _DEFAULT_AGENT is used for routing.]] - rationale - gateway/tests/test_voice_gateway.py
- [[POST emailsend to the owner sends via forward._email_service — proving the…]] - rationale - gateway/tests/test_gateway_email_service.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Sync TestClient for WebSocket tests_1]] - rationale - gateway/tests/test_security_fixes.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test approval queue endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware errors cause requests to be blocked.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAlertsLocalhostEnforcement]] - code - gateway/tests/test_main_endpoints.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestEndpointUsesService]] - code - gateway/tests/test_gateway_email_service.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[Tests that owner-bound email bypasses PII sanitisation. Root cause of the…]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[The very first frame after WS accept must be idle, not listening.]] - rationale - gateway/tests/test_voice_gateway.py
- [[When _VG_AUTH_TOKEN is empty, any connection is accepted (dev  backward…]] - rationale - gateway/tests/test_voice_gateway.py
- [[app()]] - code - gateway/tests/test_version_routes.py
- [[auth_dep()]] - code - gateway/ingest_api/main.py
- [[bypass_auth()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()]] - code - gateway/tests/test_dashboard.py
- [[client()_1]] - code - gateway/tests/test_e2e.py
- [[client()_2]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_3]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[client()_4]] - code - gateway/tests/test_security_fixes.py
- [[fixture_1]] - code
- [[fixture_2]] - code
- [[fixture_3]] - code
- [[fixture_4]] - code
- [[fixture_5]] - code
- [[send()]] - code - gateway/tests/test_gateway_email_service.py
- [[sync_client()]] - code - gateway/tests/test_dashboard.py
- [[sync_client()_1]] - code - gateway/tests/test_security_fixes.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[test_health_returns_ok()]] - code - gateway/tests/test_voice_gateway.py
- [[test_health_supports_head()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_correct_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_when_auth_not_configured()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_agent_query_param_absent_uses_default()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connect_sends_idle_first()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_missing_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_wrong_token()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/app
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 8 edges to [[_COMMUNITY_fastapi]]
- 8 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 7 edges to [[_COMMUNITY_AsyncMock]]
- 6 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_lifespan]]
- 4 edges to [[_COMMUNITY_test_forward_routing.py]]
- 3 edges to [[_COMMUNITY_test_channel_ownership.py]]
- 3 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 3 edges to [[_COMMUNITY_ingest_apimodels.py]]
- 3 edges to [[_COMMUNITY_asyncio_8]]
- 3 edges to [[_COMMUNITY_mock_stream]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_GatewayEmailService]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_TestScanParameterAllowlists]]
- 2 edges to [[_COMMUNITY_TestVersionRoutes]]
- 2 edges to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 1 edge to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 1 edge to [[_COMMUNITY_mcp_proxy.py]]
- 1 edge to [[_COMMUNITY_test_api_contract_fuzz.py]]
- 1 edge to [[_COMMUNITY_TestOpenAPIContract]]
- 1 edge to [[_COMMUNITY_TestEmailSend]]
- 1 edge to [[_COMMUNITY_test_chat_completions_alias.py]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY__TrustCaptor]]
- 1 edge to [[_COMMUNITY_dot-test_mcp_proxy_endpoint]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_test_v1_models_synthetic.py]]

## Top bridge nodes
- [[app()]] - degree 67, connects to 22 communities
- [[auth_dep()]] - degree 17, connects to 7 communities
- [[test_email_owner_bypasses_pii.py]] - degree 8, connects to 3 communities
- [[client()_1]] - degree 5, connects to 2 communities
- [[TestAlertsLocalhostEnforcement]] - degree 4, connects to 2 communities
