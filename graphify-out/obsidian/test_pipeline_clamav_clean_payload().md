---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "test_clamav_pipeline.py"
location: "L133"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_clamav_pipelinepy
---

# test_pipeline_clamav_clean_payload()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[Clean base64 payload → FORWARD.]] - `rationale_for` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[_b64_payload()]] - `calls` [EXTRACTED]
- [[_make_pipeline()]] - `calls` [EXTRACTED]
- [[asyncio_33]] - `references` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_clamav_pipelinepy
