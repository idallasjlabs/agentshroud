---
type: community
cohesion: 0.40
members: 5
---

# agentshroud-gateway service (proxy mode) (2)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[If openai_to_gemini_request raises, the request must still be     forwarded (unm]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[The combined path v1chatcompletions with model=gemini- must end     up POST]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[test_gemini_via_openai_path.py]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_proxy_rewrites_gemini_via_openai_path()]] - code - gateway/tests/test_gemini_via_openai_path.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-gateway_service_proxy_mode_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_BotConfig]]
- 1 edge to [[_COMMUNITY_Function Details (8)]]

## Top bridge nodes
- [[test_gemini_via_openai_path.py]] - degree 5, connects to 3 communities
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - degree 3, connects to 1 community
- [[test_proxy_rewrites_gemini_via_openai_path()]] - degree 3, connects to 1 community
