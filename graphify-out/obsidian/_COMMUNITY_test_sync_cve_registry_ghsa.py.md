---
type: community
members: 8
---

# test_sync_cve_registry_ghsa.py

**Members:** 8 nodes

## Members
- [[dot-test_every_agent_list_accepts_an_append()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_advisory_does_not_touch_hermes_registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[An OpenClaw advisory diffed against the Hermes list yields it as 'new'. Proves…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Runs against the REAL gatewaysecurityagent_cve_registry.py. Every registered…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestLiveRegistryLayout]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestPerAgentIsolation]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Tests for scriptssync-cve-registry.py — Phase 1 GHSA under_review auto-…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[test_sync_cve_registry_ghsa.py]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_sync_cve_registry_ghsapy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY__sync]]
- 4 edges to [[_COMMUNITY__adv]]
- 1 edge to [[_COMMUNITY_TestFailsLoudly]]
- 1 edge to [[_COMMUNITY_TestNvdAppend]]
- 1 edge to [[_COMMUNITY_TestNvdReportOnly]]
- 1 edge to [[_COMMUNITY_TestSnapshotSmoke]]
- 1 edge to [[_COMMUNITY_dot-test_fetch_paginates_via_link_cursor]]

## Top bridge nodes
- [[test_sync_cve_registry_ghsa.py]] - degree 14, connects to 7 communities
- [[dot-test_openclaw_advisory_does_not_touch_hermes_registry()]] - degree 4, connects to 2 communities
- [[dot-test_every_agent_list_accepts_an_append()]] - degree 3, connects to 2 communities
