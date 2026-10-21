---
type: community
members: 19
---

# _FakeRBAC (2)

**Members:** 19 nodes

## Members
- [[dot-__init__()_165]] - code - gateway/tests/test_soc_contributors.py
- [[dot-get_user_role()_2]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[_FakeRBAC]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC_2
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_socrouter.py]]
- 8 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 4 edges to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[_FakeRBAC]] - degree 14, connects to 3 communities
- [[TestPausedFieldWiring]] - degree 10, connects to 3 communities
- [[TestLockdownLevelWiring]] - degree 9, connects to 3 communities
- [[test_soc_contributors.py]] - degree 6, connects to 3 communities
- [[dot-test_paused_is_independent_of_lockdown_level()]] - degree 5, connects to 2 communities
