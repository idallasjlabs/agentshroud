---
type: community
members: 11
---

# Community 933

**Members:** 11 nodes

## Members
- [[A real CVE always came from a GHSA advisory, so cve_id implies ghsa_id.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[CRITICAL GUARD no entry `id` may look like a real CVE id.      This is the load]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Every `id` must be a zero-padded ASH-OCLAW-NNN  ASH-HERMES-NNN ref.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[_all_entries()]] - code - gateway/tests/test_agent_cve_registry.py
- [[cve_id must be either None or a real-looking CVE id — never junk.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[ghsa_id must be either None or a real-looking GHSA id.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[test_cve_id_field_only_holds_real_looking_cve_ids()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_entry_with_cve_id_also_has_ghsa_id()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_every_entry_id_is_synthetic_ash_ref()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_ghsa_id_field_only_holds_real_looking_ghsa_ids()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_no_entry_id_looks_like_a_cve()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_933
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 88]]

## Top bridge nodes
- [[_all_entries()]] - degree 6, connects to 1 community
- [[test_no_entry_id_looks_like_a_cve()]] - degree 3, connects to 1 community
- [[test_every_entry_id_is_synthetic_ash_ref()]] - degree 3, connects to 1 community
- [[test_cve_id_field_only_holds_real_looking_cve_ids()]] - degree 3, connects to 1 community
- [[test_ghsa_id_field_only_holds_real_looking_ghsa_ids()]] - degree 3, connects to 1 community