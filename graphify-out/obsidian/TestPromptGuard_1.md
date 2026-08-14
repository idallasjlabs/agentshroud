---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "Audit Export Pipeline"
location: "L149"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Audit_Export_Pipeline
---

# TestPromptGuard

## Connections
- [[.setup_method()_27]] - `method` [EXTRACTED]
- [[.test_base64_encoded_injection()]] - `method` [EXTRACTED]
- [[.test_benign_base64()]] - `method` [EXTRACTED]
- [[.test_clean_input()]] - `method` [EXTRACTED]
- [[.test_combined_attack_high_score()]] - `method` [EXTRACTED]
- [[.test_custom_pattern()]] - `method` [EXTRACTED]
- [[.test_dan_jailbreak()_1]] - `method` [EXTRACTED]
- [[.test_delimiter_injection()]] - `method` [EXTRACTED]
- [[.test_empty_input()_3]] - `method` [EXTRACTED]
- [[.test_forget_everything()]] - `method` [EXTRACTED]
- [[.test_ignore_instructions()]] - `method` [EXTRACTED]
- [[.test_indirect_injection()]] - `method` [EXTRACTED]
- [[.test_new_instructions_override()]] - `method` [EXTRACTED]
- [[.test_none_input()]] - `method` [EXTRACTED]
- [[.test_prompt_extraction()]] - `method` [EXTRACTED]
- [[.test_prompt_leak_question()]] - `method` [EXTRACTED]
- [[.test_role_reassignment()_1]] - `method` [EXTRACTED]
- [[.test_rtl_override()]] - `method` [EXTRACTED]
- [[.test_sanitized_output()]] - `method` [EXTRACTED]
- [[.test_unicode_zero_width()]] - `method` [EXTRACTED]
- [[.test_warn_threshold()]] - `method` [EXTRACTED]
- [[.test_xml_tag_injection()_1]] - `method` [EXTRACTED]
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
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Audit_Export_Pipeline