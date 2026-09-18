---
type: community
cohesion: 0.09
members: 49
---

# _make_tm()

**Cohesion:** 0.09 - loosely connected
**Members:** 49 nodes

## Members
- [[.test_default_mode_is_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_demotion_recorded_in_history()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_enforce_mode_blocks()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_full_level_wildcard_allows_everything()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_get_trust_respects_stored_ceiling()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_returns_none_without_config()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_logs_but_does_not_block_via_trust_gate()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_monitor_mode_still_allows_permitted_tools()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_non_severe_typed_violation_does_not_force_demotion()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_promotion_granted_once_thresholds_met()]] - code - gateway/tests/test_progressive_trust_integration.py
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
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig]] - code
- [[ProgressiveTrustConfig → TrustManager integration tests. The trust ladder…]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[SCRUM-78 — operational monitor↔enforce lever.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Seed stored scorelevel directly (same technique lifespan.py uses).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Stored level is the promotion ceiling when the ladder is active.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TestBackwardCompat]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementMode]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestGatedPromotion]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolACLComposition]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestToolGating]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestTypedViolations]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_tm
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 9 edges to [[_COMMUNITY_TrustLevel]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_TestEnforcementModeResolver]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[test_progressive_trust_integration.py]] - degree 20, connects to 7 communities
- [[_make_tm()]] - degree 24, connects to 2 communities
- [[_set_state()]] - degree 18, connects to 2 communities
- [[TestEnforcementMode]] - degree 8, connects to 2 communities
- [[TestToolACLComposition]] - degree 6, connects to 2 communities