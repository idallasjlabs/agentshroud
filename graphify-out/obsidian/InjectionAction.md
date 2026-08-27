---
source_file: "gateway/security/tool_result_injection.py"
type: "code"
community: "Community 22"
location: "L30"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_22
---

# InjectionAction

## Connections
- [[Any_19]] - `uses` [INFERRED]
- [[AuditChain]] - `uses` [INFERRED]
- [[AuditChainEntry]] - `uses` [INFERRED]
- [[Enum]] - `inherits` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[PipelineResult]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[SecurityPipeline_2]] - `uses` [INFERRED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestCleanContent]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEncodedInjection]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestHighSeverity]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestMediumSeverity]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestSanitization]] - `uses` [INFERRED]
- [[TestToolResultInjectionScanner]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[TestUnicodeObfuscation]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[pipeline.py]] - `imports` [EXTRACTED]
- [[str]] - `inherits` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_tool_injection_scan.py]] - `imports` [EXTRACTED]
- [[test_tool_result_injection.py]] - `imports` [EXTRACTED]
- [[test_ws_e_rt2_inbound_encoding.py]] - `imports` [EXTRACTED]
- [[tool_result_injection.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_22