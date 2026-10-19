---
type: community
members: 95
---

# api.py

**Members:** 95 nodes

## Members
- [[dot-__call__()_9]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_133]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_134]] - code - gateway/web/api.py
- [[dot-_verifier()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verifier()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_allowlisted_live_source_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_dropped_count_is_tamper_evident()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_generated_at_is_preserved()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_host_confusion_urls_rejected_and_never_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_mixed_valid_and_invalid_keeps_only_valid()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_multiple_valid_citations_all_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_no_candidate_urls_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_on_non_2xx()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_without_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_off_allowlist_url_dropped_and_not_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ok_requires_2xx_and_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_report_all_unverified_is_empty()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_report_keeps_verified_and_counts_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_self_asserted_verified_is_ignored()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_source_without_content_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ssrf_unsafe_urls_rejected_before_fetch()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_unparseable_url_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_unreachable_source_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_verified_report_persists_with_intact_hashchain()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_wildcard_allowlist_match_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[A draft competitive-intel report submitted for citation verification.]] - rationale - gateway/web/api.py
- [[An unverified competitor claim submitted for citation checking.]] - rationale - gateway/security/citation_verifier.py
- [[Build a CitationVerifier wired to the production (httpx) fetcher.      Isolated]] - rationale - gateway/web/api.py
- [[Check for AgentShroud updates from GitHub.]] - rationale - gateway/web/api.py
- [[CitationVerifier]] - code - gateway/security/citation_verifier.py
- [[ConfigUpdate]] - code - gateway/web/api.py
- [[Create a short-lived WebSocket-only token for management endpoints.]] - rationale - gateway/web/api.py
- [[Deterministic fetcher maps url - (status, sha_or_None). Records calls.]] - rationale - gateway/tests/test_citation_verifier.py
- [[DraftEntry]] - code - gateway/security/citation_verifier.py
- [[Export current configuration.]] - rationale - gateway/web/api.py
- [[FetchOutcome_1]] - code - gateway/tests/test_citation_verifier.py
- [[Get current configuration.]] - rationale - gateway/web/api.py
- [[Import configuration from uploaded data.]] - rationale - gateway/web/api.py
- [[IntelDraftEntry]] - code - gateway/web/api.py
- [[IntelDraftRequest]] - code - gateway/web/api.py
- [[IntelReportStore]] - code - gateway/security/intel_report.py
- [[One unverified competitor claim + its candidate source URLs.]] - rationale - gateway/web/api.py
- [[Path_35]] - code - gateway/web/api.py
- [[Persistent store for competitive intelligence reports.      Each report is saved]] - rationale - gateway/security/intel_report.py
- [[Raised when SkillGuard blocks a dangerous skill tree before deploy.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings`` and sync skillsagentsMCP into both bot configs.]] - rationale - gateway/web/api.py
- [[Re-read ``~.llm_settings``, scan for supply-chain risk, deploy to both bots.]] - rationale - gateway/web/api.py
- [[Resolve the Dockerfile for the default bot from gateway config.]] - rationale - gateway/web/api.py
- [[Resolve the source (``~.llm_settings``) and bot-config destinations.      Extr]] - rationale - gateway/web/api.py
- [[Return an IntelReportStore pointed at the configured data directory.]] - rationale - gateway/web/api.py
- [[Return recent competitive-intelligence reports in reverse-chronological order.]] - rationale - gateway/web/api.py
- [[Return the current AGENTSHROUD_MODE.]] - rationale - gateway/web/api.py
- [[Return the latest validated competitive-intelligence report.      Auth-gated (ow]] - rationale - gateway/web/api.py
- [[Return update history from audit log.]] - rationale - gateway/web/api.py
- [[Rollback OpenClaw (backward-compat alias for updatesbotopenclawrollback).]] - rationale - gateway/web/api.py
- [[Rollback a named bot container to the previous image tag.]] - rationale - gateway/web/api.py
- [[ServiceAction]] - code - gateway/web/api.py
- [[SkillGuardBlocked]] - code - gateway/web/api.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyEntry]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyReport]] - code - gateway/tests/test_citation_verifier.py
- [[Update configuration (writes YAML and optionally restarts).]] - rationale - gateway/web/api.py
- [[Validate a management WebSocket token (single-use, time-limited).]] - rationale - gateway/web/api.py
- [[Verifies competitor claims against re-fetched, allowlisted sources.]] - rationale - gateway/security/citation_verifier.py
- [[Verify and persist a draft competitive-intel report (SCRUM-75).      Each draft]] - rationale - gateway/web/api.py
- [[WebSocket_2]] - code - gateway/web/api.py
- [[WebSocket endpoint for real-time log streaming. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[WebSocket for real-time update progress. Requires scoped WS token.]] - rationale - gateway/web/api.py
- [[_FakeFetcher_1]] - code - gateway/tests/test_citation_verifier.py
- [[_create_mgmt_ws_token()]] - code - gateway/web/api.py
- [[_get_default_bot_dockerfile()]] - code - gateway/web/api.py
- [[_intel_store()]] - code - gateway/web/api.py
- [[_intel_verifier()]] - code - gateway/web/api.py
- [[_skills_reload_impl()]] - code - gateway/web/api.py
- [[_skills_reload_paths()]] - code - gateway/web/api.py
- [[_validate_mgmt_ws_token()]] - code - gateway/web/api.py
- [[api.py_2]] - code - gateway/web/api.py
- [[check_agentshroud_updates()]] - code - gateway/web/api.py
- [[citation_verifier module]] - code - gateway/security/citation_verifier.py
- [[export_config()]] - code - gateway/web/api.py
- [[get_competitive_intel()]] - code - gateway/web/api.py
- [[get_competitive_intel_history()]] - code - gateway/web/api.py
- [[get_config()_1]] - code - gateway/web/api.py
- [[get_mode()]] - code - gateway/web/api.py
- [[import_config()]] - code - gateway/web/api.py
- [[rollback_bot()]] - code - gateway/web/api.py
- [[rollback_openclaw()]] - code - gateway/web/api.py
- [[skills_reload()]] - code - gateway/web/api.py
- [[submit_competitive_intel()]] - code - gateway/web/api.py
- [[test_citation_verifier.py]] - code - gateway/tests/test_citation_verifier.py
- [[test_default_allowlist_uses_permanent_egress_domains()]] - code - gateway/tests/test_citation_verifier.py
- [[update_config()]] - code - gateway/web/api.py
- [[update_history()]] - code - gateway/web/api.py
- [[ws_logs()]] - code - gateway/web/api.py
- [[ws_updates()]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 25 edges to [[_COMMUNITY_FetchOutcome]]
- 23 edges to [[_COMMUNITY_api.py (2)]]
- 16 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 4 edges to [[_COMMUNITY_Path]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport (2)]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 3 edges to [[_COMMUNITY_RuntimeConfig]]
- 2 edges to [[_COMMUNITY_SkillGuard (2)]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]
- 1 edge to [[_COMMUNITY_ConsentFramework (2)]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_get_engine]]
- 1 edge to [[_COMMUNITY_dashboard_endpoints.py (2)]]
- 1 edge to [[_COMMUNITY_installer.py]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py (2)]]
- 1 edge to [[_COMMUNITY_upgrade]]

## Top bridge nodes
- [[api.py_2]] - degree 75, connects to 17 communities
- [[IntelReportStore]] - degree 39, connects to 4 communities
- [[DraftEntry]] - degree 45, connects to 3 communities
- [[CitationVerifier]] - degree 43, connects to 3 communities
- [[TestVerifyEntry]] - degree 19, connects to 2 communities
