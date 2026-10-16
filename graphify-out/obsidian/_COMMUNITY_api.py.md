---
type: community
cohesion: 0.03
members: 88
---

# api.py

**Cohesion:** 0.03 - loosely connected
**Members:** 88 nodes

## Members
- [[dot-__init__()_156]] - code - gateway/web/api.py
- [[Aggregate security report.]] - rationale - gateway/web/api.py
- [[Check for AgentShroud updates from GitHub.]] - rationale - gateway/web/api.py
- [[Check for OpenClaw updates (backward-compat alias for updatesbotopenclaw).]] - rationale - gateway/web/api.py
- [[Check for updates for the named bot container.]] - rationale - gateway/web/api.py
- [[Compute valid service names from config + sidecars at call-time. Uses     each b]] - rationale - gateway/web/api.py
- [[ConfigUpdate]] - code - gateway/web/api.py
- [[Create a short-lived WebSocket-only token for management endpoints.]] - rationale - gateway/web/api.py
- [[Emergency kill switch freeze, shutdown, or disconnect.]] - rationale - gateway/web/api.py
- [[Export current configuration.]] - rationale - gateway/web/api.py
- [[Full system status including all services and runtime info.]] - rationale - gateway/web/api.py
- [[Get current configuration.]] - rationale - gateway/web/api.py
- [[Get the active container engine.]] - rationale - gateway/web/api.py
- [[Import configuration from uploaded data.]] - rationale - gateway/web/api.py
- [[Path_43]] - code - gateway/web/api.py
- [[Pull latest AgentShroud, test, rebuild, restart. Auto-rollback on failure.]] - rationale - gateway/web/api.py
- [[Raised when SkillGuard blocks a dangerous skill tree before deploy.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings`` and sync skillsagentsMCP into both bot configs.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings``, scan for supply-chain risk, deploy to both bots.]] - rationale - gateway/web/api.py
- [[Rebuild containers with latest images.]] - rationale - gateway/web/api.py
- [[Resolve the Dockerfile for the default bot from gateway config.]] - rationale - gateway/web/api.py
- [[Resolve the source (``~.llm_settings``) and bot-config destinations.      Extr]] - rationale - gateway/web/api.py
- [[Restart a specific service container.]] - rationale - gateway/web/api.py
- [[Retrieve container logs with optional filtering.]] - rationale - gateway/web/api.py
- [[Return a comparison dict {feature_name {runtime supported}}.]] - rationale - gateway/runtime/security.py
- [[Return an IntelReportStore pointed at the configured data directory.]] - rationale - gateway/web/api.py
- [[Return real container names for all configured bots (e.g.     'agentshroud-open]] - rationale - gateway/web/api.py
- [[Return recent competitive-intelligence reports in reverse-chronological order.]] - rationale - gateway/web/api.py
- [[Return the current AGENTSHROUD_MODE.]] - rationale - gateway/web/api.py
- [[Return the latest validated competitive-intelligence report.      Auth-gated (ow]] - rationale - gateway/web/api.py
- [[Return update history from audit log.]] - rationale - gateway/web/api.py
- [[Return warning messages for missing security features.]] - rationale - gateway/runtime/security.py
- [[Revert to previous git commit and rebuild.]] - rationale - gateway/web/api.py
- [[Rollback OpenClaw (backward-compat alias for updatesbotopenclawrollback).]] - rationale - gateway/web/api.py
- [[Rollback a named bot container to the previous image tag.]] - rationale - gateway/web/api.py
- [[ServiceAction]] - code - gateway/web/api.py
- [[SkillGuardBlocked]] - code - gateway/web/api.py
- [[Start a specific service container.]] - rationale - gateway/web/api.py
- [[Stop a specific service container.]] - rationale - gateway/web/api.py
- [[Update configuration (writes YAML and optionally restarts).]] - rationale - gateway/web/api.py
- [[Upgrade OpenClaw (backward-compat alias for updatesbotopenclawupgrade).]] - rationale - gateway/web/api.py
- [[Upgrade a named bot container.]] - rationale - gateway/web/api.py
- [[Validate a management WebSocket token (single-use, time-limited).]] - rationale - gateway/web/api.py
- [[Validate service name against allowlist to prevent injection.]] - rationale - gateway/web/api.py
- [[WebSocket_3]] - code - gateway/web/api.py
- [[WebSocket endpoint for real-time log streaming. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[WebSocket for real-time update progress. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[_bot_service_names()]] - code - gateway/web/api.py
- [[_create_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_get_engine()]] - code - gateway/web/api.py
- [[_intel_store()]] - code - gateway/web/api.py
- [[_skills_reload_impl()]] - code - gateway/web/api.py
- [[_skills_reload_paths()]] - code - gateway/web/api.py
- [[_valid_services()]] - code - gateway/web/api.py
- [[_validate_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_validate_service_name()]] - code - gateway/web/api.py
- [[api.py]] - code - gateway/web/api.py
- [[check_agentshroud_updates()]] - code - gateway/web/api.py
- [[check_bot_updates()]] - code - gateway/web/api.py
- [[check_openclaw_updates()]] - code - gateway/web/api.py
- [[export_config()]] - code - gateway/web/api.py
- [[get_competitive_intel()]] - code - gateway/web/api.py
- [[get_competitive_intel_history()]] - code - gateway/web/api.py
- [[get_config()_1]] - code - gateway/web/api.py
- [[get_logs()]] - code - gateway/web/api.py
- [[get_mode()]] - code - gateway/web/api.py
- [[get_security_comparison()]] - code - gateway/runtime/security.py
- [[get_status()]] - code - gateway/web/api.py
- [[import_config()]] - code - gateway/web/api.py
- [[killswitch()_1]] - code - gateway/web/api.py
- [[rebuild()]] - code - gateway/web/api.py
- [[restart_service()_1]] - code - gateway/web/api.py
- [[rollback_agentshroud()]] - code - gateway/web/api.py
- [[rollback_bot()]] - code - gateway/web/api.py
- [[rollback_openclaw()]] - code - gateway/web/api.py
- [[security_report()]] - code - gateway/web/api.py
- [[skills_reload()]] - code - gateway/web/api.py
- [[start_service()_1]] - code - gateway/web/api.py
- [[stop_service()_1]] - code - gateway/web/api.py
- [[update_config()]] - code - gateway/web/api.py
- [[update_history()]] - code - gateway/web/api.py
- [[upgrade_agentshroud()]] - code - gateway/web/api.py
- [[upgrade_bot()_1]] - code - gateway/web/api.py
- [[upgrade_openclaw()]] - code - gateway/web/api.py
- [[warn_missing_features()]] - code - gateway/runtime/security.py
- [[ws_logs()]] - code - gateway/web/api.py
- [[ws_updates()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_api.py_1]]
- 11 edges to [[_COMMUNITY_ModeRequest]]
- 10 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 8 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 5 edges to [[_COMMUNITY_RuntimeConfig]]
- 4 edges to [[_COMMUNITY_test_runtime_engines.py]]
- 4 edges to [[_COMMUNITY_TestSecurityFeatures]]
- 4 edges to [[_COMMUNITY_Path]]
- 3 edges to [[_COMMUNITY_get_engine]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_KeyRotationManager]]
- 2 edges to [[_COMMUNITY_SkillGuard_1]]
- 2 edges to [[_COMMUNITY_upgrade]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_management.py]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_FetchOutcome]]
- 1 edge to [[_COMMUNITY_installer.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]

## Top bridge nodes
- [[api.py]] - degree 75, connects to 18 communities
- [[Path_43]] - degree 8, connects to 4 communities
- [[warn_missing_features()]] - degree 9, connects to 3 communities
- [[SkillGuardBlocked]] - degree 8, connects to 3 communities
- [[get_security_comparison()]] - degree 7, connects to 3 communities
