---
source_file: "gateway/tests/test_security_audit_advanced.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L107"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Session_Manager__PII/Context_Guard
---

# TestHTTPSecurity

## Connections
- [[dot-test_crlf_in_prompt_guard()]] - `method` [EXTRACTED]
- [[dot-test_deeply_nested_json()]] - `method` [EXTRACTED]
- [[dot-test_json_injection_in_context()]] - `method` [EXTRACTED]
- [[dot-test_null_byte_in_prompt()]] - `method` [EXTRACTED]
- [[dot-test_oversized_json_payload()]] - `method` [EXTRACTED]
- [[dot-test_polyglot_payload()]] - `method` [EXTRACTED]
- [[dot-test_unicode_normalization_bypass()]] - `method` [EXTRACTED]
- [[dot-test_xml_entity_expansion()]] - `method` [EXTRACTED]
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
- [[PIIConfig]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[Session]] - `uses` [INFERRED]
- [[SubagentEventType]] - `uses` [INFERRED]
- [[Test HTTP-level security CRLF, header injection, content types.]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit_advanced.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Session_Manager__PII/Context_Guard