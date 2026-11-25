---
type: community
members: 29
---

# test_security_regressions_v1_2.py

**Members:** 29 nodes

## Members
- [[dot-test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0. This is…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust. Verifies the seeding…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject user_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[fixture_31]] - code
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
- 4 edges to [[_COMMUNITY_UserSessionManager]]
- 3 edges to [[_COMMUNITY_TrustLevel]]
- 2 edges to [[_COMMUNITY_SharedMemoryManager]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TestHermesEgressAllowlist]]
- 1 edge to [[_COMMUNITY_TestCrossBotTrustPivot]]
- 1 edge to [[_COMMUNITY_TestBotIdIsolationInSharedMemory]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 19, connects to 7 communities
- [[TestHermesTrustSeeding]] - degree 4, connects to 1 community
- [[session_manager()_1]] - degree 3, connects to 1 community
- [[smm()]] - degree 3, connects to 1 community
- [[trust_manager()_1]] - degree 3, connects to 1 community
