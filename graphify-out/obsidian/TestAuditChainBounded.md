---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Security Pipeline & Audit Chain"
location: "L94"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Pipeline__Audit_Chain
---

# TestAuditChainBounded

## Connections
- [[.test_chain_continuity_preserved_across_wrap()]] - `method` [EXTRACTED]
- [[.test_default_window_is_10k()_1]] - `method` [EXTRACTED]
- [[.test_persisted_event_records_true_previous_hash()]] - `method` [EXTRACTED]
- [[.test_tamper_in_retained_window_detected()_1]] - `method` [EXTRACTED]
- [[.test_unwrapped_chain_must_anchor_at_genesis()]] - `method` [EXTRACTED]
- [[.test_verify_chain_valid_after_wrap()_1]] - `method` [EXTRACTED]
- [[.test_window_capped_at_max_entries()_1]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[The in-memory window must be bounded; full history lives in SQLite.]] - `rationale_for` [EXTRACTED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Pipeline__Audit_Chain
