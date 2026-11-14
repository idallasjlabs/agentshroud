---
type: community
members: 41
---

# Community 435

**Members:** 41 nodes

## Members
- [[.__init__()_205]] - code - gateway/tests/test_sanitizer.py
- [[.__init__()_206]] - code - gateway/tests/test_sanitizer.py
- [[.analyze()_2]] - code - gateway/tests/test_sanitizer.py
- [[Bare 10-digit Telegram UID must pass through unchanged — no PHONE_NUMBER.]] - rationale - gateway/tests/test_sanitizer.py
- [[Phone number with separator must still be redacted.]] - rationale - gateway/tests/test_sanitizer.py
- [[Regex-only path must not match bare 10-digit digit string as phone number.]] - rationale - gateway/tests/test_sanitizer.py
- [[Returns a single PERSON hit at a fixed score (0.92, just above the floor).]] - rationale - gateway/tests/test_sanitizer.py
- [[Test content with multiple PII types]] - rationale - gateway/tests/test_sanitizer.py
- [[Test content with no PII]] - rationale - gateway/tests/test_sanitizer.py
- [[Test credit card redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[Test email address redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[Test empty content handling]] - rationale - gateway/tests/test_sanitizer.py
- [[Test phone number redaction]] - rationale - gateway/tests/test_sanitizer.py
- [[UID in parens — as written in contributor logs — must not be redacted.]] - rationale - gateway/tests/test_sanitizer.py
- [[_FakeAnalyzer]] - code - gateway/tests/test_sanitizer.py
- [[_FakeRecognizerResult_1]] - code - gateway/tests/test_sanitizer.py
- [[_presidio_sanitizer()]] - code - gateway/tests/test_sanitizer.py
- [[_regex_sanitizer()]] - code - gateway/tests/test_sanitizer.py
- [[test_block_action_blocks_and_withholds_pii()]] - code - gateway/tests/test_sanitizer.py
- [[test_block_action_clean_content_passes_unchanged()]] - code - gateway/tests/test_sanitizer.py
- [[test_credit_card_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_email_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_empty_content()]] - code - gateway/tests/test_sanitizer.py
- [[test_min_confidence_above_one_rejected()]] - code - gateway/tests/test_sanitizer.py
- [[test_min_confidence_at_floor_is_identical_to_default()]] - code - gateway/tests/test_sanitizer.py
- [[test_min_confidence_can_be_raised()]] - code - gateway/tests/test_sanitizer.py
- [[test_min_confidence_cannot_be_lowered_below_floor()]] - code - gateway/tests/test_sanitizer.py
- [[test_mixed_pii()]] - code - gateway/tests/test_sanitizer.py
- [[test_monitor_mode_reports_but_never_mutates()]] - code - gateway/tests/test_sanitizer.py
- [[test_no_pii()]] - code - gateway/tests/test_sanitizer.py
- [[test_per_call_action_override()]] - code - gateway/tests/test_sanitizer.py
- [[test_per_call_invalid_action_rejected()]] - code - gateway/tests/test_sanitizer.py
- [[test_phone_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_raised_threshold_with_block_only_blocks_above_threshold()]] - code - gateway/tests/test_sanitizer.py
- [[test_real_phone_still_redacted()]] - code - gateway/tests/test_sanitizer.py
- [[test_redact_action_unchanged_and_not_blocked()]] - code - gateway/tests/test_sanitizer.py
- [[test_regex_fallback_requires_separator()]] - code - gateway/tests/test_sanitizer.py
- [[test_sanitizer.py]] - code - gateway/tests/test_sanitizer.py
- [[test_ssn_detection()]] - code - gateway/tests/test_sanitizer.py
- [[test_telegram_uid_not_redacted_as_phone()]] - code - gateway/tests/test_sanitizer.py
- [[test_uid_inside_parens_preserved()]] - code - gateway/tests/test_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_435
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 7]]

## Top bridge nodes
- [[test_sanitizer.py]] - degree 31, connects to 1 community
- [[_regex_sanitizer()]] - degree 11, connects to 1 community
- [[_presidio_sanitizer()]] - degree 8, connects to 1 community
- [[_FakeAnalyzer]] - degree 7, connects to 1 community
- [[_FakeRecognizerResult_1]] - degree 5, connects to 1 community