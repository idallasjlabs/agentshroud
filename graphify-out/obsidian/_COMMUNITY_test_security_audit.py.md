---
type: community
cohesion: 0.02
members: 152
---

# test_security_audit.py

**Cohesion:** 0.02 - loosely connected
**Members:** 152 nodes

## Members
- [[.__init__()_87]] - code - gateway/security/oauth_security.py
- [[._make_record()]] - code - gateway/tests/test_security_audit.py
- [[.check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[.create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.guard()_1]] - code - gateway/tests/test_security_audit.py
- [[.guard()_2]] - code - gateway/tests/test_security_audit.py
- [[.record_state_used()]] - code - gateway/security/oauth_security.py
- [[.register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[.sanitizer()_3]] - code - gateway/tests/test_security_audit.py
- [[.sanitizer()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_aws_key_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_aws_key_redaction_via_pattern()]] - code - gateway/tests/test_security_audit.py
- [[.test_base64_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_conversation()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_message_not_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_technical_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_context_window_stuffing()]] - code - gateway/tests/test_security_audit.py
- [[.test_conversation_history_manipulation()]] - code - gateway/tests/test_security_audit.py
- [[.test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_credit_card_amex()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_credit_card_visa()]] - code - gateway/tests/test_security_audit.py
- [[.test_dan_jailbreak()]] - code - gateway/tests/test_security_audit.py
- [[.test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_email_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_email_with_plus()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_and_none_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_env_guard_command_check()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_monitoring()]] - code - gateway/tests/test_security_audit.py
- [[.test_env_guard_scrub_output()]] - code - gateway/tests/test_security_audit.py
- [[.test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_fake_system_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_git_guard_scan_repo()]] - code - gateway/tests/test_security_audit.py
- [[.test_github_token_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_ignore_previous_instructions()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_indirect_injection_url()]] - code - gateway/tests/test_security_audit.py
- [[.test_instruction_override()]] - code - gateway/tests/test_security_audit.py
- [[.test_json_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_jwt_redaction()]] - code - gateway/tests/test_security_audit.py
- [[.test_markdown_heading_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_multilingual_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_multiple_pii_single_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_dates()]] - code - gateway/tests/test_security_audit.py
- [[.test_no_false_positive_on_zip()]] - code - gateway/tests/test_security_audit.py
- [[.test_path_traversal_rejected()_1]] - code - gateway/tests/test_oauth_security.py
- [[.test_phone_international()]] - code - gateway/tests/test_security_audit.py
- [[.test_phone_us_standard()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_boundary_handling()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_code_block()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_in_json()]] - code - gateway/tests/test_security_audit.py
- [[.test_pii_with_obfuscation_attempt()]] - code - gateway/tests/test_security_audit.py
- [[.test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[.test_prompt_leaking_via_markdown()]] - code - gateway/tests/test_security_audit.py
- [[.test_rapid_fire_messages()]] - code - gateway/tests/test_security_audit.py
- [[.test_repeated_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_role_reassignment()_1]] - code - gateway/tests/test_security_audit.py
- [[.test_role_switching()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_isolation()]] - code - gateway/tests/test_security_audit.py
- [[.test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_ssn_no_dashes()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_redaction_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_space_separated()]] - code - gateway/tests/test_security_audit.py
- [[.test_ssn_standard_format()]] - code - gateway/tests/test_security_audit.py
- [[.test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_system_prompt_extraction()]] - code - gateway/tests/test_security_audit.py
- [[.test_token_smuggling()]] - code - gateway/tests/test_security_audit.py
- [[.test_unicode_pii()]] - code - gateway/tests/test_security_audit.py
- [[.test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_xml_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_xml_tag_injection()]] - code - gateway/tests/test_security_audit.py
- [[.validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[.validate_request()]] - code - gateway/security/oauth_security.py
- [[.verify_pkce()]] - code - gateway/security/oauth_security.py
- [[Amex card 378282246310005 (15 digits starting with 37).]] - rationale - gateway/tests/test_security_audit.py
- [[Attempt to hide PII with zero-width chars.]] - rationale - gateway/tests/test_security_audit.py
- [[Base64 encoded instruction.]] - rationale - gateway/tests/test_security_audit.py
- [[Card without dashes 4111111111111111.]] - rationale - gateway/tests/test_security_audit.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Dates should not be flagged as SSNphone.]] - rationale - gateway/tests/test_security_audit.py
- [[Different sessions should not share state unsafely.]] - rationale - gateway/tests/test_security_audit.py
- [[Edge case empty string.]] - rationale - gateway/tests/test_security_audit.py
- [[Email with plus addressing user+tag@gmail.com.]] - rationale - gateway/tests/test_security_audit.py
- [[Fill context with repeated instructions.]] - rationale - gateway/tests/test_security_audit.py
- [[Injection in another language.]] - rationale - gateway/tests/test_security_audit.py
- [[International phone +1-555-867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Markdown-based injection.]] - rationale - gateway/tests/test_security_audit.py
- [[Multiple PII entities in one message.]] - rationale - gateway/tests/test_security_audit.py
- [[Normal messages should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PII at message start and end.]] - rationale - gateway/tests/test_security_audit.py
- [[PII embedded in JSON.]] - rationale - gateway/tests/test_security_audit.py
- [[PII in codemarkdown blocks.]] - rationale - gateway/tests/test_security_audit.py
- [[PII with Unicode characters nearby.]] - rationale - gateway/tests/test_security_audit.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[Rapid messages shouldn't cause errors.]] - rationale - gateway/tests/test_security_audit.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[SSN in standard XXX-XX-XXXX format.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN with spaces 123 45 6789.]] - rationale - gateway/tests/test_security_audit.py
- [[SSN without dashes 123456789 — Presidio+spaCy only (regex needs dashes).]] - rationale - gateway/tests/test_security_audit.py
- [[Same injection multiple times shouldn't bypass.]] - rationale - gateway/tests/test_security_audit.py
- [[Standard email address.]] - rationale - gateway/tests/test_security_audit.py
- [[Technical discussion mentioning 'system' shouldn't trigger.]] - rationale - gateway/tests/test_security_audit.py
- [[Test PII sanitization — works with Presidio (Python ≤3.13) or regex fallback (3.]] - rationale - gateway/tests/test_security_audit.py
- [[Test context manipulation detection.]] - rationale - gateway/tests/test_security_audit.py
- [[Test log sanitization and information leakage prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[Test prompt injection detection with adversarial payloads.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestContextGuard]] - code - gateway/tests/test_security_audit.py
- [[TestLoggingSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestPIIDetection_1]] - code - gateway/tests/test_security_audit.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestPromptGuard]] - code - gateway/tests/test_security_audit.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[Token boundary attack.]] - rationale - gateway/tests/test_security_audit.py
- [[URL-based indirect injection.]] - rationale - gateway/tests/test_security_audit.py
- [[US phone (555) 867-5309.]] - rationale - gateway/tests/test_security_audit.py
- [[Visa card 4111-1111-1111-1111.]] - rationale - gateway/tests/test_security_audit.py
- [[ZIP codes should not be flagged as SSNphoneCC.]] - rationale - gateway/tests/test_security_audit.py
- [[gatewaysecuritydns_filter.py (DNSFilterConfig)]] - code - gateway/security/dns_filter.py
- [[gatewaysecuritydrift_detector.py (DriftDetector)]] - code - gateway/security/drift_detector.py
- [[gatewaysecurityencrypted_store.py (EncryptedStore)]] - code - gateway/security/encrypted_store.py
- [[gatewaysecurityfile_sandbox.py (FileSandbox)]] - code - gateway/security/file_sandbox.py
- [[gatewaysecuritykey_vault.py (KeyVault)]] - code - gateway/security/key_vault.py
- [[gatewaysecuritymetadata_guard.py (MetadataGuard)]] - code - gateway/security/metadata_guard.py
- [[gatewaysecuritynetwork_validator.py (NetworkValidator)]] - code - gateway/security/network_validator.py
- [[gatewaysecurityprompt_guard.py (PromptGuard)]] - code - gateway/security/prompt_guard.py
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[test_security_audit.py]] - code - gateway/tests/test_security_audit.py
- [[validator()_1]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_auditpy
SORT file.name ASC
```

## Connections to other communities
- 84 edges to [[_COMMUNITY_lifespan.py]]
- 26 edges to [[_COMMUNITY_EncryptedStore]]
- 18 edges to [[_COMMUNITY_TrustManager]]
- 14 edges to [[_COMMUNITY_TestAuth]]
- 14 edges to [[_COMMUNITY_ResourceGuard]]
- 11 edges to [[_COMMUNITY_DNSFilterConfig]]
- 10 edges to [[_COMMUNITY_FileSandbox]]
- 7 edges to [[_COMMUNITY_ConsentFramework]]
- 6 edges to [[_COMMUNITY_GitGuard]]
- 5 edges to [[_COMMUNITY_KeyVaultConfig]]
- 5 edges to [[_COMMUNITY_EgressPolicy]]
- 5 edges to [[_COMMUNITY_KeyVault]]
- 4 edges to [[_COMMUNITY_TestFileSandbox]]
- 2 edges to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_health_report.py]]
- 1 edge to [[_COMMUNITY_wazuh_client.py]]

## Top bridge nodes
- [[test_security_audit.py]] - degree 63, connects to 18 communities
- [[TestPIIDetection_1]] - degree 55, connects to 12 communities
- [[TestPromptGuard]] - degree 51, connects to 12 communities
- [[TestLoggingSecurity]] - degree 47, connects to 12 communities
- [[TestContextGuard]] - degree 46, connects to 12 communities