---
type: community
members: 52
---

# LogSanitizer

**Members:** 52 nodes

## Members
- [[dot-__init__()_197]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-_filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-_sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[dot-filter()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-get_log_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[dot-setup_method()_37]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_credit_card_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_log_sanitizer_covers_stack_traces()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_token_error_no_secret_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Custom logging filter that sanitizes sensitive data from log records.]] - rationale - gateway/security/log_sanitizer.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the log sanitizer for integration with logging system.]] - rationale - gateway/ingest_api/middleware.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Log Sanitizer - Security Hardening Module Scrubs PII, credentials, and…]] - rationale - gateway/security/log_sanitizer.py
- [[LogRecord_2]] - code
- [[LogSanitizer]] - code - gateway/security/log_sanitizer.py
- [[Pattern_4]] - code
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py
- [[Stack traces containing secrets should be sanitized.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test Log Sanitizer - verify PII and credential scrubbing from log output.]] - rationale - gateway/tests/test_log_sanitizer.py
- [[Test Log Sanitizer PII Scrubbing]] - code - gateway/tests/test_log_sanitizer.py
- [[Test that errors don't leak sensitive information.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestInfoLeakage]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[Token validation errors shouldn't expose signing keys.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py_2]] - code - gateway/security/log_sanitizer.py
- [[sanitized_getLogger()]] - code - gateway/security/log_sanitizer.py
- [[t_log()]] - code - gateway/ingest_api/main.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LogSanitizer
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_EnvironmentGuard]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[LogSanitizer]] - degree 24, connects to 8 communities
- [[TestInfoLeakage]] - degree 14, connects to 6 communities
- [[log_sanitizer.py_2]] - degree 5, connects to 1 community
- [[dot-get_log_sanitizer()]] - degree 3, connects to 1 community
- [[dot-test_encrypted_store_error_no_key_leak()]] - degree 3, connects to 1 community
