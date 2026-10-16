---
type: community
cohesion: 0.33
members: 6
---

# api.py

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[Re-read ``~.llm_settings`` and sync skillsagentsMCP into both bot configs.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings``, scan for supply-chain risk, deploy to both bots.]] - rationale - gateway/web/api.py
- [[Resolve the source (``~.llm_settings``) and bot-config destinations.      Extr]] - rationale - gateway/web/api.py
- [[_skills_reload_impl()]] - code - gateway/web/api.py
- [[_skills_reload_paths()]] - code - gateway/web/api.py
- [[skills_reload()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_SkillGuard_1]]

## Top bridge nodes
- [[_skills_reload_impl()]] - degree 8, connects to 3 communities
- [[_skills_reload_paths()]] - degree 4, connects to 1 community
- [[skills_reload()]] - degree 3, connects to 1 community
