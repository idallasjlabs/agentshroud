---
source_file: "gateway/security/encoding_detector.py"
type: "rationale"
community: "PII Sanitizer Pipeline"
location: "L124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer_Pipeline
---

# Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a

## Connections
- [[.decode_rot13()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer_Pipeline