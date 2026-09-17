---
type: community
cohesion: 0.03
members: 104
---

# Runtime Security Comparison & Intel Report

**Cohesion:** 0.03 - loosely connected
**Members:** 104 nodes

## Members
- [[dot-__init__()_128]] - code - gateway/security/intel_report.py
- [[dot-__init__()_129]] - code - gateway/web/api.py
- [[dot-_load_latest_file()]] - code - gateway/security/intel_report.py
- [[dot-load_all()_1]] - code - gateway/security/intel_report.py
- [[dot-save()_1]] - code - gateway/security/intel_report.py
- [[dot-verify_chain()_2]] - code - gateway/security/intel_report.py
- [[A draft competitive-intel report submitted for citation verification.]] - rationale - gateway/web/api.py
- [[Aggregate security report.]] - rationale - gateway/web/api.py
- [[Build a CitationVerifier wired to the production (httpx) fetcher.      Isolated]] - rationale - gateway/web/api.py
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
- [[IntelDraftEntry]] - code - gateway/web/api.py
- [[IntelDraftRequest]] - code - gateway/web/api.py
- [[IntelReportStore_1]] - code - gateway/security/intel_report.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[One unverified competitor claim + its candidate source URLs.]] - rationale - gateway/web/api.py
- [[Path_33]] - code - gateway/security/intel_report.py
- [[Path_34]] - code - gateway/web/api.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Persistent store for competitive intelligence reports.      Each report is saved]] - rationale - gateway/security/intel_report.py
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
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py
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
- [[Validate a management WebSocket token (single-use, time-limited).]] - rationale - gateway/web/api.py
- [[Validate service name against allowlist to prevent injection.]] - rationale - gateway/web/api.py
- [[Verify and persist a draft competitive-intel report (SCRUM-75).      Each draft]] - rationale - gateway/web/api.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[WebSocket_4]] - code - gateway/web/api.py
- [[WebSocket endpoint for real-time log streaming. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[WebSocket for real-time update progress. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[_bot_service_names()]] - code - gateway/web/api.py
- [[_create_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_get_engine()]] - code - gateway/web/api.py
- [[_intel_store()]] - code - gateway/web/api.py
- [[_intel_verifier()]] - code - gateway/web/api.py
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
- [[get_config()]] - code - gateway/web/api.py
- [[get_logs()]] - code - gateway/web/api.py
- [[get_mode()]] - code - gateway/web/api.py
- [[get_security_comparison()]] - code - gateway/runtime/security.py
- [[get_status()]] - code - gateway/web/api.py
- [[import_config()]] - code - gateway/web/api.py
- [[killswitch()]] - code - gateway/web/api.py
- [[rebuild()]] - code - gateway/web/api.py
- [[restart_service()_1]] - code - gateway/web/api.py
- [[rollback_agentshroud()]] - code - gateway/web/api.py
- [[rollback_bot()]] - code - gateway/web/api.py
- [[rollback_openclaw()]] - code - gateway/web/api.py
- [[security_report()]] - code - gateway/web/api.py
- [[skills_reload()]] - code - gateway/web/api.py
- [[start_service()_1]] - code - gateway/web/api.py
- [[stop_service()_1]] - code - gateway/web/api.py
- [[submit_competitive_intel()]] - code - gateway/web/api.py
- [[update_config()]] - code - gateway/web/api.py
- [[update_history()]] - code - gateway/web/api.py
- [[upgrade_agentshroud()]] - code - gateway/web/api.py
- [[warn_missing_features()]] - code - gateway/runtime/security.py
- [[ws_logs()]] - code - gateway/web/api.py
- [[ws_updates()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Runtime_Security_Comparison__Intel_Report
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 70]]
- 8 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 8 edges to [[_COMMUNITY_Community 45]]
- 7 edges to [[_COMMUNITY_Community 125]]
- 5 edges to [[_COMMUNITY_Community 460]]
- 5 edges to [[_COMMUNITY_Community 863]]
- 4 edges to [[_COMMUNITY_Community 110]]
- 4 edges to [[_COMMUNITY_Community 153]]
- 4 edges to [[_COMMUNITY_Community 247]]
- 4 edges to [[_COMMUNITY_Community 463]]
- 3 edges to [[_COMMUNITY_Community 106]]
- 3 edges to [[_COMMUNITY_Community 52]]
- 3 edges to [[_COMMUNITY_Community 42]]
- 3 edges to [[_COMMUNITY_Community 889]]
- 2 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 2 edges to [[_COMMUNITY_Community 180]]
- 2 edges to [[_COMMUNITY_Community 293]]
- 2 edges to [[_COMMUNITY_Community 333]]
- 2 edges to [[_COMMUNITY_Community 808]]
- 1 edge to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Community 145]]
- 1 edge to [[_COMMUNITY_Community 292]]
- 1 edge to [[_COMMUNITY_Community 71]]
- 1 edge to [[_COMMUNITY_Community 98]]
- 1 edge to [[_COMMUNITY_Community 55]]
- 1 edge to [[_COMMUNITY_Voice Gateway STT & Browser Security]]

## Top bridge nodes
- [[api.py]] - degree 76, connects to 19 communities
- [[IntelReportStore_1]] - degree 39, connects to 5 communities
- [[get_security_comparison()]] - degree 9, connects to 4 communities
- [[warn_missing_features()]] - degree 9, connects to 3 communities
- [[_get_engine()]] - degree 15, connects to 2 communities