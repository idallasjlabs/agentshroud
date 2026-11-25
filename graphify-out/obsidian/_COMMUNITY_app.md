---
type: community
members: 126
---

# app

**Members:** 126 nodes

## Members
- [[dot-__init__()_4]] - code - gateway/tests/test_forward_routing.py
- [[dot-_post_forward()]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_inbound()]] - code - gateway/tests/test_forward_routing.py
- [[dot-process_outbound()]] - code - gateway/tests/test_forward_routing.py
- [[dot-setup_method()_1]] - code - gateway/tests/test_main_endpoints.py
- [[dot-teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_empty_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_empty_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_forward_middleware_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_forward_middleware_blocking()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_forward_middleware_error_handling()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_no_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_non_json_body_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_non_owner_user_id_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_owner_id_without_trusted_header_does_not_elevate_trust()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_owner_user_id_elevates_trust_to_full()]] - code - gateway/tests/test_forward_routing.py
- [[dot-test_passthrough_status_without_pipeline()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_requires_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_response_has_status_field()]] - code - gateway/tests/test_channel_ownership.py
- [[dot-test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_valid_payload_returns_200()]] - code - gateway/tests/test_channel_ownership.py
- [[A collaborator's user_id must NOT trigger the owner elevation.]] - rationale - gateway/tests/test_forward_routing.py
- [[Alias for hermes v0.16.0's OpenAI client. POST chatcompletions (no v1…]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[An empty string user_id must not match the owner.]] - rationale - gateway/tests/test_forward_routing.py
- [[Authentication dependency for protected endpoints]] - rationale - gateway/ingest_api/main.py
- [[Create a test FastAPI app with version routes.]] - rationale - gateway/tests/test_version_routes.py
- [[Empty payload is handled gracefully (skipped, not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Fully initialized async client with lifespan.]] - rationale - gateway/tests/test_e2e.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Main Endpoints Integration Tests - P1 Middleware Wiring Tests for main.py…]] - rationale - gateway/tests/test_main_endpoints.py
- [[Malformed body is handled defensively (empty dict fallback).]] - rationale - gateway/tests/test_channel_ownership.py
- [[Pipeline mock that records the user_trust_level passed to process_outbound.…]] - rationale - gateway/tests/test_forward_routing.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression don't break the existing v1messages path.]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[Requests with no user_id must not be elevated to FULL.]] - rationale - gateway/tests/test_forward_routing.py
- [[Response always includes a 'status' field.]] - rationale - gateway/tests/test_channel_ownership.py
- [[SCRUM-46 verify forward.py elevates trust to FULL for the owner's user_id. The…]] - rationale - gateway/tests/test_forward_routing.py
- [[Standard Telegram message payload is accepted.]] - rationale - gateway/tests/test_channel_ownership.py
- [[Sync TestClient for WebSocket tests]] - rationale - gateway/tests/test_dashboard.py
- [[Sync TestClient for WebSocket tests_1]] - rationale - gateway/tests/test_security_fixes.py
- [[Synthetic v1modelsid response so hermes v0.16.0 preflight succeeds. The…]] - rationale - gateway/tests/test_v1_models_synthetic.py
- [[Test forward endpoint with middleware integration.]] - rationale - gateway/tests/test_main_endpoints.py
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
- [[Test that middleware allows requests when they pass checks.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware can block requests with HTTP 403.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware errors cause requests to be blocked.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestClient with a stubbed proxy IP that passes the network allowlist.]] - rationale - gateway/tests/test_v1_models_synthetic.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestForwardEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestOwnerTrustElevation]] - code - gateway/tests/test_forward_routing.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestTelegramWebhook]] - code - gateway/tests/test_channel_ownership.py
- [[Tests for P3 Channel Ownership — Telegram webhook + email send. TDD red phase…]] - rationale - gateway/tests/test_channel_ownership.py
- [[Tests that owner-bound email bypasses PII sanitisation. Root cause of the…]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[WS-E SCRUM-7374 a spoofed owner user_id in the body WITHOUT the trusted…]] - rationale - gateway/tests/test_forward_routing.py
- [[When request.user_id matches _owner_user_id (with the trusted header),…]] - rationale - gateway/tests/test_forward_routing.py
- [[Without a pipeline configured, status is passthrough (not error).]] - rationale - gateway/tests/test_channel_ownership.py
- [[_TrustCaptor]] - code - gateway/tests/test_forward_routing.py
- [[app()]] - code - gateway/tests/test_version_routes.py
- [[auth_dep()]] - code - gateway/ingest_api/main.py
- [[bypass_auth()]] - code - gateway/tests/test_channel_ownership.py
- [[bypass_auth()_1]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()]] - code - gateway/tests/test_channel_ownership.py
- [[client()_1]] - code - gateway/tests/test_chat_completions_alias.py
- [[client()_2]] - code - gateway/tests/test_dashboard.py
- [[client()_3]] - code - gateway/tests/test_e2e.py
- [[client()_4]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[client()_5]] - code - gateway/tests/test_security_fixes.py
- [[client()_6]] - code - gateway/tests/test_v1_models_synthetic.py
- [[fixture_2]] - code
- [[fixture_3]] - code
- [[fixture_4]] - code
- [[fixture_5]] - code
- [[fixture_6]] - code
- [[fixture_7]] - code
- [[fixture_8]] - code
- [[parametrize]] - code
- [[sync_client()]] - code - gateway/tests/test_dashboard.py
- [[sync_client()_1]] - code - gateway/tests/test_security_fixes.py
- [[test_channel_ownership.py]] - code - gateway/tests/test_channel_ownership.py
- [[test_chat_completions_alias.py]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_passes_correct_path_to_proxy()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_routes_to_v1_path()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_email_owner_bypasses_pii.py]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[test_get_chat_completions_alias_also_routes()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py
- [[test_root_v1_messages_still_works_unchanged()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_v1_messages_still_goes_through_proxy()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_get_returns_synthetic_200()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_post_still_goes_through_proxy()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_synthetic.py]] - code - gateway/tests/test_v1_models_synthetic.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/app
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AgentTarget]]
- 12 edges to [[_COMMUNITY_ingest_apimain.py]]
- 10 edges to [[_COMMUNITY_AsyncMock]]
- 10 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 8 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 6 edges to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 4 edges to [[_COMMUNITY_lifespan]]
- 3 edges to [[_COMMUNITY_MiddlewareResult]]
- 3 edges to [[_COMMUNITY_TestStreamingProxyStatusPropagation]]
- 3 edges to [[_COMMUNITY_fastapi]]
- 3 edges to [[_COMMUNITY_GatewayEmailService]]
- 3 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 3 edges to [[_COMMUNITY_asyncio_8]]
- 3 edges to [[_COMMUNITY_mock_stream]]
- 2 edges to [[_COMMUNITY_TestEmailSend]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_TestOwnerEmailBypassesPii]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_dot-_run_proxy]]
- 1 edge to [[_COMMUNITY_fixture_1]]
- 1 edge to [[_COMMUNITY_version_routes.py]]
- 1 edge to [[_COMMUNITY_test_api_contract_fuzz.py]]
- 1 edge to [[_COMMUNITY_TestOpenAPIContract]]
- 1 edge to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_asyncio_7]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[app()]] - degree 67, connects to 18 communities
- [[test_main_endpoints.py]] - degree 25, connects to 8 communities
- [[auth_dep()]] - degree 17, connects to 5 communities
- [[test_channel_ownership.py]] - degree 9, connects to 3 communities
- [[test_email_owner_bypasses_pii.py]] - degree 8, connects to 3 communities
