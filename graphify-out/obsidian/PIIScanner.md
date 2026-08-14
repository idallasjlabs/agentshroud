---
source_file: "gateway/security/file_sandbox.py"
type: "code"
community: "URL/Domain Validation Tests"
location: "L40"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/URL/Domain_Validation_Tests
---

# PIIScanner

## Connections
- [[.__init__()_78]] - `calls` [EXTRACTED]
- [[.scan()_3]] - `method` [EXTRACTED]
- [[.test_api_key_pattern_detected()]] - `calls` [EXTRACTED]
- [[.test_credit_card_detected()]] - `calls` [EXTRACTED]
- [[.test_email_detected()]] - `calls` [EXTRACTED]
- [[.test_no_pii_clean()]] - `calls` [EXTRACTED]
- [[.test_ssn_detected()]] - `calls` [EXTRACTED]
- [[DifferentialPIIDetector]] - `semantically_similar_to` [INFERRED]
- [[TestFileAudit]] - `uses` [INFERRED]
- [[TestFileSandboxConfig]] - `uses` [INFERRED]
- [[TestNormalFileOperations]] - `uses` [INFERRED]
- [[TestPIIScanning]] - `uses` [INFERRED]
- [[TestSensitivePathBlocking]] - `uses` [INFERRED]
- [[TestStagingPatternDetection]] - `uses` [INFERRED]
- [[file_sandbox.py]] - `contains` [EXTRACTED]
- [[test_file_sandbox.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/URL/Domain_Validation_Tests