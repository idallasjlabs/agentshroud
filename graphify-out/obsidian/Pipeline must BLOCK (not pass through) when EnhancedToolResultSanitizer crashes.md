---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L392"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes

## Connections
- [[test_pipeline_fails_closed_on_enhanced_sanitizer_error()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline