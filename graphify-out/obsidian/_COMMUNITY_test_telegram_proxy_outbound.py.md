---
type: community
members: 9
---

# test_telegram_proxy_outbound.py

**Members:** 9 nodes

## Members
- [[dot-_make_owner_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback p]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction via the pipeline path must not strip parse_mode either (owner, pip]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a TelegramAPIProxy configured with a mock owner RBAC.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode=HTML must be preserved for owner when text contains no PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_telegram_proxy_outboundpy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 4 edges to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]

## Top bridge nodes
- [[dot-_make_owner_proxy()]] - degree 7, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - degree 4, connects to 2 communities
