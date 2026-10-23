---
type: community
cohesion: 0.13
members: 15
---

# ControlCenter

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[dot-test_every_agent_list_accepts_an_append()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_hermes_snapshot_zero_new()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_live_registry_is_idempotent_no_new_backlog()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_advisory_does_not_touch_hermes_registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_snapshot_registers_backlog_as_under_review()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[An OpenClaw advisory diffed against the Hermes list yields it as 'new'. Proves…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Re-running against the LIVE registry adds nothing (backlog already synced).]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Runs against the REAL gatewaysecurityagent_cve_registry.py. Every registered…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestLiveRegistryLayout]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestPerAgentIsolation]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestSnapshotSmoke]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Tests for scriptssync-cve-registry.py — Phase 1 GHSA under_review auto-…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The committed snapshot yields a real backlog, all honest under_review. Diffs…]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[scriptssync-cve-registry.py (GHSA auto-register)]] - code - scripts/sync-cve-registry.py
- [[test_sync_cve_registry_ghsa.py]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ControlCenter
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers (2)_1]]
- 4 edges to [[_COMMUNITY__adv()]]
- 1 edge to [[_COMMUNITY_fixture (2)]]
- 1 edge to [[_COMMUNITY_The NVD path emits the pre-migration schema (id=CVE-…, no ghsa_idcve_id).… (2)]]
- 1 edge to [[_COMMUNITY_An unreachable feed must fail the run, not print '0 new' and exit 0.]]
- 1 edge to [[_COMMUNITY_aquasecuritytrivy 403s the Actions token but serves the public feed. (2)]]

## Top bridge nodes
- [[test_sync_cve_registry_ghsa.py]] - degree 15, connects to 6 communities
- [[dot-test_openclaw_advisory_does_not_touch_hermes_registry()]] - degree 4, connects to 2 communities
- [[dot-test_every_agent_list_accepts_an_append()]] - degree 3, connects to 2 communities
- [[dot-test_live_registry_is_idempotent_no_new_backlog()]] - degree 3, connects to 1 community
- [[dot-test_openclaw_snapshot_registers_backlog_as_under_review()]] - degree 3, connects to 1 community
