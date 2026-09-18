---
type: community
cohesion: 0.29
members: 10
---

# _script()

**Cohesion:** 0.29 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_against_the_real_registry()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[.test_empty_registries_print_nothing()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[.test_prints_every_ghsa_id_one_per_line()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[.test_skips_none_ghsa_id_entries()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[Smoke test against the actual committed registry — every real         ghsa_id cu]] - rationale - gateway/tests/test_list_registry_ghsa_ids.py
- [[TestListRegistryGhsaIds]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[_script()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[list_registry_ghsa_ids.py]] - code - scripts/list_registry_ghsa_ids.py
- [[main()_34]] - code - scripts/list_registry_ghsa_ids.py
- [[test_list_registry_ghsa_ids.py]] - code - gateway/tests/test_list_registry_ghsa_ids.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_script
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_gateway.security.agent_cve_registry]]

## Top bridge nodes
- [[list_registry_ghsa_ids.py]] - degree 3, connects to 1 community