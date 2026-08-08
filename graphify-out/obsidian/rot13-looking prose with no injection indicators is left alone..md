---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L180"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# rot13-looking prose with no injection indicators is left alone.

## Connections
- [[test_inbound_benign_rot13_prose_not_decoded_or_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline