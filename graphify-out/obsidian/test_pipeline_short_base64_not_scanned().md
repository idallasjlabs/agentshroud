---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "PipelineAction"
location: "L189"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PipelineAction
---

# test_pipeline_short_base64_not_scanned()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - `rationale_for` [EXTRACTED]
- [[_make_pipeline()]] - `calls` [EXTRACTED]
- [[asyncio_31]] - `references` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PipelineAction
