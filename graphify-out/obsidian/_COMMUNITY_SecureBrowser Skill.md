---
type: community
cohesion: 0.05
members: 41
---

# SecureBrowser Skill

**Cohesion:** 0.05 - loosely connected
**Members:** 41 nodes

## Members
- [[.test_collaboration_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_execute_verb_is_blocked()]] - code - gateway/tests/test_telegram_proxy_outbound.py
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
- [[.test_file_query_is_blocked()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_formatting_trick_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_greeting_bypasses_interrogative_requirement()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_greeting_good_morning_is_safe()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_greeting_hello_is_safe()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_greeting_hey_is_safe()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_greeting_hi_is_safe()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_no_match_without_tokens()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_password_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pii_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_protection_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_refuse_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_restrict_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_sanitiz_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_security_model_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_what_can_you_question()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Classifier for conceptual collaborator questions.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestEgressTargetExtraction]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestLooksLikeSafeCollaboratorInfoQuery]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound target extraction helper used by egress preflight.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecureBrowser_Skill
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY__wrap_response()]]

## Top bridge nodes
- [[TestEgressTargetExtraction]] - degree 25, connects to 3 communities
- [[TestLooksLikeSafeCollaboratorInfoQuery]] - degree 24, connects to 3 communities