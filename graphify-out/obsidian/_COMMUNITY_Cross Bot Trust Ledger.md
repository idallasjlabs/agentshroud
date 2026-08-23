---
type: community
cohesion: 0.06
members: 78
---

# Cross Bot Trust Ledger

**Cohesion:** 0.06 - loosely connected
**Members:** 78 nodes

## Members
- [[.__init__()_68]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.__post_init__()_3]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.__post_init__()_9]] - code - gateway/security/trust_manager.py
- [[._missing_()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[._shared_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.get_incidents()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.record_incident()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[.test_adding_a_fourth_bot_extends_the_mesh_to_everyone()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_bot_without_registered_trust_manager_is_skipped()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_critical_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_custom_points()]] - code - gateway/tests/test_trust_manager.py
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
- [[.test_thresholds_populated()]] - code - gateway/tests/test_trust_manager.py
- [[.test_two_bots_are_mutual_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_unregistered_bot_has_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_zero_decay_fraction_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[.test_zero_max_depth_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[A single cross-bot incident recorded in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[An incident on openclaw should not re-apply to openclaw via the ledger.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[BotIncidentSeverity]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Configuration for how incidents decay peer trust scores.      Attributes]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[CrossBotTrustLedger_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[Default propagation policy.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Depth-2 propagation A → B → C but NOT C → D when max_depth=2.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[End-to-end a real incident on bot A decays trust on bots B and C         in a 3]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[IncidentRecord]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Log an incident and propagate trust decay to registered peers.          Args]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Ordered severity levels for cross-bot incidents.      Values map to IEC 62443 SL]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Peer agent not registered in TrustManager should be auto-registered.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Propagation to a peer with no registered TrustManager must not raise.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Return incidents, optionally filtered by source bot.          Args]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Test configuration options.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestBotIncidentSeverity]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestBuildFullMesh]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestConfig]] - code - gateway/tests/test_trust_manager.py
- [[TestCrossBotTrustLedgerConstruction]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestGetIncidentsLimit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentAudit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentPropagation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestTrustDecayPolicyValidation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[The exact scenario the user asked for add a 4th bot and it just works.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustConfig]] - code - gateway/security/trust_manager.py
- [[TrustDecayPolicy]] - code - gateway/security/cross_bot_trust_ledger.py
- [[TrustDecayPolicy_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustManager_3]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TrustManager_6]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[build_full_mesh N-agent-scalable topology construction.      Adding a 3rd4thN]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[cross_bot_trust_ledger.py]] - code - gateway/security/cross_bot_trust_ledger.py
- [[hermes_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[ledger()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[openclaw_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[policy()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[test_cross_bot_trust_ledger.py]] - code - gateway/tests/test_cross_bot_trust_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Cross_Bot_Trust_Ledger
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 28 edges to [[_COMMUNITY_Pipeline Unit]]
- 20 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 18 edges to [[_COMMUNITY_Progressive Trust Integration]]
- 6 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_Pipeline (proxy)]]
- 3 edges to [[_COMMUNITY_Pipeline Unit]]
- 3 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 2 edges to [[_COMMUNITY_E2e Proxy]]
- 2 edges to [[_COMMUNITY_Redteam Probes]]
- 2 edges to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Skill Guard]]
- 1 edge to [[_COMMUNITY_Killswitch Monitor & Observatory Mode]]
- 1 edge to [[_COMMUNITY_Key Vault]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Trust Manager]]

## Top bridge nodes
- [[TrustConfig]] - degree 101, connects to 16 communities
- [[BotIncidentSeverity]] - degree 25, connects to 5 communities
- [[cross_bot_trust_ledger.py]] - degree 6, connects to 3 communities
- [[CrossBotTrustLedger_1]] - degree 26, connects to 2 communities
- [[TrustManager_3]] - degree 25, connects to 2 communities