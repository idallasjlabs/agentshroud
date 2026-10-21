---
type: community
members: 7
---

# agentshroud-blueteam/SKILL.md (5)

**Members:** 7 nodes

## Members
- [[dot-export_attack_report()]] - code - gateway/security/context_guard.py
- [[dot-get_attack_summary()]] - code - gateway/security/context_guard.py
- [[dot-get_session_risk_level()]] - code - gateway/security/context_guard.py
- [[Any_7]] - code - gateway/security/context_guard.py
- [[Export attack detection report.]] - rationale - gateway/security/context_guard.py
- [[Get risk level for a session based on detected attacks.]] - rationale - gateway/security/context_guard.py
- [[Get summary of detected attacks.]] - rationale - gateway/security/context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd_5
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[dot-get_attack_summary()]] - degree 5, connects to 1 community
- [[dot-export_attack_report()]] - degree 3, connects to 1 community
- [[dot-get_session_risk_level()]] - degree 3, connects to 1 community
