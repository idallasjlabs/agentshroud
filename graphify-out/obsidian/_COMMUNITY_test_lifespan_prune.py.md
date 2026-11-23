---
type: community
members: 19
---

# test_lifespan_prune.py

**Members:** 19 nodes

## Members
- [[Create a fake contributor markdown file for the given uid.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Gateway-level collaborator activity tracker. Logs every non-owner message from…]] - rationale - gateway/security/collaborator_tracker.py
- [[Path_74]] - code
- [[Real-UID markdown files must never be deleted by the prune pass.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Return True when uid looks like a test fixture that should be silently dropped.…]] - rationale - gateway/security/collaborator_tracker.py
- [[Run the same markdown-prune logic as lifespan.py and return pruned count.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Startup prune must remove fixture markdown files from every contributor dir.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Tests for startup markdown contributor-log pruning (Bug B). Verifies that on…]] - rationale - gateway/tests/test_lifespan_prune.py
- [[_is_fixture_uid()]] - code - gateway/security/collaborator_tracker.py
- [[_make_md()]] - code - gateway/tests/test_lifespan_prune.py
- [[_prune_fixture_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[collaborator_tracker.py]] - code - gateway/security/collaborator_tracker.py
- [[parametrize_30]] - code
- [[test_is_fixture_uid_blocks_short_numeric()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_blocks_test_user_prefix()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_passes_real_uids()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_lifespan_prune.py]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_keeps_real_uid_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_walks_all_contributor_dirs()]] - code - gateway/tests/test_lifespan_prune.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_lifespan_prunepy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_dot-record_activity]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]

## Top bridge nodes
- [[_is_fixture_uid()]] - degree 9, connects to 2 communities
- [[collaborator_tracker.py]] - degree 5, connects to 2 communities
- [[test_lifespan_prune.py]] - degree 11, connects to 1 community
- [[_prune_fixture_markdown()]] - degree 6, connects to 1 community
- [[test_prune_keeps_real_uid_markdown()]] - degree 5, connects to 1 community
