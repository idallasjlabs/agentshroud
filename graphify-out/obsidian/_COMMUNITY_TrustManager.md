---
type: community
members: 123
---

# TrustManager

**Members:** 123 nodes

## Members
- [[dot-__init__()_102]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-__init__()_103]] - code - gateway/security/trust_manager.py
- [[dot-__post_init__()_5]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-_apply_decay()]] - code - gateway/security/trust_manager.py
- [[dot-_init_db()_2]] - code - gateway/security/trust_manager.py
- [[dot-_missing_()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-_promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-_propagate()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-_score_to_level()]] - code - gateway/security/trust_manager.py
- [[dot-_update_score()]] - code - gateway/security/trust_manager.py
- [[dot-close()_10]] - code - gateway/security/trust_manager.py
- [[dot-get_history()]] - code - gateway/security/trust_manager.py
- [[dot-get_incidents()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-get_trust()]] - code - gateway/security/trust_manager.py
- [[dot-incident_count()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-is_tool_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-peers_of()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-record_failure()]] - code - gateway/security/trust_manager.py
- [[dot-record_incident()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-record_success()]] - code - gateway/security/trust_manager.py
- [[dot-register_agent()]] - code - gateway/security/trust_manager.py
- [[dot-register_peer()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-register_trust_manager()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-test_10000_lookups_under_1s()]] - code - gateway/tests/test_performance.py
- [[dot-test_bot_without_registered_trust_manager_is_skipped()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_consent_required_for_sensitive_ops()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_critical_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_default_policy_is_sane()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_empty_ledger_has_no_incidents()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_fraction_above_one_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_from_string()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_get_incidents_by_source()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_get_incidents_with_limit()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_high_severity_propagates_full_fraction()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incident_limit_retained()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incident_record_fields()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_incidents_are_recorded()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_invalid_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_low_severity_not_propagated()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_medium_severity_propagates_to_peer()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_no_self_propagation()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_non_string_returns_none()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_ordering()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_propagated_to_is_empty_for_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_propagation_registers_unregistered_peer_agent()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_register_peer()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_register_peer_is_bidirectional_by_default()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_session_cannot_impersonate()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_subagent_monitor_tracks_events()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_cannot_exceed_max()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_manager_rapid_updates()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_trust_update_performance()]] - code - gateway/tests/test_performance.py
- [[dot-test_unregistered_agent_blocked()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_unregistered_bot_has_no_peers()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_violation_drops_trust_significantly()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_zero_decay_fraction_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-test_zero_max_depth_rejected()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[dot-vouch_for_agent()]] - code - gateway/security/trust_manager.py
- [[1000 trust updates (mix of successfailure).]] - rationale - gateway/tests/test_performance.py
- [[10000 trust lookups in under 1 second.]] - rationale - gateway/tests/test_performance.py
- [[A single cross-bot incident recorded in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[A single violation should meaningfully impact trust.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[An incident on openclaw should not re-apply to openclaw via the ledger.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Attach a TrustManager instance to a bot name.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[BotIncidentSeverity]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Configuration for how incidents decay peer trust scores. Attributes…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Consent framework should be available for gating.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Cross-Bot Trust Ledger — Module 27 (v1.2.0) IEC 62443 FR6 (Audit Log …]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[CrossBotTrustLedger]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Default propagation policy.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Different sessions should have different identities.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get trust history for an agent.]] - rationale - gateway/security/trust_manager.py
- [[IncidentRecord]] - code - gateway/security/cross_bot_trust_ledger.py
- [[IntEnum_2]] - code
- [[Log an incident and propagate trust decay to registered peers. Args…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Manage progressive trust for agents.]] - rationale - gateway/security/trust_manager.py
- [[Ordered severity levels for cross-bot incidents. Values map to IEC 62443 SLIR…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Owner vouches for an agent, unlocking VERIFIEDFULL promotion.]] - rationale - gateway/security/trust_manager.py
- [[Peer agent not registered in TrustManager should be auto-registered.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Per-level tool gate from the progressive trust ladder. Tri-state TrueFalse…]] - rationale - gateway/security/trust_manager.py
- [[Propagation to a peer with no registered TrustManager must not raise.]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Rapid trust score updates shouldn't corrupt state.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Recursive BFS propagation up to max_propagation_depth hops.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[Register bot_b as a peer of bot_a. Args bot_a Source bot name. bot_b Peer…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return incidents, optionally filtered by source bot. Args source_bot If…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return the number of incidents currently in the ledger.]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Return the registered peers for bot_name (empty list if none).]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Shared trust decay channel for multi-bot deployments. Usage ledger =…]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Subagent events should be trackable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test trust boundaries and privilege escalation prevention.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestBotIncidentSeverity]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestCrossBotTrustLedgerConstruction]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestGetIncidentsLimit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentAudit]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestIncidentPropagation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestPersistence_1]] - code - gateway/tests/test_trust_manager.py
- [[TestPrivilegeEscalation]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestTrustDecayPolicyValidation]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[TestTrustManagerPerformance]] - code - gateway/tests/test_performance.py
- [[Tests for Module 27 — Cross-Bot Trust Ledger. IEC 62443 FR6 (Audit Log …]] - rationale - gateway/tests/test_cross_bot_trust_ledger.py
- [[Trust check 10000 lookups in  1s.]] - rationale - gateway/tests/test_performance.py
- [[Trust score should have an upper bound.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TrustDecayPolicy]] - code - gateway/security/cross_bot_trust_ledger.py
- [[TrustManager]] - code - gateway/security/trust_manager.py
- [[Unregistered agents should not be trusted.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[cross_bot_trust_ledger.py]] - code - gateway/security/cross_bot_trust_ledger.py
- [[fixture_68]] - code
- [[hermes_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[ledger()_1]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[openclaw_tm()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[policy()]] - code - gateway/tests/test_cross_bot_trust_ledger.py
- [[test_cross_bot_trust_ledger.py]] - code - gateway/tests/test_cross_bot_trust_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustManager
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_TrustConfig]]
- 26 edges to [[_COMMUNITY_lifespan.py]]
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_asyncio_1]]
- 5 edges to [[_COMMUNITY_TestAuth_1]]
- 5 edges to [[_COMMUNITY_A2APolicyConfig]]
- 4 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 2 edges to [[_COMMUNITY_test_security_integration.py]]
- 2 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[TrustManager]] - degree 114, connects to 19 communities
- [[CrossBotTrustLedger]] - degree 40, connects to 4 communities
- [[TestPrivilegeEscalation]] - degree 12, connects to 4 communities
- [[BotIncidentSeverity]] - degree 16, connects to 3 communities
- [[test_cross_bot_trust_ledger.py]] - degree 20, connects to 2 communities
