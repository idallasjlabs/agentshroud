---
type: community
members: 37
---

# ProgressiveTrustConfig

**Members:** 37 nodes

## Members
- [[dot-get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[dot-get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[dot-is_tool_allowed()]] - code - gateway/security/progressive_trust_config.py
- [[dot-test_default_penalties_cover_all_violation_types()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_per_level()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_is_tool_allowed_wildcard()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_level_order()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_next_and_previous_levels()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Enum_27]] - code
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78). Returns…]] - rationale - gateway/security/progressive_trust_config.py
- [[First-ever unit tests for the config object itself.]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[ProgressiveTrustConfig]] - code - gateway/security/progressive_trust_config.py
- [[PromotionThreshold]] - code - gateway/security/progressive_trust_config.py
- [[SCRUM-78 — the env-var resolver must fail CLOSED (enforce).]] - rationale - gateway/tests/test_progressive_trust_integration.py
- [[TestEnforcementModeResolver]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TestProgressiveTrustConfigUnit]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Threshold for promoting to a trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Trust levels from untrusted to verified.]] - rationale - gateway/security/progressive_trust_config.py
- [[TrustLevel]] - code - gateway/security/progressive_trust_config.py
- [[Types of security violations.]] - rationale - gateway/security/progressive_trust_config.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[ViolationType]] - code - gateway/security/progressive_trust_config.py
- [[fixture_79]] - code
- [[progressive_trust_config.py]] - code - gateway/security/progressive_trust_config.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[test_a2a_ssrf_callback_is_a_severe_violation_by_default()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager()_2]] - code - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProgressiveTrustConfig
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 12 edges to [[_COMMUNITY_A2APolicyConfig]]
- 9 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_TrustLevel]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_A2AProxy]]

## Top bridge nodes
- [[ProgressiveTrustConfig]] - degree 24, connects to 6 communities
- [[ViolationType]] - degree 18, connects to 6 communities
- [[TrustLevel]] - degree 12, connects to 3 communities
- [[progressive_trust_config.py]] - degree 11, connects to 3 communities
- [[resolve_enforcement_mode()]] - degree 7, connects to 3 communities
