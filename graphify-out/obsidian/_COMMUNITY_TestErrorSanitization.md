---
type: community
members: 5
---

# TestErrorSanitization

**Members:** 5 nodes

## Members
- [[dot-test_internal_error_not_leaked()]] - code - chatbot/test_main.py
- [[dot-test_openai_auth_error_returns_503()]] - code - chatbot/test_main.py
- [[OpenAI AuthenticationError returns 503 without leaking the key.]] - rationale - chatbot/test_main.py
- [[OpenAI exceptions should not leak internal details to the client.]] - rationale - chatbot/test_main.py
- [[TestErrorSanitization]] - code - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestErrorSanitization
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chat]]

## Top bridge nodes
- [[TestErrorSanitization]] - degree 4, connects to 2 communities
- [[dot-test_internal_error_not_leaked()]] - degree 3, connects to 1 community
- [[dot-test_openai_auth_error_returns_503()]] - degree 3, connects to 1 community
