---
source_file: "gateway/security/encoding_detector.py"
type: "rationale"
community: "Canary Tripwire"
location: "L124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Canary_Tripwire
---

# Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a

## Connections
- [[dot-decode_rot13()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Canary_Tripwire