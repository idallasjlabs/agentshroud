---
type: community
members: 28
---

# A2APolicyEngine (3)

**Members:** 28 nodes

## Members
- [[dot-__init__()_125]] - code - gateway/security/a2a_policy.py
- [[dot-__init__()_126]] - code - gateway/tests/test_a2a_policy.py
- [[dot-from_dict()_4]] - code - gateway/security/a2a_policy.py
- [[dot-submit_tool_request()_1]] - code - gateway/tests/test_a2a_policy.py
- [[dot-test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-wait_for_decision()_1]] - code - gateway/tests/test_a2a_policy.py
- [[A duck-typed queue predating the ``force_tier`` kwarg — enforce() must     fall]] - rationale - gateway/tests/test_a2a_policy.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open         the ga]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyAction]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets         if n]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Any_44]] - code - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything         — an]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/a2a_policy.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at         all — a]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[_LegacyStubApprovalQueue]] - code - gateway/tests/test_a2a_policy.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible         call]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[load_config-style callers pass whatever the YAML section resolved         to, wh]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyEngine_3
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_A2APolicyEngine]]
- 13 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 5 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 3 edges to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_Path (4)]]
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]

## Top bridge nodes
- [[A2APolicyConfig]] - degree 27, connects to 4 communities
- [[A2APolicyAction]] - degree 13, connects to 4 communities
- [[_LegacyStubApprovalQueue]] - degree 11, connects to 2 communities
- [[TestDefaultA2APolicyIsFailClosed]] - degree 12, connects to 1 community
- [[dot-from_dict()_4]] - degree 5, connects to 1 community
