---
type: community
members: 17
---

# test_collaborator_tracker.py (4)

**Members:** 17 nodes

## Members
- [[CollaboratorActivityTracker_1]] - code - gateway/tests/test_lifespan_prune.py
- [[Create a fake contributor markdown file for the given uid.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Path_48]] - code - gateway/tests/test_lifespan_prune.py
- [[Real-UID markdown files must never be deleted by the prune pass.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Return True when uid looks like a test fixture that should be silently dropped.]] - rationale - gateway/security/collaborator_tracker.py
- [[Run the same markdown-prune logic as lifespan.py and return pruned count.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Startup prune must remove fixture markdown files from every contributor dir.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[_is_fixture_uid()]] - code - gateway/security/collaborator_tracker.py
- [[_make_md()]] - code - gateway/tests/test_lifespan_prune.py
- [[_prune_fixture_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[collaborator_tracker.py]] - code - gateway/security/collaborator_tracker.py
- [[test_is_fixture_uid_blocks_short_numeric()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_blocks_test_user_prefix()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_passes_real_uids()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_lifespan_prune.py]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_keeps_real_uid_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_walks_all_contributor_dirs()]] - code - gateway/tests/test_lifespan_prune.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_trackerpy_4
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_lifespan()]]

## Top bridge nodes
- [[test_lifespan_prune.py]] - degree 10, connects to 2 communities
- [[_is_fixture_uid()]] - degree 8, connects to 1 community
- [[_prune_fixture_markdown()]] - degree 7, connects to 1 community
- [[test_prune_keeps_real_uid_markdown()]] - degree 6, connects to 1 community
- [[test_prune_walks_all_contributor_dirs()]] - degree 6, connects to 1 community
