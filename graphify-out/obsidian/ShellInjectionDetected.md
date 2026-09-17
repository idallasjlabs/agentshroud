---
source_file: "gateway/security/consent_framework.py"
type: "code"
community: "ConsentFramework"
location: "L27"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ConsentFramework
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

#graphify/code #graphify/INFERRED #community/ConsentFramework