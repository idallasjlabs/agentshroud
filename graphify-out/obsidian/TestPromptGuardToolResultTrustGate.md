---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "SecurityPipeline"
location: "L651"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# TestPromptGuardToolResultTrustGate

## Connections
- [[dot-_blocking_prompt_guard()]] - `method` [EXTRACTED]
- [[dot-_passthrough_pii()_1]] - `method` [EXTRACTED]
- [[dot-test_full_trust_tool_result_injection_audited_not_blocked()]] - `method` [EXTRACTED]
- [[dot-test_standard_trust_tool_result_injection_is_blocked()]] - `method` [EXTRACTED]
- [[dot-test_untrusted_tool_result_injection_is_blocked()]] - `method` [EXTRACTED]
- [[ScanResult]] - `uses` [INFERRED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.…]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[test_pipeline_unit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SecurityPipeline
