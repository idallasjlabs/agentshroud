---
type: community
cohesion: 0.05
members: 53
---

# Module Group 75

**Cohesion:** 0.05 - loosely connected
**Members:** 53 nodes

## Members
- [[.__init__()_93]] - code - gateway/security/shared_memory.py
- [[._strip_private_content()]] - code - gateway/security/shared_memory.py
- [[.append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[.append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[.contains_private_content()]] - code - gateway/security/shared_memory.py
- [[.get_group_memory()]] - code - gateway/security/shared_memory.py
- [[.get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[.get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[.get_user_memory()]] - code - gateway/security/shared_memory.py
- [[.test_active_group_appears_first()]] - code - gateway/tests/test_shared_memory.py
- [[.test_append_to_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_append_to_user_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[.test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[.test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[.test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[.test_get_group_memory_empty_initially()]] - code - gateway/tests/test_shared_memory.py
- [[.test_get_user_memory_returns_string()]] - code - gateway/tests/test_shared_memory.py
- [[.test_multiple_appends_accumulate()]] - code - gateway/tests/test_shared_memory.py
- [[.test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_owner_sees_all_groups()]] - code - gateway/tests/test_shared_memory.py
- [[.test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[.test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_excludes_non_matching_project_scoped_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_includes_local_only_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_topic_scoped_returns_matching_group()]] - code - gateway/tests/test_shared_memory.py
- [[.test_unknown_user_sees_only_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_does_not_see_other_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_memory_isolated_between_users()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_sees_own_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[.test_user_sees_their_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[Append a timestamped entry to the group shared memory file.]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file.]] - rationale - gateway/security/shared_memory.py
- [[Build merged memory context for bot prompt injection.          Includes]] - rationale - gateway/security/shared_memory.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user.]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving         to non-]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return memory from groups whose focus_topics match the query text.          For]] - rationale - gateway/security/shared_memory.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[TestGroupMemoryReadWrite]] - code - gateway/tests/test_shared_memory.py
- [[TestMergedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py
- [[TestTopicScopedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestUserPrivateMemory]] - code - gateway/tests/test_shared_memory.py
- [[rbac()_1]] - code - gateway/tests/test_shared_memory.py
- [[session_mgr()]] - code - gateway/tests/test_shared_memory.py
- [[shared_memory.py]] - code - gateway/security/shared_memory.py
- [[smm()]] - code - gateway/tests/test_shared_memory.py
- [[test_shared_memory.py]] - code - gateway/tests/test_shared_memory.py
- [[tmp_workspace()]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_75
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 9 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 7 edges to [[_COMMUNITY_Group Config & Teams]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 22, connects to 3 communities
- [[test_shared_memory.py]] - degree 13, connects to 3 communities
- [[TestPrivateContentDetection]] - degree 13, connects to 3 communities
- [[TestMergedMemory]] - degree 11, connects to 3 communities
- [[TestGroupMemoryReadWrite]] - degree 8, connects to 3 communities