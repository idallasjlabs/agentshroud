---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L83"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# base64-wrapped DAN injection is decoded-and-blocked on the inbound path.

## Connections
- [[test_inbound_base64_injection_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline