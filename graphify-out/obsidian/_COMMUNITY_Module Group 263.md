---
type: community
cohesion: 0.19
members: 17
---

# Module Group 263

**Cohesion:** 0.19 - loosely connected
**Members:** 17 nodes

## Members
- [[CollaboratorActivityTracker_1]] - code - gateway/tests/test_lifespan_prune.py
- [[Create a fake contributor markdown file for the given uid.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Path_25]] - code - gateway/tests/test_lifespan_prune.py
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
TABLE source_file, type FROM #community/Module_Group_263
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Module Group 140]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]

## Top bridge nodes
- [[_is_fixture_uid()]] - degree 9, connects to 2 communities
- [[test_lifespan_prune.py]] - degree 9, connects to 1 community
- [[test_prune_keeps_real_uid_markdown()]] - degree 6, connects to 1 community
- [[test_prune_walks_all_contributor_dirs()]] - degree 6, connects to 1 community
- [[CollaboratorActivityTracker_1]] - degree 4, connects to 1 community
