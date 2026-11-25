---
source_file: "gateway/security/differential_pii_detector.py"
type: "code"
community: "DifferentialPIIDetector"
location: "L299"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/DifferentialPIIDetector
---

# DifferentialPIIDetector

## Connections
- [[dot-__init__()_205]] - `method` [EXTRACTED]
- [[dot-_deduplicate()]] - `method` [EXTRACTED]
- [[dot-_detect_pii()]] - `method` [EXTRACTED]
- [[dot-_detect_presidio()]] - `method` [EXTRACTED]
- [[dot-_detect_regex()]] - `method` [EXTRACTED]
- [[dot-_detector_with_fake()]] - `references` [EXTRACTED]
- [[dot-_init_presidio()_1]] - `method` [EXTRACTED]
- [[dot-_redact()]] - `method` [EXTRACTED]
- [[dot-_scan()]] - `method` [EXTRACTED]
- [[dot-scan_prompt()]] - `method` [EXTRACTED]
- [[dot-scan_tool_result()]] - `method` [EXTRACTED]
- [[dot-test_bare_city_name_not_flagged_but_street_address_is()]] - `references` [EXTRACTED]
- [[dot-test_clean_content_no_hits()]] - `references` [EXTRACTED]
- [[dot-test_core_ssn_unioned_when_presidio_misses_it()]] - `references` [EXTRACTED]
- [[dot-test_dotted_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_email_redacted_in_output()]] - `references` [EXTRACTED]
- [[dot-test_pii_hit_fields()]] - `references` [EXTRACTED]
- [[dot-test_plain_email_caught_in_prompt()]] - `references` [EXTRACTED]
- [[dot-test_plain_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_presidio_analyze_restricted_to_pii_entities()]] - `references` [EXTRACTED]
- [[dot-test_presidio_exception_falls_back_to_regex()]] - `references` [EXTRACTED]
- [[dot-test_presidio_result_becomes_pii_hit()]] - `references` [EXTRACTED]
- [[dot-test_redacted_content_is_original_when_no_pii()]] - `references` [EXTRACTED]
- [[dot-test_report_has_required_fields()]] - `references` [EXTRACTED]
- [[dot-test_scan_produces_report_with_correct_floor_used()]] - `references` [EXTRACTED]
- [[dot-test_spaced_email_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_unknown_tool_uses_default_floor()]] - `references` [EXTRACTED]
- [[dot-test_us_ssn_caught_in_tool_result()]] - `references` [EXTRACTED]
- [[dot-test_weak_hit_present_in_tool_result_only()]] - `references` [EXTRACTED]
- [[dot-test_zero_width_space_injection_caught()]] - `references` [EXTRACTED]
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts. This…]] - `rationale_for` [EXTRACTED]
- [[TestAdversarialFormattingCaught]] - `uses` [INFERRED]
- [[TestAsymmetricFloor]] - `uses` [INFERRED]
- [[TestDeterministicPresidioInit]] - `uses` [INFERRED]
- [[TestDifferentialPIIDetectorConstruction]] - `uses` [INFERRED]
- [[TestPerToolConfiguration]] - `uses` [INFERRED]
- [[TestPresidioPathContract]] - `uses` [INFERRED]
- [[TestRedaction]] - `uses` [INFERRED]
- [[TestStandardPIIAlwaysCaught]] - `uses` [INFERRED]
- [[TestToolResultPIIReport]] - `uses` [INFERRED]
- [[detector()]] - `uses` [INFERRED]
- [[differential_pii_detector.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `uses` [INFERRED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_differential_pii_detector.py]] - `imports` [EXTRACTED]
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - `uses` [INFERRED]
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/DifferentialPIIDetector
