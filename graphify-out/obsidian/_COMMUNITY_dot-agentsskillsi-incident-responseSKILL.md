---
type: community
members: 3
---

# .agents/skills/i-incident-response/SKILL.md

**Members:** 3 nodes

## Members
- [[dot-test_gates_pass_with_full_evidence()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[dot-test_gates_zero_affected_domains()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestMandatoryGates]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agents/skills/i-incident-response/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager (3) (2)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3) (2)]]

## Top bridge nodes
- [[TestMandatoryGates]] - degree 3, connects to 1 community
- [[dot-test_gates_pass_with_full_evidence()]] - degree 2, connects to 1 community
- [[dot-test_gates_zero_affected_domains()]] - degree 2, connects to 1 community
