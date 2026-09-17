---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "test_clamav_pipeline.py"
location: "L164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_clamav_pipelinepy
---

# ClamAV scan_bytes returns error → fail-open: CRITICAL log, FORWARD.

## Connections
- [[test_pipeline_clamav_error_fail_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_clamav_pipelinepy