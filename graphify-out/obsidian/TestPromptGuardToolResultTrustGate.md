---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "KeyVaultConfig"
location: "L651"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/KeyVaultConfig
---

# TestPromptGuardToolResultTrustGate

## Connections
- [[._blocking_prompt_guard()]] - `method` [EXTRACTED]
- [[._passthrough_pii()]] - `method` [EXTRACTED]
- [[.test_full_trust_tool_result_injection_audited_not_blocked()]] - `method` [EXTRACTED]
- [[.test_standard_trust_tool_result_injection_is_blocked()]] - `method` [EXTRACTED]
- [[.test_untrusted_tool_result_injection_is_blocked()]] - `method` [EXTRACTED]
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
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.      CVE-2]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/KeyVaultConfig