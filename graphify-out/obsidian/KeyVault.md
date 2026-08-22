---
source_file: "gateway/security/key_vault.py"
type: "code"
community: "Key Vault"
location: "L71"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Key_Vault
---

# KeyVault

## Connections
- [[.__init__()_90]] - `references` [EXTRACTED]
- [[.__init__()_91]] - `references` [EXTRACTED]
- [[.__init__()_89]] - `method` [EXTRACTED]
- [[._agent_in_scope()]] - `method` [EXTRACTED]
- [[._log_audit()]] - `method` [EXTRACTED]
- [[._make_vault_pipeline()]] - `calls` [EXTRACTED]
- [[.check_value_match()]] - `method` [EXTRACTED]
- [[.delete_key()]] - `method` [EXTRACTED]
- [[.get_audit_log()_5]] - `method` [EXTRACTED]
- [[.get_key()]] - `method` [EXTRACTED]
- [[.list_keys()]] - `method` [EXTRACTED]
- [[.redact()]] - `method` [EXTRACTED]
- [[.rotate_key()]] - `method` [EXTRACTED]
- [[.store_key()]] - `method` [EXTRACTED]
- [[.test_detect_api_key_patterns()]] - `calls` [EXTRACTED]
- [[.test_key_vault_init()]] - `calls` [EXTRACTED]
- [[Per-agent API key scoping, redaction, leak detection, and rotation]] - `rationale_for` [EXTRACTED]
- [[TestAuditChain]] - `uses` [INFERRED]
- [[TestAuditChainBounded]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestContextGuardInPipeline]] - `uses` [INFERRED]
- [[TestContextIntegrityInPipeline]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestEnvelopeSignerInPipeline]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestInboundPIIOwnerExemption]] - `uses` [INFERRED]
- [[TestKeyInjection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestKeyRedaction]] - `uses` [INFERRED]
- [[TestKeyRotation]] - `uses` [INFERRED]
- [[TestKeyScoping]] - `uses` [INFERRED]
- [[TestKeyStorage]] - `uses` [INFERRED]
- [[TestKeyVaultConfig]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestOutboundFilterResultBinding]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestPromptGuardToolResultTrustGate]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTrustViolationRecording]] - `uses` [INFERRED]
- [[_FakeAttack]] - `uses` [INFERRED]
- [[_FakeIntegrityScore]] - `uses` [INFERRED]
- [[key_vault.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[vault()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Key_Vault