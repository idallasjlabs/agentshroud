---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "Security Audit & Drift Detection"
location: "L482"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Drift_Detection
---

# TestFileSandbox

## Connections
- [[.monitor_sandbox()]] - `method` [EXTRACTED]
- [[.sandbox()]] - `method` [EXTRACTED]
- [[.test_absolute_path_to_sensitive_blocked()]] - `method` [EXTRACTED]
- [[.test_app_read_allowed()]] - `method` [EXTRACTED]
- [[.test_basic_traversal_blocked()]] - `method` [EXTRACTED]
- [[.test_double_encoded_traversal_blocked()]] - `method` [EXTRACTED]
- [[.test_enforce_vs_monitor_contrast()]] - `method` [EXTRACTED]
- [[.test_monitor_mode_allows_everything()_1]] - `method` [EXTRACTED]
- [[.test_null_byte_injection_blocked()]] - `method` [EXTRACTED]
- [[.test_proc_meminfo_allowed()]] - `method` [EXTRACTED]
- [[.test_proc_self_environ_blocked()]] - `method` [EXTRACTED]
- [[.test_staging_detection()]] - `method` [EXTRACTED]
- [[.test_symlink_traversal_blocked()]] - `method` [EXTRACTED]
- [[.test_tmp_read_allowed()_1]] - `method` [EXTRACTED]
- [[.test_windows_traversal_blocked()]] - `method` [EXTRACTED]
- [[.test_write_outside_allowed_blocked()]] - `method` [EXTRACTED]
- [[.test_write_pii_detection()]] - `method` [EXTRACTED]
- [[.test_write_to_app_data_allowed()]] - `method` [EXTRACTED]
- [[.test_write_to_system_dir_blocked()]] - `method` [EXTRACTED]
- [[.test_write_to_tmp_allowed()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ConfusedDeputyError]] - `uses` [INFERRED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DNSFilterConfig]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EntropyCalculator]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[KeyVault]] - `uses` [INFERRED]
- [[KeyVaultConfig]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[NetworkValidator]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[ResourceLimits]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEvent]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[Test file system sandboxing in enforce mode — blocks unauthorized access.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Drift_Detection