---
type: community
members: 6
---

# .test_forward_to_telegram_handles_http_error_non_json

**Members:** 6 nodes

## Members
- [[dot-test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_raise_http_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_raise_http_error()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_forward_to_telegram_handles_http_error_non_json
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 2 edges to [[_COMMUNITY_asyncio_5]]

## Top bridge nodes
- [[dot-test_forward_to_telegram_handles_http_error_non_json()]] - degree 5, connects to 2 communities
- [[dot-test_forward_to_telegram_returns_http_error_json()]] - degree 4, connects to 2 communities
