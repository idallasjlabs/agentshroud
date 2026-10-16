---
type: community
cohesion: 0.25
members: 8
---

# test_claude_via_openai_path.py

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[Regression don't break the existing v1messages path.]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[client()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias.py]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_passes_correct_path_to_proxy()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_routes_to_v1_path()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_get_chat_completions_alias_also_routes()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_root_v1_messages_still_works_unchanged()]] - code - gateway/tests/test_chat_completions_alias.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_claude_via_openai_pathpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py_1]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[test_chat_completions_alias.py]] - degree 7, connects to 1 community
- [[Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)]] - degree 2, connects to 1 community
- [[client()]] - degree 2, connects to 1 community
