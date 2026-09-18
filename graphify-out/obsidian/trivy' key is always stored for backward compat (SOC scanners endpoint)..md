---
source_file: "gateway/tests/test_security_toolchain.py"
type: "rationale"
community: "TestStartupScannerKeying"
location: "L395"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestStartupScannerKeying
---

# trivy' key is always stored for backward compat (SOC /scanners endpoint).

## Connections
- [[.test_legacy_trivy_key_present()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestStartupScannerKeying