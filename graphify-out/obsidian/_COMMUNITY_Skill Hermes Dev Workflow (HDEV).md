---
type: community
cohesion: 0.33
members: 7
---

# Skill: Hermes Dev Workflow (HDEV)

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skill_Hermes_Dev_Workflow_HDEV
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]

## Top bridge nodes
- [[TestSessionPathSeparation]] - degree 9, connects to 3 communities