---
type: community
members: 22
---

# Community 405

**Members:** 22 nodes

## Members
- [[Bare 10-digit Telegram UID must pass through unchanged — no PHONE_NUMBER.]] - rationale - gateway/tests/test_sanitizer.py
- [[Phone number with separator must still be redacted.]] - rationale - gateway/tests/test_sanitizer.py
- [[Regex-only path must not match bare 10-digit digit string as phone number.]] - rationale - gateway/tests/test_sanitizer.py
- [[Test content with multiple PII types]] - rationale - gateway/tests/test_sanitizer.py
- [[Test content with no PII]] - rationale - gateway/tests/test_sanitizer.py
- [[Test credit card redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[Test email address redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[Test empty content handling]] - rationale - gateway/tests/test_sanitizer.py
- [[Test phone number redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[UID in parens — as written in contributor logs — must not be redacted.]] - rationale - gateway/tests/test_sanitizer.py
- [[test_credit_card_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_email_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_empty_content()]] - code - gateway/tests/test_sanitizer.py
- [[test_mixed_pii()]] - code - gateway/tests/test_sanitizer.py
- [[test_no_pii()]] - code - gateway/tests/test_sanitizer.py
- [[test_phone_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_real_phone_still_redacted()]] - code - gateway/tests/test_sanitizer.py
- [[test_regex_fallback_requires_separator()]] - code - gateway/tests/test_sanitizer.py
- [[test_sanitizer.py]] - code - gateway/tests/test_sanitizer.py
- [[test_ssn_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_telegram_uid_not_redacted_as_phone()]] - code - gateway/tests/test_sanitizer.py
- [[test_uid_inside_parens_preserved()]] - code - gateway/tests/test_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_405
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 1]]

## Top bridge nodes
- [[test_sanitizer.py]] - degree 12, connects to 1 community