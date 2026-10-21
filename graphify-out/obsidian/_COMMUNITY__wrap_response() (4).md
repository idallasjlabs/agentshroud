---
type: community
members: 69
---

# _wrap_response() (4)

**Members:** 69 nodes

## Members
- [[dot-__init__()_194]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-_filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-_sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[dot-filter()_1]] - code - gateway/security/log_sanitizer.py
- [[dot-monitor_sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-sandbox()]] - code - gateway/tests/test_security_audit.py
- [[dot-sanitizer()_3]] - code - gateway/tests/test_security_audit.py
- [[dot-setup_method()_38]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_absolute_path_to_sensitive_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_app_read_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_basic_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_credit_card_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_double_encoded_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_enforce_vs_monitor_contrast()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_monitor_mode_allows_everything()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_null_byte_injection_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_proc_meminfo_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_proc_self_environ_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_staging_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_symlink_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_tmp_read_allowed()_1]] - code - gateway/tests/test_security_audit.py
- [[dot-test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_windows_traversal_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_outside_allowed_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_pii_detection()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_app_data_allowed()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_system_dir_blocked()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_write_to_tmp_allowed()]] - code - gateway/tests/test_security_audit.py
- [[Access to procselfenviron exposes env vars — must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Allowed read path should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[Any_78]] - code - gateway/security/log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Custom logging filter that sanitizes sensitive data from log records.]] - rationale - gateway/security/log_sanitizer.py
- [[Detect data staging patterns.]] - rationale - gateway/tests/test_security_audit.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[LogRecord_2]] - code - gateway/security/log_sanitizer.py
- [[LogSanitizer_1]] - code - gateway/security/log_sanitizer.py
- [[Monitor mode flags but allows — verify difference from enforce.]] - rationale - gateway/tests/test_security_audit.py
- [[Monitor-mode sandbox for comparison testing.]] - rationale - gateway/tests/test_security_audit.py
- [[Pattern_2]] - code - gateway/security/log_sanitizer.py
- [[Reading from app should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Same path, different modes — enforce blocks, monitor allows.]] - rationale - gateway/tests/test_security_audit.py
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py
- [[Symlink-based escape attempt blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Test file system sandboxing in enforce mode — blocks unauthorized access.]] - rationale - gateway/tests/test_security_audit.py
- [[TestFileSandbox]] - code - gateway/tests/test_security_audit.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[Writing PII should be flagged even to allowed paths.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing outside allowed paths must be blocked.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to appdata should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[Writing to tmp should be allowed.]] - rationale - gateway/tests/test_security_audit.py
- [[get_sanitizer_stats()_1]] - code - gateway/security/log_sanitizer.py
- [[install_log_sanitizer()_1]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py_2]] - code - gateway/security/log_sanitizer.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response_4
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_MiddlewareManager]]
- 12 edges to [[_COMMUNITY__wrap_response()]]
- 8 edges to [[_COMMUNITY__wrap_response() (2)_1]]
- 7 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 4 edges to [[_COMMUNITY_test_playback_state.c]]
- 4 edges to [[_COMMUNITY__wrap_response() (3)_1]]
- 3 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (2)_1]]
- 3 edges to [[_COMMUNITY_PortManager]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_NetworkSecurityFinding]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_SecureBrowser (3)]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY__wrap_response() (5)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_WebProxy]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]

## Top bridge nodes
- [[TestFileSandbox]] - degree 55, connects to 21 communities
- [[LogSanitizer_1]] - degree 45, connects to 11 communities
- [[log_sanitizer.py_2]] - degree 7, connects to 4 communities
- [[dot-monitor_sandbox()]] - degree 4, connects to 1 community
- [[dot-sandbox()]] - degree 3, connects to 1 community
