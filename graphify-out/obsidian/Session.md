---
source_file: "gateway/security/session_security.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L45"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Session_Manager__PII/Context_Guard
---

# Session

## Connections
- [[dot-create_session()]] - `references` [EXTRACTED]
- [[dot-rotate_session()]] - `references` [EXTRACTED]
- [[dot-test_session_binding()]] - `calls` [EXTRACTED]
- [[dot-test_session_cannot_impersonate()]] - `calls` [INFERRED]
- [[dot-test_session_different_fingerprints()]] - `calls` [EXTRACTED]
- [[dot-test_session_rate_limit()]] - `calls` [EXTRACTED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[session_security.py]] - `contains` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Session_Manager__PII/Context_Guard