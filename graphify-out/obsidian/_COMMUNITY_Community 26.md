---
type: community
members: 101
---

# Community 26

**Members:** 101 nodes

## Members
- [[.test_bot_agent_ids_are_namespace_separated_from_user_ids()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_foreign_writer_blocked()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_get_user_memory_openclaw_and_hermes_are_separate_paths()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_b_write_invisible_from_group_a()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_id_uses_group_prefix_namespace()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_memory_physically_isolated()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_write_invisible_from_user_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_group_writes_are_independent_namespaces()]] - code - gateway/tests/test_group_isolation.py
- [[.test_hermes_dashboard_forwarder_bind_address_is_documented()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_dashboard_stays_loopback_and_gateway_uses_the_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_memory_write_does_not_appear_in_openclaw_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_registered_with_standard_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_hermes_violation_does_not_affect_openclaw_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_legacy_no_author_write_still_appends()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_merged_memory_separates_group_and_dm()]] - code - gateway/tests/test_group_isolation.py
- [[.test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_openclaw_memory_write_does_not_appear_in_hermes_memory()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_openclaw_violation_does_not_affect_hermes_trust()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_owner_write_into_user_memory_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_path_traversal_rejected_for_crafted_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_path_traversal_rejected_for_crafted_user_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_run_standalone_sets_matching_bridge_port()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_self_write_succeeds()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[.test_shared_memory_manager_get_user_memory_accepts_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_user_dm_write_invisible_from_group()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_dm_write_invisible_from_other_group()]] - code - gateway/tests/test_group_isolation.py
- [[.test_user_session_paths_contain_bot_id()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[.test_user_write_io_failure_returns_false()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[A non-owner author cannot write into another user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[A user may write into their own private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[BT-H1 SharedMemoryManager.get_user_memory must accept a bot_id parameter.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H3 The filesystem paths for openclaw and hermes sessions differ.          Re]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 (reverse) Writing to Hermes workspace does not bleed into OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-H4 Writing to the openclaw workspace must not leak into the hermes workspace]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 The Hermes TCP dashboard forwarder (port 9119) binds on 0.0.0.0.      Thi]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[BT-M1 Verify the forwarder bind address — currently 0.0.0.0 (accepted risk).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Back-compat existing callers that pass no author_idrbac_config keep working.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Both groups store separate content with no cross-contamination.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-A memory must not appear in group-B memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-B must not appear in group-A memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a group must not appear in any user's private DM memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content written to a user DM must not appear in any group memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Finding BT-H1BT-H2BT-H3 SharedMemoryManager must not collapse bot workspaces.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Finding RT-N1RT-N2 TrustManager uses shared in-memory DB keyed by agent_id.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Group workspace content must not leak into any user's DM workspace.]] - rationale - gateway/tests/test_group_isolation.py
- [[Hermes's dashboard binds 127.0.0.1 inside its own container (vendor     hermes-a]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[If the underlying session store raises, the authorized write reports         fai]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Isolated temporary workspace for session manager.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[RT-N1 (reverse) Hermes violation must not demote OpenClaw.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N1 Recording a violation against openclaw MUST NOT change hermes trust.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N2 Bot agent IDs ('openclaw', 'hermes') are separate from user IDs.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 After seeding, hermes trust level is STANDARD (matching lifespan.py).]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[RT-N3 lifespan.py seeds 'hermes' with STANDARD trust.      Verifies the seeding]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session directory path must embed bot_id so filesystem confirms isolation.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject bot_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Session manager must reject user_id with path traversal characters.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestBotIdIsolationInSharedMemory]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestCrossBotTrustPivot]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestGroupMemoryInvisibleFromDM]] - code - gateway/tests/test_group_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[TestHermesDashboardBridgeReachability]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesDashboardForwarderBinding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestHermesTrustSeeding]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestSessionPathSeparation]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[TestUserMemoryWriteACL]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestWriteFailurePath]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[The owner may write into any user's private memory.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[User DM content must not leak into a group the user is NOT a member of.]] - rationale - gateway/tests/test_group_isolation.py
- [[Verifies per-bot session path layout is correctly separated.]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[get_merged_memory_for_user returns group section and private section separately.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py
- [[group_config.py (TeamsConfig)]] - code - gateway/security/group_config.py
- [[rbac()]] - code - gateway/tests/test_group_isolation.py
- [[rbac()_5]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[run-standalone.sh is the actual deploy path for Hermes (docker run, not]] - rationale - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_1]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()_3]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[session_manager()_4]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[session_manager.py (UserSessionManager)]] - code - gateway/security/session_manager.py
- [[shared_memory()]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()_2]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[shared_memory.py (SharedMemoryManager)]] - code - gateway/security/shared_memory.py
- [[smm()]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[teams()_2]] - code - gateway/tests/test_group_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[test_security_regressions_v1_2.py]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[test_shared_memory_write_acl.py]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[tmp_workspace()]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()_1]] - code - gateway/tests/test_security_regressions_v1_2.py
- [[trust_manager()_5]] - code - gateway/tests/test_security_regressions_v1_2.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_26
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Community 61]]
- 18 edges to [[_COMMUNITY_Community 174]]
- 15 edges to [[_COMMUNITY_Community 35]]
- 9 edges to [[_COMMUNITY_Community 81]]
- 9 edges to [[_COMMUNITY_Community 15]]
- 7 edges to [[_COMMUNITY_Community 28]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 1 edge to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 757]]
- 1 edge to [[_COMMUNITY_Community 821]]
- 1 edge to [[_COMMUNITY_Community 778]]

## Top bridge nodes
- [[test_security_regressions_v1_2.py]] - degree 19, connects to 6 communities
- [[test_group_isolation.py]] - degree 19, connects to 5 communities
- [[test_shared_memory_write_acl.py]] - degree 14, connects to 5 communities
- [[TestGroupMemoryNamespaceIsolation]] - degree 13, connects to 5 communities
- [[TestGroupMemoryInvisibleFromDM]] - degree 12, connects to 5 communities