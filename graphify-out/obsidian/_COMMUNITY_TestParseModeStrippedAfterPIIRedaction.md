---
type: community
members: 13
---

# TestParseModeStrippedAfterPIIRedaction

**Members:** 13 nodes

## Members
- [[dot-_make_owner_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback…_1]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction via the pipeline path must not strip parse_mode either (owner,…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for Telegram HTML parse error caused by PII placeholders. When…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a TelegramAPIProxy configured with a mock owner RBAC.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestParseModeStrippedAfterPIIRedaction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode=HTML must be preserved for owner when text contains no PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestParseModeStrippedAfterPIIRedaction
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY__make_sanitizer]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[TestParseModeStrippedAfterPIIRedaction]] - degree 8, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - degree 6, connects to 1 community
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - degree 5, connects to 1 community
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - degree 5, connects to 1 community
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - degree 5, connects to 1 community
