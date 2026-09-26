---
source_file: "gateway/tests/test_session_manager.py"
type: "rationale"
community: "KeyVaultConfig"
location: "L313"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/KeyVaultConfig
---

# Registry writes must be atomic (os.replace) and serialized (lock).      The sess

## Connections
- [[TestAtomicRegistryWrites]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/KeyVaultConfig