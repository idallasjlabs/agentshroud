---
type: community
cohesion: 0.33
members: 6
---

# test_call_agent_uses_structured_timeout()

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[__aexit__()]] - code - gateway/tests/test_voice_gateway.py
- [[__init__()]] - code - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must pass a structured httpx.Timeout to AsyncClient.      The]] - rationale - gateway/tests/test_voice_gateway.py
- [[stream()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_uses_structured_timeout()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_uses_structured_timeout()_1]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_call_agent_uses_structured_timeout
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_patch]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[test_call_agent_uses_structured_timeout()]] - degree 7, connects to 3 communities
- [[test_call_agent_uses_structured_timeout()_1]] - degree 2, connects to 1 community