---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "test_security_audit.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# test_security_audit.py

## Connections
- [[AlertDispatcher]] - `references` [EXTRACTED]
- [[ConfusedDeputyError]] - `imports` [EXTRACTED]
- [[ConsentDecision]] - `imports` [EXTRACTED]
- [[ContainerSnapshot]] - `imports` [EXTRACTED]
- [[ContextGuard]] - `imports` [EXTRACTED]
- [[DNSFilterConfig]] - `imports` [EXTRACTED]
- [[DriftDetector]] - `imports` [EXTRACTED]
- [[EgressEvent]] - `imports` [EXTRACTED]
- [[EgressPolicy]] - `imports` [EXTRACTED]
- [[EncryptedStore]] - `imports` [EXTRACTED]
- [[EntropyCalculator]] - `imports` [EXTRACTED]
- [[EnvironmentGuard]] - `imports` [EXTRACTED]
- [[FileSandbox]] - `imports` [EXTRACTED]
- [[FileSandboxConfig]] - `imports` [EXTRACTED]
- [[GitGuard]] - `imports` [EXTRACTED]
- [[IsolationStatus]] - `imports` [EXTRACTED]
- [[KeyVault]] - `imports` [EXTRACTED]
- [[KeyVaultConfig]] - `imports` [EXTRACTED]
- [[LogSanitizer_1]] - `imports` [EXTRACTED]
- [[MetadataGuard]] - `imports` [EXTRACTED]
- [[NetworkValidator]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[PKCEViolation]] - `imports` [EXTRACTED]
- [[PromptGuard]] - `imports` [EXTRACTED]
- [[RedirectMismatch]] - `imports` [EXTRACTED]
- [[ResourceGuard]] - `imports` [EXTRACTED]
- [[ResourceLimits]] - `imports` [EXTRACTED]
- [[Session]] - `imports` [EXTRACTED]
- [[SubagentEvent]] - `imports` [EXTRACTED]
- [[SubagentMonitor]] - `imports` [EXTRACTED]
- [[TestAuditTrail]] - `contains` [EXTRACTED]
- [[TestAuth]] - `contains` [EXTRACTED]
- [[TestContainerSecurity]] - `contains` [EXTRACTED]
- [[TestContextGuard]] - `contains` [EXTRACTED]
- [[TestCryptography]] - `contains` [EXTRACTED]
- [[TestFileSandbox]] - `contains` [EXTRACTED]
- [[TestLoggingSecurity]] - `contains` [EXTRACTED]
- [[TestNetworkSecurity]] - `contains` [EXTRACTED]
- [[TestPIIDetection_1]] - `contains` [EXTRACTED]
- [[TestPromptGuard]] - `contains` [EXTRACTED]
- [[TestResourceProtection]] - `contains` [EXTRACTED]
- [[TestSupplyChain]] - `contains` [EXTRACTED]
- [[ThreatAssessment]] - `imports` [EXTRACTED]
- [[TrustManager]] - `imports` [EXTRACTED]
- [[clamav_scanner.py_2]] - `imports_from` [EXTRACTED]
- [[falco_monitor.py_2]] - `imports_from` [EXTRACTED]
- [[gateway.security.trivy_report]] - `imports_from` [EXTRACTED]
- [[gatewaysecuritydns_filter.py (DNSFilterConfig)]] - `references` [EXTRACTED]
- [[gatewaysecuritydrift_detector.py (DriftDetector)]] - `references` [EXTRACTED]
- [[gatewaysecurityencrypted_store.py (EncryptedStore)]] - `references` [EXTRACTED]
- [[gatewaysecurityfile_sandbox.py (FileSandbox)]] - `references` [EXTRACTED]
- [[gatewaysecuritykey_vault.py (KeyVault)]] - `references` [EXTRACTED]
- [[gatewaysecuritymetadata_guard.py (MetadataGuard)]] - `references` [EXTRACTED]
- [[gatewaysecuritynetwork_validator.py (NetworkValidator)]] - `references` [EXTRACTED]
- [[gatewaysecurityprompt_guard.py (PromptGuard)]] - `references` [EXTRACTED]
- [[health_report.py]] - `imports_from` [EXTRACTED]
- [[oauth_security.py]] - `references` [EXTRACTED]
- [[parse_clamscan_output()]] - `imports` [EXTRACTED]
- [[run_canary()_1]] - `imports` [EXTRACTED]
- [[run_clamscan()]] - `imports` [EXTRACTED]
- [[run_trivy_scan]] - `imports` [EXTRACTED]
- [[test_security_audit_advanced.py]] - `conceptually_related_to` [INFERRED]
- [[wazuh_client.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_security_auditpy