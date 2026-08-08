---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PII Sanitizer Pipeline"
location: "L391"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# test_pipeline_fails_closed_on_enhanced_sanitizer_error()

## Connections
- [[Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `calls` [EXTRACTED]
- [[_BrokenSanitizer]] - `calls` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline