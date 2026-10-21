---
source_file: "gateway/security/drift_detector.py"
type: "code"
community: "_wrap_response() (2)"
location: "L24"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/_wrap_response_2
---

# ContainerSnapshot

## Connections
- [[dot-check_drift()]] - `references` [EXTRACTED]
- [[dot-config_hash()]] - `method` [EXTRACTED]
- [[dot-from_dict()_3]] - `method` [EXTRACTED]
- [[dot-get_baseline()]] - `references` [EXTRACTED]
- [[dot-set_baseline()]] - `references` [EXTRACTED]
- [[dot-setup_method()_20]] - `calls` [EXTRACTED]
- [[dot-test_acknowledge_alert()]] - `calls` [EXTRACTED]
- [[dot-test_alerts_persisted()]] - `calls` [EXTRACTED]
- [[dot-test_config_hash_changes()]] - `calls` [EXTRACTED]
- [[dot-test_drift_detector_baseline()]] - `calls` [EXTRACTED]
- [[dot-test_drift_detector_concurrent_writes()]] - `calls` [INFERRED]
- [[dot-test_drift_detector_detects_change()]] - `calls` [EXTRACTED]
- [[dot-test_drift_no_false_positive()]] - `calls` [EXTRACTED]
- [[dot-test_image_change()]] - `calls` [EXTRACTED]
- [[dot-test_new_capability()]] - `calls` [EXTRACTED]
- [[dot-test_new_env_var()]] - `calls` [EXTRACTED]
- [[dot-test_new_mount()]] - `calls` [EXTRACTED]
- [[dot-test_no_baseline_no_alerts()]] - `calls` [EXTRACTED]
- [[dot-test_no_drift()]] - `calls` [EXTRACTED]
- [[dot-test_privileged_escalation()]] - `calls` [EXTRACTED]
- [[dot-test_read_only_disabled()]] - `calls` [EXTRACTED]
- [[dot-test_removed_capability()]] - `calls` [EXTRACTED]
- [[dot-test_seccomp_drift()]] - `calls` [EXTRACTED]
- [[dot-test_simultaneous_baseline_and_config_change()]] - `calls` [EXTRACTED]
- [[dot-to_dict()_6]] - `method` [EXTRACTED]
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
- [[drift_detector.py]] - `contains` [EXTRACTED]
- [[test_drift_detection_in_pipeline()]] - `calls` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/_wrap_response_2
