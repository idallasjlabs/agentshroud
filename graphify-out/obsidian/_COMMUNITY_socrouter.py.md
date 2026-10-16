---
type: community
cohesion: 0.04
members: 129
---

# soc/router.py

**Cohesion:** 0.04 - loosely connected
**Members:** 129 nodes

## Members
- [[Add or override a specific egress domain rule (CC-10).      Supports optional sc]] - rationale - gateway/soc/router.py
- [[Change the root log level at runtime without restart (CC-44).]] - rationale - gateway/soc/router.py
- [[Clear shared memory for a group workspace (owner only).]] - rationale - gateway/soc/router.py
- [[Create a new group at runtime (owner only).]] - rationale - gateway/soc/router.py
- [[Create a time-bounded privilege delegation (owner only).]] - rationale - gateway/soc/router.py
- [[Delete a group at runtime (owner only).]] - rationale - gateway/soc/router.py
- [[Exchange gateway token for a session cookie.]] - rationale - gateway/soc/router.py
- [[Get tool allowdeny lists for a user or group entity.]] - rationale - gateway/soc/router.py
- [[In-place openclaw upgrade runs npm install -g inside the bot container.      No]] - rationale - gateway/soc/router.py
- [[Issue a short-lived WebSocket token for wssoc.]] - rationale - gateway/soc/router.py
- [[JSONResponse]] - code - gateway/soc/router.py
- [[Launch security-scan.sh for the given scanner and discard the handle (fire-and-f]] - rationale - gateway/soc/router.py
- [[List all active privilege delegations.]] - rationale - gateway/soc/router.py
- [[List security modules with availability, mode, and descriptions (CC-42, CC-43).]] - rationale - gateway/soc/router.py
- [[List service privacy policies (read-only view).]] - rationale - gateway/soc/router.py
- [[Live per-module enforcement heat-map (SCRUM-80).      Real allowblocksanitize]] - rationale - gateway/soc/router.py
- [[Operator-ready risk summary with plain-English bullets and per-user risk map (V9]] - rationale - gateway/soc/router.py
- [[Pause a contributor's bot access without removing their record.]] - rationale - gateway/soc/router.py
- [[Pull the latest Hermes Agent image and restart the container.      Unlike OpenCl]] - rationale - gateway/soc/router.py
- [[Pull the latest image for a container and restart it.]] - rationale - gateway/soc/router.py
- [[Query GitHub releases API. Returns {tag_name ..., html_url ...} or {error]] - rationale - gateway/soc/router.py
- [[Read raw shared memory for a group workspace.]] - rationale - gateway/soc/router.py
- [[Read the live per-module enforcement counters (SCRUM-80); tolerate absence.]] - rationale - gateway/soc/router.py
- [[Recent scanner events from the in-process startupscheduled scan history.      C]] - rationale - gateway/soc/router.py
- [[Remove an egress rule for a domain (CC-10).]] - rationale - gateway/soc/router.py
- [[Rename a group (CC-34).]] - rationale - gateway/soc/router.py
- [[Reset the config integrity baseline to the current file state.      Use after a]] - rationale - gateway/soc/router.py
- [[Resume a paused contributor's bot access.]] - rationale - gateway/soc/router.py
- [[Return all active egress rules preloaded permanent, user-created permanent, ses]] - rationale - gateway/soc/router.py
- [[Return current LLM quota failover statistics.]] - rationale - gateway/soc/router.py
- [[Return full collaborator activity log. limit=0 returns all entries.      Returns]] - rationale - gateway/soc/router.py
- [[Return the latest Software Bill of Materials (SBOM) in SPDX JSON format.      Ge]] - rationale - gateway/soc/router.py
- [[Return the latest Trivy vulnerability scan results.      Trivy scans are run at]] - rationale - gateway/soc/router.py
- [[Revoke a privilege delegation. Omit privilege to revoke all for the user.]] - rationale - gateway/soc/router.py
- [[Revoke an active rule from a past approval decision (CC-40).]] - rationale - gateway/soc/router.py
- [[Run a Trivy CVE scan immediately and send the report via Telegram.      Requires]] - rationale - gateway/soc/router.py
- [[Run a command inside the agentshroud-openclaw container via the Docker socket.]] - rationale - gateway/soc/router.py
- [[Run a shell command on the Docker Compose host via SSH.      Requires AGENTSHROU]] - rationale - gateway/soc/router.py
- [[SCLCaller]] - code - gateway/soc/router.py
- [[ServiceActionRequest]] - code - gateway/soc/router.py
- [[Set per-user collab mode override (persists across restarts).]] - rationale - gateway/soc/router.py
- [[Switch a security module between enforcemonitordisabled modes at runtime (CC-4]] - rationale - gateway/soc/router.py
- [[Unified scanner aggregation Trivy, Falco, ClamAV, Wazuh, OpenSCAP.      Returns]] - rationale - gateway/soc/router.py
- [[Update a user's display name (CC-35).]] - rationale - gateway/soc/router.py
- [[_app_state()]] - code - gateway/soc/router.py
- [[_confirmation_required()]] - code - gateway/soc/router.py
- [[_docker_exec_bot()]] - code - gateway/soc/router.py
- [[_fetch_latest_release()]] - code - gateway/soc/router.py
- [[_file_hash()]] - code - gateway/soc/router.py
- [[_launch_scan_background()]] - code - gateway/soc/router.py
- [[_log_audit()]] - code - gateway/soc/router.py
- [[_module_stats_snapshot()]] - code - gateway/soc/router.py
- [[_risk_level_label()]] - code - gateway/soc/router.py
- [[_ssh_compose()]] - code - gateway/soc/router.py
- [[acknowledge_config_integrity()]] - code - gateway/soc/router.py
- [[add_collaborator()]] - code - gateway/soc/router.py
- [[add_group_member()]] - code - gateway/soc/router.py
- [[approve_egress()]] - code - gateway/soc/router.py
- [[approve_request()]] - code - gateway/soc/router.py
- [[auth_login()]] - code - gateway/soc/router.py
- [[auth_ws_token()]] - code - gateway/soc/router.py
- [[build_correlation_summary()]] - code - gateway/security/soc_correlation.py
- [[clear_group_memory()]] - code - gateway/soc/router.py
- [[create_delegation()]] - code - gateway/soc/router.py
- [[create_group()]] - code - gateway/soc/router.py
- [[delete_group()]] - code - gateway/soc/router.py
- [[deny_egress()]] - code - gateway/soc/router.py
- [[deny_request()]] - code - gateway/soc/router.py
- [[emergency_block_egress()]] - code - gateway/soc/router.py
- [[export_audit()]] - code - gateway/soc/router.py
- [[get_collaborator_activity()]] - code - gateway/soc/router.py
- [[get_egress_log()]] - code - gateway/soc/router.py
- [[get_egress_rules()]] - code - gateway/soc/router.py
- [[get_group()]] - code - gateway/soc/router.py
- [[get_group_memory()]] - code - gateway/soc/router.py
- [[get_health()]] - code - gateway/soc/router.py
- [[get_llm_failover_stats()]] - code - gateway/soc/router.py
- [[get_modules()]] - code - gateway/soc/router.py
- [[get_modules_heatmap()]] - code - gateway/soc/router.py
- [[get_privacy_policies()]] - code - gateway/soc/router.py
- [[get_risk_score()]] - code - gateway/soc/router.py
- [[get_risk_summary()]] - code - gateway/soc/router.py
- [[get_sbom()]] - code - gateway/soc/router.py
- [[get_scan_results()]] - code - gateway/soc/router.py
- [[get_scanner_recent_events()]] - code - gateway/soc/router.py
- [[get_scanner_results()]] - code - gateway/soc/router.py
- [[get_security_alerts()]] - code - gateway/soc/router.py
- [[get_service_logs()]] - code - gateway/soc/router.py
- [[get_soc_correlation()]] - code - gateway/soc/router.py
- [[get_tool_acl()]] - code - gateway/soc/router.py
- [[get_trivy_results()]] - code - gateway/soc/router.py
- [[get_updates()]] - code - gateway/soc/router.py
- [[get_user()]] - code - gateway/soc/router.py
- [[killswitch_disconnect()]] - code - gateway/soc/router.py
- [[killswitch_freeze()]] - code - gateway/soc/router.py
- [[killswitch_shutdown()]] - code - gateway/soc/router.py
- [[list_delegations()]] - code - gateway/soc/router.py
- [[list_groups()]] - code - gateway/soc/router.py
- [[list_pending_approvals()]] - code - gateway/soc/router.py
- [[list_services()]] - code - gateway/soc/router.py
- [[list_users()]] - code - gateway/soc/router.py
- [[override_egress_rule()]] - code - gateway/soc/router.py
- [[pause_collaborator_endpoint()]] - code - gateway/soc/router.py
- [[rebuild_all_services()]] - code - gateway/soc/router.py
- [[remove_egress_rule()]] - code - gateway/soc/router.py
- [[remove_group_member()]] - code - gateway/soc/router.py
- [[rename_group()]] - code - gateway/soc/router.py
- [[restart_service()]] - code - gateway/soc/router.py
- [[revoke_collaborator()]] - code - gateway/soc/router.py
- [[revoke_delegation()]] - code - gateway/soc/router.py
- [[revoke_egress_history()]] - code - gateway/soc/router.py
- [[rollback_gateway()]] - code - gateway/soc/router.py
- [[run_scanner()]] - code - gateway/soc/router.py
- [[set_group_mode()]] - code - gateway/soc/router.py
- [[set_log_level()]] - code - gateway/soc/router.py
- [[set_module_mode()]] - code - gateway/soc/router.py
- [[set_user_collab_mode()]] - code - gateway/soc/router.py
- [[set_user_role()_1]] - code - gateway/soc/router.py
- [[socrouter.py]] - code - gateway/soc/router.py
- [[start_service()]] - code - gateway/soc/router.py
- [[stop_service()]] - code - gateway/soc/router.py
- [[trigger_cve_report()]] - code - gateway/soc/router.py
- [[unpause_collaborator_endpoint()]] - code - gateway/soc/router.py
- [[update_display_name()]] - code - gateway/soc/router.py
- [[update_service()]] - code - gateway/soc/router.py
- [[upgrade_bot()]] - code - gateway/soc/router.py
- [[upgrade_gateway()]] - code - gateway/soc/router.py
- [[upgrade_hermes()]] - code - gateway/soc/router.py
- [[verify_audit_chain()]] - code - gateway/soc/router.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/soc/routerpy
SORT file.name ASC
```

## Connections to other communities
- 71 edges to [[_COMMUNITY__FakeRBAC]]
- 31 edges to [[_COMMUNITY_test_soc_bots.py]]
- 20 edges to [[_COMMUNITY_telegram_proxy.py_1]]
- 12 edges to [[_COMMUNITY_ServiceManager_1]]
- 12 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 4 edges to [[_COMMUNITY_test_dashboard.py]]
- 4 edges to [[_COMMUNITY_SlackAPIProxy]]
- 3 edges to [[_COMMUNITY_soc.js]]
- 3 edges to [[_COMMUNITY_DelegationManager]]
- 3 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 2 edges to [[_COMMUNITY_test_collaborator_greeter.py_1]]
- 2 edges to [[_COMMUNITY__load_latest_json]]
- 2 edges to [[_COMMUNITY_soc_dashboard]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_migrate-cve-registry-ghsa.py]]
- 1 edge to [[_COMMUNITY_AgentTarget_4]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY__FakeRBAC_1]]
- 1 edge to [[_COMMUNITY_test_soc_router_coverage.py]]

## Top bridge nodes
- [[socrouter.py]] - degree 161, connects to 23 communities
- [[JSONResponse]] - degree 28, connects to 4 communities
- [[build_correlation_summary()]] - degree 10, connects to 4 communities
- [[SCLCaller]] - degree 87, connects to 3 communities
- [[create_group()]] - degree 8, connects to 3 communities
