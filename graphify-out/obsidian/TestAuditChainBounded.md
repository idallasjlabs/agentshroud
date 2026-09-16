---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L94"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# TestAuditChainBounded

## Connections
- [[dot-test_append_owner_bypass_persists_high_severity()]] - `method` [EXTRACTED]
- [[dot-test_chain_continuity_preserved_across_wrap()]] - `method` [EXTRACTED]
- [[dot-test_default_window_is_10k()]] - `method` [EXTRACTED]
- [[dot-test_persisted_event_records_true_previous_hash()]] - `method` [EXTRACTED]
- [[dot-test_tamper_in_retained_window_detected()]] - `method` [EXTRACTED]
- [[dot-test_unwrapped_chain_must_anchor_at_genesis()]] - `method` [EXTRACTED]
- [[dot-test_verify_chain_valid_after_wrap()]] - `method` [EXTRACTED]
- [[dot-test_window_capped_at_max_entries()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[CrossBotTrustLedger_1]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[OutboundInfoFilter]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[ScanResult_1]] - `uses` [INFERRED]
- [[SecurityPipeline_1]] - `uses` [INFERRED]
- [[The in-memory window must be bounded; full history lives in SQLite.]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Signed_Instruction_Envelopes__Security_Pipeline