---
type: community
members: 98
---

# MCP Policy Engine

**Members:** 98 nodes

## Members
- [[._apply_decay()]] - code - gateway/security/trust_manager.py
- [[._force_demotion()]] - code - gateway/security/trust_manager.py
- [[._init_db()_2]] - code - gateway/security/trust_manager.py
- [[._promotion_allowed()]] - code - gateway/security/trust_manager.py
- [[._score_to_level()]] - code - gateway/security/trust_manager.py
- [[._update_score()]] - code - gateway/security/trust_manager.py
- [[.close()_10]] - code - gateway/security/trust_manager.py
- [[.get_history()]] - code - gateway/security/trust_manager.py
- [[.get_trust()]] - code - gateway/security/trust_manager.py
- [[.is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[.is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[.record_failure()]] - code - gateway/security/trust_manager.py
- [[.record_success()]] - code - gateway/security/trust_manager.py
- [[.record_violation()]] - code - gateway/security/trust_manager.py
- [[.register_agent()]] - code - gateway/security/trust_manager.py
- [[.setup_method()_28]] - code - gateway/tests/test_security_hardening.py
- [[.teardown_method()_6]] - code - gateway/tests/test_security_hardening.py
- [[.test_10000_lookups_under_1s()]] - code - gateway/tests/test_performance.py
- [[.test_action_allowed_basic()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_denied_high_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_action_unknown_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[.test_default_config()_8]] - code - gateway/tests/test_trust_manager.py
- [[.test_failure_decreases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_trust_unknown()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history()]] - code - gateway/tests/test_security_hardening.py
- [[.test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[.test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[.test_rate_limiting_prevents_rapid_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_agent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_score_never_negative()]] - code - gateway/tests/test_security_hardening.py
- [[.test_sqlite_persistence()]] - code - gateway/tests/test_security_hardening.py
- [[.test_success_increases_score()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_escalation_attack()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_level_enforcement()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[.test_trust_level_progression()]] - code - gateway/tests/test_security_hardening.py
- [[.test_trust_recovery()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_update_performance()]] - code - gateway/tests/test_performance.py
- [[.test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[.test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[.test_violation_large_decrease()]] - code - gateway/tests/test_security_hardening.py
- [[.vouch_for_agent()]] - code - gateway/security/trust_manager.py
- [[1000 trust updates (mix of successfailure).]] - rationale - gateway/tests/test_performance.py
- [[10000 trust lookups in under 1 second.]] - rationale - gateway/tests/test_performance.py
- [[Apply time-based decay to score.]] - rationale - gateway/security/trust_manager.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Check the progressive ladder's threshold for promotion to target_level.]] - rationale - gateway/security/trust_manager.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Convert score to trust level based on thresholds.]] - rationale - gateway/security/trust_manager.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[Cross-Bot Trust Ledger (Module 27)]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Drop an agent one trust level immediately (severe violations).]] - rationale - gateway/security/trust_manager.py
- [[Get current trust level and score for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Get trust history for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Low-trust agents should be blocked from high-risk actions.]] - rationale - gateway/tests/test_security_audit.py
- [[Manage progressive trust for agents.]] - rationale - gateway/security/trust_manager.py
- [[Owner vouches for an agent, unlocking VERIFIEDFULL promotion.]] - rationale - gateway/security/trust_manager.py
- [[Per-level tool gate from the progressive trust ladder.          Tri-state True]] - rationale - gateway/security/trust_manager.py
- [[Rapid successes should be capped by rate limiting.]] - rationale - gateway/tests/test_security_hardening.py
- [[Record a failedblocked action, decreasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Record a security violation, significantly decreasing trust.          With a pro]] - rationale - gateway/security/trust_manager.py
- [[Record a successful action, increasing trust.]] - rationale - gateway/security/trust_manager.py
- [[Register a new agent with initial trust.]] - rationale - gateway/security/trust_manager.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestPersistence_2]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_trust_manager.py
- [[TestTrustManager]] - code - gateway/tests/test_security_hardening.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[Trust should recover after good behavior.]] - rationale - gateway/tests/test_security_audit.py
- [[TrustManager_1]] - code - gateway/security/trust_manager.py
- [[Verify you can't jump from UNTRUSTED to FULL in one step.]] - rationale - gateway/tests/test_security_hardening.py
- [[_score_identity_authentication() (domain 13, FR1)]] - code - gateway/security/scanner_integration.py
- [[manager()_4]] - code - gateway/tests/test_trust_manager.py
- [[strict_config()_3]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_agent_cve_registry.py — agent CVE advisory registry integrity tests]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[trust_manager()_3]] - code - gateway/tests/test_e2e_watchtower.py
- [[trust_manager()_4]] - code - gateway/tests/test_security_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCP_Policy_Engine
SORT file.name ASC
```

## Connections to other communities
- 54 edges to [[_COMMUNITY_Gateway Test Suite]]
- 18 edges to [[_COMMUNITY_Gateway Test Suite]]
- 16 edges to [[_COMMUNITY_SOC RBAC & Auth]]
- 13 edges to [[_COMMUNITY_MCP Proxy Config]]
- 13 edges to [[_COMMUNITY_Telegram Proxy Test Suite]]
- 11 edges to [[_COMMUNITY_Auth & Exception Types]]
- 10 edges to [[_COMMUNITY_Gateway Test Suite]]
- 9 edges to [[_COMMUNITY_Gateway Test Suite]]
- 9 edges to [[_COMMUNITY_Gateway Test Suite]]
- 7 edges to [[_COMMUNITY_Security Module Middleware]]
- 6 edges to [[_COMMUNITY_SOC Collaborator Lifecycle]]
- 5 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_Slack API Proxy]]
- 3 edges to [[_COMMUNITY_Collaborator Response Templates]]
- 2 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Security Docs]]
- 2 edges to [[_COMMUNITY_Bot Skill Config]]
- 2 edges to [[_COMMUNITY_Audit Export Pipeline]]
- 2 edges to [[_COMMUNITY_Bot Skill Config]]
- 2 edges to [[_COMMUNITY_Docker Deploy Scripts]]
- 1 edge to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Approval Queue Tests]]
- 1 edge to [[_COMMUNITY_SOC Dashboard]]
- 1 edge to [[_COMMUNITY_ESP32 Firmware]]
- 1 edge to [[_COMMUNITY_docsreference]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Planning Docs]]

## Top bridge nodes
- [[TrustManager_1]] - degree 189, connects to 28 communities
- [[TestTrustManager]] - degree 35, connects to 10 communities
- [[test_trust_manager.py]] - degree 14, connects to 2 communities
- [[.test_rate_limiting_prevents_rapid_escalation()]] - degree 4, connects to 2 communities
- [[trust_manager()]] - degree 3, connects to 2 communities