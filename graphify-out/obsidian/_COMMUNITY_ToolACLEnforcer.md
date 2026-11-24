---
type: community
members: 63
---

# ToolACLEnforcer

**Members:** 63 nodes

## Members
- [[dot-_can_use_tool_impl()]] - code - gateway/security/tool_acl.py
- [[dot-_get_group_tool_allowlist()]] - code - gateway/security/tool_acl.py
- [[dot-_get_role()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_from_origin()]] - code - gateway/security/tool_acl.py
- [[dot-can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[dot-check_tool_rate_limit()]] - code - gateway/security/tool_acl.py
- [[dot-get_allowed_tools()]] - code - gateway/security/tool_acl.py
- [[dot-get_denial_counts()]] - code - gateway/security/tool_acl.py
- [[dot-get_denied_tools()]] - code - gateway/security/tool_acl.py
- [[dot-test_default_mode_is_enforce()_7]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_enforcer_without_trust_manager_unchanged()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
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
- [[Authorize a tool call, refusing owner elevation over an unverified origin. WHY…]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke the named tool. Returns (allowed bool,…]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group…]] - rationale - gateway/security/tool_acl.py
- [[Collect additional tools granted to the user via their group memberships.]] - rationale - gateway/security/tool_acl.py
- [[Enforces tool-level access control based on user role and group membership.…]] - rationale - gateway/security/tool_acl.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig → TrustManager integration tests. The trust ladder…]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80), then…]] - rationale - gateway/security/tool_acl.py
- [[Return True if the user is within rate limits for the given tool. Side-effect…]] - rationale - gateway/security/tool_acl.py
- [[Return per-user tool denial counts since last restart (V9-2 SOC correlation).]] - rationale - gateway/security/tool_acl.py
- [[Return the list of tools the user is allowed to use (union of all sets).]] - rationale - gateway/security/tool_acl.py
- [[Return tools explicitly denied for this user.]] - rationale - gateway/security/tool_acl.py
- [[SCRUM-78 — operational monitor↔enforce lever.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Seed stored scorelevel directly (same technique lifespan.py uses).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Stored level is the promotion ceiling when the ladder is active.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TestBackwardCompat]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementMode]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestGatedPromotion]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolGating]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestTypedViolations]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ToolACLEnforcer]] - code - gateway/security/tool_acl.py
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolACLEnforcer
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_ProgressiveTrustConfig]]
- 14 edges to [[_COMMUNITY_test_tool_acl.py]]
- 9 edges to [[_COMMUNITY_TrustLevel]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_test_module_stats.py]]
- 4 edges to [[_COMMUNITY_GroupRoleResolver]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[ToolACLEnforcer]] - degree 44, connects to 6 communities
- [[test_progressive_trust_integration.py]] - degree 24, connects to 3 communities
- [[_set_state()]] - degree 18, connects to 2 communities
- [[TestEnforcementMode]] - degree 9, connects to 2 communities
- [[TestToolGating]] - degree 8, connects to 2 communities
