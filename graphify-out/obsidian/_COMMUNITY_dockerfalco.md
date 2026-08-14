---
type: community
members: 18
---

# docker/falco

**Members:** 18 nodes

## Members
- [[._filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
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
- [[Install the log sanitizer on all existing loggers.]] - rationale - gateway/security/log_sanitizer.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py
- [[install_log_sanitizer()]] - code - gateway/security/log_sanitizer.py
- [[test_log_sanitizer.py]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/docker/falco
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Auth & Exception Types]]

## Top bridge nodes
- [[TestLogSanitizer]] - degree 17, connects to 1 community
- [[install_log_sanitizer()]] - degree 5, connects to 1 community
- [[test_log_sanitizer.py]] - degree 3, connects to 1 community