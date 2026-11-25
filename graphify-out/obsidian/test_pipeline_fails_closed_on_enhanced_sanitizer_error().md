---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PIISanitizer"
location: "L391"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIISanitizer
---

# test_pipeline_fails_closed_on_enhanced_sanitizer_error()

## Connections
- [[Pipeline must BLOCK (not pass through) when EnhancedToolResultSanitizer crashes…]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[_BrokenSanitizer]] - `calls` [EXTRACTED]
- [[asyncio_7]] - `references` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIISanitizer
