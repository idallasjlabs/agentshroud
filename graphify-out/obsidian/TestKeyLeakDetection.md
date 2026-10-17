---
source_file: "gateway/tests/test_key_vault.py"
type: "code"
community: "AuditChain"
location: "L141"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# TestKeyLeakDetection

## Connections
- [[dot-test_detect_api_key_patterns()]] - `method` [EXTRACTED]
- [[dot-test_detect_key_in_outbound()]] - `method` [EXTRACTED]
- [[dot-test_leak_detection_logged()]] - `method` [EXTRACTED]
- [[dot-test_no_leak_clean_message()]] - `method` [EXTRACTED]
- [[KeyInjector]] - `uses` [INFERRED]
- [[KeyLeakDetector]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[test_key_vault.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain
