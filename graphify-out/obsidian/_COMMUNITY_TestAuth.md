---
type: community
members: 7
---

# TestAuth

**Members:** 7 nodes

## Members
- [[dot-test_chat_allows_valid_token()]] - code - chatbot/test_main.py
- [[dot-test_chat_allows_when_no_token_configured()]] - code - chatbot/test_main.py
- [[dot-test_chat_requires_auth_when_token_set()]] - code - chatbot/test_main.py
- [[TestAuth]] - code - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is not set, chat is open (backward compat).]] - rationale - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is set and correct token given, request proceeds.]] - rationale - chatbot/test_main.py
- [[When CHATBOT_AUTH_TOKEN is set, chat without a token returns 401.]] - rationale - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuth
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]

## Top bridge nodes
- [[TestAuth]] - degree 5, connects to 2 communities
