---
type: community
members: 21
---

# ._is_valid_domain_name

**Members:** 21 nodes

## Members
- [[dot-_is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_is_valid_domain_name_accepts_hyphenated_inner_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_accepts_mixed_case_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_accepts_numeric_inner_labels()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_accepts_standard_host()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_accepts_uppercase_input_via_normalization()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_enforces_tld_rules()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_handles_none_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_empty_or_whitespace()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_leading_or_trailing_dot()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_malformed_hosts()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_overlong_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_overlong_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_punycode_and_non_ascii_labels()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_single_label_host()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_underscore_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_rejects_whitespace_inside_label()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_valid_domain_name_strips_surrounding_whitespace()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDomainValidationHelper]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for domain validator used by egress approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_valid_domain_name
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]

## Top bridge nodes
- [[TestDomainValidationHelper]] - degree 20, connects to 2 communities
- [[dot-_is_valid_domain_name()]] - degree 20, connects to 2 communities
