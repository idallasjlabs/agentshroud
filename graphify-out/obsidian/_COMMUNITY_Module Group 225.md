---
type: community
cohesion: 0.10
members: 21
---

# Module Group 225

**Cohesion:** 0.10 - loosely connected
**Members:** 21 nodes

## Members
- [[.test_extract_first_egress_target_accepts_uppercase_http_scheme()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_does_not_treat_email_as_domain_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_handles_bare_domain_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_handles_empty_inputs()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_ignores_markdown_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_ignores_non_http_scheme_and_uses_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_ignores_text_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_ignores_version_like_tokens()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_prefers_first_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_rejects_ip_literal_bare_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_returns_none_when_no_url_or_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_skips_email_then_finds_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_skips_protocol_relative_host_without_tld()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_strips_markdown_wrapper_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_strips_trailing_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_supports_parenthesized_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_supports_protocol_relative_urls()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_supports_protocol_relative_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_trims_wrapping_quotes()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressTargetExtraction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound target extraction helper used by egress preflight.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_225
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]

## Top bridge nodes
- [[TestEgressTargetExtraction]] - degree 25, connects to 3 communities