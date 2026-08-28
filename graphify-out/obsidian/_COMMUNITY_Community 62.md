---
type: community
cohesion: 0.03
members: 77
---

# Community 62

**Cohesion:** 0.03 - loosely connected
**Members:** 77 nodes

## Members
- [[.__init__()_117]] - code - gateway/security/shared_memory.py
- [[._is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[._strip_private_content()]] - code - gateway/security/shared_memory.py
- [[.append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[.append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[.contains_private_content()]] - code - gateway/security/shared_memory.py
- [[.get_group_memory()]] - code - gateway/security/shared_memory.py
- [[.get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[.get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[.get_user_memory()]] - code - gateway/security/shared_memory.py
- [[.test_ai_security_research_domains_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_duckduckgo_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_failover_search_engines_in_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hc_ping_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_nousresearch_in_permanent_allowlist()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[AI-security researchcompetitive-intel domains must be allowlisted.          The]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Append a timestamped entry to the group shared memory file.          Authorizati]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.          Authorization (RT-5, WS-E]] - rationale - gateway/security/shared_memory.py
- [[BT-H1 SharedMemoryManager.get_user_memory must accept a bot_id parameter.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H3 The filesystem paths for openclaw and hermes sessions differ.          Re]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 (reverse) Writing to Hermes workspace does not bleed into OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 Writing to the openclaw workspace must not leak into the hermes workspace]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0.      Thi]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes base image is from nousresearch.com — must be in egress allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes ddgs-based web search requires duckduckgo.com.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes heartbeat uses hc-ping.com for dead-man's switch.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor     hermes-a]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[PR190 failover search engines must be allowlisted.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust.      Verifies the seeding]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user.          Args             user_id The user]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving         to non-]] - rationale - gateway/security/shared_memory.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory.          R]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return memory from groups whose focus_topics match the query text.          For]] - rationale - gateway/security/shared_memory.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[TestBotIdIsolationInSharedMemory]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesEgressAllowlist]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Verify that Hermes-specific egress destinations are in the canonical allowlist.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_3]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()_5]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_62
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Community 27]]
- 17 edges to [[_COMMUNITY_Progressive Trust]]
- 14 edges to [[_COMMUNITY_Community 57]]
- 10 edges to [[_COMMUNITY_Session Management]]
- 2 edges to [[_COMMUNITY_SOC Collaborators]]
- 1 edge to [[_COMMUNITY_RBAC & SOC Realtime]]
- 1 edge to [[_COMMUNITY_Community 51]]
- 1 edge to [[_COMMUNITY_Community 774]]
- 1 edge to [[_COMMUNITY_Community 756]]
- 1 edge to [[_COMMUNITY_Security Audit & Drift Detection]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 56, connects to 7 communities
- [[test_security_regressions_v1_2.py]] - degree 19, connects to 5 communities
- [[TestHermesEgressAllowlist]] - degree 11, connects to 2 communities
- [[TestBotIdIsolationInSharedMemory]] - degree 10, connects to 2 communities
- [[TestCrossBotTrustPivot]] - degree 9, connects to 2 communities