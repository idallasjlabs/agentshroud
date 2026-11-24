---
type: community
members: 42
---

# SharedMemoryManager

**Members:** 42 nodes

## Members
- [[dot-__init__()_96]] - code - gateway/security/shared_memory.py
- [[dot-_is_authorized_group_writer()]] - code - gateway/security/shared_memory.py
- [[dot-_is_owner()_1]] - code - gateway/security/group_workspace.py
- [[dot-_strip_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-append_to_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-append_to_user_memory()]] - code - gateway/security/shared_memory.py
- [[dot-contains_private_content()]] - code - gateway/security/shared_memory.py
- [[dot-get_group_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_merged_memory_for_user()]] - code - gateway/security/shared_memory.py
- [[dot-get_topic_scoped_memory()]] - code - gateway/security/shared_memory.py
- [[dot-get_user_groups_by_id()]] - code - gateway/security/rbac_config.py
- [[dot-get_user_memory()]] - code - gateway/security/shared_memory.py
- [[dot-is_owner()_3]] - code - gateway/security/rbac_config.py
- [[dot-test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_empty_author_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_member_authorized()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_missing_rbac_is_denied()]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[dot-test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[An emptyNone author is never authorized.]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Append a timestamped entry to the group shared memory file. Authorization…]] - rationale - gateway/security/shared_memory.py
- [[Append content to user's private memory file. Authorization (RT-5, WS-E HIGH)…]] - rationale - gateway/security/shared_memory.py
- [[Build merged memory context for bot prompt injection. Includes 1. User's own…]] - rationale - gateway/security/shared_memory.py
- [[Check if user is the owner (any platform).]] - rationale - gateway/security/rbac_config.py
- [[High-level shared-memory API wrapping UserSessionManager storage.]] - rationale - gateway/security/shared_memory.py
- [[No RBAC principal → cannot authorize → deny (fail-closed).]] - rationale - gateway/tests/test_shared_memory_write_acl.py
- [[Read raw group shared memory. Returns empty string if not yet created.]] - rationale - gateway/security/shared_memory.py
- [[Read raw private memory for a user. Args user_id The user whose memory to…]] - rationale - gateway/security/shared_memory.py
- [[Remove private-looking content from shared memory before serving to non-owner…]] - rationale - gateway/security/shared_memory.py
- [[Return True if ``author_id`` may WRITE to ``group_id`` shared memory. RT-5…]] - rationale - gateway/security/shared_memory.py
- [[Return True if text contains patterns matching privatesensitive content.]] - rationale - gateway/security/shared_memory.py
- [[Return True if user_id is the system owner (oversight override).]] - rationale - gateway/security/group_workspace.py
- [[Return member IDs of a group, or empty list if no teams config.]] - rationale - gateway/security/rbac_config.py
- [[Return memory from groups whose focus_topics match the query text. For…]] - rationale - gateway/security/shared_memory.py
- [[SharedMemoryManager]] - code - gateway/security/shared_memory.py
- [[TestAuthorizationHelper]] - code - gateway/tests/test_shared_memory_write_acl.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SharedMemoryManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_GroupWorkspaceManager]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_test_shared_memory.py]]
- 3 edges to [[_COMMUNITY_TeamsConfig]]
- 2 edges to [[_COMMUNITY_test_group_isolation.py]]
- 2 edges to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[SharedMemoryManager]] - degree 27, connects to 7 communities
- [[TestPrivateContentDetection]] - degree 10, connects to 1 community
- [[dot-is_owner()_3]] - degree 7, connects to 1 community
- [[TestAuthorizationHelper]] - degree 5, connects to 1 community
- [[dot-_is_owner()_1]] - degree 4, connects to 1 community
