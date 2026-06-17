---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "Module Group 323"
location: "L797"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Module_Group_323
---

# TestPromptGuardEvasion

## Connections
- [[.setup_method()_29]] - `method` [EXTRACTED]
- [[.test_double_base64_injection()]] - `method` [EXTRACTED]
- [[.test_fullwidth_detection()]] - `method` [EXTRACTED]
- [[.test_homoglyph_detection()]] - `method` [EXTRACTED]
- [[.test_mixed_case_still_caught()]] - `method` [EXTRACTED]
- [[.test_rtl_override_detection()]] - `method` [EXTRACTED]
- [[.test_zero_width_evasion()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
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
- [[PromptGuard]] - `uses` [INFERRED]
- [[Tests for prompt guard evasion techniques.]] - `rationale_for` [EXTRACTED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Module_Group_323