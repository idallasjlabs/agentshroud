---
type: community
members: 2
---

# System Audit Documentation (SAD)

**Members:** 2 nodes

## Members
- [[dot-test_unknown_model_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown model errors should be rewritten without leaking raw stack text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/System_Audit_Documentation_SAD
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_CronStateMonitor]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2)]]

## Top bridge nodes
- [[dot-test_unknown_model_error_is_sanitized()]] - degree 4, connects to 3 communities
