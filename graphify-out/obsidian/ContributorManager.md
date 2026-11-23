---
source_file: "gateway/soc/contributors.py"
type: "code"
community: "ContributorManager"
location: "L24"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ContributorManager
---

# ContributorManager

## Connections
- [[dot-__init__()_158]] - `method` [EXTRACTED]
- [[dot-_build_record()]] - `method` [EXTRACTED]
- [[dot-_ensure_rbac()]] - `method` [EXTRACTED]
- [[dot-_ensure_teams()]] - `method` [EXTRACTED]
- [[dot-_load_paused_ids()]] - `method` [EXTRACTED]
- [[dot-get_contributor()]] - `method` [EXTRACTED]
- [[dot-list_contributors()]] - `method` [EXTRACTED]
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_prefers_app_wide_progressive_lockdown()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_real_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_suspended_level()]] - `calls` [EXTRACTED]
- [[dot-test_list_contributors_populates_paused_per_user()]] - `calls` [EXTRACTED]
- [[dot-test_non_paused_user_reports_paused_false()]] - `calls` [EXTRACTED]
- [[dot-test_paused_is_independent_of_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_paused_user_reports_paused_true()]] - `calls` [EXTRACTED]
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - `rationale_for` [EXTRACTED]
- [[ContributorRecord]] - `uses` [INFERRED]
- [[Platform]] - `uses` [INFERRED]
- [[RBACConfig]] - `uses` [INFERRED]
- [[TestLockdownLevelWiring]] - `uses` [INFERRED]
- [[TestPausedFieldWiring]] - `uses` [INFERRED]
- [[contributors.py]] - `contains` [EXTRACTED]
- [[get_user()]] - `uses` [INFERRED]
- [[list_users()]] - `uses` [INFERRED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_soc_contributors.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ContributorManager
