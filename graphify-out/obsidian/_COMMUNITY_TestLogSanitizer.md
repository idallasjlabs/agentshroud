---
type: community
cohesion: 0.24
members: 15
---

# TestLogSanitizer

**Cohesion:** 0.24 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-_filter_msg()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-setup_method()_33]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_aws_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_clean_message_unchanged()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_credit_card_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_filter_always_returns_true()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_openai_key_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_password_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_secret_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_ssn_redacted()_1]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_in_url_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_telegram_bot_token_shorter_id_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_token_assignment_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[dot-test_user_path_redacted()]] - code - gateway/tests/test_log_sanitizer.py
- [[TestLogSanitizer]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestLogSanitizer
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[TestLogSanitizer]] - degree 17, connects to 1 community
- [[dot-setup_method()_33]] - degree 2, connects to 1 community
