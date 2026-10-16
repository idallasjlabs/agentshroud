---
type: community
cohesion: 0.04
members: 78
---

# api.py

**Cohesion:** 0.04 - loosely connected
**Members:** 78 nodes

## Members
- [[dot-test_resolves_hermes_to_the_real_renamed_container()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_resolves_openclaw_to_the_convention_default()]] - code - gateway/tests/test_web_api_coverage.py
- [[dot-test_unknown_bot_id_falls_back_to_the_naive_guess()]] - code - gateway/tests/test_web_api_coverage.py
- [[Check for AgentShroud updates from GitHub.]] - rationale - gateway/web/api.py
- [[Check for OpenClaw updates (backward-compat alias for updatesbotopenclaw).]] - rationale - gateway/web/api.py
- [[Check for updates for the named bot container.]] - rationale - gateway/web/api.py
- [[Compute valid service names from config + sidecars at call-time. Uses     each b]] - rationale - gateway/web/api.py
- [[ConfigUpdate]] - code - gateway/web/api.py
- [[Create a short-lived WebSocket-only token for management endpoints.]] - rationale - gateway/web/api.py
- [[Emergency kill switch freeze, shutdown, or disconnect.]] - rationale - gateway/web/api.py
- [[Export current configuration.]] - rationale - gateway/web/api.py
- [[Get current configuration.]] - rationale - gateway/web/api.py
- [[Get the active container engine.]] - rationale - gateway/web/api.py
- [[Import configuration from uploaded data.]] - rationale - gateway/web/api.py
- [[Path_38]] - code - gateway/web/api.py
- [[Pull latest AgentShroud, test, rebuild, restart. Auto-rollback on failure.]] - rationale - gateway/web/api.py
- [[Rebuild containers with latest images.]] - rationale - gateway/web/api.py
- [[Resolve the Dockerfile for the default bot from gateway config.]] - rationale - gateway/web/api.py
- [[Resolve the real Docker container name for a given bot_id — from     BotConfig.r]] - rationale - gateway/web/api.py
- [[Resolve the source (``~.llm_settings``) and bot-config destinations.      Extr]] - rationale - gateway/web/api.py
- [[Restart a specific service container.]] - rationale - gateway/web/api.py
- [[Retrieve container logs with optional filtering.]] - rationale - gateway/web/api.py
- [[Return an IntelReportStore pointed at the configured data directory.]] - rationale - gateway/web/api.py
- [[Return recent competitive-intelligence reports in reverse-chronological order.]] - rationale - gateway/web/api.py
- [[Return the current AGENTSHROUD_MODE.]] - rationale - gateway/web/api.py
- [[Return the latest validated competitive-intelligence report.      Auth-gated (ow]] - rationale - gateway/web/api.py
- [[Return update history from audit log.]] - rationale - gateway/web/api.py
- [[Revert to previous git commit and rebuild.]] - rationale - gateway/web/api.py
- [[Rollback OpenClaw (backward-compat alias for updatesbotopenclawrollback).]] - rationale - gateway/web/api.py
- [[Rollback a named bot container to the previous image tag.]] - rationale - gateway/web/api.py
- [[Serve the main dashboard page.]] - rationale - gateway/web/management.py
- [[Start a specific service container.]] - rationale - gateway/web/api.py
- [[Stop a specific service container.]] - rationale - gateway/web/api.py
- [[TestResolveBotContainer]] - code - gateway/tests/test_web_api_coverage.py
- [[Update configuration (writes YAML and optionally restarts).]] - rationale - gateway/web/api.py
- [[Upgrade OpenClaw (backward-compat alias for updatesbotopenclawupgrade).]] - rationale - gateway/web/api.py
- [[Upgrade a named bot container.]] - rationale - gateway/web/api.py
- [[Validate a management WebSocket token (single-use, time-limited).]] - rationale - gateway/web/api.py
- [[Validate service name against allowlist to prevent injection.]] - rationale - gateway/web/api.py
- [[WebSocket endpoint for real-time log streaming. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[WebSocket for real-time update progress. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[_create_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_get_engine()]] - code - gateway/web/api.py
- [[_intel_store()]] - code - gateway/web/api.py
- [[_resolve_bot_container must use BotConfig.resolved_container_name, not     a har]] - rationale - gateway/tests/test_web_api_coverage.py
- [[_resolve_bot_container()]] - code - gateway/web/api.py
- [[_skills_reload_paths()]] - code - gateway/web/api.py
- [[_valid_services()]] - code - gateway/web/api.py
- [[_validate_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_validate_service_name()]] - code - gateway/web/api.py
- [[api.py_2]] - code - gateway/web/api.py
- [[check_agentshroud_updates()]] - code - gateway/web/api.py
- [[check_bot_updates()]] - code - gateway/web/api.py
- [[check_openclaw_updates()]] - code - gateway/web/api.py
- [[dashboard_main()]] - code - gateway/web/management.py
- [[export_config()]] - code - gateway/web/api.py
- [[get_competitive_intel()]] - code - gateway/web/api.py
- [[get_competitive_intel_history()]] - code - gateway/web/api.py
- [[get_config()]] - code - gateway/web/api.py
- [[get_logs()]] - code - gateway/web/api.py
- [[get_mode()]] - code - gateway/web/api.py
- [[import_config()]] - code - gateway/web/api.py
- [[killswitch()]] - code - gateway/web/api.py
- [[rebuild()]] - code - gateway/web/api.py
- [[restart_service()_1]] - code - gateway/web/api.py
- [[rollback_agentshroud()]] - code - gateway/web/api.py
- [[rollback_bot()]] - code - gateway/web/api.py
- [[rollback_openclaw()]] - code - gateway/web/api.py
- [[start_service()_1]] - code - gateway/web/api.py
- [[stop_service()_1]] - code - gateway/web/api.py
- [[update_config()]] - code - gateway/web/api.py
- [[update_history()]] - code - gateway/web/api.py
- [[upgrade_agentshroud()]] - code - gateway/web/api.py
- [[upgrade_bot()_1]] - code - gateway/web/api.py
- [[upgrade_openclaw()]] - code - gateway/web/api.py
- [[ws_logs()]] - code - gateway/web/api.py
- [[ws_updates()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_api.py_1]]
- 13 edges to [[_COMMUNITY_ModeRequest]]
- 11 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 8 edges to [[_COMMUNITY_get_engine]]
- 5 edges to [[_COMMUNITY_SkillGuard_1]]
- 5 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection_1]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 2 edges to [[_COMMUNITY_create_auth_dependency]]
- 2 edges to [[_COMMUNITY_upgrade]]
- 1 edge to [[_COMMUNITY_FetchOutcome]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_TestSecurityFeatures]]
- 1 edge to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_installer.py]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]
- 1 edge to [[_COMMUNITY_ReportStore]]

## Top bridge nodes
- [[api.py_2]] - degree 75, connects to 18 communities
- [[Path_38]] - degree 8, connects to 3 communities
- [[ConfigUpdate]] - degree 7, connects to 3 communities
- [[_intel_store()]] - degree 7, connects to 3 communities
- [[_resolve_bot_container()]] - degree 9, connects to 2 communities
