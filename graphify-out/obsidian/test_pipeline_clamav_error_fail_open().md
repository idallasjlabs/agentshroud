---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "PipelineAction"
location: "L170"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/PipelineAction
---

# test_pipeline_clamav_error_fail_open()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - `rationale_for` [EXTRACTED]
- [[PipelineAction]] - `uses` [INFERRED]
- [[_b64_payload()]] - `calls` [EXTRACTED]
- [[_make_pipeline()]] - `calls` [EXTRACTED]
- [[asyncio_31]] - `references` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/PipelineAction
