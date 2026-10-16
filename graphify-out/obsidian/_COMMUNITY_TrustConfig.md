---
type: community
cohesion: 0.04
members: 120
---

# TrustConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 120 nodes

## Members
- [[dot-__init__()_98]] - code - gateway/security/tool_acl.py
- [[dot-__init__()_99]] - code - gateway/security/trust_manager.py
- [[dot-_apply_decay()]] - code - gateway/security/trust_manager.py
- [[dot-_force_demotion()]] - code - gateway/security/trust_manager.py
- [[dot-_init_db()_2]] - code - gateway/security/trust_manager.py
- [[dot-_promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-_score_to_level()]] - code - gateway/security/trust_manager.py
- [[dot-_update_score()]] - code - gateway/security/trust_manager.py
- [[dot-check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[dot-enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[dot-get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_trust()]] - code - gateway/security/trust_manager.py
- [[dot-get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[dot-is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-is_tool_allowed()]] - code - gateway/security/progressive_trust_config.py
- [[dot-is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[dot-record_failure()]] - code - gateway/security/trust_manager.py
- [[dot-record_success()]] - code - gateway/security/trust_manager.py
- [[dot-record_violation()]] - code - gateway/security/trust_manager.py
- [[dot-register_agent()]] - code - gateway/security/trust_manager.py
- [[dot-test_default_mode_is_enforce()_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_score_alone_cannot_promote_with_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_score_alone_promotes_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_severe_violation_forces_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_tool_allowed_at_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_tool_denied_above_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_trust_deny_wins_over_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_typed_penalty_from_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unknown_tool_falls_through_to_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unknown_tool_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unregistered_agent_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_untyped_violation_uses_legacy_points()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_vouching_required_for_top_rung()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[A ladder with thresholds small enough for unit tests.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[ADMIN_TOOLS]] - code - gateway/security/tool_acl.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[COLLABORATOR_ALLOWED_TOOLS]] - code - gateway/security/tool_acl.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Enforces tool-level access control based on user role and group membership.]] - rationale - gateway/security/tool_acl.py
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78).      Returns]] - rationale - gateway/security/progressive_trust_config.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[PRIVATE_TOOLS]] - code - gateway/security/tool_acl.py
- [[Per-level tool gate from the progressive trust ladder.          Tri-state True]] - rationale - gateway/security/trust_manager.py
- [[Progressive Trust Ladder (threshold-gated promotion + typed-violation demotion)]] - rationale - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig]] - code - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_1]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig_2]] - code - gateway/security/progressive_trust_config.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust.          With a pro]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[Return True if the user is within rate limits for the given tool.          Side-]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[SCRUM-78 — operational monitor↔enforce lever.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[SCRUM-78 — the env-var resolver must fail CLOSED (enforce).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Seed stored scorelevel directly (same technique lifespan.py uses).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Stored level is the promotion ceiling when the ladder is active.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TestBackwardCompat]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementMode]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementModeResolver]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestGatedPromotion]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolGating]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestTypedViolations]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Threshold for promoting to a trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[TrustLevel_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager_1]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[ViolationType_1]] - code - gateway/security/trust_manager.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[enforcer()_3]] - code - gateway/tests/test_group_rbac.py
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py
- [[trust_manager.py]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustConfig
SORT file.name ASC
```

## Connections to other communities
- 64 edges to [[_COMMUNITY_PIIConfig]]
- 36 edges to [[_COMMUNITY_RBACConfig]]
- 22 edges to [[_COMMUNITY_A2APolicyEngine]]
- 9 edges to [[_COMMUNITY_AgentRegistry]]
- 8 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 6 edges to [[_COMMUNITY_EgressFilterConfig]]
- 5 edges to [[_COMMUNITY_RBACConfig_2]]
- 4 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 4 edges to [[_COMMUNITY_AuditChain]]
- 3 edges to [[_COMMUNITY_GroupRoleResolver]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_DataLedger]]
- 1 edge to [[_COMMUNITY_GovernanceAction]]
- 1 edge to [[_COMMUNITY_PipelineAction]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_ForwardRequest]]
- 1 edge to [[_COMMUNITY_AlertDispatcher_1]]
- 1 edge to [[_COMMUNITY_AgentRegistry_1]]
- 1 edge to [[_COMMUNITY_TrustConfig_1]]
- 1 edge to [[_COMMUNITY_TrustConfig_2]]

## Top bridge nodes
- [[TrustLevel_1]] - degree 54, connects to 11 communities
- [[ToolACLEnforcer]] - degree 77, connects to 6 communities
- [[ViolationType]] - degree 39, connects to 5 communities
- [[trust_manager.py]] - degree 9, connects to 4 communities
- [[ProgressiveTrustConfig_2]] - degree 40, connects to 3 communities
