---
type: community
members: 52
---

# TestOutboundClassifierHelpers

**Members:** 52 nodes

## Members
- [[dot-_apply_outbound_status_notices()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_contains_critical_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_contains_high_risk_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_contains_internal_approval_banner()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_contains_legacy_block_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_no_reply_token()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_looks_like_filename_reference()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_contains_high_risk_leakage_detects_bootstrap_md_in_content_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_high_risk_leakage_detects_function_calls_xml()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_high_risk_leakage_detects_identity_md_in_reveal_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_high_risk_leakage_detects_invoke_xml()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_high_risk_leakage_skips_bootstrap_md_in_denial_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_high_risk_leakage_skips_protected_header_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_detects_allow_always_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_detects_allow_once_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_detects_deny_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_detects_standard_banner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_ignores_normal_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_internal_approval_banner_ignores_unrelated_deny_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_legacy_block_notice_detects_legacy_bracket_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contains_legacy_block_notice_detects_legacy_protected_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_skips_identity_md()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_extract_first_egress_target_still_catches_real_domains()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_false_on_empty_string()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_false_on_non_string()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_no_reply_token_accepts_fenced_and_punctuated_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_is_no_reply_token_rejects_non_token_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_looks_like_filename_reference_catches_common_extensions()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_looks_like_filename_reference_rejects_real_domains()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_no_false_positive_on_domain_mention()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_no_false_positive_on_generic_llm_response()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_true_on_callback_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_true_on_deny_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_true_on_real_egress_banner_header()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Best-effort check to avoid treating local file names as egress domains.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Common LLM prose with 'risk', 'tool', 'id' must NOT trigger the matcher.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Detect internal approvalegress banner text that must remain owner-only.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect leakage patterns blocked for local_onlyproject_scoped collaborators.…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect legacy bracket-style block notices for collaborator normalization.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect patterns that must redact for ALL non-owner chats, including…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect plain NO_REPLY sentinel with light punctuation wrapping.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Generic 'domain' mention without the egress emoji must not trigger.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Inline-keyboard callback tokens must always match (egress_allow_always_uuid).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Map internal statuspolicy texts to user-safe replacement notices. Pure helper…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Our own protected notices must never be double-filtered.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestInternalBannerMatcher]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundClassifierHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[The canonical 🌐 Egress Request header from TelegramEgressNotifier must match.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound helper classifiers used by collaborator filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_contains_internal_approval_banner must only fire on real egress banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[bootstrap.md mentioned in a denial should NOT trigger the high-risk filter.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[egress_deny_ callback token must match.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundClassifierHelpers
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 7 edges to [[_COMMUNITY_normalize_input]]
- 6 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 3 edges to [[_COMMUNITY_dot-_extract_first_egress_target]]
- 3 edges to [[_COMMUNITY_asyncio_1]]
- 2 edges to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[dot-_contains_high_risk_collaborator_leakage()]] - degree 11, connects to 4 communities
- [[TestOutboundClassifierHelpers]] - degree 24, connects to 3 communities
- [[dot-_apply_outbound_status_notices()]] - degree 9, connects to 3 communities
- [[dot-_contains_critical_collaborator_leakage()]] - degree 6, connects to 3 communities
- [[dot-_looks_like_filename_reference()]] - degree 6, connects to 3 communities
