---
type: community
cohesion: 0.33
members: 9
---

# Severity

**Cohesion:** 0.33 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-client()_1]] - code - gateway/tests/test_skill_guard.py
- [[dot-test_reload_allows_clean_skill()]] - code - gateway/tests/test_skill_guard.py
- [[dot-test_reload_blocks_dangerous_skill()]] - code - gateway/tests/test_skill_guard.py
- [[dot-test_reload_fails_closed_on_unreadable_file()]] - code - gateway/tests/test_skill_guard.py
- [[CompletedProcess]] - code - gateway/tests/test_skill_guard.py
- [[Ordered severity ladder (``IntEnum`` so comparisons work).]] - rationale - gateway/security/skill_guard.py
- [[Severity]] - code - gateway/security/skill_guard.py
- [[TestClient]] - code - gateway/tests/test_skill_guard.py
- [[TestReloadIntegration]] - code - gateway/tests/test_skill_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Severity
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_SkillGuard]]
- 11 edges to [[_COMMUNITY_Path_2]]
- 8 edges to [[_COMMUNITY_SkillGuard_1]]
- 4 edges to [[_COMMUNITY_Recommendation_1]]
- 1 edge to [[_COMMUNITY_TestCleanSkill]]

## Top bridge nodes
- [[Severity]] - degree 24, connects to 5 communities
- [[CompletedProcess]] - degree 6, connects to 4 communities
- [[TestReloadIntegration]] - degree 10, connects to 3 communities
- [[TestClient]] - degree 9, connects to 3 communities
- [[dot-test_reload_allows_clean_skill()]] - degree 4, connects to 1 community
