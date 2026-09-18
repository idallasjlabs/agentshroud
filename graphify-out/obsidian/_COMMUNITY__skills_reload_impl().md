---
type: community
cohesion: 0.50
members: 4
---

# _skills_reload_impl()

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Re-read ``~.llm_settings`` and sync skillsagentsMCP into both bot configs.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings``, scan for supply-chain risk, deploy to both bots.]] - rationale - gateway/web/api.py
- [[_skills_reload_impl()]] - code - gateway/web/api.py
- [[skills_reload()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_skills_reload_impl
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_DraftEntry]]

## Top bridge nodes
- [[_skills_reload_impl()]] - degree 8, connects to 4 communities
- [[skills_reload()]] - degree 3, connects to 1 community