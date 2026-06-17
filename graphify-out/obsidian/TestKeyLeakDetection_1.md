---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L461"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Action__Instruction_Envelope
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
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyLeakDetector wiring — stored credential values must never leave the gateway.]] - `rationale_for` [EXTRACTED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Action__Instruction_Envelope