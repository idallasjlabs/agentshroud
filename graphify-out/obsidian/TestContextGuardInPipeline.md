---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "MCP Proxy Config"
location: "L211"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Proxy_Config
---

# TestContextGuardInPipeline

## Connections
- [[.test_clean_message_passes()]] - `method` [EXTRACTED]
- [[.test_context_guard_error_fails_closed()]] - `method` [EXTRACTED]
- [[.test_critical_injection_blocks()]] - `method` [EXTRACTED]
- [[.test_high_injection_blocks()]] - `method` [EXTRACTED]
- [[.test_no_context_guard_passes_through()]] - `method` [EXTRACTED]
- [[.test_non_owner_block_does_not_emit_owner_bypass()]] - `method` [EXTRACTED]
- [[.test_owner_bypass_audited_at_every_guard()]] - `method` [EXTRACTED]
- [[.test_owner_bypass_is_recorded_in_audit_chain()]] - `method` [EXTRACTED]
- [[.test_repetition_attack_does_not_block()]] - `method` [EXTRACTED]
- [[.test_skip_context_guard_bypasses_step0()]] - `method` [EXTRACTED]
- [[AuditChain]] - `uses` [INFERRED]
- [[ContextGuard must run in SecurityPipeline.process_inbound() — A2.]] - `rationale_for` [EXTRACTED]
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

#graphify/code #graphify/INFERRED #community/MCP_Proxy_Config