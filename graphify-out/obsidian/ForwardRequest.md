---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "Config Validation & Router"
location: "L22"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Config_Validation__Router
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
- [[Any_9]] - `uses` [INFERRED]
- [[BaseModel]] - `inherits` [EXTRACTED]
- [[ForwardError]] - `uses` [INFERRED]
- [[ForwardRequest_1]] - `uses` [INFERRED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[Path_26]] - `uses` [INFERRED]
- [[Request to forward content through the gateway      Received from iOS Shortcuts,]] - `rationale_for` [EXTRACTED]
- [[RouterConfig_1]] - `uses` [INFERRED]
- [[RouterError]] - `uses` [INFERRED]
- [[TestAgentIdPropagatedFromTarget]] - `uses` [INFERRED]
- [[TestAllExampleConfigsExist]] - `uses` [INFERRED]
- [[TestConfigValidation]] - `uses` [INFERRED]
- [[TestMinimalConfig]] - `uses` [INFERRED]
- [[TestOutboundBlockedNotDelivered]] - `uses` [INFERRED]
- [[TestOwnerSpoofingViaForwardBody]] - `uses` [INFERRED]
- [[TestOwnerTrustElevation]] - `uses` [INFERRED]
- [[TestParanoidConfig]] - `uses` [INFERRED]
- [[TestRecommendedConfig]] - `uses` [INFERRED]
- [[_BlockedOutboundPipeline]] - `uses` [INFERRED]
- [[_BlockingPipeline]] - `uses` [INFERRED]
- [[_PassthroughPipeline]] - `uses` [INFERRED]
- [[_PipelineCaptor]] - `uses` [INFERRED]
- [[_TrustCaptor]] - `uses` [INFERRED]
- [[_process_inbound()]] - `shares_data_with` [EXTRACTED]
- [[_request()]] - `calls` [EXTRACTED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[models.py]] - `contains` [EXTRACTED]
- [[router.py]] - `imports` [EXTRACTED]
- [[test_config_validation.py]] - `imports` [EXTRACTED]
- [[test_empty_content_rejection()]] - `calls` [EXTRACTED]
- [[test_forward_request_valid()]] - `calls` [EXTRACTED]
- [[test_forward_request_validation_empty_content()]] - `calls` [EXTRACTED]
- [[test_forward_request_validation_invalid_source()]] - `calls` [EXTRACTED]
- [[test_forward_routing.py]] - `imports` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_hermes_and_openclaw_coexist()]] - `calls` [EXTRACTED]
- [[test_invalid_source_rejection()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]
- [[test_malformed_json_metadata()]] - `calls` [EXTRACTED]
- [[test_resolve_target_default()]] - `calls` [EXTRACTED]
- [[test_resolve_target_explicit()]] - `calls` [EXTRACTED]
- [[test_resolve_target_invalid_explicit()]] - `calls` [EXTRACTED]
- [[test_resolves_hermes_target()]] - `calls` [EXTRACTED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]
- [[test_shortcut_content_types_accepted()]] - `calls` [EXTRACTED]
- [[test_shortcut_empty_content_rejected()]] - `calls` [EXTRACTED]
- [[test_shortcut_rejects_unknown_content_type()]] - `calls` [EXTRACTED]
- [[test_shortcut_source_accepted()]] - `calls` [EXTRACTED]
- [[test_valid_sources()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Config_Validation__Router