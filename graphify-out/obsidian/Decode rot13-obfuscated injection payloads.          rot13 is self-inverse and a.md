---
source_file: "gateway/security/encoding_detector.py"
type: "rationale"
community: "SOC RBAC & Auth"
location: "L124"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# Decode rot13-obfuscated injection payloads.          rot13 is self-inverse and a

## Connections
- [[.decode_rot13()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_RBAC__Auth