---
type: community
cohesion: 0.03
members: 140
---

# MemoryIntegrityMonitor

**Cohesion:** 0.03 - loosely connected
**Members:** 140 nodes

## Members
- [[.__init__()_127]] - code - gateway/security/trust_manager.py
- [[._apply_decay()]] - code - gateway/security/trust_manager.py
- [[._force_demotion()]] - code - gateway/security/trust_manager.py
- [[._init_db()_2]] - code - gateway/security/trust_manager.py
- [[._promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[._score_to_level()]] - code - gateway/security/trust_manager.py
- [[._update_score()]] - code - gateway/security/trust_manager.py
- [[.close()_11]] - code - gateway/security/trust_manager.py
- [[.get_history()]] - code - gateway/security/trust_manager.py
- [[.get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_trust()]] - code - gateway/security/trust_manager.py
- [[.get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[.is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[.is_tool_allowed()]] - code - gateway/security/progressive_trust_config.py
- [[.is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[.record_failure()]] - code - gateway/security/trust_manager.py
- [[.record_success()]] - code - gateway/security/trust_manager.py
- [[.record_violation()]] - code - gateway/security/trust_manager.py
- [[.register_agent()]] - code - gateway/security/trust_manager.py
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_default_mode_is_enforce()_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[.test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_score_alone_cannot_promote_with_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_score_alone_promotes_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_severe_violation_forces_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_tool_allowed_at_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_tool_denied_above_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_trust_deny_wins_over_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_trust_level_enforcement()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_recovery()]] - code - gateway/tests/test_security_audit.py
- [[.test_typed_penalty_from_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unknown_tool_falls_through_to_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unknown_tool_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unregistered_agent_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_untyped_violation_uses_legacy_points()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_vouching_required_for_top_rung()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.vouch_for_agent()]] - code - gateway/security/trust_manager.py
- [[A ladder with thresholds small enough for unit tests.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0.      Thi]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78).      Returns]] - rationale - gateway/security/progressive_trust_config.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust history for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Low-trust agents should be blocked from high-risk actions.]] - rationale - gateway/tests/test_security_audit.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Manage progressive trust for agents.]] - rationale - gateway/security/trust_manager.py
- [[Owner vouches for an agent, unlocking VERIFIEDFULL promotion.]] - rationale - gateway/security/trust_manager.py
- [[Per-level tool gate from the progressive trust ladder.          Tri-state True]] - rationale - gateway/security/trust_manager.py
- [[Progressive Trust Ladder (threshold-gated promotion + typed-violation demotion)]] - rationale - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_1]] - code - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig]] - code - gateway/security/progressive_trust_config.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust.      Verifies the seeding]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust.          With a pro]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[SCRUM-78 — operational monitor↔enforce lever.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[SCRUM-78 — the env-var resolver must fail CLOSED (enforce).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Seed stored scorelevel directly (same technique lifespan.py uses).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Stored level is the promotion ceiling when the ladder is active.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestBackwardCompat]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestEnforcementMode]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementModeResolver]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestGatedPromotion]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestPersistence_2]] - code - gateway/tests/test_trust_manager.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolGating]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestTypedViolations]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Threshold for promoting to a trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[Trust should recover after good behavior.]] - rationale - gateway/tests/test_security_audit.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[TrustLevel_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager_1]] - code - gateway/security/trust_manager.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[ViolationType_1]] - code - gateway/security/trust_manager.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_4]] - code - gateway/tests/test_security_integration.py
- [[trust_manager.py]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MemoryIntegrityMonitor
SORT file.name ASC
```

## Connections to other communities
- 53 edges to [[_COMMUNITY_TrustConfig]]
- 29 edges to [[_COMMUNITY_AgentTarget]]
- 27 edges to [[_COMMUNITY_lifespan.py]]
- 19 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 18 edges to [[_COMMUNITY_RBACConfig]]
- 13 edges to [[_COMMUNITY_WebProxyConfig]]
- 11 edges to [[_COMMUNITY_test_security_audit.py]]
- 11 edges to [[_COMMUNITY_ConsentFramework]]
- 11 edges to [[_COMMUNITY_ServiceManager]]
- 8 edges to [[_COMMUNITY__wrap_response()]]
- 6 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 5 edges to [[_COMMUNITY_EgressPolicy]]
- 5 edges to [[_COMMUNITY_falco_monitor.py]]
- 5 edges to [[_COMMUNITY_ResourceGuard]]
- 5 edges to [[_COMMUNITY_test_approval_queue.py]]
- 5 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 4 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 2 edges to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 2 edges to [[_COMMUNITY_icloudscriptscalendar.js]]
- 2 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_Skill Hermes Dev Workflow (HDEV)]]
- 2 edges to [[_COMMUNITY_AgentShroud Recovery Plan v0.4.0]]
- 1 edge to [[_COMMUNITY_Daedalus — Concept Illustrator]]
- 1 edge to [[_COMMUNITY_Vulcan — Subject Matter Auditor]]
- 1 edge to [[_COMMUNITY_Socrates — Dialogue Architect]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_failover.py]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]

## Top bridge nodes
- [[TrustManager_1]] - degree 184, connects to 26 communities
- [[TrustLevel_1]] - degree 62, connects to 19 communities
- [[ViolationType]] - degree 39, connects to 5 communities
- [[trust_manager.py]] - degree 10, connects to 5 communities
- [[ProgressiveTrustConfig]] - degree 40, connects to 3 communities