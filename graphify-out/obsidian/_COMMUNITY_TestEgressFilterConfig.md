---
type: community
members: 20
---

# TestEgressFilterConfig

**Members:** 20 nodes

## Members
- [[dot-from_environment()]] - code - gateway/security/egress_config.py
- [[dot-test_default_config()_5]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_denylist_wildcards()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_basic()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_effective_allowlist_with_denylist()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_egress_mode_override()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_defaults_to_enforce()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_from_environment_enforce()]] - code - gateway/tests/test_egress_enforce.py
- [[dot-test_from_environment_monitor()]] - code - gateway/tests/test_egress_enforce.py
- [[Create config from environment variables and AGENTSHROUD_MODE.]] - rationale - gateway/security/egress_config.py
- [[Test EgressFilterConfig functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test allowlist with denylist in strict mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test basic allowlist functionality.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in enforce mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test config creation from environment in monitor mode.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test denylist wildcard matching.]] - rationale - gateway/tests/test_egress_enforce.py
- [[Test specific egress mode environment variable.]] - rationale - gateway/tests/test_egress_enforce.py
- [[TestEgressConfigDefaultEnforce]] - code - gateway/tests/test_round2_hardening.py
- [[TestEgressFilterConfig]] - code - gateway/tests/test_egress_enforce.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_middleware.py]]

## Top bridge nodes
- [[TestEgressConfigDefaultEnforce]] - degree 3, connects to 2 communities
- [[TestEgressFilterConfig]] - degree 10, connects to 1 community
- [[dot-from_environment()]] - degree 6, connects to 1 community
- [[dot-test_default_config()_5]] - degree 3, connects to 1 community
- [[dot-test_denylist_wildcards()]] - degree 3, connects to 1 community
