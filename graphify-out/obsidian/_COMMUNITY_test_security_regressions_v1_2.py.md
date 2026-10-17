---
type: community
members: 27
---

# test_security_regressions_v1_2.py

**Members:** 27 nodes

## Members
- [[dot-test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[dot-test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0. This is…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Fail any real urlopen fast unless a test installs its own fake. Blocked-message…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor hermes-…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust. Verifies the seeding…]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Stub the fire-and-forget owner activity mirror. The mirror runs via…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[_no_owner_mirror()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_no_real_telegram_network()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_noop()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_refuse()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- 2 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py (2)]]
- 1 edge to [[_COMMUNITY_TestSessionPathSeparation]]
- 1 edge to [[_COMMUNITY_TestHermesEgressAllowlist]]
- 1 edge to [[_COMMUNITY_TestBotIdIsolationInSharedMemory]]
- 1 edge to [[_COMMUNITY_TestRewriteRequestHeaders]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 13, connects to 5 communities
- [[TestHermesDashboardBridgeReachability]] - degree 5, connects to 1 community
- [[_no_owner_mirror()]] - degree 4, connects to 1 community
- [[_no_real_telegram_network()]] - degree 4, connects to 1 community
