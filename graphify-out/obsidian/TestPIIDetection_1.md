---
source_file: "gateway/tests/test_security_audit.py"
type: "code"
community: "P3 Infrastructure Security Modules"
location: "L39"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/P3_Infrastructure_Security_Modules
---

# TestPIIDetection

## Connections
- [[dot-sanitizer()_1]] - `method` [EXTRACTED]
- [[dot-test_credit_card_amex()]] - `method` [EXTRACTED]
- [[dot-test_credit_card_no_dashes()]] - `method` [EXTRACTED]
- [[dot-test_credit_card_visa()]] - `method` [EXTRACTED]
- [[dot-test_email_standard()]] - `method` [EXTRACTED]
- [[dot-test_email_with_plus()]] - `method` [EXTRACTED]
- [[dot-test_empty_and_none_input()]] - `method` [EXTRACTED]
- [[dot-test_multiple_pii_single_message()]] - `method` [EXTRACTED]
- [[dot-test_no_false_positive_on_dates()]] - `method` [EXTRACTED]
- [[dot-test_no_false_positive_on_zip()]] - `method` [EXTRACTED]
- [[dot-test_phone_international()]] - `method` [EXTRACTED]
- [[dot-test_phone_us_standard()]] - `method` [EXTRACTED]
- [[dot-test_pii_boundary_handling()]] - `method` [EXTRACTED]
- [[dot-test_pii_in_code_block()]] - `method` [EXTRACTED]
- [[dot-test_pii_in_json()]] - `method` [EXTRACTED]
- [[dot-test_pii_with_obfuscation_attempt()]] - `method` [EXTRACTED]
- [[dot-test_ssn_no_dashes()]] - `method` [EXTRACTED]
- [[dot-test_ssn_space_separated()]] - `method` [EXTRACTED]
- [[dot-test_ssn_standard_format()]] - `method` [EXTRACTED]
- [[dot-test_unicode_pii()]] - `method` [EXTRACTED]
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
- [[Test PII sanitization — works with Presidio (Python ≤3.13) or regex fallback (3.]] - `rationale_for` [EXTRACTED]
- [[ThreatAssessment]] - `uses` [INFERRED]
- [[TrustManager]] - `uses` [INFERRED]
- [[test_security_audit.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/P3_Infrastructure_Security_Modules