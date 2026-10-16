---
type: community
cohesion: 0.10
members: 22
---

# A2APolicyConfig

**Cohesion:** 0.10 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_156]] - code - gateway/security/a2a_policy.py
- [[dot-__post_init__()_7]] - code - gateway/security/a2a_policy.py
- [[dot-from_dict()_8]] - code - gateway/security/a2a_policy.py
- [[dot-test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open         the ga]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyConfig_1]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets         if n]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Any_63]] - code - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything         — an]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - rationale - gateway/security/a2a_policy.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at         all — a]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible         call]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[load_config-style callers pass whatever the YAML section resolved         to, wh]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyConfig
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_A2APolicyEngine]]
- 7 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 6 edges to [[_COMMUNITY_A2AMethod]]
- 6 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 1 edge to [[_COMMUNITY_Path]]

## Top bridge nodes
- [[A2APolicyConfig_1]] - degree 27, connects to 4 communities
- [[TestDefaultA2APolicyIsFailClosed]] - degree 12, connects to 3 communities
- [[test_a2a_policy_default_failclosed.py]] - degree 5, connects to 3 communities
- [[dot-from_dict()_8]] - degree 5, connects to 2 communities
- [[dot-test_bare_config_denies_every_peer()]] - degree 4, connects to 1 community
