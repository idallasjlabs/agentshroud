---
source_file: "gateway/security/scanner_integration.py"
type: "code"
community: "Bot CVE Scorecard"
location: "L2617"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Bot_CVE_Scorecard
---

# compute_bot_scorecard()

## Connections
- [[.test_clean_image_score_100()]] - `calls` [EXTRACTED]
- [[.test_domains_has_vuln_and_egress()]] - `calls` [EXTRACTED]
- [[.test_egress_filter_exception_defaults_denials_zero()]] - `calls` [EXTRACTED]
- [[.test_formula_combined_penalty()]] - `calls` [EXTRACTED]
- [[.test_formula_critical_penalty()]] - `calls` [EXTRACTED]
- [[.test_formula_egress_denials_penalty()]] - `calls` [EXTRACTED]
- [[.test_formula_high_penalty()]] - `calls` [EXTRACTED]
- [[.test_formula_medium_penalty()]] - `calls` [EXTRACTED]
- [[.test_missing_bot_returns_empty_image()]] - `calls` [EXTRACTED]
- [[.test_no_scan_data_defaults_zeros()]] - `calls` [EXTRACTED]
- [[.test_result_structure_has_required_keys()]] - `calls` [EXTRACTED]
- [[.test_risk_level_red_below_50()]] - `calls` [EXTRACTED]
- [[.test_risk_level_yellow_50_to_79()]] - `calls` [EXTRACTED]
- [[.test_score_clamped_to_hundred()]] - `calls` [EXTRACTED]
- [[.test_score_clamped_to_zero()]] - `calls` [EXTRACTED]
- [[Any_55]] - `references` [EXTRACTED]
- [[Per-bot scorecard scoped to a single bot's image scan and egress stats.      Sco]] - `rationale_for` [EXTRACTED]
- [[get_security_scorecard()]] - `calls` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[scanner_integration.py]] - `contains` [EXTRACTED]
- [[test_soc_bots.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Bot_CVE_Scorecard