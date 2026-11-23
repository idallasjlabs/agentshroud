---
type: community
members: 8
---

# health_check

**Members:** 8 nodes

## Members
- [[dot-test_health_degraded_without_client()]] - code - chatbot/test_main.py
- [[dot-test_health_healthy_with_client()]] - code - chatbot/test_main.py
- [[Health check endpoint for Docker. Reports degraded status when the OpenAI…]] - rationale - chatbot/main.py
- [[Health endpoint reports degraded when OpenAI client is not available.]] - rationale - chatbot/test_main.py
- [[Health endpoint reports healthy when OpenAI client is available.]] - rationale - chatbot/test_main.py
- [[TestHealthCheck]] - code - chatbot/test_main.py
- [[get_1]] - code
- [[health_check()]] - code - chatbot/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/health_check
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]

## Top bridge nodes
- [[TestHealthCheck]] - degree 4, connects to 1 community
- [[health_check()]] - degree 4, connects to 1 community
