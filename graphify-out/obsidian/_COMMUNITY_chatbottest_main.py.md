---
type: community
cohesion: 0.40
members: 5
---

# chatbot/test_main.py

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_internal_error_not_leaked()]] - code - chatbot/test_main.py
- [[.test_openai_auth_error_returns_503()]] - code - chatbot/test_main.py
- [[OpenAI AuthenticationError returns 503 without leaking the key.]] - rationale - chatbot/test_main.py
- [[OpenAI exceptions should not leak internal details to the client.]] - rationale - chatbot/test_main.py
- [[TestErrorSanitization]] - code - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/chatbot/test_mainpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Slack API Proxy]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_chatbottest_main.py]]

## Top bridge nodes
- [[TestErrorSanitization]] - degree 4, connects to 2 communities
- [[.test_internal_error_not_leaked()]] - degree 3, connects to 1 community
- [[.test_openai_auth_error_returns_503()]] - degree 3, connects to 1 community