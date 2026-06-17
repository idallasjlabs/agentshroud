---
type: community
cohesion: 0.05
members: 76
---

# Version Routes & Manager Tools

**Cohesion:** 0.05 - loosely connected
**Members:** 76 nodes

## Members
- [[.test_after_operations()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_after_upgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_blocked_on_invalid()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_blocked_on_invalid_version()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_dry_run()_1]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_dry_run()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_empty_history()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_has_timestamp()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_invalid_version_format()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_masks_bearer()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_masks_password()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_masks_token()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_no_history()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_no_history_unknown()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_no_mask_short_values()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_no_previous_version()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_plain_text_unchanged()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_returns_versions()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_sequential_upgrades()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_successful_downgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_successful_rollback()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_successful_upgrade()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_valid_version()]] - code - gateway/tests/test_agentshroud_manager.py
- [[.test_with_env_var()]] - code - gateway/tests/test_agentshroud_manager.py
- [[Any_8]] - code - gateway/ingest_api/version_routes.py
- [[Any_66]] - code - gateway/tools/agentshroud_manager.py
- [[Check the currently installed OpenClaw version.]] - rationale - gateway/tools/agentshroud_manager.py
- [[Connection_1]] - code - gateway/tools/agentshroud_manager.py
- [[Create a temporary database for testing.]] - rationale - gateway/tests/test_agentshroud_manager.py
- [[Downgrade OpenClaw to a previous version.      Requires security review (risk of]] - rationale - gateway/tools/agentshroud_manager.py
- [[Downgrade to a previous version. Requires approval_id unless dry_run.]] - rationale - gateway/ingest_api/version_routes.py
- [[Get SQLite connection for version history.]] - rationale - gateway/tools/agentshroud_manager.py
- [[Get the currently installed OpenClaw version.]] - rationale - gateway/ingest_api/version_routes.py
- [[Get version change history.]] - rationale - gateway/ingest_api/version_routes.py
- [[List all version history entries.]] - rationale - gateway/tools/agentshroud_manager.py
- [[List available OpenClaw versions (from git tags or known versions).]] - rationale - gateway/tools/agentshroud_manager.py
- [[List available OpenClaw versions.]] - rationale - gateway/ingest_api/version_routes.py
- [[Mask sensitive credentials in text output.]] - rationale - gateway/tools/agentshroud_manager.py
- [[Perform a security review before version change.      Checks     - Known CVEs f]] - rationale - gateway/tools/agentshroud_manager.py
- [[Perform security review for a target version (no approval needed).]] - rationale - gateway/ingest_api/version_routes.py
- [[Request for rollback operation.]] - rationale - gateway/ingest_api/version_routes.py
- [[Request for version change operations.]] - rationale - gateway/ingest_api/version_routes.py
- [[Rollback to the previous version.]] - rationale - gateway/tools/agentshroud_manager.py
- [[Rollback to the previous version. Requires approval_id.]] - rationale - gateway/ingest_api/version_routes.py
- [[RollbackRequest]] - code - gateway/ingest_api/version_routes.py
- [[TestCheckCurrentVersion]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestDowngrade]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestListAvailableVersions]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestListVersions]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestMaskCredentials]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestRollback]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestSecurityReview]] - code - gateway/tests/test_agentshroud_manager.py
- [[TestUpgrade]] - code - gateway/tests/test_agentshroud_manager.py
- [[Upgrade OpenClaw to a target version.      Requires a prior security review and]] - rationale - gateway/tools/agentshroud_manager.py
- [[Upgrade to a target version. Requires approval_id unless dry_run.]] - rationale - gateway/ingest_api/version_routes.py
- [[VersionRequest]] - code - gateway/ingest_api/version_routes.py
- [[_get_db()]] - code - gateway/tools/agentshroud_manager.py
- [[agentshroud_manager.py]] - code - gateway/tools/agentshroud_manager.py
- [[check_current_version()]] - code - gateway/tools/agentshroud_manager.py
- [[downgrade()]] - code - gateway/tools/agentshroud_manager.py
- [[downgrade_version()]] - code - gateway/ingest_api/version_routes.py
- [[get_available_versions()]] - code - gateway/ingest_api/version_routes.py
- [[get_current_version()]] - code - gateway/ingest_api/version_routes.py
- [[get_version_history()]] - code - gateway/ingest_api/version_routes.py
- [[list_available_versions()]] - code - gateway/tools/agentshroud_manager.py
- [[list_versions()]] - code - gateway/tools/agentshroud_manager.py
- [[mask_credentials()]] - code - gateway/tools/agentshroud_manager.py
- [[review_version()]] - code - gateway/ingest_api/version_routes.py
- [[rollback()]] - code - gateway/tools/agentshroud_manager.py
- [[rollback_version()]] - code - gateway/ingest_api/version_routes.py
- [[security_review()]] - code - gateway/tools/agentshroud_manager.py
- [[test_agentshroud_manager.py]] - code - gateway/tests/test_agentshroud_manager.py
- [[tmp_db()]] - code - gateway/tests/test_agentshroud_manager.py
- [[upgrade()]] - code - gateway/tools/agentshroud_manager.py
- [[upgrade_version()]] - code - gateway/ingest_api/version_routes.py
- [[version_routes.py]] - code - gateway/ingest_api/version_routes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Version_Routes__Manager_Tools
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Module Group 83]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[version_routes.py]] - degree 19, connects to 1 community
- [[VersionRequest]] - degree 6, connects to 1 community
- [[RollbackRequest]] - degree 4, connects to 1 community