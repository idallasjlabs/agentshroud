---
source_file: "gateway/security/drift_detector.py"
type: "code"
community: "Security Audit & Drift Detection"
location: "L24"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Drift_Detection
---

# ContainerSnapshot

## Connections
- [[.check_drift()]] - `references` [EXTRACTED]
- [[.config_hash()]] - `method` [EXTRACTED]
- [[.from_dict()_5]] - `method` [EXTRACTED]
- [[.get_baseline()]] - `references` [EXTRACTED]
- [[.set_baseline()]] - `references` [EXTRACTED]
- [[.setup_method()_30]] - `calls` [EXTRACTED]
- [[.test_acknowledge_alert()]] - `calls` [EXTRACTED]
- [[.test_alerts_persisted()]] - `calls` [EXTRACTED]
- [[.test_config_hash_changes()]] - `calls` [EXTRACTED]
- [[.test_drift_detector_baseline()]] - `calls` [EXTRACTED]
- [[.test_drift_detector_concurrent_writes()]] - `calls` [INFERRED]
- [[.test_drift_detector_detects_change()]] - `calls` [EXTRACTED]
- [[.test_drift_no_false_positive()]] - `calls` [EXTRACTED]
- [[.test_image_change()]] - `calls` [EXTRACTED]
- [[.test_new_capability()]] - `calls` [EXTRACTED]
- [[.test_new_env_var()]] - `calls` [EXTRACTED]
- [[.test_new_mount()]] - `calls` [EXTRACTED]
- [[.test_no_baseline_no_alerts()]] - `calls` [EXTRACTED]
- [[.test_no_drift()]] - `calls` [EXTRACTED]
- [[.test_privileged_escalation()]] - `calls` [EXTRACTED]
- [[.test_read_only_disabled()]] - `calls` [EXTRACTED]
- [[.test_removed_capability()]] - `calls` [EXTRACTED]
- [[.test_seccomp_drift()]] - `calls` [EXTRACTED]
- [[.test_simultaneous_baseline_and_config_change()]] - `calls` [EXTRACTED]
- [[.to_dict()_8]] - `method` [EXTRACTED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
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
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[drift_detector.py]] - `contains` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[test_drift_detection_in_pipeline()]] - `calls` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Drift_Detection