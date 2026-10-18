---
source_file: "gateway/tests/test_pipeline_unit.py"
type: "code"
community: "SecurityPipeline"
location: "L699"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/SecurityPipeline
---

# .test_untrusted_tool_result_injection_is_blocked()

## Connections
- [[dot-_blocking_prompt_guard()]] - `calls` [EXTRACTED]
- [[dot-_passthrough_pii()]] - `calls` [EXTRACTED]
- [[SecurityPipeline_1]] - `calls` [EXTRACTED]
- [[TestPromptGuardToolResultTrustGate]] - `method` [EXTRACTED]
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - `rationale_for` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/SecurityPipeline
