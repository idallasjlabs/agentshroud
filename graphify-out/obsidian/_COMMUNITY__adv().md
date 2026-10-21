---
type: community
members: 11
---

# _adv()

**Members:** 11 nodes

## Members
- [[dot-test_cvss_none_when_absent()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dedup_by_cve_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_dedup_by_ghsa_id()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_duplicate_within_same_feed_page_registered_once()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_id_numbering_continues_from_max()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_idempotent_on_rerun()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_never_fabricates_ids_skips_advisory_without_ghsa()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_new_advisory_becomes_under_review()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[dot-test_per_agent_prefix_applied()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[TestProcessGhsaAdvisories]] - code - gateway/tests/test_sync_cve_registry_ghsa.py
- [[_adv()]] - code - gateway/tests/test_sync_cve_registry_ghsa.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_adv
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers (2)]]
- 4 edges to [[_COMMUNITY_ControlCenter]]
- 1 edge to [[_COMMUNITY_dot-test_fetch_paginates_via_link_cursor() (2)]]
- 1 edge to [[_COMMUNITY_An unreachable feed must fail the run, not print '0 new' and exit 0.]]
- 1 edge to [[_COMMUNITY_aquasecuritytrivy 403s the Actions token but serves the public feed. (2)]]

## Top bridge nodes
- [[_adv()]] - degree 19, connects to 5 communities
- [[TestProcessGhsaAdvisories]] - degree 10, connects to 1 community
- [[dot-test_cvss_none_when_absent()]] - degree 3, connects to 1 community
- [[dot-test_dedup_by_cve_id()]] - degree 3, connects to 1 community
- [[dot-test_dedup_by_ghsa_id()]] - degree 3, connects to 1 community
