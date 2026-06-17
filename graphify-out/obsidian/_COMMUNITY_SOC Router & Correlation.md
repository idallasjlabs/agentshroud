---
type: community
cohesion: 0.04
members: 129
---

# SOC Router & Correlation

**Cohesion:** 0.04 - loosely connected
**Members:** 129 nodes

## Members
- [[Add or override a specific egress domain rule (CC-10).      Supports optional sc]] - rationale - gateway/soc/router.py
- [[Append a collaborator UID to the persistent store (idempotent, file-locked).]] - rationale - gateway/security/rbac_config.py
- [[Change the root log level at runtime without restart (CC-44).]] - rationale - gateway/soc/router.py
- [[Clear shared memory for a group workspace (owner only).]] - rationale - gateway/soc/router.py
- [[Container Security Scorecard — 12-domain maturity assessment.      Standards bas]] - rationale - gateway/soc/router.py
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
- [[Operator-ready risk summary with plain-English bullets and per-user risk map (V9]] - rationale - gateway/soc/router.py
- [[Pull the latest Hermes Agent image and restart the container.      Unlike OpenCl]] - rationale - gateway/soc/router.py
- [[Pull the latest image for a container and restart it.]] - rationale - gateway/soc/router.py
- [[Query GitHub releases API. Returns {tag_name ..., html_url ...} or {error]] - rationale - gateway/soc/router.py
- [[Read raw shared memory for a group workspace.]] - rationale - gateway/soc/router.py
- [[Recent scanner events from the in-process startupscheduled scan history.      C]] - rationale - gateway/soc/router.py
- [[Remove an egress rule for a domain (CC-10).]] - rationale - gateway/soc/router.py
- [[Rename a group (CC-34).]] - rationale - gateway/soc/router.py
- [[Reset the config integrity baseline to the current file state.      Use after a]] - rationale - gateway/soc/router.py
- [[Return all active egress rules preloaded permanent, user-created permanent, ses]] - rationale - gateway/soc/router.py
- [[Return current LLM quota failover statistics.]] - rationale - gateway/soc/router.py
- [[Return egress decision history (approvedenytimeout) (CC-40).]] - rationale - gateway/soc/router.py
- [[Return full collaborator activity log. limit=0 returns all entries.      Returns]] - rationale - gateway/soc/router.py
- [[Return the latest Software Bill of Materials (SBOM) in SPDX JSON format.      Ge]] - rationale - gateway/soc/router.py
- [[Return the latest Trivy vulnerability scan results.      Trivy scans are run at]] - rationale - gateway/soc/router.py
- [[Revoke a privilege delegation. Omit privilege to revoke all for the user.]] - rationale - gateway/soc/router.py
- [[Revoke an active rule from a past approval decision (CC-40).]] - rationale - gateway/soc/router.py
- [[Run a Trivy CVE scan immediately and send the report via Telegram.      Requires]] - rationale - gateway/soc/router.py
- [[Run a command inside the agentshroud-openclaw container via the Docker socket.]] - rationale - gateway/soc/router.py
- [[Run a shell command on the Docker Compose host via SSH.      Requires AGENTSHROU]] - rationale - gateway/soc/router.py
- [[SCLCaller_1]] - code - gateway/soc/router.py
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
- [[_risk_level_label()]] - code - gateway/soc/router.py
- [[_ssh_compose()]] - code - gateway/soc/router.py
- [[acknowledge_config_integrity()]] - code - gateway/soc/router.py
- [[add_collaborator()_1]] - code - gateway/soc/router.py
- [[add_group_member()_1]] - code - gateway/soc/router.py
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
- [[get_egress_history()]] - code - gateway/soc/router.py
- [[get_egress_log()]] - code - gateway/soc/router.py
- [[get_egress_pending()_1]] - code - gateway/soc/router.py
- [[get_egress_rules()]] - code - gateway/soc/router.py
- [[get_group()]] - code - gateway/soc/router.py
- [[get_group_memory()]] - code - gateway/soc/router.py
- [[get_health()_1]] - code - gateway/soc/router.py
- [[get_llm_failover_stats()]] - code - gateway/soc/router.py
- [[get_modules()]] - code - gateway/soc/router.py
- [[get_privacy_policies()]] - code - gateway/soc/router.py
- [[get_risk_score()]] - code - gateway/soc/router.py
- [[get_risk_summary()]] - code - gateway/soc/router.py
- [[get_sbom()_1]] - code - gateway/soc/router.py
- [[get_scan_results()]] - code - gateway/soc/router.py
- [[get_scanner_recent_events()]] - code - gateway/soc/router.py
- [[get_scanner_results()]] - code - gateway/soc/router.py
- [[get_security_alerts()]] - code - gateway/soc/router.py
- [[get_security_events()]] - code - gateway/soc/router.py
- [[get_security_scorecard()]] - code - gateway/soc/router.py
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
- [[list_pending_approvals()_1]] - code - gateway/soc/router.py
- [[list_services()]] - code - gateway/soc/router.py
- [[list_users()]] - code - gateway/soc/router.py
- [[override_egress_rule()]] - code - gateway/soc/router.py
- [[persist_approved_collaborator()]] - code - gateway/security/rbac_config.py
- [[rebuild_all_services()]] - code - gateway/soc/router.py
- [[remove_egress_rule()]] - code - gateway/soc/router.py
- [[remove_group_member()]] - code - gateway/soc/router.py
- [[rename_group()]] - code - gateway/soc/router.py
- [[restart_service()_1]] - code - gateway/soc/router.py
- [[revoke_collaborator()]] - code - gateway/soc/router.py
- [[revoke_delegation()]] - code - gateway/soc/router.py
- [[revoke_egress_history()]] - code - gateway/soc/router.py
- [[rollback_gateway()]] - code - gateway/soc/router.py
- [[router.py_1]] - code - gateway/soc/router.py
- [[run_scanner()]] - code - gateway/soc/router.py
- [[set_group_mode()]] - code - gateway/soc/router.py
- [[set_log_level()]] - code - gateway/soc/router.py
- [[set_module_mode()]] - code - gateway/soc/router.py
- [[set_user_collab_mode()]] - code - gateway/soc/router.py
- [[set_user_role()_1]] - code - gateway/soc/router.py
- [[start_service()]] - code - gateway/soc/router.py
- [[stop_service()_1]] - code - gateway/soc/router.py
- [[trigger_cve_report()]] - code - gateway/soc/router.py
- [[update_display_name()]] - code - gateway/soc/router.py
- [[update_service()]] - code - gateway/soc/router.py
- [[upgrade_bot()]] - code - gateway/soc/router.py
- [[upgrade_gateway()]] - code - gateway/soc/router.py
- [[upgrade_hermes()]] - code - gateway/soc/router.py
- [[verify_audit_chain()]] - code - gateway/soc/router.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOC_Router__Correlation
SORT file.name ASC
```

## Connections to other communities
- 83 edges to [[_COMMUNITY_Module Group 83]]
- 32 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 14 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 13 edges to [[_COMMUNITY_Module Group 208]]
- 12 edges to [[_COMMUNITY_SOC Services]]
- 9 edges to [[_COMMUNITY_RBAC Configuration]]
- 7 edges to [[_COMMUNITY_SOC Authentication]]
- 5 edges to [[_COMMUNITY_Module Group 206]]
- 4 edges to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 3 edges to [[_COMMUNITY_Module Group 190]]
- 3 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 2 edges to [[_COMMUNITY_Module Group 135]]
- 2 edges to [[_COMMUNITY_Module Group 195]]
- 2 edges to [[_COMMUNITY_Module Group 231]]
- 2 edges to [[_COMMUNITY_Group Config & Teams]]
- 2 edges to [[_COMMUNITY_Module Group 381]]
- 2 edges to [[_COMMUNITY_Module Group 228]]
- 2 edges to [[_COMMUNITY_Module Group 134]]
- 2 edges to [[_COMMUNITY_Module Group 213]]
- 2 edges to [[_COMMUNITY_Module Group 75]]
- 2 edges to [[_COMMUNITY_Module Group 543]]
- 2 edges to [[_COMMUNITY_Module Group 556]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 196]]
- 1 edge to [[_COMMUNITY_Module Group 84]]
- 1 edge to [[_COMMUNITY_Module Group 169]]
- 1 edge to [[_COMMUNITY_Module Group 554]]
- 1 edge to [[_COMMUNITY_Module Group 335]]
- 1 edge to [[_COMMUNITY_SOC Services & Health Status]]

## Top bridge nodes
- [[router.py_1]] - degree 154, connects to 22 communities
- [[JSONResponse]] - degree 42, connects to 6 communities
- [[build_correlation_summary()]] - degree 12, connects to 4 communities
- [[persist_approved_collaborator()]] - degree 7, connects to 4 communities
- [[SCLCaller_1]] - degree 87, connects to 3 communities