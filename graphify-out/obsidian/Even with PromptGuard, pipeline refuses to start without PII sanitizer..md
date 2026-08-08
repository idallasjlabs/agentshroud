---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L365"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Even with PromptGuard, pipeline refuses to start without PII sanitizer.

## Connections
- [[.test_pipeline_raises_with_only_prompt_guard()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline