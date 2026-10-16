---
type: community
cohesion: 0.06
members: 32
---

# test_shared_memory.py

**Cohesion:** 0.06 - loosely connected
**Members:** 32 nodes

## Members
- [[dot-test_active_group_appears_first()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_append_to_user_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_clean_text_not_flagged()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_collaborator_gets_filtered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_api_key_pattern()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_bearer_token()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_detects_private_section_header()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_get_group_memory_empty_initially()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_get_user_memory_returns_string()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_multiple_appends_accumulate()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_gets_unfiltered_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_owner_sees_all_groups()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_content_redacts_api_key()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_strip_private_section()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_excludes_non_matching_project_scoped_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_includes_local_only_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_topic_scoped_returns_matching_group()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_unknown_user_sees_only_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_does_not_see_other_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_memory_isolated_between_users()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_own_private_memory()]] - code - gateway/tests/test_shared_memory.py
- [[dot-test_user_sees_their_group_memory()]] - code - gateway/tests/test_shared_memory.py
- [[TestGroupMemoryReadWrite]] - code - gateway/tests/test_shared_memory.py
- [[TestMergedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestPrivateContentDetection]] - code - gateway/tests/test_shared_memory.py
- [[TestTopicScopedMemory]] - code - gateway/tests/test_shared_memory.py
- [[TestUserPrivateMemory]] - code - gateway/tests/test_shared_memory.py
- [[session_mgr()]] - code - gateway/tests/test_shared_memory.py
- [[smm()_1]] - code - gateway/tests/test_shared_memory.py
- [[test_shared_memory.py]] - code - gateway/tests/test_shared_memory.py
- [[tmp_workspace()_2]] - code - gateway/tests/test_shared_memory.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_shared_memorypy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_RBACConfig]]
- 7 edges to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[test_shared_memory.py]] - degree 13, connects to 2 communities
- [[TestPrivateContentDetection]] - degree 13, connects to 2 communities
- [[TestMergedMemory]] - degree 11, connects to 2 communities
- [[TestGroupMemoryReadWrite]] - degree 8, connects to 2 communities
- [[TestTopicScopedMemory]] - degree 8, connects to 2 communities
