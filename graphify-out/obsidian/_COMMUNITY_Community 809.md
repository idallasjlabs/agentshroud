---
type: community
members: 120
---

# Community 809

**Members:** 120 nodes

## Members
- [[.__init__()_108]] - code - gateway/security/log_sanitizer.py
- [[._compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[._filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[._sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[.filter()_1]] - code - gateway/security/log_sanitizer.py
- [[.sanitizer()_2]] - code - gateway/tests/test_security_audit.py
- [[.setup_method()_7]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_binary_data_in_text_fields()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_consent_required_for_sensitive_ops()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_credit_card_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_crlf_in_prompt_guard()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_has_csp_meta()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_html_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_dashboard_no_inline_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_deeply_nested_context_attacks()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_deeply_nested_json()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_encrypted_store_constant_time()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_hmac_comparison_for_secrets()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_json_injection_in_context()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_many_pii_entities()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_no_mixed_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_no_pickle_in_security_modules()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_no_shell_true_in_subprocess()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_no_yaml_unsafe_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_null_byte_in_prompt()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_oversized_json_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_pii_scan_time_independent_of_content()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_polyglot_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_prompt_guard_no_early_exit_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_rapid_fire_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_regex_redos_email()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_regex_redos_ssn()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_requirements_pinned()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_session_cannot_impersonate()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_subagent_monitor_tracks_events()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_token_validation_rejects_fast()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_trust_cannot_exceed_max()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_unicode_normalization_bypass()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_unregistered_agent_blocked()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_very_long_message()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_violation_drops_trust_significantly()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_xml_entity_expansion()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_xss_in_dashboard_inputs()]] - code - gateway/tests/test_security_audit_advanced.py
- [[A single violation should meaningfully impact trust.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Any_56]] - code - gateway/security/log_sanitizer.py
- [[Binary data in text fields shouldn't crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[CRLF injection in prompt shouldn't bypass detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Consent framework should be available for gating.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Custom logging filter that sanitizes sensitive data from log records.]] - rationale - gateway/security/log_sanitizer.py
- [[Dashboard should escape user inputs (no raw innerHTML from API).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have Content-Security-Policy or mention it.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should have an HTML file.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not contain hardcoded secrets.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Dashboard should not load HTTP resources.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Deeply nested JSON shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Different sessions should have different identities.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Email regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Encryptiondecryption time should not leak plaintext length.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[Invalid tokens should be rejected quickly (no expensive operations).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[JSON injection in message shouldn't manipulate context.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[LogRecord_1]] - code - gateway/security/log_sanitizer.py
- [[LogSanitizer_1]] - code - gateway/security/log_sanitizer.py
- [[Message with hundreds of PII entities should complete.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Nested context attacks shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[No yaml.load() without Loader (arbitrary code execution).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Null bytes shouldn't bypass prompt guard.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[PII scanning time should be roughly linear, not exponential.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[Polyglot (valid as multiple formats) shouldn't bypass checks.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard should scan full input, not short-circuit on first match.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Rapid scanning shouldn't degrade or crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Requirements should have pinned versions.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[SSN regex should not be vulnerable to ReDoS.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py
- [[Security modules should not use pickle (deserialization attack).]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subagent events should be trackable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Subprocess calls should not pass shell=True.          Uses AST analysis to flag]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test HTTP-level security CRLF, header injection, content types.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test dependency and supply chain security.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test for timing side-channels in security-critical comparisons.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test resilience against denial of service patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test trust boundaries and privilege escalation prevention.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test web dashboard and API security headers.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestDependencySecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestDoSPrevention]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestHTTPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[TestPrivilegeEscalation]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestTimingAttacks]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestWebSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[Trust score should have an upper bound.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Unicode tricks shouldn't bypass PII detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Unregistered agents should not be trusted.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Verify hmac.compare_digest is available for constant-time comparison.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Very large JSON shouldn't crash the parser.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Very long messages should be handled without crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[XXE-style payloads shouldn't crash processing.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py
- [[test_security_audit_advanced.py]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_809
SORT file.name ASC
```

## Connections to other communities
- 44 edges to [[_COMMUNITY_Community 72]]
- 31 edges to [[_COMMUNITY_Community 0]]
- 19 edges to [[_COMMUNITY_Community 52]]
- 19 edges to [[_COMMUNITY_Community 121]]
- 18 edges to [[_COMMUNITY_Community 84]]
- 9 edges to [[_COMMUNITY_Community 557]]
- 6 edges to [[_COMMUNITY_Community 152]]
- 6 edges to [[_COMMUNITY_Community 21]]
- 6 edges to [[_COMMUNITY_Community 31]]
- 6 edges to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 684]]
- 1 edge to [[_COMMUNITY_Community 76]]
- 1 edge to [[_COMMUNITY_Community 394]]
- 1 edge to [[_COMMUNITY_Community 140]]
- 1 edge to [[_COMMUNITY_Community 60]]
- 1 edge to [[_COMMUNITY_Community 137]]

## Top bridge nodes
- [[TestHTTPSecurity]] - degree 32, connects to 10 communities
- [[TestDoSPrevention]] - degree 32, connects to 10 communities
- [[TestPrivilegeEscalation]] - degree 30, connects to 10 communities
- [[TestTimingAttacks]] - degree 29, connects to 10 communities
- [[TestWebSecurity]] - degree 29, connects to 10 communities