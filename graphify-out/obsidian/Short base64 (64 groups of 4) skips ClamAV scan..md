---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "Community 220"
location: "L190"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_220
---

# Short base64 (<64 groups of 4) skips ClamAV scan.

## Connections
- [[test_pipeline_short_base64_not_scanned()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_220