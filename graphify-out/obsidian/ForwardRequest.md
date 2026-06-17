---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Agent Routing & Request Models"
location: "L20"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Agent_Routing__Request_Models
---

# ForwardRequest

## Connections
- [[.content_not_empty()]] - `method` [EXTRACTED]
- [[.test_agent_id_propagated_for_openclaw()]] - `calls` [EXTRACTED]
- [[.test_empty_content_rejected()]] - `calls` [EXTRACTED]
- [[.test_invalid_source_rejected()]] - `calls` [EXTRACTED]
- [[.test_valid_forward_request()]] - `calls` [EXTRACTED]
- [[.validate_source()]] - `method` [EXTRACTED]
- [[AgentTarget_1]] - `uses` [INFERRED]
- [[Any_7]] - `uses` [INFERRED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[ForwardError]] - `uses` [INFERRED]
- [[ForwardRequest_1]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Path_21]] - `uses` [INFERRED]
- [[Request]] - `uses` [INFERRED]
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - `rationale_for` [EXTRACTED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[RouterError]] - `uses` [INFERRED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[TestAgentIdPropagatedFromTarget]] - `uses` [INFERRED]
- [[TestAllExampleConfigsExist]] - `uses` [INFERRED]
- [[TestApprovalEndpoints]] - `uses` [INFERRED]
- [[TestConfigValidation]] - `uses` [INFERRED]
- [[TestErrorHandling]] - `uses` [INFERRED]
- [[TestForwardEndpoint]] - `uses` [INFERRED]
- [[TestGoogleAPIProxy]] - `uses` [INFERRED]
- [[TestHermesDashboardPathTraversal]] - `uses` [INFERRED]
- [[TestMCPProxyEndpoint]] - `uses` [INFERRED]
- [[TestMinimalConfig]] - `uses` [INFERRED]
- [[TestOutboundBlockedNotDelivered]] - `uses` [INFERRED]
- [[TestParanoidConfig]] - `uses` [INFERRED]
- [[TestQuarantineEndpoints]] - `uses` [INFERRED]
- [[TestRecommendedConfig]] - `uses` [INFERRED]
- [[TestStatusEndpoint]] - `uses` [INFERRED]
- [[WebSocket_2]] - `uses` [INFERRED]
- [[_BlockedOutboundPipeline]] - `uses` [INFERRED]
- [[_PipelineCaptor]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[router.py]] - `imports` [EXTRACTED]
- [[test_config_validation.py]] - `imports` [EXTRACTED]
- [[test_empty_content_rejection()]] - `calls` [EXTRACTED]
- [[test_forward_request_valid()]] - `calls` [EXTRACTED]
- [[test_forward_request_validation_empty_content()]] - `calls` [EXTRACTED]
- [[test_forward_request_validation_invalid_source()]] - `calls` [EXTRACTED]
- [[test_forward_routing.py]] - `imports` [EXTRACTED]
- [[test_hermes_and_openclaw_coexist()]] - `calls` [EXTRACTED]
- [[test_invalid_source_rejection()]] - `calls` [EXTRACTED]
- [[test_main_endpoints.py]] - `imports` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]
- [[test_malformed_json_metadata()]] - `calls` [EXTRACTED]
- [[test_resolve_target_default()]] - `calls` [EXTRACTED]
- [[test_resolve_target_explicit()]] - `calls` [EXTRACTED]
- [[test_resolve_target_invalid_explicit()]] - `calls` [EXTRACTED]
- [[test_resolves_hermes_target()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]
- [[test_valid_sources()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Agent_Routing__Request_Models