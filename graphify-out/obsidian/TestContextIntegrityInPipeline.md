---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Key Vault & Audit Chain"
location: "L410"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Key_Vault__Audit_Chain
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
- [[CrossBotTrustLedger]] - `uses` [INFERRED]
- [[EnvelopeSigner]] - `uses` [INFERRED]
- [[InjectionAction]] - `uses` [INFERRED]
- [[InstructionEnvelope]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
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