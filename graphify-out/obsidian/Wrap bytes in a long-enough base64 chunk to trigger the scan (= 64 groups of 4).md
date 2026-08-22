---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "rationale"
community: "Clamav Pipeline"
location: "L119"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Clamav_Pipeline
---

# Wrap bytes in a long-enough base64 chunk to trigger the scan (>= 64 groups of 4)

## Connections
- [[_b64_payload()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Clamav_Pipeline