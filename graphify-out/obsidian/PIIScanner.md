---
source_file: "gateway/security/file_sandbox.py"
type: "code"
community: "KillSwitchMonitor"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/KillSwitchMonitor
---

# PIIScanner

## Connections
- [[dot-__init__()_26]] - `calls` [EXTRACTED]
- [[dot-scan()_1]] - `method` [EXTRACTED]
- [[dot-test_api_key_pattern_detected()]] - `calls` [EXTRACTED]
- [[dot-test_credit_card_detected()]] - `calls` [EXTRACTED]
- [[dot-test_email_detected()]] - `calls` [EXTRACTED]
- [[dot-test_no_pii_clean()]] - `calls` [EXTRACTED]
- [[dot-test_ssn_detected()]] - `calls` [EXTRACTED]
- [[TestFileAudit]] - `uses` [INFERRED]
- [[TestFileSandboxConfig]] - `uses` [INFERRED]
- [[TestNormalFileOperations]] - `uses` [INFERRED]
- [[TestPIIScanning]] - `uses` [INFERRED]
- [[TestSensitivePathBlocking]] - `uses` [INFERRED]
- [[TestStagingPatternDetection]] - `uses` [INFERRED]
- [[file_sandbox.py]] - `contains` [EXTRACTED]
- [[test_file_sandbox.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/KillSwitchMonitor
