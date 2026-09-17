---
source_file: "gateway/security/oauth_security.py"
type: "code"
community: "test_security_audit.py"
location: "L39"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_security_auditpy
---

# RedirectMismatch

## Connections
- [[.validate_redirect_uri()]] - `calls` [EXTRACTED]
- [[OAuthError]] - `inherits` [EXTRACTED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestClientValidation]] - `uses` [INFERRED]
- [[TestConsentCookieBinding]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPKCE]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestRedirectURI]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestStateValidation]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[oauth_security.py]] - `contains` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/test_security_auditpy