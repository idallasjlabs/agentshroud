---
type: community
cohesion: 0.15
members: 35
---

# test_skill_guard.py

**Cohesion:** 0.15 - loosely connected
**Members:** 35 nodes

## Members
- [[._run_sync()]] - code - gateway/tests/test_skill_guard.py
- [[.client()_2]] - code - gateway/tests/test_skill_guard.py
- [[.test_cli_allows_clean_tree_zero()]] - code - gateway/tests/test_skill_guard.py
- [[.test_cli_blocks_dangerous_tree_nonzero()]] - code - gateway/tests/test_skill_guard.py
- [[.test_cli_fails_closed_on_unreadable_file()]] - code - gateway/tests/test_skill_guard.py
- [[.test_cli_missing_source_nonzero()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_clean_tree_returns_ok()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_dangerous_tree_returns_blocked()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_empty_source_returns_usage()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_flag_only_tree_returns_ok()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_missing_source_returns_usage()]] - code - gateway/tests/test_skill_guard.py
- [[.test_main_unreadable_file_fails_closed()]] - code - gateway/tests/test_skill_guard.py
- [[.test_reload_allows_clean_skill()]] - code - gateway/tests/test_skill_guard.py
- [[.test_reload_blocks_dangerous_skill()]] - code - gateway/tests/test_skill_guard.py
- [[.test_reload_fails_closed_on_unreadable_file()]] - code - gateway/tests/test_skill_guard.py
- [[.test_sync_aborts_on_dangerous_tree()]] - code - gateway/tests/test_skill_guard.py
- [[.test_sync_allows_clean_tree()]] - code - gateway/tests/test_skill_guard.py
- [[.test_sync_dry_run_does_not_write_but_still_scans()]] - code - gateway/tests/test_skill_guard.py
- [[CompletedProcess_4]] - code - gateway/tests/test_skill_guard.py
- [[Exercise ``gateway.skills.scan.main`` directly for exit-code coverage.]] - rationale - gateway/tests/test_skill_guard.py
- [[Ordered severity ladder (``IntEnum`` so comparisons work).]] - rationale - gateway/security/skill_guard.py
- [[Path_22]] - code - gateway/tests/test_skill_guard.py
- [[Raised when SkillGuard is handed content it cannot scan.]] - rationale - gateway/security/skill_guard.py
- [[Severity]] - code - gateway/security/skill_guard.py
- [[SkillScanError]] - code - gateway/security/skill_guard.py
- [[TestClient_1]] - code - gateway/tests/test_skill_guard.py
- [[TestReloadIntegration]] - code - gateway/tests/test_skill_guard.py
- [[TestScanEntrypoint]] - code - gateway/tests/test_skill_guard.py
- [[TestScanEntrypointInProcess]] - code - gateway/tests/test_skill_guard.py
- [[TestSyncScriptPreflight]] - code - gateway/tests/test_skill_guard.py
- [[The parallel bash sync path must invoke SkillGuard before copying.]] - rationale - gateway/tests/test_skill_guard.py
- [[_run_scan_cli()]] - code - gateway/tests/test_skill_guard.py
- [[_write_tree()_1]] - code - gateway/tests/test_skill_guard.py
- [[gatewaysecurityskill_guard.py (SkillGuard)]] - code - gateway/security/skill_guard.py
- [[test_skill_guard.py]] - code - gateway/tests/test_skill_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_skill_guardpy
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_SkillGuard]]
- 33 edges to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_sync-llm-settings.sh]]
- 1 edge to [[_COMMUNITY_FetchOutcome]]
- 1 edge to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[test_skill_guard.py]] - degree 28, connects to 5 communities
- [[SkillScanError]] - degree 24, connects to 3 communities
- [[Severity]] - degree 24, connects to 2 communities
- [[Path_22]] - degree 24, connects to 1 community
- [[TestScanEntrypointInProcess]] - degree 13, connects to 1 community