---
source_file: "gateway/security/key_vault.py"
type: "code"
community: "KeyVault"
location: "L159"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/KeyVault
---

# KeyLeakDetector

## Connections
- [[dot-__init__()_35]] - `method` [EXTRACTED]
- [[dot-_make_vault_pipeline()]] - `calls` [EXTRACTED]
- [[dot-scan_outbound()]] - `method` [EXTRACTED]
- [[dot-test_detect_api_key_patterns()]] - `calls` [EXTRACTED]
- [[dot-test_detect_key_in_outbound()]] - `calls` [EXTRACTED]
- [[dot-test_leak_detection_logged()]] - `calls` [EXTRACTED]
- [[dot-test_no_leak_clean_message()]] - `calls` [EXTRACTED]
- [[TestKeyLeakDetection]] - `uses` [INFERRED]
- [[TestKeyLeakDetection_1]] - `uses` [INFERRED]
- [[key_vault.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_key_vault.py]] - `imports` [EXTRACTED]
- [[test_pipeline_unit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/KeyVault
