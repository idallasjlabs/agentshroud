---
type: community
members: 12
---

# Community 8

**Members:** 12 nodes

## Members
- [[.test_raw_web_search_json_collaborator_safe_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_owner_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_log_called_with_correct_params()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_no_egress_filter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_query_truncation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator chat raw web_search JSON produces a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner chat raw web_search JSON produces 'Switch to tool-capable model' message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Queries longer than 200 chars are truncated in the SOC log reason.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestWebSearchLog]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests for _trigger_web_search_log and raw web_search JSON outbound handling.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log calls log_external_decision with Brave domain and query.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log returns silently when egress_filter is None.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_8
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 870]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 265]]

## Top bridge nodes
- [[TestWebSearchLog]] - degree 11, connects to 5 communities
- [[.test_web_search_log_called_with_correct_params()]] - degree 4, connects to 1 community
- [[.test_web_search_no_egress_filter()]] - degree 4, connects to 1 community
- [[.test_web_search_query_truncation()]] - degree 4, connects to 1 community
- [[.test_raw_web_search_json_owner_message()]] - degree 4, connects to 1 community