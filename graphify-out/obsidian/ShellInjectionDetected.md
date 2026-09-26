---
source_file: "gateway/security/consent_framework.py"
type: "code"
community: "test_filter_xml_blocks.py"
location: "L27"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_filter_xml_blockspy
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

#graphify/code #graphify/INFERRED #community/test_filter_xml_blockspy