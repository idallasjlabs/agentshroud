---
source_file: "gateway/security/key_vault.py"
type: "code"
community: "KeyVault"
location: "L153"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/KeyVault
---

# KeyInjector

## Connections
- [[.__init__()_184]] - `method` [EXTRACTED]
- [[.inject_for_request()]] - `method` [EXTRACTED]
- [[.test_inject_auth_header()]] - `calls` [EXTRACTED]
- [[.test_inject_fails_for_unscoped()]] - `calls` [EXTRACTED]
- [[.test_inject_preserves_existing_headers()]] - `calls` [EXTRACTED]
- [[TestKeyInjection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[TestKeyRedaction]] - `uses` [INFERRED]
- [[TestKeyRotation]] - `uses` [INFERRED]
- [[TestKeyScoping]] - `uses` [INFERRED]
- [[TestKeyStorage]] - `uses` [INFERRED]
- [[TestKeyVaultConfig]] - `uses` [INFERRED]
- [[key_vault.py_2]] - `contains` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/KeyVault