---
source_file: "gateway/security/prompt_guard.py"
type: "code"
community: "SecurityPipeline"
location: "L36"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/SecurityPipeline
---

# ScanResult

## Connections
- [[dot-_blocking_prompt_guard()]] - `calls` [EXTRACTED]
- [[dot-scan()_1]] - `references` [EXTRACTED]
- [[dot-scan_tool_result()_1]] - `references` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[prompt_guard.py]] - `contains` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/SecurityPipeline
