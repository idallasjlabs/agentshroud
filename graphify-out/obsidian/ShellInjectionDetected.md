---
source_file: "gateway/security/consent_framework.py"
type: "code"
community: "Gateway Test Suite"
location: "L27"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# ShellInjectionDetected

## Connections
- [[.validate_config()]] - `calls` [EXTRACTED]
- [[ConfigValidationError]] - `inherits` [EXTRACTED]
- [[TestConsentDecision]] - `uses` [INFERRED]
- [[TestEnvironmentValidation]] - `uses` [INFERRED]
- [[TestServerConfigValidation]] - `uses` [INFERRED]
- [[TestWhitelistBlacklist]] - `uses` [INFERRED]
- [[consent_framework.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite