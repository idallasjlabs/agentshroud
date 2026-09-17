---
source_file: "gateway/security/scanner_integration.py"
type: "code"
community: "Community 415"
location: "L2617"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_415
---

# compute_bot_scorecard()

## Connections
- [[dot-test_clean_image_score_100()]] - `calls` [EXTRACTED]
- [[dot-test_domains_has_vuln_and_egress()]] - `calls` [EXTRACTED]
- [[dot-test_egress_filter_exception_defaults_denials_zero()]] - `calls` [EXTRACTED]
- [[dot-test_formula_combined_penalty()]] - `calls` [EXTRACTED]
- [[dot-test_formula_critical_penalty()]] - `calls` [EXTRACTED]
- [[dot-test_formula_egress_denials_penalty()]] - `calls` [EXTRACTED]
- [[dot-test_formula_high_penalty()]] - `calls` [EXTRACTED]
- [[dot-test_formula_medium_penalty()]] - `calls` [EXTRACTED]
- [[dot-test_missing_bot_returns_empty_image()]] - `calls` [EXTRACTED]
- [[dot-test_no_scan_data_defaults_zeros()]] - `calls` [EXTRACTED]
- [[dot-test_result_structure_has_required_keys()]] - `calls` [EXTRACTED]
- [[dot-test_risk_level_red_below_50()]] - `calls` [EXTRACTED]
- [[dot-test_risk_level_yellow_50_to_79()]] - `calls` [EXTRACTED]
- [[dot-test_score_clamped_to_hundred()]] - `calls` [EXTRACTED]
- [[dot-test_score_clamped_to_zero()]] - `calls` [EXTRACTED]
- [[Any_72]] - `references` [EXTRACTED]
- [[Per-bot scorecard scoped to a single bot's image scan and egress stats.      Sco]] - `rationale_for` [EXTRACTED]
- [[TestComputeBotScorecard_1]] - `calls` [EXTRACTED]
- [[get_security_scorecard()]] - `calls` [EXTRACTED]
- [[scanner_integration.py]] - `contains` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[test_manage_soc_report_endpoint()]] - `shares_data_with` [INFERRED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_415