---
source_file: "gateway/security/key_vault.py"
type: "code"
community: "MCP Proxy Config"
location: "L165"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Proxy_Config
---

# KeyLeakDetector

## Connections
- [[.__init__()_88]] - `method` [EXTRACTED]
- [[._make_vault_pipeline()]] - `calls` [EXTRACTED]
- [[.scan_outbound()]] - `method` [EXTRACTED]
- [[.test_detect_api_key_patterns()]] - `calls` [EXTRACTED]
- [[.test_detect_key_in_outbound()]] - `calls` [EXTRACTED]
- [[.test_leak_detection_logged()]] - `calls` [EXTRACTED]
- [[.test_no_leak_clean_message()]] - `calls` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyInjection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
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
- [[key_vault.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCP_Proxy_Config