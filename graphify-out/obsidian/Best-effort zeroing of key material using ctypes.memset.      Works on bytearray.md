---
source_file: "gateway/security/encrypted_store.py"
type: "rationale"
community: "Encrypted Store (security)"
location: "L35"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Encrypted_Store_security
---

# Best-effort zeroing of key material using ctypes.memset.      Works on bytearray

## Connections
- [[_secure_zero()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Encrypted_Store_security