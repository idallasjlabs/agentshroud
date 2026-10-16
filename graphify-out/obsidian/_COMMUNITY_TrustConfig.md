---
type: community
cohesion: 0.04
members: 126
---

# TrustConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 126 nodes

## Members
- [[dot-__init__()_36]] - code - gateway/security/trust_manager.py
- [[dot-__post_init__()_1]] - code - gateway/security/trust_manager.py
- [[dot-_force_demotion()]] - code - gateway/security/trust_manager.py
- [[dot-_init_db()_1]] - code - gateway/security/trust_manager.py
- [[dot-get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[dot-is_tool_allowed()]] - code - gateway/security/progressive_trust_config.py
- [[dot-record_violation()]] - code - gateway/security/trust_manager.py
- [[dot-test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_custom_points()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_default_config()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_default_mode_is_enforce()_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_register_idempotent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_score_alone_cannot_promote_with_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_score_alone_promotes_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_severe_violation_forces_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_thresholds_populated()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_tool_allowed_at_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_tool_denied_above_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_trust_deny_wins_over_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_typed_penalty_from_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unknown_tool_falls_through_to_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unknown_tool_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unregistered_agent_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_untyped_violation_uses_legacy_points()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_vouching_required_for_top_rung()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[A ladder with thresholds small enough for unit tests.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78).      Returns]] - rationale - gateway/security/progressive_trust_config.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Progressive Trust Ladder (threshold-gated promotion + typed-violation demotion)]] - rationale - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig]] - code - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_1]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig_2]] - code - gateway/security/progressive_trust_config.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[Record a security violation, significantly decreasing trust.          With a pro]] - rationale - gateway/security/trust_manager.py
- [[SCRUM-78 — operational monitor↔enforce lever.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[SCRUM-78 — the env-var resolver must fail CLOSED (enforce).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Seed stored scorelevel directly (same technique lifespan.py uses).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Stored level is the promotion ceiling when the ladder is active.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test configuration options.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestBackwardCompat]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestConfig]] - code - gateway/tests/test_trust_manager.py
- [[TestEnforcementMode]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementModeResolver]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestGatedPromotion]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestPersistence_1]] - code - gateway/tests/test_trust_manager.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolGating]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_trust_manager.py
- [[TestTypedViolations]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Threshold for promoting to a trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[TrustConfig]] - code - gateway/security/trust_manager.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[TrustLevel_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager_1]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[ViolationType_1]] - code - gateway/security/trust_manager.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[manager()]] - code - gateway/tests/test_trust_manager.py
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[strict_config()_1]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_a2a_ssrf_callback_is_a_severe_violation_by_default()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py
- [[trust_manager.py]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustConfig
SORT file.name ASC
```

## Connections to other communities
- 52 edges to [[_COMMUNITY_PIIConfig]]
- 23 edges to [[_COMMUNITY_AgentRegistry]]
- 20 edges to [[_COMMUNITY_A2APolicyEngine]]
- 19 edges to [[_COMMUNITY_Role]]
- 18 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 8 edges to [[_COMMUNITY_dot-_update_score]]
- 7 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 6 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_PipelineAction]]
- 4 edges to [[_COMMUNITY_Enum]]
- 4 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 4 edges to [[_COMMUNITY__FakeAttack]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 3 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_TestTrustProgression]]
- 2 edges to [[_COMMUNITY_A2AProxyResult]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_TestEgressSSRF]]
- 1 edge to [[_COMMUNITY_subagent_governance.py]]
- 1 edge to [[_COMMUNITY_Recommendation_1]]
- 1 edge to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_EnvelopeSigner]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_test_e2e.py]]

## Top bridge nodes
- [[TrustConfig]] - degree 101, connects to 13 communities
- [[TrustLevel_1]] - degree 54, connects to 10 communities
- [[ViolationType]] - degree 39, connects to 7 communities
- [[trust_manager.py]] - degree 9, connects to 4 communities
- [[ProgressiveTrustConfig_2]] - degree 40, connects to 3 communities
