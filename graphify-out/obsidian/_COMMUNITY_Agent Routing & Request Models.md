---
type: community
cohesion: 0.02
members: 121
---

# Agent Routing & Request Models

**Cohesion:** 0.02 - loosely connected
**Members:** 121 nodes

## Members
- [[.__init__()_9]] - code - gateway/ingest_api/router.py
- [[.__init__()_117]] - code - gateway/tests/test_forward_routing.py
- [[._run_forward()]] - code - gateway/tests/test_forward_routing.py
- [[.health_check()]] - code - gateway/ingest_api/router.py
- [[.list_targets()]] - code - gateway/ingest_api/router.py
- [[.process_inbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_inbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_3]] - code - gateway/tests/test_forward_routing.py
- [[.process_outbound()_2]] - code - gateway/tests/test_forward_routing.py
- [[.register_bots()]] - code - gateway/ingest_api/router.py
- [[.resolve_target()]] - code - gateway/ingest_api/router.py
- [[.test_404_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_agent_id_propagated_for_hermes()]] - code - gateway/tests/test_forward_routing.py
- [[.test_agent_id_propagated_for_openclaw()]] - code - gateway/tests/test_forward_routing.py
- [[.test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_blocked_outbound_replaced_with_policy_notice()]] - code - gateway/tests/test_forward_routing.py
- [[.test_default_not_used_in_pipeline()]] - code - gateway/tests/test_forward_routing.py
- [[.test_discard_blocked_message_not_found_returns_error()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_forward_middleware_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_forward_middleware_blocking()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_forward_middleware_error_handling()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_method_not_allowed()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_quarantine_summary_counts_inbound_and_outbound()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_release_blocked_outbound_marks_item_released()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[AgentTarget_1]] - code - gateway/ingest_api/router.py
- [[AgentTarget]] - code - gateway/ingest_api/models.py
- [[AgentTarget accepts custom chat_path and health_path.]] - rationale - gateway/tests/test_router.py
- [[AgentTarget defaults chat_path and health_path correctly.]] - rationale - gateway/tests/test_router.py
- [[Any_7]] - code - gateway/ingest_api/router.py
- [[Both bots must be reachable via the same router without conflict.]] - rationale - gateway/tests/test_router.py
- [[Build a minimal mock app_state that returns a target with the given bot name.]] - rationale - gateway/tests/test_forward_routing.py
- [[Check health of one or all agent targets          Args             target Spec]] - rationale - gateway/ingest_api/router.py
- [[Create a router instance for testing]] - rationale - gateway/tests/test_router.py
- [[Determine which agent should receive this content          Args             req]] - rationale - gateway/ingest_api/router.py
- [[Downstream agent target]] - rationale - gateway/ingest_api/models.py
- [[ForwardRequest_1]] - code - gateway/ingest_api/router.py
- [[ForwardRequest]] - code - gateway/ingest_api/models.py
- [[Inbound passes; outbound returns blocked=True with the original text intact.]] - rationale - gateway/tests/test_forward_routing.py
- [[Initialize router          Args             config Router configuration]] - rationale - gateway/ingest_api/router.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Minimal pipeline mock that records which agent_id it was called with.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'hermes' as agent_id when routed to hermes.]] - rationale - gateway/tests/test_forward_routing.py
- [[Pipeline receives 'openclaw' as agent_id when routed to openclaw.]] - rationale - gateway/tests/test_forward_routing.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Populate routing targets from the bots registry.          Iterates all BotConfig]] - rationale - gateway/ingest_api/router.py
- [[Raised when no valid routing target found]] - rationale - gateway/ingest_api/router.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression 'default' must never appear in agent_id when a named target is resol]] - rationale - gateway/tests/test_forward_routing.py
- [[Regression forward returned out_result.sanitized_message without checking]] - rationale - gateway/tests/test_forward_routing.py
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - rationale - gateway/ingest_api/models.py
- [[Return all configured agent targets          Returns             List of AgentT]] - rationale - gateway/ingest_api/router.py
- [[RouterConfig_1]] - code - gateway/ingest_api/router.py
- [[RouterError]] - code - gateway/ingest_api/router.py
- [[Test forward endpoint with middleware integration.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test mcpproxy endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 404 handling for non-existent endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test 405 handling for wrong HTTP methods.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test approval queue endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test error handling across endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test forwarding handles HTTP error responses]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles timeout exception]] - rationale - gateway/tests/test_router.py
- [[Test forwarding handles unexpected exceptions]] - rationale - gateway/tests/test_router.py
- [[Test forwarding to offline agent raises ForwardError]] - rationale - gateway/tests/test_router.py
- [[Test health check for offline agent]] - rationale - gateway/tests/test_router.py
- [[Test health check for single target]] - rationale - gateway/tests/test_router.py
- [[Test health check with healthy agent]] - rationale - gateway/tests/test_router.py
- [[Test listing all configured targets]] - rationale - gateway/tests/test_router.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test quarantine management endpoints in main.py.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test routing to default target]] - rationale - gateway/tests/test_router.py
- [[Test routing with explicit route_to]] - rationale - gateway/tests/test_router.py
- [[Test routing with invalid explicit target falls back to default]] - rationale - gateway/tests/test_router.py
- [[Test that middleware allows requests when they pass checks.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware can block requests with HTTP 403.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test that middleware errors cause requests to be blocked.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestAgentIdPropagatedFromTarget]] - code - gateway/tests/test_forward_routing.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestErrorHandling]] - code - gateway/tests/test_main_endpoints.py
- [[TestForwardEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestOutboundBlockedNotDelivered]] - code - gateway/tests/test_forward_routing.py
- [[TestQuarantineEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[Verify that the resolved target.name is used as agent_id in pipeline calls.]] - rationale - gateway/tests/test_forward_routing.py
- [[_BlockedOutboundPipeline]] - code - gateway/tests/test_forward_routing.py
- [[_PipelineCaptor]] - code - gateway/tests/test_forward_routing.py
- [[_make_mock_app_state()]] - code - gateway/tests/test_forward_routing.py
- [[forward_to_agent builds URL from target.chat_path.]] - rationale - gateway/tests/test_router.py
- [[health_check builds URL from target.health_path.]] - rationale - gateway/tests/test_router.py
- [[route_to='hermes' must resolve to the Hermes AgentTarget.]] - rationale - gateway/tests/test_router.py
- [[router()]] - code - gateway/tests/test_router.py
- [[test_agent_target_custom_paths()]] - code - gateway/tests/test_router.py
- [[test_agent_target_default_paths()]] - code - gateway/tests/test_router.py
- [[test_forward_routing.py]] - code - gateway/tests/test_forward_routing.py
- [[test_forward_to_agent_http_error()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_offline()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_timeout()]] - code - gateway/tests/test_router.py
- [[test_forward_to_agent_unexpected_error()]] - code - gateway/tests/test_router.py
- [[test_forward_uses_chat_path()]] - code - gateway/tests/test_router.py
- [[test_health_check_healthy_agent()]] - code - gateway/tests/test_router.py
- [[test_health_check_offline_agent()]] - code - gateway/tests/test_router.py
- [[test_health_check_single_target()]] - code - gateway/tests/test_router.py
- [[test_health_check_uses_health_path()]] - code - gateway/tests/test_router.py
- [[test_hermes_and_openclaw_coexist()]] - code - gateway/tests/test_router.py
- [[test_list_targets()]] - code - gateway/tests/test_router.py
- [[test_main_endpoints.py]] - code - gateway/tests/test_main_endpoints.py
- [[test_resolve_target_default()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolve_target_invalid_explicit()]] - code - gateway/tests/test_router.py
- [[test_resolves_hermes_target()]] - code - gateway/tests/test_router.py
- [[test_router.py]] - code - gateway/tests/test_router.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_Routing__Request_Models
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 11 edges to [[_COMMUNITY_SSH Proxy & Gateway Config]]
- 10 edges to [[_COMMUNITY_Module Group 74]]
- 9 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 6 edges to [[_COMMUNITY_Module Group 99]]
- 5 edges to [[_COMMUNITY_Module Group 61]]
- 4 edges to [[_COMMUNITY_Config Validation Tests]]
- 4 edges to [[_COMMUNITY_Module Group 135]]
- 3 edges to [[_COMMUNITY_Module Group 317]]
- 2 edges to [[_COMMUNITY_Module Group 83]]
- 2 edges to [[_COMMUNITY_Module Group 189]]
- 2 edges to [[_COMMUNITY_Module Group 195]]
- 1 edge to [[_COMMUNITY_Module Group 113]]

## Top bridge nodes
- [[ForwardRequest]] - degree 63, connects to 9 communities
- [[test_main_endpoints.py]] - degree 13, connects to 3 communities
- [[RouterError]] - degree 7, connects to 3 communities
- [[AgentTarget]] - degree 30, connects to 2 communities
- [[test_router.py]] - degree 26, connects to 2 communities