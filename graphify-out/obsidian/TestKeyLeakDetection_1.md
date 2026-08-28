---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Key Vault & Audit Chain"
location: "L573"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Key_Vault__Audit_Chain
---

# TestKeyLeakDetection

## Connections
- [[._make_vault_pipeline()]] - `method` [EXTRACTED]
- [[._passthrough_pii()]] - `method` [EXTRACTED]
- [[.test_clean_response_passes_unchanged()_1]] - `method` [EXTRACTED]
- [[.test_detector_failure_fails_closed_for_non_owner()]] - `method` [EXTRACTED]
- [[.test_generic_key_pattern_audited_but_not_blocked()]] - `method` [EXTRACTED]
- [[.test_key_leak_increments_sanitized_stat_and_audits()]] - `method` [EXTRACTED]
- [[.test_stored_key_value_redacted_from_outbound()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - `rationale_for` [EXTRACTED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Key_Vault__Audit_Chain