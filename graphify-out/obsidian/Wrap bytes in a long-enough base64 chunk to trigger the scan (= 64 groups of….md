---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "cli/main.py"
location: "L126"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/cli/mainpy
---

# Wrap bytes in a long-enough base64 chunk to trigger the scan (>= 64 groups of…

## Connections
- [[_b64_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/cli/mainpy
