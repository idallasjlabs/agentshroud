---
type: community
members: 31
---

# Community 890

**Members:** 31 nodes

## Members
- [[.__init__()_145]] - code - gateway/soc/contributors.py
- [[.__init__()_209]] - code - gateway/tests/test_soc_contributors.py
- [[._build_record()]] - code - gateway/soc/contributors.py
- [[._ensure_rbac()]] - code - gateway/soc/contributors.py
- [[._ensure_teams()]] - code - gateway/soc/contributors.py
- [[._load_paused_ids()]] - code - gateway/soc/contributors.py
- [[.get_contributor()]] - code - gateway/soc/contributors.py
- [[.get_user_role()_3]] - code - gateway/tests/test_soc_contributors.py
- [[.list_contributors()]] - code - gateway/soc/contributors.py
- [[.test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_prefers_app_wide_progressive_lockdown()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[SCRUM-203 the app-wide instance on app_state.progressive_lockdown wins.]] - rationale - gateway/tests/test_soc_contributors.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_890
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_Community 10]]
- 10 edges to [[_COMMUNITY_Community 75]]
- 8 edges to [[_COMMUNITY_Community 8]]
- 6 edges to [[_COMMUNITY_Community 194]]
- 2 edges to [[_COMMUNITY_Community 223]]

## Top bridge nodes
- [[ContributorManager]] - degree 62, connects to 5 communities
- [[_FakeRBAC_1]] - degree 15, connects to 2 communities
- [[TestLockdownLevelWiring]] - degree 10, connects to 2 communities
- [[TestPausedFieldWiring]] - degree 10, connects to 2 communities
- [[test_soc_contributors.py]] - degree 6, connects to 2 communities