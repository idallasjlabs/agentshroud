---
type: community
cohesion: 0.02
members: 114
---

# Security Regressions V1 2

**Cohesion:** 0.02 - loosely connected
**Members:** 114 nodes

## Members
- [[.__init__()_127]] - code - gateway/security/trust_manager.py
- [[._init_db()_2]] - code - gateway/security/trust_manager.py
- [[.close()_11]] - code - gateway/security/trust_manager.py
- [[.get_history()]] - code - gateway/security/trust_manager.py
- [[.is_action_allowed()]] - code - gateway/security/trust_manager.py
- [[.is_tool_allowed()_1]] - code - gateway/security/trust_manager.py
- [[.test_ai_security_research_domains_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_basic_can_read()]] - code - gateway/tests/test_trust_manager.py
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_default_config()_8]] - code - gateway/tests/test_trust_manager.py
- [[.test_duckduckgo_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_failover_search_engines_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_get_trust_registered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_trust_unregistered()]] - code - gateway/tests/test_trust_manager.py
- [[.test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hc_ping_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_history_empty_for_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_history_recorded()]] - code - gateway/tests/test_trust_manager.py
- [[.test_nousresearch_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_persistence_across_instances()]] - code - gateway/tests/test_trust_manager.py
- [[.test_rate_limiting_prevents_rapid_escalation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_idempotent()_1]] - code - gateway/tests/test_trust_manager.py
- [[.test_register_new_agent()]] - code - gateway/tests/test_trust_manager.py
- [[.test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_trust_level_enforcement()]] - code - gateway/tests/test_security_audit.py
- [[.test_trust_level_ordering()]] - code - gateway/tests/test_trust_manager.py
- [[.test_trust_recovery()]] - code - gateway/tests/test_security_audit.py
- [[.test_unregistered_denied()]] - code - gateway/tests/test_trust_manager.py
- [[.test_untrusted_limited()]] - code - gateway/tests/test_trust_manager.py
- [[.test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.vouch_for_agent()]] - code - gateway/security/trust_manager.py
- [[AI-security researchcompetitive-intel domains must be allowlisted.          The]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H1 SharedMemoryManager.get_user_memory must accept a bot_id parameter.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H3 The filesystem paths for openclaw and hermes sessions differ.          Re]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 (reverse) Writing to Hermes workspace does not bleed into OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 Writing to the openclaw workspace must not leak into the hermes workspace]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0.      Thi]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Check if an agent's trust level allows a given action.]] - rationale - gateway/security/trust_manager.py
- [[Config with strict thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a temporary trust database.]] - rationale - gateway/tests/test_trust_manager.py
- [[Create a trust manager with temp DB.]] - rationale - gateway/tests/test_trust_manager.py
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Get trust history for an agent.]] - rationale - gateway/security/trust_manager.py
- [[Hermes base image is from nousresearch.com — must be in egress allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes ddgs-based web search requires duckduckgo.com.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes heartbeat uses hc-ping.com for dead-man's switch.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor     hermes-a]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Low-trust agents should be blocked from high-risk actions.]] - rationale - gateway/tests/test_security_audit.py
- [[Manage progressive trust for agents.]] - rationale - gateway/security/trust_manager.py
- [[Owner vouches for an agent, unlocking VERIFIEDFULL promotion.]] - rationale - gateway/security/trust_manager.py
- [[PR190 failover search engines must be allowlisted.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Per-level tool gate from the progressive trust ladder.          Tri-state True]] - rationale - gateway/security/trust_manager.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust.      Verifies the seeding]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Rapid successes should be capped by rate limiting.]] - rationale - gateway/tests/test_security_hardening.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Test agent registration and initial trust.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test that actions are gated by trust level.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust history tracking.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust level hierarchy and thresholds.]] - rationale - gateway/tests/test_trust_manager.py
- [[Test trust survives restart.]] - rationale - gateway/tests/test_trust_manager.py
- [[TestActionGating]] - code - gateway/tests/test_trust_manager.py
- [[TestAgentRegistration]] - code - gateway/tests/test_trust_manager.py
- [[TestBotIdIsolationInSharedMemory]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesEgressAllowlist]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHistory]] - code - gateway/tests/test_trust_manager.py
- [[TestPersistence_2]] - code - gateway/tests/test_trust_manager.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestTrustLevels_1]] - code - gateway/tests/test_trust_manager.py
- [[Trust manager starting at untrusted.]] - rationale - gateway/tests/test_trust_manager.py
- [[Trust should recover after good behavior.]] - rationale - gateway/tests/test_security_audit.py
- [[TrustManager_1]] - code - gateway/security/trust_manager.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Verify that Hermes-specific egress destinations are in the canonical allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[_score_identity_authentication() (domain 13, FR1)]] - code - gateway/security/scanner_integration.py
- [[manager()_4]] - code - gateway/tests/test_trust_manager.py
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_3]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[strict_config()_3]] - code - gateway/tests/test_trust_manager.py
- [[strict_manager()]] - code - gateway/tests/test_trust_manager.py
- [[test_agent_cve_registry.py — agent CVE advisory registry integrity tests]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_trust_manager.py]] - code - gateway/tests/test_trust_manager.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_db()]] - code - gateway/tests/test_trust_manager.py
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_2]] - code - gateway/tests/test_e2e_proxy.py
- [[trust_manager()_3]] - code - gateway/tests/test_e2e_watchtower.py
- [[trust_manager()_4]] - code - gateway/tests/test_security_integration.py
- [[trust_manager()_5]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Regressions_V1_2
SORT file.name ASC
```

## Connections to other communities
- 46 edges to [[_COMMUNITY_Progressive Trust Integration]]
- 42 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 29 edges to [[_COMMUNITY_Cross Bot Trust Ledger]]
- 13 edges to [[_COMMUNITY_Pipeline Unit]]
- 11 edges to [[_COMMUNITY_Shared Memory Write Acl]]
- 10 edges to [[_COMMUNITY_Middleware & Session Isolation]]
- 9 edges to [[_COMMUNITY_A2a Integration]]
- 9 edges to [[_COMMUNITY_OAuth & Metadata Guard]]
- 8 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 8 edges to [[_COMMUNITY_Security Hardening]]
- 5 edges to [[_COMMUNITY_Security Hardening]]
- 3 edges to [[_COMMUNITY_E2e Proxy]]
- 3 edges to [[_COMMUNITY_Security Hardening]]
- 2 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 2 edges to [[_COMMUNITY_Proxy Dashboard]]
- 2 edges to [[_COMMUNITY_Pipeline Unit]]
- 2 edges to [[_COMMUNITY_Redteam Probes]]
- 2 edges to [[_COMMUNITY_Trust Manager]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_System overview (00 - START HERE)]]
- 1 edge to [[_COMMUNITY_Forward Routing]]
- 1 edge to [[_COMMUNITY_Performance]]
- 1 edge to [[_COMMUNITY_Performance]]
- 1 edge to [[_COMMUNITY_Key Vault]]
- 1 edge to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 1 edge to [[_COMMUNITY_Git Guard (security)]]
- 1 edge to [[_COMMUNITY_Security Audit]]
- 1 edge to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Security Hardening]]
- 1 edge to [[_COMMUNITY_Hermes Dashboard Bridge]]

## Top bridge nodes
- [[TrustManager_1]] - degree 195, connects to 32 communities
- [[test_security_regressions_v1_2.py]] - degree 19, connects to 5 communities
- [[test_trust_manager.py]] - degree 14, connects to 3 communities
- [[TestHermesEgressAllowlist]] - degree 11, connects to 3 communities
- [[TestBotIdIsolationInSharedMemory]] - degree 10, connects to 3 communities