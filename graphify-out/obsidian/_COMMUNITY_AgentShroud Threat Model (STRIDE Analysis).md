---
type: community
members: 10
---

# AgentShroud Threat Model (STRIDE Analysis)

**Members:** 10 nodes

## Members
- [[dot-test_against_the_real_registry()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[dot-test_empty_registries_print_nothing()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[dot-test_prints_every_ghsa_id_one_per_line()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[dot-test_skips_none_ghsa_id_entries()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[Smoke test against the actual committed registry — every real         ghsa_id cu]] - rationale - gateway/tests/test_list_registry_ghsa_ids.py
- [[TestListRegistryGhsaIds]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[_script()]] - code - gateway/tests/test_list_registry_ghsa_ids.py
- [[list_registry_ghsa_ids.py]] - code - scripts/list_registry_ghsa_ids.py
- [[main()_36]] - code - scripts/list_registry_ghsa_ids.py
- [[test_list_registry_ghsa_ids.py]] - code - gateway/tests/test_list_registry_ghsa_ids.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Threat_Model_STRIDE_Analysis
SORT file.name ASC
```
