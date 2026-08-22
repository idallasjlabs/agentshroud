---
source_file: "gateway/security/outbound_filter.py"
type: "code"
community: "Outbound Filter"
location: "L66"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Outbound_Filter
---

# OutboundInfoFilter

## Connections
- [[.__init__()_103]] - `method` [EXTRACTED]
- [[._classify_response_risk()]] - `method` [EXTRACTED]
- [[._compile_patterns()_1]] - `method` [EXTRACTED]
- [[._is_allowed_for_trust()]] - `method` [EXTRACTED]
- [[.filter_response()]] - `method` [EXTRACTED]
- [[.get_stats()_17]] - `method` [EXTRACTED]
- [[.setup_method()_18]] - `calls` [EXTRACTED]
- [[.setup_method()_17]] - `calls` [EXTRACTED]
- [[.test_custom_patterns()]] - `calls` [EXTRACTED]
- [[.test_initialization_with_config()]] - `calls` [EXTRACTED]
- [[.test_monitor_mode()]] - `calls` [EXTRACTED]
- [[.test_outbound_filter_still_escalates_fabricated_notice()]] - `calls` [EXTRACTED]
- [[.test_real_world_agent_responses()]] - `calls` [EXTRACTED]
- [[.test_trust_level_overrides()]] - `calls` [EXTRACTED]
- [[.test_with_pii_sanitizer_compatibility()]] - `calls` [EXTRACTED]
- [[Main outbound information filtering engine.      Uses compiled regex patterns to]] - `rationale_for` [EXTRACTED]
- [[Outbound Information Filter Tests]] - `references` [EXTRACTED]
- [[OutputCanary]] - `conceptually_related_to` [INFERRED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestFabricatedSecurityNotice]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestIntegration]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestOutboundInfoFilter]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[outbound_filter.py]] - `contains` [EXTRACTED]
- [[test_outbound_filter.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Outbound_Filter