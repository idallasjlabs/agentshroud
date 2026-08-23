---
type: community
cohesion: 0.05
members: 100
---

# Progressive Trust Integration

**Cohesion:** 0.05 - loosely connected
**Members:** 100 nodes

## Members
- [[._apply_decay()]] - code - gateway/security/trust_manager.py
- [[._force_demotion()]] - code - gateway/security/trust_manager.py
- [[._promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[._score_to_level()]] - code - gateway/security/trust_manager.py
- [[._update_score()]] - code - gateway/security/trust_manager.py
- [[.get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_trust()]] - code - gateway/security/trust_manager.py
- [[.get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[.is_tool_allowed()]] - code - gateway/security/progressive_trust_config.py
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
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78).      Returns]] - rationale - gateway/security/progressive_trust_config.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[High score with too few interactions must NOT climb the ladder.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[MALICIOUS_INTENT drops a level even when the score would not.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig_1]] - code - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[ProgressiveTrustConfig]] - code - gateway/security/progressive_trust_config.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust.          With a pro]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
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
- [[Tools outside the ladder vocabulary get no opinion (ACL decides).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[TrustLevel_2]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager_4]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager WITHOUT a progressive config must behave exactly as before.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TrustManager._update_score() (progressive promotion gate)]] - code - gateway/security/trust_manager.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[ViolationType_1]] - code - gateway/security/trust_manager.py
- [[_fast_ladder()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_make_tm()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[_set_state()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Progressive_Trust_Integration
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 20 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 19 edges to [[_COMMUNITY_A2a Integration]]
- 18 edges to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 12 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 8 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 6 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_Pipeline (proxy)]]
- 2 edges to [[_COMMUNITY_A2a Proxy (proxy)]]
- 2 edges to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Pipeline Unit]]
- 1 edge to [[_COMMUNITY_Skill Guard]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 1 edge to [[_COMMUNITY_Session Manager]]
- 1 edge to [[_COMMUNITY_Docs Accuracy]]
- 1 edge to [[_COMMUNITY_Redteam Probes]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Trust Manager]]

## Top bridge nodes
- [[TrustLevel_1]] - degree 67, connects to 17 communities
- [[ViolationType]] - degree 39, connects to 8 communities
- [[ProgressiveTrustConfig]] - degree 40, connects to 5 communities
- [[test_progressive_trust_integration.py]] - degree 23, connects to 4 communities
- [[TrustLevel]] - degree 26, connects to 3 communities