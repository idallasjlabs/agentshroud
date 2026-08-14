---
source_file: "gateway/tests/test_key_vault.py"
type: "code"
community: "MCP Proxy Config"
location: "L80"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MCP_Proxy_Config
---

# TestKeyInjection

## Connections
- [[.test_inject_auth_header()]] - `method` [EXTRACTED]
- [[.test_inject_fails_for_unscoped()]] - `method` [EXTRACTED]
- [[.test_inject_preserves_existing_headers()]] - `method` [EXTRACTED]
- [[KeyInjector]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[test_key_vault.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MCP_Proxy_Config