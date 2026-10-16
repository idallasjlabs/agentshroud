---
type: community
cohesion: 0.04
members: 92
---

# gateway/ingest_api/main.py (/hermes-dashboard/ HTTP + WebSocket reverse proxy)

**Cohesion:** 0.04 - loosely connected
**Members:** 92 nodes

## Members
- [[Audit feed for private-data access policy violations.]] - rationale - gateway/ingest_api/main.py
- [[AuthRequired_1]] - code
- [[Comprehensive container security profile — runs all applicable checks.]] - rationale - gateway/ingest_api/main.py
- [[Consolidated SOC report for dashboardSIEM pull workflows.]] - rationale - gateway/ingest_api/main.py
- [[Cross-signal SOC correlation summary.]] - rationale - gateway/ingest_api/main.py
- [[Export tamper-evident audit events in SOCSIEM formats.]] - rationale - gateway/ingest_api/main.py
- [[Fetch one report (metadata + content). Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[Forget this' - permanently delete a ledger entry Implements right to erasure.…]] - rationale - gateway/ingest_api/main.py
- [[Generate comprehensive security health report.]] - rationale - gateway/ingest_api/main.py
- [[Get DNS blocklist statistics. Returns current DNS filtering statistics from the…]] - rationale - gateway/ingest_api/main.py
- [[Get a single ledger entry by ID Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[Get kill switch monitor status and recent results. Returns Current status…]] - rationale - gateway/ingest_api/main.py
- [[Get permissions summary for a user (admin+ only).]] - rationale - gateway/ingest_api/main.py
- [[Get permissions summary for the current user.]] - rationale - gateway/ingest_api/main.py
- [[HTTP CONNECT proxy traffic statistics. Shows allowedblocked counts and recent…]] - rationale - gateway/ingest_api/main.py
- [[Ingest API (POST ingest)]] - image - docs/diagrams/images/diagram-03-gateway-components.svg
- [[LLMProxy.get_stats]] - code - gateway/proxy/llm_proxy.py
- [[List all configured agent targets with health status Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[List all security modules and their status.]] - rationale - gateway/ingest_api/main.py
- [[List all users and their roles (admin+ only).]] - rationale - gateway/security/rbac.py
- [[List configured SSH hosts (names only)]] - rationale - gateway/ingest_api/main.py
- [[List pending interactive egress approval requests.]] - rationale - gateway/ingest_api/main.py
- [[List quarantined blocked inbound messages for admin review.]] - rationale - gateway/ingest_api/main.py
- [[List quarantined blocked outbound messages for admin review.]] - rationale - gateway/ingest_api/main.py
- [[List recent egress attempts for dashboardSOC triage.]] - rationale - gateway/ingest_api/main.py
- [[List report metadata (no content), newest first, optionally by bot. Cross-bot…]] - rationale - gateway/ingest_api/main.py
- [[Preview egress risk heuristic for domainport combos.]] - rationale - gateway/ingest_api/main.py
- [[Query SSH audit entries from ledger]] - rationale - gateway/ingest_api/main.py
- [[Query the data ledger Returns paginated results with optional filters.…]] - rationale - gateway/ingest_api/main.py
- [[Remove a domain from the local denylist. Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[Remove an egress rule by domain.]] - rationale - gateway/ingest_api/main.py
- [[Return LLM proxy statistics.]] - rationale - gateway/ingest_api/main.py
- [[Return a paginated list of blocked domains. Authentication required.]] - rationale - gateway/ingest_api/main.py
- [[Return current private-data policy configuration and enforcement state.]] - rationale - gateway/ingest_api/main.py
- [[Return egress rules and emergency-block status.]] - rationale - gateway/ingest_api/main.py
- [[Return recent Falco runtime security alerts with summary.]] - rationale - gateway/ingest_api/main.py
- [[Return recent Wazuh HIDS alerts with FIM and rootkit summary.]] - rationale - gateway/ingest_api/main.py
- [[Return recent security telemetry events with optional filters.]] - rationale - gateway/ingest_api/main.py
- [[Return scanner result history for SOC timeline views.]] - rationale - gateway/ingest_api/main.py
- [[SOC 2 Trust Service Criteria compliance coverage report. Maps active…]] - rationale - gateway/ingest_api/main.py
- [[Scored security health report — grade, per-tool scores, recommendations.…]] - rationale - gateway/ingest_api/main.py
- [[Summarize inboundoutbound quarantine state for SOCdashboard use.]] - rationale - gateway/ingest_api/main.py
- [[System Control - Live Dashboard Shows real-time system status with links to…]] - rationale - gateway/ingest_api/main.py
- [[_active()]] - code - gateway/ingest_api/main.py
- [[_count_by_status()]] - code - gateway/ingest_api/main.py
- [[_top_reasons()]] - code - gateway/ingest_api/main.py
- [[asyncio]] - code
- [[container_security_profile()]] - code - gateway/ingest_api/main.py
- [[delete]] - code
- [[delete_ledger_entry()]] - code - gateway/ingest_api/main.py
- [[egress_log()]] - code - gateway/ingest_api/main.py
- [[egress_pending()]] - code - gateway/ingest_api/main.py
- [[egress_remove_rule()]] - code - gateway/ingest_api/main.py
- [[egress_risk_preview()]] - code - gateway/ingest_api/main.py
- [[egress_rules()]] - code - gateway/ingest_api/main.py
- [[falco_alerts()]] - code - gateway/ingest_api/main.py
- [[full_security_report()]] - code - gateway/ingest_api/main.py
- [[gateway package __init__]] - code - gateway/__init__.py
- [[get]] - code
- [[get_dns_stats()]] - code - gateway/ingest_api/main.py
- [[get_ledger_entry()]] - code - gateway/ingest_api/main.py
- [[get_my_permissions()]] - code - gateway/ingest_api/main.py
- [[get_report()]] - code - gateway/ingest_api/main.py
- [[get_soc2_compliance_report()]] - code - gateway/ingest_api/main.py
- [[get_user_permissions()]] - code - gateway/ingest_api/main.py
- [[ingest_apimain.py]] - code - gateway/ingest_api/main.py
- [[killswitch_status()]] - code - gateway/ingest_api/main.py
- [[list_agents()]] - code - gateway/ingest_api/main.py
- [[list_blocked_domains()]] - code - gateway/ingest_api/main.py
- [[list_blocked_message_quarantine()]] - code - gateway/ingest_api/main.py
- [[list_blocked_outbound_quarantine()]] - code - gateway/ingest_api/main.py
- [[list_reports()]] - code - gateway/ingest_api/main.py
- [[list_security_modules()]] - code - gateway/ingest_api/main.py
- [[list_users_and_roles()]] - code - gateway/ingest_api/main.py
- [[llm_proxy_stats]] - code - gateway/ingest_api/main.py
- [[privacy_audit()]] - code - gateway/ingest_api/main.py
- [[privacy_policy_status()]] - code - gateway/ingest_api/main.py
- [[proxy_status()]] - code - gateway/ingest_api/main.py
- [[quarantine_summary()]] - code - gateway/ingest_api/main.py
- [[query_ledger()]] - code - gateway/ingest_api/main.py
- [[remove_blocked_domain()]] - code - gateway/ingest_api/main.py
- [[scanner_history()]] - code - gateway/ingest_api/main.py
- [[security_health_report()]] - code - gateway/ingest_api/main.py
- [[soc_correlation()]] - code - gateway/ingest_api/main.py
- [[soc_events()]] - code - gateway/ingest_api/main.py
- [[soc_export()]] - code - gateway/ingest_api/main.py
- [[soc_redirect()]] - code - gateway/ingest_api/main.py
- [[soc_report()]] - code - gateway/ingest_api/main.py
- [[ssh_history()]] - code - gateway/ingest_api/main.py
- [[ssh_hosts()]] - code - gateway/ingest_api/main.py
- [[system_control()]] - code - gateway/ingest_api/main.py
- [[wazuh_alerts()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/gateway/ingest_api/mainpy_/hermes-dashboard/_HTTP__WebSocket_reverse_proxy
SORT file.name ASC
```

## Connections to other communities
- 42 edges to [[_COMMUNITY_AuditChain_1]]
- 15 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 9 edges to [[_COMMUNITY_test_prompt_guard.py_2]]
- 5 edges to [[_COMMUNITY__is_op_reference_allowed]]
- 3 edges to [[_COMMUNITY_Request]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py_1]]
- 3 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY_InjectionAction_1]]
- 2 edges to [[_COMMUNITY_Commit list 2026-10-10 through 2026-10-16 on main]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_test_docs_accuracy.py]]
- 1 edge to [[_COMMUNITY_sync-cve-registry.py]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_AlertTelegramRelay]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_ADR-005 SHA-256 Hash Chain Audit Integrity_1]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_CREDENTIAL-PROTECTION-IMPLEMENTED]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[ingest_apimain.py]] - degree 114, connects to 23 communities
- [[AuthRequired_1]] - degree 66, connects to 5 communities
- [[get]] - degree 39, connects to 1 community
- [[get_my_permissions()]] - degree 5, connects to 1 community
- [[get_user_permissions()]] - degree 5, connects to 1 community
