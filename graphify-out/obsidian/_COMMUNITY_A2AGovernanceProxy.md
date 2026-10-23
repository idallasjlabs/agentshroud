---
type: community
cohesion: 0.06
members: 66
---

# A2AGovernanceProxy

**Cohesion:** 0.06 - loosely connected
**Members:** 66 nodes

## Members
- [[dot-__init__()_194]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-__post_init__()_9]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-_shared_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-get_incidents()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-test_adding_a_fourth_bot_extends_the_mesh_to_everyone()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_bot_without_registered_trust_manager_is_skipped()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_critical_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_default_policy_is_sane()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_empty_bot_list_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_empty_ledger_has_no_incidents()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_every_bot_shares_the_same_trust_manager()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_fraction_above_one_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_from_string()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_get_incidents_by_source()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_get_incidents_with_limit()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_high_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incident_limit_retained()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incident_on_one_bot_propagates_to_all_mesh_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incident_record_fields()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incidents_are_recorded()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_invalid_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_low_severity_not_propagated()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_medium_severity_propagates_to_peer()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_no_self_propagation()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_non_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_ordering()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_propagated_to_is_empty_for_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_propagation_limited_to_max_depth()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_propagation_registers_unregistered_peer_agent()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_register_peer()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_register_peer_is_bidirectional_by_default()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_single_bot_has_no_peers_and_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_three_bots_form_a_full_mesh()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_two_bots_are_mutual_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_unregistered_bot_has_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_zero_decay_fraction_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_zero_max_depth_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[A single cross-bot incident recorded in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[An incident on openclaw should not re-apply to openclaw via the ledger.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Configuration for how incidents decay peer trust scores.      Attributes]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[CrossBotTrustLedger_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[Default propagation policy.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Depth-2 propagation A → B → C but NOT C → D when max_depth=2.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[End-to-end a real incident on bot A decays trust on bots B and C         in a 3]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[IncidentRecord]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Peer agent not registered in TrustManager should be auto-registered.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Propagation to a peer with no registered TrustManager must not raise.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Return incidents, optionally filtered by source bot.          Args]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[TestBotIncidentSeverity]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestBuildFullMesh]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestCrossBotTrustLedgerConstruction]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestGetIncidentsLimit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentAudit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentPropagation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestTrustDecayPolicyValidation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[The exact scenario the user asked for add a 4th bot and it just works.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustDecayPolicy]] - code - gateway/security/cross_bot_trust_ledger.py
- [[TrustDecayPolicy_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustManager_4]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[build_full_mesh N-agent-scalable topology construction.      Adding a 3rd4thN]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[cross_bot_trust_ledger.py]] - code - gateway/security/cross_bot_trust_ledger.py
- [[hermes_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[ledger()_2]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[openclaw_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[policy()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[test_cross_bot_trust_ledger.py]] - code - gateway/tests/test_cross_bot_trust_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AGovernanceProxy
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_socrouter.py]]
- 15 edges to [[_COMMUNITY_KeyVaultConfig]]
- 13 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 1 edge to [[_COMMUNITY_dot-build_full_mesh()]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]

## Top bridge nodes
- [[cross_bot_trust_ledger.py]] - degree 6, connects to 4 communities
- [[CrossBotTrustLedger_1]] - degree 26, connects to 3 communities
- [[TrustManager_4]] - degree 25, connects to 3 communities
- [[test_cross_bot_trust_ledger.py]] - degree 17, connects to 3 communities
- [[TestBuildFullMesh]] - degree 16, connects to 3 communities
