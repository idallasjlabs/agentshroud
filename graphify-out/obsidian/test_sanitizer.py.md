---
source_file: "gateway/tests/test_sanitizer.py"
type: "code"
community: "Community 435"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_435
---

# test_sanitizer.py

## Connections
- [[PIIConfig]] - `imports` [EXTRACTED]
- [[PIISanitizer]] - `imports` [EXTRACTED]
- [[_FakeAnalyzer]] - `contains` [EXTRACTED]
- [[_FakeAnonymizer]] - `contains` [EXTRACTED]
- [[_FakeRecognizerResult_1]] - `contains` [EXTRACTED]
- [[_presidio_sanitizer()]] - `contains` [EXTRACTED]
- [[_regex_sanitizer()]] - `contains` [EXTRACTED]
- [[test_block_action_blocks_and_withholds_pii()]] - `contains` [EXTRACTED]
- [[test_block_action_clean_content_passes_unchanged()]] - `contains` [EXTRACTED]
- [[test_credit_card_detection()]] - `contains` [EXTRACTED]
- [[test_disabled_config_not_blocked()]] - `contains` [EXTRACTED]
- [[test_email_detection()]] - `contains` [EXTRACTED]
- [[test_empty_content()]] - `contains` [EXTRACTED]
- [[test_min_confidence_above_one_rejected()]] - `contains` [EXTRACTED]
- [[test_min_confidence_at_floor_is_identical_to_default()]] - `contains` [EXTRACTED]
- [[test_min_confidence_can_be_raised()]] - `contains` [EXTRACTED]
- [[test_min_confidence_cannot_be_lowered_below_floor()]] - `contains` [EXTRACTED]
- [[test_mixed_pii()]] - `contains` [EXTRACTED]
- [[test_monitor_mode_reports_but_never_mutates()]] - `contains` [EXTRACTED]
- [[test_no_pii()]] - `contains` [EXTRACTED]
- [[test_per_call_action_override()]] - `contains` [EXTRACTED]
- [[test_per_call_invalid_action_rejected()]] - `contains` [EXTRACTED]
- [[test_performance.py]] - `shares_data_with` [INFERRED]
- [[test_phone_detection()]] - `contains` [EXTRACTED]
- [[test_raised_threshold_with_block_only_blocks_above_threshold()]] - `contains` [EXTRACTED]
- [[test_real_phone_still_redacted()]] - `contains` [EXTRACTED]
- [[test_redact_action_unchanged_and_not_blocked()]] - `contains` [EXTRACTED]
- [[test_regex_fallback_requires_separator()]] - `contains` [EXTRACTED]
- [[test_ssn_detection()]] - `contains` [EXTRACTED]
- [[test_telegram_uid_not_redacted_as_phone()]] - `contains` [EXTRACTED]
- [[test_uid_inside_parens_preserved()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_435