---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "cli/main.py"
location: "L190"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/cli/mainpy
---

# Short base64 (<64 groups of 4) skips ClamAV scan.

## Connections
- [[test_pipeline_short_base64_not_scanned()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/cli/mainpy
