---
source_file: "gateway/ingest_api/models.py"
type: "code"
community: "AgentTarget"
location: "L22"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentTarget
---

# ForwardRequest

## Connections
- [[dot-content_not_empty()]] - `method` [EXTRACTED]
- [[dot-resolve_target()]] - `references` [EXTRACTED]
- [[dot-test_agent_id_propagated_for_openclaw()]] - `calls` [EXTRACTED]
- [[dot-test_empty_content_rejected()]] - `calls` [EXTRACTED]
- [[dot-test_invalid_source_rejected()]] - `calls` [EXTRACTED]
- [[dot-test_valid_forward_request()]] - `calls` [EXTRACTED]
- [[dot-validate_source()]] - `method` [EXTRACTED]
- [[BaseModel_5]] - `inherits` [EXTRACTED]
- [[MultiAgentRouter]] - `uses` [INFERRED]
- [[Request to forward content through the gateway Received from iOS Shortcuts,…]] - `rationale_for` [EXTRACTED]
- [[TestAgentIdPropagatedFromTarget]] - `uses` [INFERRED]
- [[TestConfigValidation]] - `uses` [INFERRED]
- [[_process_inbound()]] - `uses` [INFERRED]
- [[_request()]] - `calls` [EXTRACTED]
- [[_resolve_user_trust_level()]] - `uses` [INFERRED]
- [[forward.py]] - `imports` [EXTRACTED]
- [[forward_content()]] - `uses` [INFERRED]
- [[forward_content_stream()]] - `uses` [INFERRED]
- [[ingest_apimodels.py]] - `contains` [EXTRACTED]
- [[ingest_apirouter.py]] - `imports` [EXTRACTED]
- [[test_config_validation.py]] - `imports` [EXTRACTED]
- [[test_empty_content_rejection()]] - `calls` [EXTRACTED]
- [[test_forward_request_valid()]] - `uses` [INFERRED]
- [[test_forward_request_validation_empty_content()]] - `uses` [INFERRED]
- [[test_forward_request_validation_invalid_source()]] - `uses` [INFERRED]
- [[test_forward_routing.py]] - `imports` [EXTRACTED]
- [[test_forward_stream.py]] - `imports` [EXTRACTED]
- [[test_hermes_and_openclaw_coexist()]] - `uses` [INFERRED]
- [[test_invalid_source_rejection()]] - `calls` [EXTRACTED]
- [[test_main_simple.py]] - `imports` [EXTRACTED]
- [[test_malformed_json_metadata()]] - `uses` [INFERRED]
- [[test_resolve_target_default()]] - `uses` [INFERRED]
- [[test_resolve_target_explicit()]] - `uses` [INFERRED]
- [[test_resolve_target_invalid_explicit()]] - `uses` [INFERRED]
- [[test_resolves_hermes_target()]] - `uses` [INFERRED]
- [[test_router.py]] - `imports` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]
- [[test_shortcut_content_types_accepted()]] - `uses` [INFERRED]
- [[test_shortcut_empty_content_rejected()]] - `calls` [EXTRACTED]
- [[test_shortcut_rejects_unknown_content_type()]] - `calls` [EXTRACTED]
- [[test_shortcut_source_accepted()]] - `calls` [EXTRACTED]
- [[test_valid_sources()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentTarget
