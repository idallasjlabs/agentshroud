---
source_file: "gateway/security/encrypted_store.py"
type: "rationale"
community: "KeyVault"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/KeyVault
---

# Best-effort zeroing of key material using ctypes.memset.      Works on bytearray

## Connections
- [[_secure_zero()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/KeyVault
