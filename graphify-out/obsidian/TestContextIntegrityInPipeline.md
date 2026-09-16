---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Signed Instruction Envelopes & Security Pipeline"
location: "L410"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Signed_Instruction_Envelopes__Security_Pipeline
---

# TestContextIntegrityInPipeline

## Connections
- [[dot-test_high_score_forwards_and_records()]] - `method` [EXTRACTED]
- [[dot-test_lockdown_block_is_audited()]] - `method` [EXTRACTED]
- [[dot-test_lockdown_score_allows_owner()]] - `method` [EXTRACTED]
- [[dot-test_lockdown_score_blocks_non_owner()]] - `method` [EXTRACTED]
- [[dot-test_no_scorer_leaves_result_unscored()]] - `method` [EXTRACTED]
- [[dot-test_scorer_error_allows_owner()]] - `method` [EXTRACTED]
- [[dot-test_scorer_error_fails_closed_non_owner()]] - `method` [EXTRACTED]
- [[dot-test_scorer_invoked_with_session_segments()]] - `method` [EXTRACTED]
- [[dot-test_warn_zone_forwards()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[ContextIntegrityScorer must run in process_inbound() — C21 wiring.]] - `rationale_for` [EXTRACTED]
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
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Signed_Instruction_Envelopes__Security_Pipeline