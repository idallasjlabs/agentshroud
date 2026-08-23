---
type: community
cohesion: 0.12
members: 18
---

# A2a Policy Default Failclosed

**Cohesion:** 0.12 - loosely connected
**Members:** 18 nodes

## Members
- [[.from_dict()_2]] - code - gateway/security/a2a_policy.py
- [[.test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open         the ga]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyAction]] - code - gateway/security/a2a_policy.py
- [[Any_29]] - code - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything         — an]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/a2a_policy.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at         all — a]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible         call]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[load_config-style callers pass whatever the YAML section resolved         to, wh]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2a_Policy_Default_Failclosed
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_A2a Integration]]
- 6 edges to [[_COMMUNITY_A2a Policy]]
- 3 edges to [[_COMMUNITY_A2a Policy (security)]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]
- 1 edge to [[_COMMUNITY_Mcp Policy]]

## Top bridge nodes
- [[A2APolicyAction]] - degree 13, connects to 3 communities
- [[TestDefaultA2APolicyIsFailClosed]] - degree 12, connects to 2 communities
- [[.from_dict()_2]] - degree 5, connects to 2 communities
- [[test_a2a_policy_default_failclosed.py]] - degree 5, connects to 2 communities
- [[.test_configured_allowlist_still_works_alongside_fail_closed_default()]] - degree 3, connects to 1 community