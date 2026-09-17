---
type: community
cohesion: 0.12
members: 33
---

# Community 226

**Cohesion:** 0.12 - loosely connected
**Members:** 33 nodes

## Members
- [[dot-__init__()_99]] - code - gateway/proxy/telegram_proxy.py
- [[dot-__init__()_100]] - code - gateway/soc/contributors.py
- [[dot-__init__()_101]] - code - gateway/tests/test_soc_contributors.py
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-get_user_role()_2]] - code - gateway/tests/test_soc_contributors.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
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
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[GET users endpoint]] - code - gateway/soc/router.py
- [[Read persisted paused-collaborator IDs from disk.      Owner-initiated manual pa]] - rationale - gateway/security/rbac_config.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[load_paused_collaborator_ids()]] - code - gateway/security/rbac_config.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_226
SORT file.name ASC
```

## Connections to other communities
- 24 edges to [[_COMMUNITY_Community 153]]
- 10 edges to [[_COMMUNITY_Community 58]]
- 9 edges to [[_COMMUNITY_Community 68]]
- 8 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 6 edges to [[_COMMUNITY_SOC Correlation & Router]]
- 1 edge to [[_COMMUNITY_Community 119]]
- 1 edge to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Collaborator Activity & Telegram Proxy]]
- 1 edge to [[_COMMUNITY_Community 388]]

## Top bridge nodes
- [[ContributorManager]] - degree 58, connects to 5 communities
- [[load_paused_collaborator_ids()]] - degree 8, connects to 4 communities
- [[dot-__init__()_99]] - degree 5, connects to 4 communities
- [[_FakeRBAC_1]] - degree 14, connects to 2 communities
- [[TestPausedFieldWiring]] - degree 10, connects to 2 communities