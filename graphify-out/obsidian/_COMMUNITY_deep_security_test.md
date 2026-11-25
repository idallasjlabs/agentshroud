---
type: community
members: 64
---

# deep_security_test

**Members:** 64 nodes

## Members
- [[dot-__init__()_201]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-_filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-_sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[dot-filter()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-get_log_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[dot-setup_method()_36]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_credit_card_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Comprehensive security integration test — tests every module with real payloads.]] - rationale - gateway/ingest_api/main.py
- [[Custom logging filter that sanitizes sensitive data from log records.]] - rationale - gateway/security/log_sanitizer.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the log sanitizer for integration with logging system.]] - rationale - gateway/ingest_api/middleware.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[Log Sanitizer - Security Hardening Module Scrubs PII, credentials, and…]] - rationale - gateway/security/log_sanitizer.py
- [[LogRecord_1]] - code
- [[LogSanitizer]] - code - gateway/security/log_sanitizer.py
- [[Pattern_5]] - code
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py
- [[Test Log Sanitizer - verify PII and credential scrubbing from log output.]] - rationale - gateway/tests/test_log_sanitizer.py
- [[Test Log Sanitizer PII Scrubbing]] - code - gateway/tests/test_log_sanitizer.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[_check_mod()]] - code - gateway/ingest_api/main.py
- [[_pii()]] - code - gateway/ingest_api/main.py
- [[atest()]] - code - gateway/ingest_api/main.py
- [[deep_security_test()]] - code - gateway/ingest_api/main.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py_2]] - code - gateway/security/log_sanitizer.py
- [[sanitized_getLogger()]] - code - gateway/security/log_sanitizer.py
- [[t_alert()]] - code - gateway/ingest_api/main.py
- [[t_audit()]] - code - gateway/ingest_api/main.py
- [[t_auth()]] - code - gateway/ingest_api/main.py
- [[t_canary()]] - code - gateway/ingest_api/main.py
- [[t_clamav()]] - code - gateway/ingest_api/main.py
- [[t_context()]] - code - gateway/ingest_api/main.py
- [[t_dns()]] - code - gateway/ingest_api/main.py
- [[t_drift()]] - code - gateway/ingest_api/main.py
- [[t_egress()]] - code - gateway/ingest_api/main.py
- [[t_encrypt()]] - code - gateway/ingest_api/main.py
- [[t_git()]] - code - gateway/ingest_api/main.py
- [[t_hardening()]] - code - gateway/ingest_api/main.py
- [[t_keyvault()]] - code - gateway/ingest_api/main.py
- [[t_log()]] - code - gateway/ingest_api/main.py
- [[t_metadata()]] - code - gateway/ingest_api/main.py
- [[t_op()]] - code - gateway/ingest_api/main.py
- [[t_prompt()]] - code - gateway/ingest_api/main.py
- [[t_trivy()]] - code - gateway/ingest_api/main.py
- [[t_trust()]] - code - gateway/ingest_api/main.py
- [[test()]] - code - gateway/ingest_api/main.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/deep_security_test
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_middleware.py]]
- 5 edges to [[_COMMUNITY_EnvironmentGuard]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_PIISanitizer]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_ContainerSnapshot]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_Session]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]

## Top bridge nodes
- [[deep_security_test()]] - degree 48, connects to 13 communities
- [[LogSanitizer]] - degree 24, connects to 6 communities
- [[dot-test_empty_inputs_everywhere()]] - degree 5, connects to 3 communities
- [[log_sanitizer.py_2]] - degree 5, connects to 1 community
- [[dot-get_log_sanitizer()]] - degree 3, connects to 1 community
