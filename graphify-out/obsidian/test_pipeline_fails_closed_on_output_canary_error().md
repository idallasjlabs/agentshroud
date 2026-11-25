---
source_file: "gateway/tests/test_e2e_watchtower.py"
type: "code"
community: "PIISanitizer"
location: "L410"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PIISanitizer
---

# test_pipeline_fails_closed_on_output_canary_error()

## Connections
- [[Pipeline must BLOCK (not pass through) when OutputCanary crashes for non-owner.]] - `rationale_for` [EXTRACTED]
- [[SecurityPipeline]] - `uses` [INFERRED]
- [[_BrokenOutputCanary]] - `calls` [EXTRACTED]
- [[asyncio_7]] - `references` [EXTRACTED]
- [[test_e2e_watchtower.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PIISanitizer
