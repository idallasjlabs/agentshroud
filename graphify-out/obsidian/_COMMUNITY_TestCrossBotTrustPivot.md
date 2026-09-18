---
type: community
cohesion: 0.25
members: 8
---

# TestCrossBotTrustPivot

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestCrossBotTrustPivot
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[TestCrossBotTrustPivot]] - degree 9, connects to 4 communities