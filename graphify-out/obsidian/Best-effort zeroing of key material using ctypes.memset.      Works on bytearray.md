---
source_file: "gateway/security/encrypted_store.py"
type: "rationale"
community: "Gateway Security Module"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# Best-effort zeroing of key material using ctypes.memset.      Works on bytearray

## Connections
- [[_secure_zero()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module