---
source_file: "gateway/security/consent_framework.py"
type: "code"
community: "ServerConfig"
location: "L40"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ServerConfig
---

# ConsentDecision

## Connections
- [[dot-test_decision_approved()]] - `calls` [INFERRED]
- [[dot-test_decision_denied()]] - `calls` [INFERRED]
- [[dot-test_decision_has_timestamp()]] - `calls` [INFERRED]
- [[dot-validate_config()]] - `calls` [EXTRACTED]
- [[dot-validate_configs()]] - `references` [EXTRACTED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConsentDecision]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[consent_framework.py]] - `contains` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ServerConfig
