---
type: community
members: 44
---

# Community 684

**Members:** 44 nodes

## Members
- [[.__init__()_93]] - code - gateway/security/log_sanitizer.py
- [[._compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[._contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[._filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[._looks_like_credential()]] - code - gateway/security/env_guard.py
- [[._record_leakage()]] - code - gateway/security/env_guard.py
- [[.check_command_execution()]] - code - gateway/security/env_guard.py
- [[.check_file_access()]] - code - gateway/security/env_guard.py
- [[.scrub_command_output()]] - code - gateway/security/env_guard.py
- [[.setup_method()_7]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_credit_card_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_install_log_sanitizer_no_error()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[.test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[Any_46]] - code - gateway/security/log_sanitizer.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Get statistics about sanitization patterns.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[Pattern_1]] - code - gateway/security/log_sanitizer.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[get_sanitizer_stats()]] - code - gateway/security/log_sanitizer.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[log_sanitizer.py]] - code - gateway/security/log_sanitizer.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_684
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_Community 0]]
- 4 edges to [[_COMMUNITY_Community 362]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 72]]
- 1 edge to [[_COMMUNITY_Community 420]]
- 1 edge to [[_COMMUNITY_Community 76]]

## Top bridge nodes
- [[env_guard.py]] - degree 10, connects to 6 communities
- [[log_sanitizer.py]] - degree 7, connects to 4 communities
- [[.check_command_execution()]] - degree 5, connects to 2 communities
- [[get_env_guard()]] - degree 4, connects to 2 communities
- [[TestLogSanitizer]] - degree 17, connects to 1 community