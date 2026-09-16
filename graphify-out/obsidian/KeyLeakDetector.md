---
source_file: "gateway/security/key_vault.py"
type: "code"
community: "Community 80"
location: "L165"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_80
---

# KeyLeakDetector

## Connections
- [[dot-__init__()_185]] - `method` [EXTRACTED]
- [[dot-_make_vault_pipeline()]] - `calls` [EXTRACTED]
- [[dot-scan_outbound()]] - `method` [EXTRACTED]
- [[dot-test_detect_api_key_patterns()]] - `calls` [EXTRACTED]
- [[dot-test_detect_key_in_outbound()]] - `calls` [EXTRACTED]
- [[dot-test_leak_detection_logged()]] - `calls` [EXTRACTED]
- [[dot-test_no_leak_clean_message()]] - `calls` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyInjection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestKeyRedaction]] - `uses` [INFERRED]
- [[TestKeyRotation]] - `uses` [INFERRED]
- [[TestKeyScoping]] - `uses` [INFERRED]
- [[TestKeyStorage]] - `uses` [INFERRED]
- [[TestKeyVaultConfig]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[key_vault.py_2]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_80