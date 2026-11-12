---
type: community
members: 123
---

# Community 11

**Members:** 123 nodes

## Members
- [[.__init__()_136]] - code - gateway/security/tool_acl.py
- [[.__init__()_142]] - code - gateway/security/trust_manager.py
- [[._apply_decay()]] - code - gateway/security/trust_manager.py
- [[._force_demotion()]] - code - gateway/security/trust_manager.py
- [[._init_db()_2]] - code - gateway/security/trust_manager.py
- [[._promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[._score_to_level()]] - code - gateway/security/trust_manager.py
- [[._update_score()]] - code - gateway/security/trust_manager.py
- [[.check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[.enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[.get_denial_counts()]] - code - gateway/security/tool_acl.py
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
- [[.test_default_mode_is_enforce()_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_no_rbac_defaults_to_viewer()]] - code - gateway/tests/test_tool_acl.py
- [[.test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_score_alone_cannot_promote_with_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_score_alone_promotes_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_severe_violation_forces_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_tool_allowed_at_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_tool_denied_above_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_trust_deny_wins_over_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_typed_penalty_from_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unknown_tool_falls_through_to_acl()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unknown_tool_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_unregistered_agent_returns_none()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_untyped_violation_uses_legacy_points()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_vouching_required_for_top_rung()]] - code - gateway/tests/test_progressive_trust_integration.py
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
- [[ProgressiveTrustConfig]] - code - gateway/security/progressive_trust_config.py
- [[ProgressiveTrustConfig_1]] - code - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_2]] - code - gateway/tests/test_progressive_trust_integration.py
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
- [[TrustManager_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[ViolationType_1]] - code - gateway/security/trust_manager.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[enforcer()]] - code - gateway/tests/test_group_rbac.py
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager.py]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_11
SORT file.name ASC
```

## Connections to other communities
- 75 edges to [[_COMMUNITY_Community 7]]
- 36 edges to [[_COMMUNITY_Community 33]]
- 22 edges to [[_COMMUNITY_Community 307]]
- 8 edges to [[_COMMUNITY_Community 300]]
- 8 edges to [[_COMMUNITY_Community 61]]
- 5 edges to [[_COMMUNITY_Community 1566]]
- 4 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 6]]
- 3 edges to [[_COMMUNITY_Community 52]]
- 2 edges to [[_COMMUNITY_Community 493]]
- 2 edges to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 203]]
- 1 edge to [[_COMMUNITY_Community 924]]
- 1 edge to [[_COMMUNITY_Community 1985]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 123]]
- 1 edge to [[_COMMUNITY_Community 1119]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 888]]
- 1 edge to [[_COMMUNITY_Community 792]]
- 1 edge to [[_COMMUNITY_Community 947]]
- 1 edge to [[_COMMUNITY_Community 1291]]

## Top bridge nodes
- [[TrustLevel_1]] - degree 62, connects to 14 communities
- [[ToolACLEnforcer]] - degree 77, connects to 6 communities
- [[ViolationType]] - degree 39, connects to 6 communities
- [[trust_manager.py]] - degree 10, connects to 3 communities
- [[ProgressiveTrustConfig]] - degree 40, connects to 2 communities