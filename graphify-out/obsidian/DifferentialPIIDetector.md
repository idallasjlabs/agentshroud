---
source_file: "gateway/tests/test_differential_pii_detector.py"
type: "code"
community: "Community 46"
location: "L44"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_46
---

# DifferentialPIIDetector

## Connections
- [[dot-_detector_with_fake()]] - `references` [EXTRACTED]
- [[dot-test_bare_city_name_not_flagged_but_street_address_is()]] - `references` [EXTRACTED]
- [[dot-test_clean_content_no_hits()]] - `references` [EXTRACTED]
- [[dot-test_core_ssn_unioned_when_presidio_misses_it()]] - `references` [EXTRACTED]
- [[dot-test_default_config_has_correct_floors()]] - `calls` [EXTRACTED]
- [[dot-test_dotted_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_email_redacted_in_output()]] - `references` [EXTRACTED]
- [[dot-test_init_does_not_construct_bare_analyzer_engine()]] - `calls` [EXTRACTED]
- [[dot-test_init_wires_explicit_nlp_engine_when_model_present()]] - `calls` [EXTRACTED]
- [[dot-test_pii_hit_fields()]] - `references` [EXTRACTED]
- [[dot-test_plain_email_caught_in_prompt()]] - `references` [EXTRACTED]
- [[dot-test_plain_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_presidio_analyze_restricted_to_pii_entities()]] - `references` [EXTRACTED]
- [[dot-test_presidio_exception_falls_back_to_regex()]] - `references` [EXTRACTED]
- [[dot-test_presidio_result_becomes_pii_hit()]] - `references` [EXTRACTED]
- [[dot-test_redact_on_hit_false_preserves_original()]] - `calls` [EXTRACTED]
- [[dot-test_redacted_content_is_original_when_no_pii()]] - `references` [EXTRACTED]
- [[dot-test_regex_fallback_when_model_absent()]] - `calls` [EXTRACTED]
- [[dot-test_report_has_required_fields()]] - `references` [EXTRACTED]
- [[dot-test_scan_produces_report_with_correct_floor_used()]] - `references` [EXTRACTED]
- [[dot-test_spaced_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_tool_specific_floor_override()]] - `calls` [EXTRACTED]
- [[dot-test_unknown_tool_uses_default_floor()]] - `references` [EXTRACTED]
- [[dot-test_us_ssn_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_weak_hit_present_in_tool_result_only()]] - `references` [EXTRACTED]
- [[dot-test_zero_width_space_injection_caught()]] - `references` [EXTRACTED]
- [[DifferentialPIIConfig_1]] - `uses` [INFERRED]
- [[DifferentialPIIDetector_1]] - `uses` [INFERRED]
- [[PIIHit]] - `uses` [INFERRED]
- [[PIIHitSeverity]] - `uses` [INFERRED]
- [[detector()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_46