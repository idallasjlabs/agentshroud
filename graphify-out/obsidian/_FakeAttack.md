---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "Community 22"
location: "L191"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_22
---

# _FakeAttack

## Connections
- [[.test_blocked_request_decays_trust_score()]] - `calls` [EXTRACTED]
- [[.test_blocked_request_propagates_to_cross_bot_peer()]] - `calls` [EXTRACTED]
- [[.test_critical_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_high_injection_blocks()]] - `calls` [EXTRACTED]
- [[.test_missing_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[.test_non_owner_block_does_not_emit_owner_bypass()]] - `calls` [EXTRACTED]
- [[.test_owner_bypass_audited_at_every_guard()]] - `calls` [EXTRACTED]
- [[.test_owner_bypass_is_recorded_in_audit_chain()]] - `calls` [EXTRACTED]
- [[.test_owner_exempted_block_does_not_decay_trust()]] - `calls` [EXTRACTED]
- [[.test_repetition_attack_does_not_block()]] - `calls` [EXTRACTED]
- [[.test_skip_context_guard_bypasses_step0()]] - `calls` [EXTRACTED]
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
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_22