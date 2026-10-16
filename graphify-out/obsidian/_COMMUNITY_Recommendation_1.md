---
type: community
cohesion: 0.31
members: 10
---

# Recommendation

**Cohesion:** 0.31 - loosely connected
**Members:** 10 nodes

## Members
- [[IntEnum]] - code
- [[Path_2]] - code - gateway/skills/scan.py
- [[Read every manifest entry under source, failing CLOSED on unreadable files.]] - rationale - gateway/skills/scan.py
- [[Recommendation]] - code - gateway/security/skill_guard.py
- [[ScanResult_2]] - code - gateway/skills/scan.py
- [[What the caller should do with the scanned skill.]] - rationale - gateway/security/skill_guard.py
- [[_build_tree()]] - code - gateway/skills/scan.py
- [[_print_findings()]] - code - gateway/skills/scan.py
- [[main()_2]] - code - gateway/skills/scan.py
- [[scan.py]] - code - gateway/skills/scan.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Recommendation
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_SkillGuard]]
- 9 edges to [[_COMMUNITY_SkillGuard_1]]
- 4 edges to [[_COMMUNITY_Severity]]
- 4 edges to [[_COMMUNITY_Path_2]]
- 3 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_ThreatAssessment]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_TestCleanSkill]]

## Top bridge nodes
- [[IntEnum]] - degree 7, connects to 6 communities
- [[Recommendation]] - degree 27, connects to 5 communities
- [[scan.py]] - degree 8, connects to 3 communities
- [[Path_2]] - degree 6, connects to 2 communities
- [[ScanResult_2]] - degree 5, connects to 2 communities
