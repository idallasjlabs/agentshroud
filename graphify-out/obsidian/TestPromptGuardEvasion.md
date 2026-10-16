---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "AlertDispatcher"
location: "L797"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/AlertDispatcher
---

# TestPromptGuardEvasion

## Connections
- [[dot-setup_method()_16]] - `method` [EXTRACTED]
- [[dot-test_double_base64_injection()]] - `method` [EXTRACTED]
- [[dot-test_fullwidth_detection()]] - `method` [EXTRACTED]
- [[dot-test_homoglyph_detection()]] - `method` [EXTRACTED]
- [[dot-test_mixed_case_still_caught()]] - `method` [EXTRACTED]
- [[dot-test_rtl_override_detection()]] - `method` [EXTRACTED]
- [[dot-test_zero_width_evasion()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig_1]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `uses` [INFERRED]
- [[PatternRule]] - `uses` [INFERRED]
- [[PromptGuard_1]] - `uses` [INFERRED]
- [[Tests for prompt guard evasion techniques.]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/AlertDispatcher
