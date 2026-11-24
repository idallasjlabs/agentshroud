---
type: community
members: 43
---

# TrustLevel

**Members:** 43 nodes

## Members
- [[dot-__init__()_217]] - code - gateway/security/trust_manager.py
- [[dot-_apply_decay()]] - code - gateway/security/trust_manager.py
- [[dot-_force_demotion()]] - code - gateway/security/trust_manager.py
- [[dot-_init_db()_2]] - code - gateway/security/trust_manager.py
- [[dot-_promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-_score_to_level()]] - code - gateway/security/trust_manager.py
- [[dot-_update_score()]] - code - gateway/security/trust_manager.py
- [[dot-get_trust()]] - code - gateway/security/trust_manager.py
- [[dot-is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[dot-is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[dot-record_failure()]] - code - gateway/security/trust_manager.py
- [[dot-record_success()]] - code - gateway/security/trust_manager.py
- [[dot-record_violation()]] - code - gateway/security/trust_manager.py
- [[dot-register_agent()]] - code - gateway/security/trust_manager.py
- [[dot-test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[dot-test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[Agent with low trust cannot perform elevated actions.]] - rationale - gateway/tests/test_security_integration.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[IntEnum_4]] - code
- [[Per-level tool gate from the progressive trust ladder. Tri-state TrueFalse…]] - rationale - gateway/security/trust_manager.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust. With a progressive…]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustLevel_1]] - code - gateway/security/trust_manager.py
- [[test_trust_insufficient_action_blocked()]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustLevel
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_TrustManager]]
- 9 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 3 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 3 edges to [[_COMMUNITY_ProgressiveTrustConfig]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_security_integration.py]]
- 1 edge to [[_COMMUNITY_TestTrustProgression]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[TrustLevel_1]] - degree 41, connects to 9 communities
- [[dot-record_violation()]] - degree 6, connects to 2 communities
- [[TestEnumMapping]] - degree 5, connects to 2 communities
- [[dot-__init__()_217]] - degree 5, connects to 2 communities
- [[dot-_update_score()]] - degree 9, connects to 1 community
