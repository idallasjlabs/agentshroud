---
type: community
cohesion: 0.25
members: 9
---

# Community 970

**Cohesion:** 0.25 - loosely connected
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
TABLE source_file, type FROM #community/Community_970
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Tool Result Sanitizer & XML Injection Filtering]]
- 4 edges to [[_COMMUNITY_Community 85]]
- 1 edge to [[_COMMUNITY_Community 93]]

## Top bridge nodes
- [[dot-_make_owner_proxy()]] - degree 7, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_email_fallback_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_phone_fallback_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_and_placeholder_escaped_pipeline_path()]] - degree 4, connects to 2 communities
- [[dot-test_parse_mode_preserved_when_no_pii_detected()]] - degree 4, connects to 2 communities