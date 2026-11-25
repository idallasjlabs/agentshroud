---
type: community
members: 12
---

# FakeClock

**Members:** 12 nodes

## Members
- [[dot-__call__()_3]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-__init__()_26]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-advance()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_blocks_inside_window_still_escalate()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_decay_off_by_default_blocks_never_age_out()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_level_of_reflects_decay_without_new_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_old_blocks_age_out_when_window_set()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_realert_after_full_decay()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_rejects_non_positive_window()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_suspension_is_sticky_under_decay()]] - code - gateway/tests/test_progressive_lockdown.py
- [[FakeClock]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestDecay]] - code - gateway/tests/test_progressive_lockdown.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FakeClock
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 2 edges to [[_COMMUNITY_test_progressive_lockdown.py]]
- 1 edge to [[_COMMUNITY_LockdownLevel]]

## Top bridge nodes
- [[TestDecay]] - degree 10, connects to 3 communities
- [[FakeClock]] - degree 10, connects to 1 community
- [[dot-test_blocks_inside_window_still_escalate()]] - degree 3, connects to 1 community
- [[dot-test_decay_off_by_default_blocks_never_age_out()]] - degree 3, connects to 1 community
- [[dot-test_level_of_reflects_decay_without_new_blocks()]] - degree 3, connects to 1 community
