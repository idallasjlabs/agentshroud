---
type: community
cohesion: 0.60
members: 6
---

# ._results()

**Cohesion:** 0.60 - moderately connected
**Members:** 6 nodes

## Members
- [[dot-_results()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_rewrite_is_idempotent()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_rewrite_never_touches_hermes()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_rewrite_sets_status_and_layers()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_rewrite_untargeted_id_unchanged()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[TestRewrite]] - code - gateway/tests/test_triage_cve_mitigations.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_results
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]

## Top bridge nodes
- [[TestRewrite]] - degree 7, connects to 2 communities
- [[dot-_results()]] - degree 8, connects to 1 community
- [[dot-test_rewrite_is_idempotent()]] - degree 3, connects to 1 community
- [[dot-test_rewrite_never_touches_hermes()]] - degree 3, connects to 1 community
- [[dot-test_rewrite_sets_status_and_layers()]] - degree 3, connects to 1 community
