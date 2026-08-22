---
source_file: "gateway/security/encrypted_store.py"
type: "rationale"
community: "Security Hardening"
location: "L212"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Hardening
---

# Extract the key_id from an encrypted blob without decrypting.

## Connections
- [[.get_blob_key_id()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Hardening