---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "Community 330"
location: "L163"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_330
---

# test_pipeline_clamav_error_fail_open()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - `rationale_for` [EXTRACTED]
- [[_b64_payload()]] - `calls` [EXTRACTED]
- [[_make_pipeline()]] - `calls` [EXTRACTED]
- [[test_clamav_pipeline.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_330