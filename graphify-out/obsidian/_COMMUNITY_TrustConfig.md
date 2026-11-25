---
type: community
members: 58
---

# TrustConfig

**Members:** 58 nodes

## Members
- [[dot-__post_init__()_9]] - code - gateway/security/trust_manager.py
- [[dot-_shared_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-build_full_mesh()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-test_adding_a_fourth_bot_extends_the_mesh_to_everyone()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_custom_points()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_default_config()_7]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_empty_bot_list_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_every_bot_shares_the_same_trust_manager()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_incident_on_one_bot_propagates_to_all_mesh_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_propagation_limited_to_max_depth()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_rate_limiting_prevents_rapid_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_single_bot_has_no_peers_and_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_three_bots_form_a_full_mesh()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_thresholds_populated()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_two_bots_are_mutual_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[Build a ledger where every bot in bot_ids is a mutual peer of every other…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[Depth-2 propagation A → B → C but NOT C → D when max_depth=2.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[End-to-end a real incident on bot A decays trust on bots B and C in a 3-bot…]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Rapid successes should be capped by rate limiting.]] - rationale - gateway/tests/test_security_hardening.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test configuration options.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestBuildFullMesh]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestConfig_1]] - code - gateway/tests/test_trust_manager.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[Tests for Progressive Trust System.]] - rationale - gateway/tests/test_trust_manager.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[The exact scenario the user asked for add a 4th bot and it just works.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[TrustConfig]] - code - gateway/security/trust_manager.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[build_full_mesh N-agent-scalable topology construction. Adding a 3rd4thNth…]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[fixture_134]] - code
- [[manager()_4]] - code - gateway/tests/test_trust_manager.py
- [[strict_config()_3]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustConfig
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_TrustManager]]
- 10 edges to [[_COMMUNITY_TrustLevel]]
- 4 edges to [[_COMMUNITY_asyncio_2]]
- 3 edges to [[_COMMUNITY_TestTrustManager]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_PIISanitizer]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TestTrustProgression]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[TrustConfig]] - degree 38, connects to 9 communities
- [[test_trust_manager.py]] - degree 16, connects to 3 communities
- [[dot-build_full_mesh()]] - degree 12, connects to 3 communities
- [[TestTrustManagerHardened]] - degree 6, connects to 2 communities
- [[TestBuildFullMesh]] - degree 14, connects to 1 community
