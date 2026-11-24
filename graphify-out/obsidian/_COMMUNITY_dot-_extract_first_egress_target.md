---
type: community
members: 25
---

# ._extract_first_egress_target

**Members:** 25 nodes

## Members
- [[dot-_extract_first_egress_target()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_extract_first_egress_target_accepts_uppercase_http_scheme()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_does_not_treat_email_as_domain_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_handles_bare_domain_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_handles_empty_inputs()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_markdown_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_non_http_scheme_and_uses_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_text_filename_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_ignores_version_like_tokens()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_prefers_first_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_rejects_ip_literal_bare_target()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_returns_none_when_no_url_or_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_email_then_finds_http_url()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_md_filenames()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_protocol_relative_host_without_tld()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_strips_markdown_wrapper_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_strips_trailing_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_parenthesized_bare_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_protocol_relative_urls()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_supports_protocol_relative_with_query()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_trims_wrapping_quotes()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[BOOTSTRAP.md must NOT be treated as an egress domain.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Extract first outbound web target (URL or bare domain) for egress preflight.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestEgressTargetExtraction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound target extraction helper used by egress preflight.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_extract_first_egress_target
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[dot-_extract_first_egress_target()]] - degree 25, connects to 2 communities
- [[TestEgressTargetExtraction]] - degree 22, connects to 2 communities
- [[dot-test_extract_first_egress_target_skips_md_filenames()]] - degree 3, connects to 1 community
