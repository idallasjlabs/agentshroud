---
type: community
members: 12
---

# TestLifespan

**Members:** 12 nodes

## Members
- [[dot-test_get_auth_token_reads_secret_file_over_env()]] - code - chatbot/test_main.py
- [[dot-test_lifespan_logs_when_auth_token_configured()]] - code - chatbot/test_main.py
- [[dot-test_lifespan_reads_api_key_from_secret_file()]] - code - chatbot/test_main.py
- [[dot-test_lifespan_with_api_key_initializes_async_client()]] - code - chatbot/test_main.py
- [[dot-test_lifespan_without_api_key_leaves_client_none()]] - code - chatbot/test_main.py
- [[TestLifespan]] - code - chatbot/test_main.py
- [[When the Docker secret file exists, it wins over the env var.]] - rationale - chatbot/test_main.py
- [[When the Docker secret file for the OpenAI key exists, it wins over the env var…]] - rationale - chatbot/test_main.py
- [[fake_exists()]] - code - chatbot/test_main.py
- [[fake_exists()_1]] - code - chatbot/test_main.py
- [[fake_read_text()]] - code - chatbot/test_main.py
- [[fake_read_text()_1]] - code - chatbot/test_main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestLifespan
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_main.py]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]

## Top bridge nodes
- [[TestLifespan]] - degree 6, connects to 2 communities
- [[dot-test_get_auth_token_reads_secret_file_over_env()]] - degree 4, connects to 1 community
