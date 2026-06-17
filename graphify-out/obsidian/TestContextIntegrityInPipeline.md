---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Pipeline Action & Instruction Envelope"
location: "L298"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Pipeline_Action__Instruction_Envelope
---

# TestContextIntegrityInPipeline

## Connections
- [[.test_high_score_forwards_and_records()]] - `method` [EXTRACTED]
- [[.test_lockdown_block_is_audited()]] - `method` [EXTRACTED]
- [[.test_lockdown_score_allows_owner()]] - `method` [EXTRACTED]
- [[.test_lockdown_score_blocks_non_owner()]] - `method` [EXTRACTED]
- [[.test_no_scorer_leaves_result_unscored()]] - `method` [EXTRACTED]
- [[.test_scorer_error_allows_owner()]] - `method` [EXTRACTED]
- [[.test_scorer_error_fails_closed_non_owner()]] - `method` [EXTRACTED]
- [[.test_scorer_invoked_with_session_segments()]] - `method` [EXTRACTED]
- [[.test_warn_zone_forwards()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - `rationale_for` [EXTRACTED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Pipeline_Action__Instruction_Envelope