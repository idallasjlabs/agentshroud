---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L298"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# rot13 layer is surfaced when the decoded text reveals injection language.

## Connections
- [[test_encoding_detector_decodes_rot13_injection()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline