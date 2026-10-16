---
type: community
cohesion: 0.05
members: 93
---

# test_soc_bots.py

**Cohesion:** 0.05 - loosely connected
**Members:** 93 nodes

## Members
- [[dot-_make_state_with_bot()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bot_dict_has_required_keys()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bot_id_augments_result_with_image_scan()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bot_id_calls_compute_bot_scorecard()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bot_id_returns_per_bot_config()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bots_backward_compat_no_bots_config()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bots_no_config_returns_synthetic_entry()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bots_returns_correct_structure()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_bots_returns_default_true_on_default_bot()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_clean_image_score_100()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_config_none_returns_empty_dict()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_domains_has_vuln_and_egress()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_egress_filter_exception_defaults_denials_zero()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_activity_by_bot_id_in_source()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_egress_log_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_events_by_exact_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_history_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_pending_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_filters_services_by_bot_image()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_formula_combined_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_formula_critical_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_formula_egress_denials_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_formula_high_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_formula_medium_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_known_bot_returns_cve_summary()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_missing_bot_returns_empty_image()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_calls_global_scorecard()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_defaults_to_openclaw()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_omits_bot_keys()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_returns_all_events()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_returns_all_pending()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_returns_all_services()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_returns_full_history()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_bot_id_returns_global_config()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_no_scan_data_defaults_zeros()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_result_structure_has_required_keys()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_returns_default_when_config_is_none()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_returns_default_when_no_bots_config()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_returns_registered_bots()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_risk_level_red_below_50()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_risk_level_yellow_50_to_79()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_score_clamped_to_hundred()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_score_clamped_to_zero()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_security_events_filters_by_bot_id()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_security_events_nonexistent_bot_returns_empty_not_404()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_single_bot_returns_list_of_one()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_unknown_bot_id_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[dot-test_unknown_bot_returns_error()]] - code - gateway/tests/test_soc_bots.py
- [[Backward-compat config attr absent → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Backward-compat no bots section → return single OpenClaw default.]] - rationale - gateway/tests/test_soc_bots.py
- [[Bot not in config → image='', scan skipped, score based on egress only.]] - rationale - gateway/tests/test_soc_bots.py
- [[Bot with no image scan data should default criticalhighmedium to 0.]] - rationale - gateway/tests/test_soc_bots.py
- [[Build an SCLCaller with OWNER role — no FastAPI dependency resolution.]] - rationale - gateway/tests/test_soc_bots.py
- [[Container Security Scorecard — 12-domain maturity assessment.      Standards bas]] - rationale - gateway/soc/router.py
- [[If egress_filter.get_stats raises, denials defaults to 0 (no crash).]] - rationale - gateway/tests/test_soc_bots.py
- [[Per-bot scorecard scoped to a single bot's image scan and egress stats.      Sco]] - rationale - gateway/security/scanner_integration.py
- [[Return egress decision history (approvedenytimeout) (CC-40).]] - rationale - gateway/soc/router.py
- [[Return the list of registered bots. Falls back to backward-compat OpenClaw defau]] - rationale - gateway/soc/router.py
- [[Return the tracked advisory registry for the wrapped AI agent.      When bot_id]] - rationale - gateway/soc/router.py
- [[TestAgentCvesBotId]] - code - gateway/tests/test_soc_bots.py
- [[TestBotSelectorFrontend]] - code - gateway/tests/test_soc_bots.py
- [[TestComputeBotScorecard_1]] - code - gateway/tests/test_soc_bots.py
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
- [[compute_bot_scorecard()]] - code - gateway/security/scanner_integration.py
- [[get_agent_cves()]] - code - gateway/soc/router.py
- [[get_config()]] - code - gateway/soc/router.py
- [[get_egress_history()]] - code - gateway/soc/router.py
- [[get_egress_log()]] - code - gateway/soc/router.py
- [[get_egress_pending()]] - code - gateway/soc/router.py
- [[get_scanner_results()]] - code - gateway/soc/router.py
- [[get_security_events()]] - code - gateway/soc/router.py
- [[get_security_scorecard()]] - code - gateway/soc/router.py
- [[list_bots()]] - code - gateway/soc/router.py
- [[list_services()]] - code - gateway/soc/router.py
- [[test_soc_bots.py]] - code - gateway/tests/test_soc_bots.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_botspy
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_socrouter.py]]
- 17 edges to [[_COMMUNITY_Role]]
- 13 edges to [[_COMMUNITY_RBACConfig]]
- 9 edges to [[_COMMUNITY_AsyncMock]]
- 8 edges to [[_COMMUNITY_Enum]]
- 4 edges to [[_COMMUNITY_ServiceManager]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]

## Top bridge nodes
- [[test_soc_bots.py]] - degree 38, connects to 5 communities
- [[compute_bot_scorecard()]] - degree 23, connects to 4 communities
- [[_make_owner_caller()]] - degree 29, connects to 2 communities
- [[TestComputeBotScorecard_1]] - degree 20, connects to 2 communities
- [[TestBotSelectorFrontend]] - degree 12, connects to 2 communities
