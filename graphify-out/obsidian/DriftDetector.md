---
source_file: "gateway/security/drift_detector.py"
type: "code"
community: "_wrap_response() (2)"
location: "L59"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_wrap_response_2
---

# DriftDetector

## Connections
- [[dot-__init__()_13]] - `calls` [EXTRACTED]
- [[dot-__init__()_111]] - `method` [EXTRACTED]
- [[dot-_init_db()_2]] - `method` [EXTRACTED]
- [[dot-acknowledge_alert()]] - `method` [EXTRACTED]
- [[dot-check_drift()]] - `method` [EXTRACTED]
- [[dot-close()_8]] - `method` [EXTRACTED]
- [[dot-get_alerts()]] - `method` [EXTRACTED]
- [[dot-get_baseline()]] - `method` [EXTRACTED]
- [[dot-set_baseline()]] - `method` [EXTRACTED]
- [[dot-setup_method()_20]] - `calls` [EXTRACTED]
- [[dot-test_drift_detector_baseline()]] - `calls` [EXTRACTED]
- [[dot-test_drift_detector_concurrent_writes()]] - `calls` [INFERRED]
- [[dot-test_drift_detector_detects_change()]] - `calls` [EXTRACTED]
- [[dot-test_drift_no_false_positive()]] - `calls` [EXTRACTED]
- [[dot-test_simultaneous_baseline_and_config_change()]] - `calls` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Detect configuration drift from known-good baselines.]] - `rationale_for` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `shares_data_with` [EXTRACTED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[NetworkValidator]] - `semantically_similar_to` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
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
- [[TestPIIDetection_2]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation_1]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[drift_detector.py]] - `contains` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_drift_detection_in_pipeline()]] - `calls` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/_wrap_response_2
