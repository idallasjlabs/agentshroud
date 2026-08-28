---
type: community
cohesion: 0.05
members: 91
---

# Community 41

**Cohesion:** 0.05 - loosely connected
**Members:** 91 nodes

## Members
- [[.__init__()_25]] - code - gateway/proxy/mcp_audit.py
- [[.__init__()_32]] - code - gateway/proxy/pipeline.py
- [[.__init__()_53]] - code - gateway/security/alert_dispatcher.py
- [[.__init__()_68]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.__post_init__()_3]] - code - gateway/security/cross_bot_trust_ledger.py
- [[._missing_()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[._propagate()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[._shared_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.build_full_mesh()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.get_incidents()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.incident_count()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.peers_of()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.record_incident()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.register_peer()_1]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.register_trust_manager()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.test_adding_a_fourth_bot_extends_the_mesh_to_everyone()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_bot_without_registered_trust_manager_is_skipped()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_critical_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_default_policy_is_sane()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_empty_bot_list_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_empty_ledger_has_no_incidents()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_every_bot_shares_the_same_trust_manager()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_fraction_above_one_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_from_string()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_get_incidents_by_source()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_get_incidents_with_limit()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_high_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
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
- [[.test_register_peer()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_register_peer_is_bidirectional_by_default()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_single_bot_has_no_peers_and_does_not_raise()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_three_bots_form_a_full_mesh()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_two_bots_are_mutual_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_unregistered_bot_has_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_zero_decay_fraction_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_zero_max_depth_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[A single cross-bot incident recorded in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[An incident on openclaw should not re-apply to openclaw via the ledger.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Attach a TrustManager instance to a bot name.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[BotIncidentSeverity]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Build a ledger where every bot in bot_ids is a mutual peer of         every ot]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Configuration for how incidents decay peer trust scores.      Attributes]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[CrossBotTrustLedger_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[CrossBotTrustLedger]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Default propagation policy.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Depth-2 propagation A → B → C but NOT C → D when max_depth=2.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[End-to-end a real incident on bot A decays trust on bots B and C         in a 3]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[IncidentRecord]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Log an incident and propagate trust decay to registered peers.          Args]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Ordered severity levels for cross-bot incidents.      Values map to IEC 62443 SL]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Path_5]] - code - gateway/security/alert_dispatcher.py
- [[Peer agent not registered in TrustManager should be auto-registered.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Propagation to a peer with no registered TrustManager must not raise.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Recursive BFS propagation up to max_propagation_depth hops.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Register bot_b as a peer of bot_a.          Args             bot_a Source bot]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return incidents, optionally filtered by source bot.          Args]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return the number of incidents currently in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return the registered peers for bot_name (empty list if none).]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Shared trust decay channel for multi-bot deployments.      Usage          ledg]] - rationale - gateway/security/cross_bot_trust_ledger.py
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
- [[TrustManager]] - code - gateway/security/cross_bot_trust_ledger.py
- [[TrustManager_3]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[build_full_mesh N-agent-scalable topology construction.      Adding a 3rd4thN]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[cross_bot_trust_ledger.py]] - code - gateway/security/cross_bot_trust_ledger.py
- [[deque]] - code - gateway/security/killswitch_monitor.py
- [[hermes_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[ledger()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[openclaw_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[policy()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[test_cross_bot_trust_ledger.py]] - code - gateway/tests/test_cross_bot_trust_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_41
SORT file.name ASC
```

## Connections to other communities
- 36 edges to [[_COMMUNITY_Progressive Trust]]
- 15 edges to [[_COMMUNITY_Key Vault & Audit Chain]]
- 5 edges to [[_COMMUNITY_Community 47]]
- 3 edges to [[_COMMUNITY_Community 25]]
- 1 edge to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 553]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Community 206]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 198]]

## Top bridge nodes
- [[BotIncidentSeverity]] - degree 25, connects to 5 communities
- [[CrossBotTrustLedger]] - degree 38, connects to 3 communities
- [[deque]] - degree 8, connects to 2 communities
- [[cross_bot_trust_ledger.py]] - degree 6, connects to 2 communities
- [[CrossBotTrustLedger_1]] - degree 26, connects to 1 community