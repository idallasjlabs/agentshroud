---
type: community
cohesion: 0.36
members: 8
---

# Skill: Branding Specialist (BS)

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_plan_classifies_create_when_dest_absent()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_is_deterministic()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_is_pure_writes_nothing()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[.test_plan_maps_canonical_to_each_bot_destination()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[Compute the deploy plan without mutating the filesystem.      Pure with respect]] - rationale - gateway/skills/manifest.py
- [[TestPlanDeploy]] - code - gateway/tests/test_skills_manifest_sync.py
- [[The plan is a pure function it maps canonical source entries to each     per-bo]] - rationale - gateway/tests/test_skills_manifest_sync.py
- [[plan_deploy()]] - code - gateway/skills/manifest.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skill_Branding_Specialist_BS
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AWS Cloud Management & FinOps Agent]]
- 8 edges to [[_COMMUNITY_Incident → Test Backfill Rule (R3 extension) ev]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]

## Top bridge nodes
- [[plan_deploy()]] - degree 13, connects to 3 communities
- [[TestPlanDeploy]] - degree 11, connects to 2 communities
- [[.test_plan_classifies_create_when_dest_absent()]] - degree 4, connects to 1 community
- [[.test_plan_is_deterministic()]] - degree 4, connects to 1 community
- [[.test_plan_is_pure_writes_nothing()]] - degree 4, connects to 1 community