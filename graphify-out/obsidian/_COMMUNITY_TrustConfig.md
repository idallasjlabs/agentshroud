---
type: community
cohesion: 0.04
members: 104
---

# TrustConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 104 nodes

## Members
- [[.__post_init__()_3]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.__post_init__()_9]] - code - gateway/security/trust_manager.py
- [[._missing_()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[._shared_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_adding_a_fourth_bot_extends_the_mesh_to_everyone()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[.test_bot_without_registered_trust_manager_is_skipped()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_critical_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_custom_points()]] - code - gateway/tests/test_trust_manager.py
- [[.test_default_config()_8]] - code - gateway/tests/test_trust_manager.py
- [[.test_default_policy_is_sane()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_empty_bot_list_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_empty_ledger_has_no_incidents()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_every_bot_shares_the_same_trust_manager()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_fraction_above_one_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_from_string()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_get_incidents_by_source()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_get_incidents_with_limit()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_high_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[.test_incident_limit_retained()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_incident_on_one_bot_propagates_to_all_mesh_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_incident_record_fields()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_incidents_are_recorded()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_invalid_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_low_severity_not_propagated()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_medium_severity_propagates_to_peer()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_no_self_propagation()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_non_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_ordering()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_propagated_to_is_empty_for_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_propagation_limited_to_max_depth()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_propagation_registers_unregistered_peer_agent()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_rate_limiting_prevents_rapid_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_peer()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_register_peer_is_bidirectional_by_default()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_single_bot_has_no_peers_and_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_three_bots_form_a_full_mesh()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_thresholds_populated()]] - code - gateway/tests/test_trust_manager.py
- [[.test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[.test_two_bots_are_mutual_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_unregistered_bot_has_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[.test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[.test_zero_decay_fraction_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_zero_max_depth_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[A single cross-bot incident recorded in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[An incident on openclaw should not re-apply to openclaw via the ledger.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[BotIncidentSeverity]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Configuration for how incidents decay peer trust scores.      Attributes]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[CrossBotTrustLedger_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[Default propagation policy.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Depth-2 propagation A → B → C but NOT C → D when max_depth=2.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[End-to-end a real incident on bot A decays trust on bots B and C         in a 3]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[IncidentRecord]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Ordered severity levels for cross-bot incidents.      Values map to IEC 62443 SL]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Peer agent not registered in TrustManager should be auto-registered.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Propagation to a peer with no registered TrustManager must not raise.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Rapid successes should be capped by rate limiting.]] - rationale - gateway/tests/test_security_hardening.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test configuration options.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestBotIncidentSeverity]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestBuildFullMesh]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestConfig]] - code - gateway/tests/test_trust_manager.py
- [[TestCrossBotTrustLedgerConstruction]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestGetIncidentsLimit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestIncidentAudit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentPropagation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestTrustDecayPolicyValidation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_trust_manager.py
- [[The exact scenario the user asked for add a 4th bot and it just works.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[TrustConfig]] - code - gateway/security/trust_manager.py
- [[TrustDecayPolicy]] - code - gateway/security/cross_bot_trust_ledger.py
- [[TrustDecayPolicy_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustManager_3]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[build_full_mesh N-agent-scalable topology construction.      Adding a 3rd4thN]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[cross_bot_trust_ledger.py]] - code - gateway/security/cross_bot_trust_ledger.py
- [[hermes_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[ledger()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[manager()_4]] - code - gateway/tests/test_trust_manager.py
- [[openclaw_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[policy()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[strict_config()_3]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_cross_bot_trust_ledger.py]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py
- [[trust_manager()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[trust_manager()_3]] - code - gateway/tests/test_e2e_watchtower.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustConfig
SORT file.name ASC
```

## Connections to other communities
- 53 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 32 edges to [[_COMMUNITY_RBACConfig]]
- 14 edges to [[_COMMUNITY_WebProxyConfig]]
- 6 edges to [[_COMMUNITY_ConsentFramework]]
- 5 edges to [[_COMMUNITY_falco_monitor.py]]
- 4 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_test_approval_queue.py]]
- 3 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_AgentShroud Recovery Plan v0.4.0]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_Daedalus — Concept Illustrator]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_Local LLM Support — Implementation Review]]

## Top bridge nodes
- [[TrustConfig]] - degree 101, connects to 14 communities
- [[BotIncidentSeverity]] - degree 25, connects to 4 communities
- [[TrustDecayPolicy]] - degree 17, connects to 3 communities
- [[cross_bot_trust_ledger.py]] - degree 6, connects to 3 communities
- [[CrossBotTrustLedger_1]] - degree 26, connects to 2 communities