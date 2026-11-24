---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "PipelineAction"
location: "L162"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PipelineAction
---

# test_pipeline_clamav_not_configured()

## Connections
- [[No clamav_scanner configured → step skipped, no error.]] - `rationale_for` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[_make_pipeline()]] - `calls` [EXTRACTED]
- [[asyncio_31]] - `references` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PipelineAction
