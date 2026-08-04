---
type: community
cohesion: 0.20
members: 10
---

# Module Group 390

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[._make_owner_proxy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_preserved_when_no_pii_detected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_stripped_when_email_redacted_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_stripped_when_phone_redacted_fallback_path()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_parse_mode_stripped_when_pipeline_sanitizes_email()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Return a TelegramAPIProxy configured with a mock owner RBAC.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode must be removed when pipeline produces EMAIL_ADDRESS (owner, pipeli]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode must be removed when sanitizer injects EMAIL_ADDRESS (owner, fallba]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode must be removed when sanitizer injects PHONE_NUMBER (owner, fallbac]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[parse_mode=HTML must be preserved for owner when text contains no PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_390
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 4 edges to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound Tests]]

## Top bridge nodes
- [[._make_owner_proxy()]] - degree 7, connects to 2 communities
- [[.test_parse_mode_preserved_when_no_pii_detected()]] - degree 4, connects to 2 communities
- [[.test_parse_mode_stripped_when_email_redacted_fallback_path()]] - degree 4, connects to 2 communities
- [[.test_parse_mode_stripped_when_phone_redacted_fallback_path()]] - degree 4, connects to 2 communities
- [[.test_parse_mode_stripped_when_pipeline_sanitizes_email()]] - degree 4, connects to 2 communities
