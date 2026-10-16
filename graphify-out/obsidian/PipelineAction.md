---
source_file: "gateway/proxy/pipeline.py"
type: "code"
community: "PIIConfig"
location: "L44"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PIIConfig
---

# PipelineAction

## Connections
- [[BotIncidentSeverity]] - `uses` [INFERRED]
- [[Enum_3]] - `inherits` [EXTRACTED]
- [[FilterResult_1]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[PipelineResult]] - `uses` [INFERRED]
- [[RBACConfig_4]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[TestAuditChain_1]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestE2E01PromptGuardBlocking]] - `uses` [INFERRED]
- [[TestE2E02InboundPIIRedaction]] - `uses` [INFERRED]
- [[TestE2E03OutboundPIIRedaction]] - `uses` [INFERRED]
- [[TestE2E04ContextGuardBlocking]] - `uses` [INFERRED]
- [[TestE2E05CanaryTripwire]] - `uses` [INFERRED]
- [[TestE2E06EncodingBypassDetection]] - `uses` [INFERRED]
- [[TestE2E07TrustEnforcement]] - `uses` [INFERRED]
- [[TestE2E08AuditChainIntegrity]] - `uses` [INFERRED]
- [[TestE2E09SessionIsolation]] - `uses` [INFERRED]
- [[TestE2E10FailClosed]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundFallbackToDirectSanitizer]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestInboundPipelineBlockedNonOwner]] - `uses` [INFERRED]
- [[TestInboundPipelineBlockedOwner]] - `uses` [INFERRED]
- [[TestInboundPipelineExceptionNonOwner]] - `uses` [INFERRED]
- [[TestInboundPipelineExceptionOwner]] - `uses` [INFERRED]
- [[TestInboundPipelineWired]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestOutboundPipelineBlocked]] - `uses` [INFERRED]
- [[TestOutboundPipelineWired]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[ViolationType]] - `uses` [INFERRED]
- [[_BrokenOutputCanary]] - `uses` [INFERRED]
- [[_BrokenSanitizer]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[_PassInboundPipeline]] - `uses` [INFERRED]
- [[_StubForwarder]] - `uses` [INFERRED]
- [[pipeline.py_1]] - `contains` [EXTRACTED]
- [[str_3]] - `inherits` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `imports` [EXTRACTED]
- [[test_e2e_proxy.py]] - `imports` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_telegram_pipeline.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PIIConfig
