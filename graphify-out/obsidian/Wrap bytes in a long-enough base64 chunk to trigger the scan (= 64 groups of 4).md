---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "Planning Docs"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Planning_Docs
---

# Wrap bytes in a long-enough base64 chunk to trigger the scan (>= 64 groups of 4)

## Connections
- [[_b64_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Planning_Docs