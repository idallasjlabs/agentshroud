---
type: community
members: 31
---

# ContributorManager

**Members:** 31 nodes

## Members
- [[dot-__init__()_145]] - code - gateway/soc/contributors.py
- [[dot-__init__()_146]] - code - gateway/tests/test_soc_contributors.py
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-get_user_role()_3]] - code - gateway/tests/test_soc_contributors.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_prefers_app_wide_progressive_lockdown()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Constraint check paused (owner-initiated) and lockdown_level (auto-escalation)…]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[SCRUM-203 the app-wide instance on app_state.progressive_lockdown wins.]] - rationale - gateway/tests/test_soc_contributors.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[Tests for gatewaysoccontributors.py — ContributorManager record building. No…]] - rationale - gateway/tests/test_soc_contributors.py
- [[_FakeRBAC_2]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted store is…]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContributorManager
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_RBACConfig]]
- 8 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 8 edges to [[_COMMUNITY_socmodels.py]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_LockdownLevel]]

## Top bridge nodes
- [[test_soc_contributors.py]] - degree 10, connects to 4 communities
- [[ContributorManager]] - degree 27, connects to 3 communities
- [[TestLockdownLevelWiring]] - degree 10, connects to 2 communities
- [[TestPausedFieldWiring]] - degree 10, connects to 2 communities
- [[_FakeRBAC_2]] - degree 13, connects to 1 community
