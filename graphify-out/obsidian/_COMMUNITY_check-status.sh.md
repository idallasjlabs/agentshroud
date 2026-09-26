---
type: community
cohesion: 1.00
members: 2
---

# check-status.sh

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_timeout_error_is_sanitized_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Timeout rewrites should apply when JSON payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check-statussh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_timeout_error_is_sanitized_for_json_message_field()]] - degree 4, connects to 3 communities