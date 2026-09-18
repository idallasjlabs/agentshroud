---
source_file: "gateway/security/drift_detector.py"
type: "code"
community: "lifespan.py"
location: "L59"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/lifespanpy
---

# DriftDetector

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_16]] - `method` [EXTRACTED]
- [[._init_db()_1]] - `method` [EXTRACTED]
- [[.acknowledge_alert()]] - `method` [EXTRACTED]
- [[.check_drift()]] - `method` [EXTRACTED]
- [[.close()_2]] - `method` [EXTRACTED]
- [[.get_alerts()]] - `method` [EXTRACTED]
- [[.get_baseline()]] - `method` [EXTRACTED]
- [[.set_baseline()]] - `method` [EXTRACTED]
- [[.setup_method()_10]] - `calls` [EXTRACTED]
- [[.test_drift_detector_baseline()]] - `calls` [EXTRACTED]
- [[.test_drift_detector_concurrent_writes()]] - `calls` [INFERRED]
- [[.test_drift_detector_detects_change()]] - `calls` [EXTRACTED]
- [[.test_drift_no_false_positive()]] - `calls` [EXTRACTED]
- [[.test_simultaneous_baseline_and_config_change()]] - `calls` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Detect configuration drift from known-good baselines.]] - `rationale_for` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `shares_data_with` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[NetworkValidator]] - `semantically_similar_to` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestDriftDetector]] - `uses` [INFERRED]
- [[TestDriftDetectorHardened]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEncryptedStore]] - `uses` [INFERRED]
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
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[drift_detector.py_2]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_drift_detection_in_pipeline()]] - `calls` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/lifespanpy