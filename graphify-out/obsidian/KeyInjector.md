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
- [[dot-__init__()_159]] - `method` [EXTRACTED]
- [[dot-inject_for_request()]] - `method` [EXTRACTED]
- [[dot-test_inject_auth_header()]] - `calls` [EXTRACTED]
- [[dot-test_inject_fails_for_unscoped()]] - `calls` [EXTRACTED]
- [[dot-test_inject_preserves_existing_headers()]] - `calls` [EXTRACTED]
- [[TestKeyInjection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestKeyRedaction]] - `uses` [INFERRED]
- [[TestKeyRotation]] - `uses` [INFERRED]
- [[TestKeyScoping]] - `uses` [INFERRED]
- [[TestKeyStorage]] - `uses` [INFERRED]
- [[TestKeyVaultConfig]] - `uses` [INFERRED]
- [[key_vault.py_2]] - `contains` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/KeyVault
