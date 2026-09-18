---
type: community
cohesion: 0.10
members: 28
---

# TrustLevel

**Cohesion:** 0.10 - loosely connected
**Members:** 28 nodes

## Members
- [[._apply_decay()]] - code - gateway/security/trust_manager.py
- [[._force_demotion()]] - code - gateway/security/trust_manager.py
- [[._promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[._score_to_level()]] - code - gateway/security/trust_manager.py
- [[._update_score()]] - code - gateway/security/trust_manager.py
- [[.get_trust()]] - code - gateway/security/trust_manager.py
- [[.is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[.is_tool_allowed()]] - code - gateway/security/trust_manager.py
- [[.record_failure()]] - code - gateway/security/trust_manager.py
- [[.record_success()]] - code - gateway/security/trust_manager.py
- [[.record_violation()]] - code - gateway/security/trust_manager.py
- [[.register_agent()]] - code - gateway/security/trust_manager.py
- [[.test_mapping_is_bijective_and_total()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[.test_renamed_rungs_map_correctly()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Per-level tool gate from the progressive trust ladder. Tri-state TrueFalse…]] - rationale - gateway/security/trust_manager.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust. With a progressive…]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[TestEnumMapping]] - code - gateway/tests/test_progressive_trust_integration.py
- [[TrustLevel]] - code - gateway/security/trust_manager.py
- [[ViolationType_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TrustLevel
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_TrustManager]]
- 9 edges to [[_COMMUNITY__make_tm()]]
- 7 edges to [[_COMMUNITY_EgressAction]]
- 7 edges to [[_COMMUNITY_test_trust_manager.py]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_EncryptedStore]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_UserSession]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_e2e.py]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]
- 1 edge to [[_COMMUNITY_TestBotIdIsolationInSharedMemory]]
- 1 edge to [[_COMMUNITY_TestCrossBotTrustPivot]]
- 1 edge to [[_COMMUNITY_TestHermesEgressAllowlist]]
- 1 edge to [[_COMMUNITY_TestSessionPathSeparation]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[TrustLevel]] - degree 57, connects to 19 communities
- [[._update_score()]] - degree 9, connects to 1 community
- [[.get_trust()]] - degree 7, connects to 1 community
- [[.record_violation()]] - degree 6, connects to 1 community
- [[._score_to_level()]] - degree 6, connects to 1 community