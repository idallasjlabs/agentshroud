---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "Community 45"
location: "L44"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_45
---

# DifferentialPIIDetector

## Connections
- [[._detector_with_fake()]] - `references` [EXTRACTED]
- [[.test_bare_city_name_not_flagged_but_street_address_is()]] - `references` [EXTRACTED]
- [[.test_clean_content_no_hits()]] - `references` [EXTRACTED]
- [[.test_core_ssn_unioned_when_presidio_misses_it()]] - `references` [EXTRACTED]
- [[.test_default_config_has_correct_floors()]] - `calls` [EXTRACTED]
- [[.test_dotted_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[.test_email_redacted_in_output()]] - `references` [EXTRACTED]
- [[.test_init_does_not_construct_bare_analyzer_engine()]] - `calls` [EXTRACTED]
- [[.test_init_wires_explicit_nlp_engine_when_model_present()]] - `calls` [EXTRACTED]
- [[.test_pii_hit_fields()]] - `references` [EXTRACTED]
- [[.test_plain_email_caught_in_prompt()]] - `references` [EXTRACTED]
- [[.test_plain_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[.test_presidio_analyze_restricted_to_pii_entities()]] - `references` [EXTRACTED]
- [[.test_presidio_exception_falls_back_to_regex()]] - `references` [EXTRACTED]
- [[.test_presidio_result_becomes_pii_hit()]] - `references` [EXTRACTED]
- [[.test_redact_on_hit_false_preserves_original()]] - `calls` [EXTRACTED]
- [[.test_redacted_content_is_original_when_no_pii()]] - `references` [EXTRACTED]
- [[.test_regex_fallback_when_model_absent()]] - `calls` [EXTRACTED]
- [[.test_report_has_required_fields()]] - `references` [EXTRACTED]
- [[.test_scan_produces_report_with_correct_floor_used()]] - `references` [EXTRACTED]
- [[.test_spaced_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[.test_tool_specific_floor_override()]] - `calls` [EXTRACTED]
- [[.test_unknown_tool_uses_default_floor()]] - `references` [EXTRACTED]
- [[.test_us_ssn_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[.test_weak_hit_present_in_tool_result_only()]] - `references` [EXTRACTED]
- [[.test_zero_width_space_injection_caught()]] - `references` [EXTRACTED]
- [[DifferentialPIIConfig]] - `uses` [INFERRED]
- [[DifferentialPIIDetector]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[detector()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_45