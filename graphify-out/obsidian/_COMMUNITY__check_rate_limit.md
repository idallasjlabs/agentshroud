---
type: community
members: 5
---

# _check_rate_limit

**Members:** 5 nodes

## Members
- [[dot-test_rate_limit_enforced()_1]] - code - chatbot/test_main.py
- [[Exceeding the rate limit returns 429.]] - rationale - chatbot/test_main.py
- [[Raise 429 if the client has exceeded the rate limit.]] - rationale - chatbot/main.py
- [[TestRateLimit]] - code - chatbot/test_main.py
- [[_check_rate_limit()]] - code - chatbot/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_check_rate_limit
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chat]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]

## Top bridge nodes
- [[_check_rate_limit()]] - degree 4, connects to 2 communities
- [[TestRateLimit]] - degree 3, connects to 1 community
