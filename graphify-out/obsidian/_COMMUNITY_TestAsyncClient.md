---
type: community
members: 7
---

# TestAsyncClient

**Members:** 7 nodes

## Members
- [[dot-test_chat_success_returns_parsed_response()]] - code - chatbot/test_main.py
- [[dot-test_openai_rate_limit_error_returns_429()]] - code - chatbot/test_main.py
- [[dot-test_uses_async_openai_client()]] - code - chatbot/test_main.py
- [[A successful OpenAI completion returns 200 with the parsed fields via the…]] - rationale - chatbot/test_main.py
- [[OpenAI's own RateLimitError is translated to a 429 for the caller.]] - rationale - chatbot/test_main.py
- [[TestAsyncClient]] - code - chatbot/test_main.py
- [[Verify the module uses AsyncOpenAI, not sync OpenAI.]] - rationale - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAsyncClient
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chat]]

## Top bridge nodes
- [[TestAsyncClient]] - degree 5, connects to 2 communities
- [[dot-test_chat_success_returns_parsed_response()]] - degree 3, connects to 1 community
- [[dot-test_openai_rate_limit_error_returns_429()]] - degree 3, connects to 1 community
