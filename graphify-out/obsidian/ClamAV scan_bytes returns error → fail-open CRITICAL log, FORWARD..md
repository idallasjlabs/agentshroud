---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "asyncio"
location: "L171"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/asyncio
---

# ClamAV scan_bytes returns error → fail-open: CRITICAL log, FORWARD.

## Connections
- [[test_pipeline_clamav_error_fail_open()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/asyncio
