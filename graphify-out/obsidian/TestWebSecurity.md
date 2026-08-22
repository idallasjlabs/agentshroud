---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Security Audit & Watchtower Tests"
location: "L706"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Security_Audit__Watchtower_Tests
---

# TestWebSecurity

## Connections
- [[.test_dashboard_has_csp_meta()]] - `method` [EXTRACTED]
- [[.test_dashboard_html_exists()]] - `method` [EXTRACTED]
- [[.test_dashboard_no_inline_secrets()]] - `method` [EXTRACTED]
- [[.test_no_mixed_content()]] - `method` [EXTRACTED]
- [[.test_xss_in_dashboard_inputs()]] - `method` [EXTRACTED]
- [[AlertDispatcher]] - `uses` [INFERRED]
- [[ConsentDecision]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[ContextGuard]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressChannel]] - `uses` [INFERRED]
- [[EgressEvent]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[EntropyCalculator]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandbox]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MetadataGuard]] - `uses` [INFERRED]
- [[PIIConfig_1]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[Test web dashboard and API security headers.]] - `rationale_for` [EXTRACTED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Security_Audit__Watchtower_Tests