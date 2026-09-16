---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "Alert Dispatcher & RBAC Reliability"
location: "L603"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Alert_Dispatcher__RBAC_Reliability
---

# TestNetworkSecurity

## Connections
- [[dot-test_browser_security_loaded()]] - `method` [EXTRACTED]
- [[dot-test_dns_entropy_calculator()]] - `method` [EXTRACTED]
- [[dot-test_dns_filter_config()]] - `method` [EXTRACTED]
- [[dot-test_dns_low_entropy_legit()]] - `method` [EXTRACTED]
- [[dot-test_egress_filter_loaded()]] - `method` [EXTRACTED]
- [[dot-test_egress_monitor_loaded()]] - `method` [EXTRACTED]
- [[dot-test_metadata_oversized_headers()]] - `method` [EXTRACTED]
- [[dot-test_metadata_path_traversal_stripped()]] - `method` [EXTRACTED]
- [[dot-test_metadata_sanitize_filename()]] - `method` [EXTRACTED]
- [[dot-test_network_validator_importable()]] - `method` [EXTRACTED]
- [[dot-test_oauth_redirect_mismatch()]] - `method` [EXTRACTED]
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
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[ResourceLimits]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEvent]] - `uses` [INFERRED]
- [[SubagentMonitor]] - `uses` [INFERRED]
- [[Test DNS filtering, SSRF prevention, and egress control.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Alert_Dispatcher__RBAC_Reliability