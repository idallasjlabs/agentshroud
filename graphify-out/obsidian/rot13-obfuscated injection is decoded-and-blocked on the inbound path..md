---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L105"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# rot13-obfuscated injection is decoded-and-blocked on the inbound path.

## Connections
- [[test_inbound_rot13_injection_blocked()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline