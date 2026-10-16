---
type: community
cohesion: 0.08
members: 29
---

# test_security_regressions_v1_2.py

**Cohesion:** 0.08 - loosely connected
**Members:** 29 nodes

## Members
- [[dot-test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0. This is…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs. A…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust. Verifies the seeding…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[fixture]] - code
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not compose…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[tmp_workspace()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[v1.2.0 Security Regression Tests Every test in this file corresponds to a…]] - rationale - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_security_regressions_v1_2py
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_TestSessionPathSeparation]]
- 1 edge to [[_COMMUNITY_TestHermesEgressAllowlist]]
- 1 edge to [[_COMMUNITY_TestBotIdIsolationInSharedMemory]]
- 1 edge to [[_COMMUNITY_TestRewriteRequestHeaders]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 13, connects to 4 communities
- [[TestHermesDashboardBridgeReachability]] - degree 5, connects to 1 community
