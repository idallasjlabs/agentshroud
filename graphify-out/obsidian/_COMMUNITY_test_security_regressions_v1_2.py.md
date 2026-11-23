---
type: community
members: 59
---

# test_security_regressions_v1_2.py

**Members:** 59 nodes

## Members
- [[dot-test_ai_security_research_domains_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_duckduckgo_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_failover_search_engines_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hc_ping_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_nousresearch_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[AI-security researchcompetitive-intel domains must be allowlisted. These…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H1 SharedMemoryManager.get_user_memory must accept a bot_id parameter. The…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H3 The filesystem paths for openclaw and hermes sessions differ.…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 (reverse) Writing to Hermes workspace does not bleed into OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 Writing to the openclaw workspace must not leak into the hermes…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0. This is…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes base image is from nousresearch.com — must be in egress allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes ddgs-based web search requires duckduckgo.com.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes heartbeat uses hc-ping.com for dead-man's switch.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[PR190 failover search engines must be allowlisted.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs. A…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust. Verifies the seeding…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject user_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestBotIdIsolationInSharedMemory]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesEgressAllowlist]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Verify that Hermes-specific egress destinations are in the canonical allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[fixture_25]] - code
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not compose…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[tmp_workspace()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[v1.2.0 Security Regression Tests Every test in this file corresponds to a…]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_regressions_v1_2py
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 2 edges to [[_COMMUNITY_SharedMemoryManager]]
- 2 edges to [[_COMMUNITY_TrustManager]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 19, connects to 4 communities
- [[TestCrossBotTrustPivot]] - degree 6, connects to 1 community
- [[TestHermesTrustSeeding]] - degree 4, connects to 1 community
- [[session_manager()_1]] - degree 3, connects to 1 community
- [[smm()]] - degree 3, connects to 1 community
