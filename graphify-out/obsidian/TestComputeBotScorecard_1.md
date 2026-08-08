---
source_file: "gateway/tests/test_soc_bots.py"
type: "code"
community: "Bot CVE Scorecard"
location: "L649"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Bot_CVE_Scorecard
---

# TestComputeBotScorecard

## Connections
- [[._make_state_with_bot()]] - `method` [EXTRACTED]
- [[.test_clean_image_score_100()]] - `method` [EXTRACTED]
- [[.test_domains_has_vuln_and_egress()]] - `method` [EXTRACTED]
- [[.test_egress_filter_exception_defaults_denials_zero()]] - `method` [EXTRACTED]
- [[.test_formula_combined_penalty()]] - `method` [EXTRACTED]
- [[.test_formula_critical_penalty()]] - `method` [EXTRACTED]
- [[.test_formula_egress_denials_penalty()]] - `method` [EXTRACTED]
- [[.test_formula_high_penalty()]] - `method` [EXTRACTED]
- [[.test_formula_medium_penalty()]] - `method` [EXTRACTED]
- [[.test_missing_bot_returns_empty_image()]] - `method` [EXTRACTED]
- [[.test_no_scan_data_defaults_zeros()]] - `method` [EXTRACTED]
- [[.test_result_structure_has_required_keys()]] - `method` [EXTRACTED]
- [[.test_risk_level_red_below_50()]] - `method` [EXTRACTED]
- [[.test_risk_level_yellow_50_to_79()]] - `method` [EXTRACTED]
- [[.test_score_clamped_to_hundred()]] - `method` [EXTRACTED]
- [[.test_score_clamped_to_zero()]] - `method` [EXTRACTED]
- [[RBACConfig_1]] - `uses` [INFERRED]
- [[Role_1]] - `uses` [INFERRED]
- [[test_soc_bots.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Bot_CVE_Scorecard