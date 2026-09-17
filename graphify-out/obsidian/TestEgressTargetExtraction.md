---
source_file: "gateway/tests/test_telegram_proxy_outbound.py"
type: "code"
community: "Tool Result Sanitizer & XML Injection Filtering"
location: "L3845"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tool_Result_Sanitizer__XML_Injection_Filtering
---

# TestEgressTargetExtraction

## Connections
- [[dot-test_extract_first_egress_target_accepts_uppercase_http_scheme()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_does_not_treat_email_as_domain_target()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_handles_bare_domain_with_query()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_handles_empty_inputs()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_ignores_markdown_filename_token()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_ignores_non_http_scheme_and_uses_bare_domain()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_ignores_text_filename_token()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_ignores_version_like_tokens()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_prefers_first_http_url()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_rejects_ip_literal_bare_target()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_returns_none_when_no_url_or_domain()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_skips_email_then_finds_http_url()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_skips_protocol_relative_host_without_tld()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_strips_markdown_wrapper_punctuation()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_strips_trailing_punctuation()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_supports_parenthesized_bare_domain()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_supports_protocol_relative_urls()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_supports_protocol_relative_with_query()]] - `method` [EXTRACTED]
- [[dot-test_extract_first_egress_target_trims_wrapping_quotes()]] - `method` [EXTRACTED]
- [[CollaboratorActivityTracker_1]] - `uses` [INFERRED]
- [[PIIConfig_2]] - `uses` [INFERRED]
- [[PIISanitizer]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[Unit tests for outbound target extraction helper used by egress preflight.]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tool_Result_Sanitizer__XML_Injection_Filtering