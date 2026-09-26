---
type: community
cohesion: 1.00
members: 2
---

# perform_mcp_oauth_preflight.sh

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[.test_session_lock_error_is_sanitized_for_users()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal session lock errors should be rewritten to safe user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/perform_mcp_oauth_preflightsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY__make_proxy()]]

## Top bridge nodes
- [[.test_session_lock_error_is_sanitized_for_users()]] - degree 4, connects to 3 communities