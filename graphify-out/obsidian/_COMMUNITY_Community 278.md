---
type: community
cohesion: 0.14
members: 30
---

# Community 278

**Cohesion:** 0.14 - loosely connected
**Members:** 30 nodes

## Members
- [[dot-test_append_targets_correct_agent_marker()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_cvss_none_when_absent()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dedup_by_cve_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dedup_by_ghsa_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dry_run_writes_nothing()_1]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_duplicate_within_same_feed_page_registered_once()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_entry_to_py_handles_none_cvss()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_entry_to_py_roundtrips()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_fetch_paginates_via_link_cursor()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_hermes_snapshot_zero_new()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_id_numbering_continues_from_max()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_idempotent_on_rerun()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_live_registry_is_idempotent_no_new_backlog()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_never_fabricates_ids_skips_advisory_without_ghsa()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_new_advisory_becomes_under_review()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_advisory_does_not_touch_hermes_registry()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_openclaw_snapshot_registers_backlog_as_under_review()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_per_agent_prefix_applied()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[An OpenClaw advisory diffed against the Hermes list yields it as 'new'.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[Re-running against the LIVE registry adds nothing (backlog already synced).]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestFetch]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestPerAgentIsolation]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestProcessGhsaAdvisories]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestSerialization]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestSnapshotSmoke]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[The committed snapshot yields a real backlog, all honest under_review.]] - rationale - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_adv()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_sync()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[scriptssync-cve-registry.py (GHSA auto-register)]] - code - scripts/sync-cve-registry.py
- [[test_sync_cve_registry_ghsa.py]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_278
SORT file.name ASC
```
