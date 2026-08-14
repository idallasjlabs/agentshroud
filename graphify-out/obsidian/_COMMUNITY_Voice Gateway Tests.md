---
type: community
members: 71
---

# Voice Gateway Tests

**Members:** 71 nodes

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
- [[.test_no_bot_id_calls_global_scorecard()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_defaults_to_openclaw()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_omits_bot_keys()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_events()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_pending()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_all_services()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_full_history()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_bot_id_returns_global_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_returns_default_when_config_is_none()]] - code - gateway/tests/test_soc_bots.py
- [[.test_returns_default_when_no_bots_config()]] - code - gateway/tests/test_soc_bots.py
- [[.test_returns_registered_bots()]] - code - gateway/tests/test_soc_bots.py
- [[.test_security_events_filters_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[.test_security_events_nonexistent_bot_returns_empty_not_404()]] - code - gateway/tests/test_soc_bots.py
- [[.test_single_bot_returns_list_of_one()]] - code - gateway/tests/test_soc_bots.py
- [[.test_unknown_bot_id_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[.test_unknown_bot_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[Backward-compat config attr absent → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Backward-compat no bots section → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Build an SCLCaller with OWNER role — no FastAPI dependency resolution.]] - rationale - gateway/tests/test_soc_bots.py
- [[Container Security Scorecard — 12-domain maturity assessment.      Standards bas]] - rationale - gateway/soc/router.py
- [[Return egress decision history (approvedenytimeout) (CC-40).]] - rationale - gateway/soc/router.py
- [[Return the list of registered bots. Falls back to backward-compat OpenClaw defau]] - rationale - gateway/soc/router.py
- [[Return the tracked advisory registry for the wrapped AI agent.      When bot_id]] - rationale - gateway/soc/router.py
- [[TestAgentCvesBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestBotSelectorFrontend]] - code - gateway/tests/test_soc_bots.py
- [[TestCollaboratorActivityBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestConfigBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestEgressHistoryBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestEgressLogBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestEgressPendingBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestListBots]] - code - gateway/tests/test_soc_bots.py
- [[TestScannersBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestScorecardBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestSecurityEventsBotFilter]] - code - gateway/tests/test_soc_bots.py
- [[TestServicesBotFilter]] - code - gateway/tests/test_soc_bots.py
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
- [[get_agent_cves()]] - code - gateway/soc/router.py
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
- 31 edges to [[_COMMUNITY_Enhanced Approval Queue]]
- 28 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 10 edges to [[_COMMUNITY_Gateway Test Suite]]
- 9 edges to [[_COMMUNITY_Gateway Test Suite]]
- 5 edges to [[_COMMUNITY_Planning Docs]]
- 5 edges to [[_COMMUNITY_Tool Chain Analyzer]]
- 3 edges to [[_COMMUNITY_Community 1513]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docspapers]]

## Top bridge nodes
- [[test_soc_bots.py]] - degree 38, connects to 6 communities
- [[get_security_scorecard()]] - degree 9, connects to 3 communities
- [[.test_filters_egress_log_by_bot_id()]] - degree 6, connects to 3 communities
- [[_make_owner_caller()]] - degree 29, connects to 2 communities
- [[get_security_events()]] - degree 9, connects to 2 communities