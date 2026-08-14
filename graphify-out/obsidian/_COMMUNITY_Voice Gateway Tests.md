---
type: community
members: 92
---

# Voice Gateway Tests

**Members:** 92 nodes

## Members
- [[.test_bot_dict_has_required_keys()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bot_id_augments_result_with_image_scan()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bot_id_calls_compute_bot_scorecard()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bot_id_returns_per_bot_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bots_backward_compat_no_bots_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bots_no_config_returns_synthetic_entry()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bots_returns_correct_structure()]] - code - gateway/tests/test_soc_bots.py
- [[.test_bots_returns_default_true_on_default_bot()]] - code - gateway/tests/test_soc_bots.py
- [[.test_config_none_returns_empty_dict()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_activity_by_bot_id_in_source()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_egress_log_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_events_by_exact_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_history_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_pending_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_filters_services_by_bot_image()]] - code - gateway/tests/test_soc_bots.py
- [[.test_known_bot_returns_cve_summary()]] - code - gateway/tests/test_soc_bots.py
- [[.test_minimal_construction()]] - code - gateway/tests/test_soc_models.py
- [[.test_no_bot_id_calls_global_scorecard()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_defaults_to_openclaw()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_omits_bot_keys()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_events()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_pending()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_services()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_full_history()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_global_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_optional_fields_default_none()]] - code - gateway/tests/test_soc_models.py
- [[.test_returns_default_when_config_is_none()]] - code - gateway/tests/test_soc_bots.py
- [[.test_returns_default_when_no_bots_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_returns_registered_bots()]] - code - gateway/tests/test_soc_bots.py
- [[.test_security_events_filters_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_security_events_nonexistent_bot_returns_empty_not_404()]] - code - gateway/tests/test_soc_bots.py
- [[.test_severity_ordering()_1]] - code - gateway/tests/test_soc_models.py
- [[.test_single_bot_returns_list_of_one()]] - code - gateway/tests/test_soc_bots.py
- [[.test_unknown_bot_id_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[.test_unknown_bot_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[Any_65]] - code - gateway/soc/event_adapter.py
- [[Backward-compat config attr absent → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Backward-compat no bots section → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Best-effort conversion of arbitrary event dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Best-effort mapping of arbitrary severity strings to Severity enum.]] - rationale - gateway/soc/event_adapter.py
- [[Build an SCLCaller with OWNER role — no FastAPI dependency resolution.]] - rationale - gateway/tests/test_soc_bots.py
- [[Collect recent SecurityEvents from AuditStore (async-safe read).]] - rationale - gateway/soc/event_adapter.py
- [[Container Security Scorecard — 12-domain maturity assessment.      Standards bas]] - rationale - gateway/soc/router.py
- [[Convert AuditEvent (from AuditStore) to SecurityEvent.      AuditEvent fields e]] - rationale - gateway/soc/event_adapter.py
- [[Convert a PipelineResult to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an AnomalyAlert (from EgressMonitorSOCCorrelation) to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Convert an EgressAttempt or egress dict to SecurityEvent.]] - rationale - gateway/soc/event_adapter.py
- [[Return egress decision history (approvedenytimeout) (CC-40).]] - rationale - gateway/soc/router.py
- [[Return full collaborator activity log. limit=0 returns all entries.      Returns]] - rationale - gateway/soc/router.py
- [[Return the list of registered bots. Falls back to backward-compat OpenClaw defau]] - rationale - gateway/soc/router.py
- [[Return the tracked advisory registry for the wrapped AI agent.      When bot_id]] - rationale - gateway/soc/router.py
- [[SecurityEvent]] - code - gateway/soc/event_adapter.py
- [[SecurityEvent_1]] - code - gateway/soc/models.py
- [[Severity_1]] - code - gateway/soc/event_adapter.py
- [[TestAgentCvesBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestBotSelectorFrontend]] - code - gateway/tests/test_soc_bots.py
- [[TestConfigBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestEgressHistoryBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestEgressPendingBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestListBots]] - code - gateway/tests/test_soc_bots.py
- [[TestScorecardBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestSecurityEvent]] - code - gateway/tests/test_soc_models.py
- [[TestSecurityEventsBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[Unified scanner aggregation Trivy, Falco, ClamAV, Wazuh, OpenSCAP.      Returns]] - rationale - gateway/soc/router.py
- [[Unit tests for the M6 bot selector backend — socv1bots + bot_id filtering.]] - rationale - gateway/tests/test_soc_bots.py
- [[When app_state.config is None, return empty dict (backward-compat).]] - rationale - gateway/tests/test_soc_bots.py
- [[When bot_id is given, services whose image matches the bot's image are returned.]] - rationale - gateway/tests/test_soc_bots.py
- [[_make_app_state()]] - code - gateway/tests/test_soc_bots.py
- [[_make_bot_config()]] - code - gateway/tests/test_soc_bots.py
- [[_make_m6_app_state()]] - code - gateway/tests/test_soc_bots.py
- [[_make_m6_bot_config()]] - code - gateway/tests/test_soc_bots.py
- [[_make_m6_caller()]] - code - gateway/tests/test_soc_bots.py
- [[_make_owner_caller()]] - code - gateway/tests/test_soc_bots.py
- [[_map_severity()]] - code - gateway/soc/event_adapter.py
- [[collect_recent_events()]] - code - gateway/soc/event_adapter.py
- [[event_adapter.py]] - code - gateway/soc/event_adapter.py
- [[from_anomaly_alert()]] - code - gateway/soc/event_adapter.py
- [[from_audit_chain_entry()]] - code - gateway/soc/event_adapter.py
- [[from_dict()]] - code - gateway/soc/event_adapter.py
- [[from_egress_attempt()]] - code - gateway/soc/event_adapter.py
- [[from_pipeline_result()]] - code - gateway/soc/event_adapter.py
- [[get_agent_cves()]] - code - gateway/soc/router.py
- [[get_collaborator_activity()]] - code - gateway/soc/router.py
- [[get_config()]] - code - gateway/soc/router.py
- [[get_egress_history()]] - code - gateway/soc/router.py
- [[get_egress_pending()_1]] - code - gateway/soc/router.py
- [[get_scanner_results()]] - code - gateway/soc/router.py
- [[get_security_events()]] - code - gateway/soc/router.py
- [[get_security_scorecard()]] - code - gateway/soc/router.py
- [[list_bots()]] - code - gateway/soc/router.py
- [[list_services()]] - code - gateway/soc/router.py
- [[test_soc_bots.py]] - code - gateway/tests/test_soc_bots.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Voice_Gateway_Tests
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 32 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 10 edges to [[_COMMUNITY_Architecture Docs]]
- 9 edges to [[_COMMUNITY_Gateway Test Suite]]
- 8 edges to [[_COMMUNITY_Gateway Test Suite]]
- 8 edges to [[_COMMUNITY_Gateway Security Module]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Bot Skill Config]]
- 1 edge to [[_COMMUNITY_docspapers]]
- 1 edge to [[_COMMUNITY_Tool Chain Analyzer]]

## Top bridge nodes
- [[test_soc_bots.py]] - degree 38, connects to 5 communities
- [[SecurityEvent_1]] - degree 19, connects to 3 communities
- [[event_adapter.py]] - degree 11, connects to 3 communities
- [[get_security_scorecard()]] - degree 9, connects to 3 communities
- [[.test_filters_egress_log_by_bot_id()]] - degree 6, connects to 3 communities