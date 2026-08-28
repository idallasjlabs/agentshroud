---
source_file: "gateway/security/session_security.py"
type: "code"
community: "Security Audit & Drift Detection"
location: "L45"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Drift_Detection
---

# Session

## Connections
- [[.create_session()]] - `references` [EXTRACTED]
- [[.rotate_session()]] - `references` [EXTRACTED]
- [[.test_session_binding()]] - `calls` [EXTRACTED]
- [[.test_session_cannot_impersonate()]] - `calls` [INFERRED]
- [[.test_session_different_fingerprints()]] - `calls` [EXTRACTED]
- [[.test_session_rate_limit()]] - `calls` [EXTRACTED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
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
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[session_security.py]] - `contains` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Drift_Detection