---
type: community
cohesion: 0.12
members: 16
---

# Egress Enforce

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_default_config()_1]] - code - gateway/tests/test_egress_enforce.py
- [[.test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[.test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._1]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Enforce
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]

## Top bridge nodes
- [[TestEgressFilterConfig]] - degree 12, connects to 2 communities
- [[.test_default_config()_1]] - degree 3, connects to 1 community
- [[.test_denylist_wildcards()]] - degree 3, connects to 1 community
- [[.test_effective_allowlist_basic()]] - degree 3, connects to 1 community
- [[.test_effective_allowlist_with_denylist()]] - degree 3, connects to 1 community