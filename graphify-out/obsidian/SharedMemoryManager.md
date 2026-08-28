---
source_file: "gateway/security/shared_memory.py"
type: "code"
community: "Community 62"
location: "L54"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_62
---

# SharedMemoryManager

## Connections
- [[.__init__()_117]] - `method` [EXTRACTED]
- [[._is_authorized_group_writer()]] - `method` [EXTRACTED]
- [[._strip_private_content()]] - `method` [EXTRACTED]
- [[.append_to_group_memory()]] - `method` [EXTRACTED]
- [[.append_to_user_memory()]] - `method` [EXTRACTED]
- [[.contains_private_content()]] - `method` [EXTRACTED]
- [[.get_group_memory()]] - `method` [EXTRACTED]
- [[.get_merged_memory_for_user()]] - `method` [EXTRACTED]
- [[.get_topic_scoped_memory()]] - `method` [EXTRACTED]
- [[.get_user_memory()]] - `method` [EXTRACTED]
- [[GroupAccessDenied]] - `uses` [INFERRED]
- [[GroupWorkspaceManager]] - `uses` [INFERRED]
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - `rationale_for` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[TestAgentRegistryGroupIdentity]] - `uses` [INFERRED]
- [[TestAuthorizationHelper]] - `uses` [INFERRED]
- [[TestBotIdIsolationInSharedMemory]] - `uses` [INFERRED]
- [[TestConfigGate]] - `uses` [INFERRED]
- [[TestCrossBotTrustPivot]] - `uses` [INFERRED]
- [[TestCrossGroupIsolation]] - `uses` [INFERRED]
- [[TestDefensiveGuards]] - `uses` [INFERRED]
- [[TestDmIsolation]] - `uses` [INFERRED]
- [[TestGroupMemoryInvisibleFromDM]] - `uses` [INFERRED]
- [[TestGroupMemoryNamespaceIsolation]] - `uses` [INFERRED]
- [[TestGroupMemoryReadWrite]] - `uses` [INFERRED]
- [[TestGroupMemoryWriteACL]] - `uses` [INFERRED]
- [[TestHermesDashboardBridgeReachability]] - `uses` [INFERRED]
- [[TestHermesDashboardForwarderBinding]] - `uses` [INFERRED]
- [[TestHermesEgressAllowlist]] - `uses` [INFERRED]
- [[TestHermesTrustSeeding]] - `uses` [INFERRED]
- [[TestInboundChokepointWiring]] - `uses` [INFERRED]
- [[TestMembersShareGroupWorkspace]] - `uses` [INFERRED]
- [[TestMergedMemory]] - `uses` [INFERRED]
- [[TestNonMemberDenied]] - `uses` [INFERRED]
- [[TestPrivateContentDetection]] - `uses` [INFERRED]
- [[TestSessionPathSeparation]] - `uses` [INFERRED]
- [[TestTopicScopedMemory]] - `uses` [INFERRED]
- [[TestUserMemoryWriteACL]] - `uses` [INFERRED]
- [[TestUserPrivateMemory]] - `uses` [INFERRED]
- [[TestWriteFailurePath]] - `uses` [INFERRED]
- [[UserSessionManager]] - `uses` [INFERRED]
- [[WorkspaceContext]] - `uses` [INFERRED]
- [[get_group_memory()]] - `calls` [EXTRACTED]
- [[group_workspace.py]] - `imports` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[shared_memory()]] - `calls` [EXTRACTED]
- [[shared_memory()_1]] - `calls` [EXTRACTED]
- [[shared_memory()_2]] - `calls` [EXTRACTED]
- [[shared_memory.py]] - `contains` [EXTRACTED]
- [[smm()]] - `calls` [EXTRACTED]
- [[smm()_1]] - `calls` [EXTRACTED]
- [[test_group_isolation.py]] - `imports` [EXTRACTED]
- [[test_group_workspace_manager.py]] - `imports` [EXTRACTED]
- [[test_security_regressions_v1_2.py]] - `imports` [EXTRACTED]
- [[test_shared_memory.py]] - `imports` [EXTRACTED]
- [[test_shared_memory_write_acl.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_62