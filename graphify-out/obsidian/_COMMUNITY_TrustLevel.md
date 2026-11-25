---
type: community
members: 73
---

# TrustLevel

**Members:** 73 nodes

## Members
- [[dot-__init__()_103]] - code - gateway/security/trust_manager.py
- [[dot-_apply_decay()]] - code - gateway/security/trust_manager.py
- [[dot-_force_demotion()]] - code - gateway/security/trust_manager.py
- [[dot-_init_db()_1]] - code - gateway/security/trust_manager.py
- [[dot-_promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-_score_to_level()]] - code - gateway/security/trust_manager.py
- [[dot-_update_score()]] - code - gateway/security/trust_manager.py
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
- [[dot-test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Enum_25]] - code
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78). Returns…]] - rationale - gateway/security/progressive_trust_config.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[IntEnum_5]] - code
- [[Per-level tool gate from the progressive trust ladder. Tri-state TrueFalse…]] - rationale - gateway/security/trust_manager.py
- [[ProgressiveTrustConfig]] - code - gateway/security/progressive_trust_config.py
- [[ProgressiveTrustConfig → TrustManager integration tests. The trust ladder…]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust. With a progressive…]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[SCRUM-129 Phase 4 — A2A trust-scoring wiring. Reuses TrustManager as-is…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[SCRUM-78 — the env-var resolver must fail CLOSED (enforce).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementModeResolver]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Threshold for promoting to a trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[fixture_84]] - code
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_a2a_ssrf_callback_is_a_severe_violation_by_default()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_trust_scoring.py]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_violation_types_exist()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_progressive_trust_integration.py]] - code - gateway/tests/test_progressive_trust_integration.py
- [[trust_manager()_3]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager.py]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustLevel
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 22 edges to [[_COMMUNITY_TrustManager]]
- 12 edges to [[_COMMUNITY_A2APolicyEngine]]
- 10 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_A2AProxy]]
- 4 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 3 edges to [[_COMMUNITY_PIISanitizer]]
- 3 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 3 edges to [[_COMMUNITY_lifespan]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_TestTrustProgression]]
- 1 edge to [[_COMMUNITY_TestCrossBotTrustPivot]]
- 1 edge to [[_COMMUNITY_A2APeerTestDouble]]
- 1 edge to [[_COMMUNITY_TestTrustManager]]
- 1 edge to [[_COMMUNITY_test_canary.py]]

## Top bridge nodes
- [[TrustLevel_1]] - degree 41, connects to 12 communities
- [[trust_manager.py]] - degree 24, connects to 12 communities
- [[ProgressiveTrustConfig]] - degree 24, connects to 6 communities
- [[ViolationType]] - degree 18, connects to 5 communities
- [[test_progressive_trust_integration.py]] - degree 24, connects to 3 communities
