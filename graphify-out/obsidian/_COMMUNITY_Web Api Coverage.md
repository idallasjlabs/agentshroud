---
type: community
cohesion: 0.38
members: 7
---

# Web Api Coverage

**Cohesion:** 0.38 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_resolves_hermes_to_the_real_renamed_container()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_resolves_openclaw_to_the_convention_default()]] - code - gateway/tests/test_web_api_coverage.py
- [[.test_unknown_bot_id_falls_back_to_the_naive_guess()]] - code - gateway/tests/test_web_api_coverage.py
- [[Resolve the real Docker container name for a given bot_id — from     BotConfig.r]] - rationale - gateway/web/api.py
- [[TestResolveBotContainer]] - code - gateway/tests/test_web_api_coverage.py
- [[_resolve_bot_container must use BotConfig.resolved_container_name, not     a har]] - rationale - gateway/tests/test_web_api_coverage.py
- [[_resolve_bot_container()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Web_Api_Coverage
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Web Api Coverage]]
- 3 edges to [[_COMMUNITY_Api (web)]]
- 1 edge to [[_COMMUNITY_Config]]

## Top bridge nodes
- [[_resolve_bot_container()]] - degree 9, connects to 3 communities
- [[TestResolveBotContainer]] - degree 8, connects to 1 community