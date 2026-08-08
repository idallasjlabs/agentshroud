---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Cross-Bot Trust Ledger"
location: "L833"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Cross-Bot_Trust_Ledger
---

# TestTrustViolationRecording

## Connections
- [[._pipeline_with_trust()]] - `method` [EXTRACTED]
- [[.test_blocked_request_decays_trust_score()]] - `method` [EXTRACTED]
- [[.test_blocked_request_propagates_to_cross_bot_peer()]] - `method` [EXTRACTED]
- [[.test_clean_request_does_not_touch_trust_score()]] - `method` [EXTRACTED]
- [[.test_missing_trust_manager_does_not_raise()]] - `method` [EXTRACTED]
- [[.test_owner_exempted_block_does_not_decay_trust()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
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
- [[SecurityPipeline._maybe_record_trust_violation — centralized hook that     fires]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Cross-Bot_Trust_Ledger