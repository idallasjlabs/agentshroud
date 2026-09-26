---
source_file: "gateway/security/encoding_detector.py"
type: "rationale"
community: "EgressFilter"
location: "L124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressFilter
---

# Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a

## Connections
- [[.decode_rot13()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressFilter