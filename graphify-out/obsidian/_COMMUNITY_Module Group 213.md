---
type: community
cohesion: 0.20
members: 22
---

# Module Group 213

**Cohesion:** 0.20 - loosely connected
**Members:** 22 nodes

## Members
- [[._make_state_with_bot()]] - code - gateway/tests/test_soc_bots.py
- [[.test_clean_image_score_100()]] - code - gateway/tests/test_soc_bots.py
- [[.test_domains_has_vuln_and_egress()]] - code - gateway/tests/test_soc_bots.py
- [[.test_egress_filter_exception_defaults_denials_zero()]] - code - gateway/tests/test_soc_bots.py
- [[.test_formula_combined_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[.test_formula_critical_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[.test_formula_egress_denials_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[.test_formula_high_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[.test_formula_medium_penalty()]] - code - gateway/tests/test_soc_bots.py
- [[.test_missing_bot_returns_empty_image()]] - code - gateway/tests/test_soc_bots.py
- [[.test_no_scan_data_defaults_zeros()]] - code - gateway/tests/test_soc_bots.py
- [[.test_result_structure_has_required_keys()]] - code - gateway/tests/test_soc_bots.py
- [[.test_risk_level_red_below_50()]] - code - gateway/tests/test_soc_bots.py
- [[.test_risk_level_yellow_50_to_79()]] - code - gateway/tests/test_soc_bots.py
- [[.test_score_clamped_to_hundred()]] - code - gateway/tests/test_soc_bots.py
- [[.test_score_clamped_to_zero()]] - code - gateway/tests/test_soc_bots.py
- [[Bot not in config → image='', scan skipped, score based on egress only.]] - rationale - gateway/tests/test_soc_bots.py
- [[Bot with no image scan data should default criticalhighmedium to 0.]] - rationale - gateway/tests/test_soc_bots.py
- [[If egress_filter.get_stats raises, denials defaults to 0 (no crash).]] - rationale - gateway/tests/test_soc_bots.py
- [[Per-bot scorecard scoped to a single bot's image scan and egress stats.      Sco]] - rationale - gateway/security/scanner_integration.py
- [[TestComputeBotScorecard_1]] - code - gateway/tests/test_soc_bots.py
- [[compute_bot_scorecard()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_213
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 2 edges to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Security Scanner Integration]]
- 1 edge to [[_COMMUNITY_Module Group 228]]

## Top bridge nodes
- [[compute_bot_scorecard()]] - degree 21, connects to 4 communities
- [[TestComputeBotScorecard_1]] - degree 19, connects to 3 communities
- [[._make_state_with_bot()]] - degree 15, connects to 1 community
- [[.test_egress_filter_exception_defaults_denials_zero()]] - degree 5, connects to 1 community
- [[.test_no_scan_data_defaults_zeros()]] - degree 5, connects to 1 community
