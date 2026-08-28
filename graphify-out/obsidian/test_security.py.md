---
source_file: "gateway/tests/test_security.py"
type: "code"
community: "Config Validation & Router"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Config_Validation__Router
---

# test_security.py

## Connections
- [[ForwardRequest]] - `imports` [EXTRACTED]
- [[RateLimiter]] - `imports` [EXTRACTED]
- [[gatewayingest_apiauth.py (RateLimiter, verify_token)]] - `references` [EXTRACTED]
- [[test_constant_time_comparison()]] - `contains` [EXTRACTED]
- [[test_empty_content_rejection()]] - `contains` [EXTRACTED]
- [[test_extremely_long_content()]] - `contains` [EXTRACTED]
- [[test_false_positive_patterns()]] - `contains` [EXTRACTED]
- [[test_invalid_source_rejection()]] - `contains` [EXTRACTED]
- [[test_malformed_json_metadata()]] - `contains` [EXTRACTED]
- [[test_multiple_same_type_pii()]] - `contains` [EXTRACTED]
- [[test_nested_pii_patterns()]] - `contains` [EXTRACTED]
- [[test_null_bytes_in_content()]] - `contains` [EXTRACTED]
- [[test_rate_limiter()]] - `contains` [EXTRACTED]
- [[test_shortcut_content_types_accepted()]] - `contains` [EXTRACTED]
- [[test_shortcut_empty_content_rejected()]] - `contains` [EXTRACTED]
- [[test_shortcut_rejects_unknown_content_type()]] - `contains` [EXTRACTED]
- [[test_shortcut_source_accepted()]] - `contains` [EXTRACTED]
- [[test_special_characters_in_pii()]] - `contains` [EXTRACTED]
- [[test_sql_injection_attempt()]] - `contains` [EXTRACTED]
- [[test_timing_attack_resistance()]] - `contains` [EXTRACTED]
- [[test_unicode_content()]] - `contains` [EXTRACTED]
- [[test_valid_sources()]] - `contains` [EXTRACTED]
- [[test_very_large_content()]] - `contains` [EXTRACTED]
- [[test_xss_attempt()]] - `contains` [EXTRACTED]
- [[verify_token()]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Config_Validation__Router