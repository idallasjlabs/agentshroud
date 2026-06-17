---
type: community
cohesion: 0.08
members: 26
---

# Module Group 187

**Cohesion:** 0.08 - loosely connected
**Members:** 26 nodes

## Members
- [[.test_contains_high_risk_leakage_detects_bootstrap_md_in_content_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_high_risk_leakage_detects_function_calls_xml()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_high_risk_leakage_detects_identity_md_in_reveal_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_high_risk_leakage_detects_invoke_xml()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_high_risk_leakage_skips_bootstrap_md_in_denial_context()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_high_risk_leakage_skips_protected_header_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_detects_allow_always_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_detects_allow_once_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_detects_deny_callback()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_detects_standard_banner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_ignores_normal_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_internal_approval_banner_ignores_unrelated_deny_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_legacy_block_notice_detects_legacy_bracket_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contains_legacy_block_notice_detects_legacy_protected_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_skips_identity_md()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_skips_md_filenames()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_extract_first_egress_target_still_catches_real_domains()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_no_reply_token_accepts_fenced_and_punctuated_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_is_no_reply_token_rejects_non_token_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_looks_like_filename_reference_catches_common_extensions()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_looks_like_filename_reference_rejects_real_domains()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[BOOTSTRAP.md must NOT be treated as an egress domain.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Our own protected notices must never be double-filtered.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundClassifierHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound helper classifiers used by collaborator filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[bootstrap.md mentioned in a denial should NOT trigger the high-risk filter.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_187
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]

## Top bridge nodes
- [[TestOutboundClassifierHelpers]] - degree 27, connects to 3 communities