---
type: community
cohesion: 0.27
members: 11
---

# Community 816

**Cohesion:** 0.27 - loosely connected
**Members:** 11 nodes

## Members
- [[._make_owner_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_preserved_when_no_pii_detected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction must not strip parse_mode for the whole message (owner, fallback p]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PII redaction via the pipeline path must not strip parse_mode either (owner, pip]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for Telegram HTML parse error caused by PII placeholders.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a TelegramAPIProxy configured with a mock owner RBAC.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestParseModeStrippedAfterPIIRedaction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode=HTML must be preserved for owner when text contains no PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_816
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Community 93]]
- 3 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 96]]

## Top bridge nodes
- [[TestParseModeStrippedAfterPIIRedaction]] - degree 11, connects to 3 communities
- [[._make_owner_proxy()]] - degree 7, connects to 1 community
- [[.test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - degree 4, connects to 1 community
- [[.test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - degree 4, connects to 1 community
- [[.test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - degree 4, connects to 1 community