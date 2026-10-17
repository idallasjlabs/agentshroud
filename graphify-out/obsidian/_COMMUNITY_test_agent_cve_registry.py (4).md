---
type: community
members: 6
---

# test_agent_cve_registry.py (4)

**Members:** 6 nodes

## Members
- [[A single shared output path makes multi-agent coverage impossible.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[An agent with no version source must be refused, never verdicted.      Emitting]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Import the triage script by path.      It must be registered in sys.modules befo]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[_load_triage_module()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_gap_reports_are_per_agent()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_untriageable_agents_are_refused_not_guessed()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_agent_cve_registrypy_4
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_agent_cve_registry.py]]

## Top bridge nodes
- [[_load_triage_module()]] - degree 4, connects to 1 community
- [[test_gap_reports_are_per_agent()]] - degree 3, connects to 1 community
- [[test_untriageable_agents_are_refused_not_guessed()]] - degree 3, connects to 1 community
