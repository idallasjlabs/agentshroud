---
type: community
cohesion: 0.03
members: 74
---

# Telegram Outbound Test Rationale

**Cohesion:** 0.03 - loosely connected
**Members:** 74 nodes

## Members
- [[.test_agent_failed_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_empty_text_with_message_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_payload_with_draft_field_is_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_removed_for_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_llm_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_draft_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_tool_call_json_with_zero_width_chars_is_suppressed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_non_standard_port_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_punycode_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_queues_egress_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_scheme_relative_url_queues_https_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_runtime_profile_memory_error_text_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_sanitize_reason_hides_internal_paths()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_timeout_error_is_sanitized_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_timeout_error_is_sanitized_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Agent timeout prefix variants should also map to retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive internal egress approval banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Consecutive-dot domains should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains over 253 chars should be rejected before queueing approvals.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedding provider wording variants should rewrite for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Empty text field must not bypass filtering when caption contains tool payload.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload empty text should not shadow message filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload using draft field should still suppress tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTML parse mode should be dropped for redaction placeholder tokens.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when form payload uses messag]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphen-separated embedding-provider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphenated embedding-provider wording should still trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal pseudo-TLD hosts should be rejected from approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON content field should keep healthcheck sandbox text unchanged when SKILL]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped in markdown fence should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Obfuscated tool-call JSON should still be normalized and suppressed.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Previously emitted runtime-profile memory text should be normalized to generic g]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PunycodeIDN domains should be rejected from approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw timeout errors should be rewritten to deterministic retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw web_fetch JSON should queue interactive egress approval for the destination.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Runtime memory provider errors should rewrite when payload uses draft field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Scheme-relative URLs in leaked JSON should normalize to HTTPS approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundPipelineIntegration]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _filter_outbound calls the full security pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Timeout rewrites should apply to urlencoded Telegram payloads too.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Timeout rewrites should apply when JSON payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing quote punctuation in leaked URL should still normalize and queue approv]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Uppercase HTTP schemes should normalize and queue on port 80.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[User-facing block reasons should not expose modules or file paths.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[web_fetch approvals should not queue for non-standard destination ports.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Outbound_Test_Rationale
SORT file.name ASC
```

## Connections to other communities
- 62 edges to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 62 edges to [[_COMMUNITY_Telegram Proxy Outbound Tests]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 140]]
- 1 edge to [[_COMMUNITY_Module Group 747]]
- 1 edge to [[_COMMUNITY_Module Group 689]]
- 1 edge to [[_COMMUNITY_Module Group 759]]
- 1 edge to [[_COMMUNITY_Module Group 679]]
- 1 edge to [[_COMMUNITY_Module Group 686]]
- 1 edge to [[_COMMUNITY_Module Group 684]]
- 1 edge to [[_COMMUNITY_Module Group 682]]
- 1 edge to [[_COMMUNITY_Module Group 680]]
- 1 edge to [[_COMMUNITY_Module Group 681]]
- 1 edge to [[_COMMUNITY_Module Group 683]]
- 1 edge to [[_COMMUNITY_Module Group 685]]
- 1 edge to [[_COMMUNITY_Module Group 763]]
- 1 edge to [[_COMMUNITY_Module Group 760]]
- 1 edge to [[_COMMUNITY_Module Group 761]]
- 1 edge to [[_COMMUNITY_Module Group 678]]
- 1 edge to [[_COMMUNITY_Module Group 758]]
- 1 edge to [[_COMMUNITY_Module Group 688]]
- 1 edge to [[_COMMUNITY_Module Group 687]]
- 1 edge to [[_COMMUNITY_Module Group 735]]
- 1 edge to [[_COMMUNITY_Module Group 714]]
- 1 edge to [[_COMMUNITY_Module Group 756]]
- 1 edge to [[_COMMUNITY_Module Group 704]]
- 1 edge to [[_COMMUNITY_Module Group 755]]
- 1 edge to [[_COMMUNITY_Module Group 708]]
- 1 edge to [[_COMMUNITY_Module Group 693]]
- 1 edge to [[_COMMUNITY_Module Group 698]]
- 1 edge to [[_COMMUNITY_Module Group 694]]
- 1 edge to [[_COMMUNITY_Module Group 706]]
- 1 edge to [[_COMMUNITY_Module Group 690]]
- 1 edge to [[_COMMUNITY_Module Group 705]]
- 1 edge to [[_COMMUNITY_Module Group 691]]
- 1 edge to [[_COMMUNITY_Module Group 717]]
- 1 edge to [[_COMMUNITY_Module Group 721]]
- 1 edge to [[_COMMUNITY_Module Group 723]]
- 1 edge to [[_COMMUNITY_Module Group 719]]
- 1 edge to [[_COMMUNITY_Module Group 711]]
- 1 edge to [[_COMMUNITY_Module Group 737]]
- 1 edge to [[_COMMUNITY_Module Group 740]]
- 1 edge to [[_COMMUNITY_Module Group 696]]
- 1 edge to [[_COMMUNITY_Module Group 700]]
- 1 edge to [[_COMMUNITY_Module Group 697]]
- 1 edge to [[_COMMUNITY_Module Group 702]]
- 1 edge to [[_COMMUNITY_Module Group 701]]
- 1 edge to [[_COMMUNITY_Module Group 707]]
- 1 edge to [[_COMMUNITY_Module Group 692]]
- 1 edge to [[_COMMUNITY_Module Group 766]]
- 1 edge to [[_COMMUNITY_Module Group 695]]
- 1 edge to [[_COMMUNITY_Module Group 677]]
- 1 edge to [[_COMMUNITY_Module Group 767]]
- 1 edge to [[_COMMUNITY_Module Group 752]]
- 1 edge to [[_COMMUNITY_Module Group 709]]
- 1 edge to [[_COMMUNITY_Module Group 764]]
- 1 edge to [[_COMMUNITY_Module Group 765]]
- 1 edge to [[_COMMUNITY_Module Group 749]]
- 1 edge to [[_COMMUNITY_Module Group 750]]
- 1 edge to [[_COMMUNITY_Module Group 754]]
- 1 edge to [[_COMMUNITY_Module Group 753]]
- 1 edge to [[_COMMUNITY_Module Group 729]]
- 1 edge to [[_COMMUNITY_Module Group 725]]
- 1 edge to [[_COMMUNITY_Module Group 728]]
- 1 edge to [[_COMMUNITY_Module Group 726]]
- 1 edge to [[_COMMUNITY_Module Group 727]]
- 1 edge to [[_COMMUNITY_Module Group 751]]
- 1 edge to [[_COMMUNITY_Module Group 730]]
- 1 edge to [[_COMMUNITY_Module Group 732]]
- 1 edge to [[_COMMUNITY_Module Group 731]]
- 1 edge to [[_COMMUNITY_Module Group 733]]
- 1 edge to [[_COMMUNITY_Module Group 739]]
- 1 edge to [[_COMMUNITY_Module Group 734]]
- 1 edge to [[_COMMUNITY_Module Group 736]]
- 1 edge to [[_COMMUNITY_Module Group 738]]
- 1 edge to [[_COMMUNITY_Module Group 744]]
- 1 edge to [[_COMMUNITY_Module Group 746]]
- 1 edge to [[_COMMUNITY_Module Group 742]]
- 1 edge to [[_COMMUNITY_Module Group 748]]
- 1 edge to [[_COMMUNITY_Module Group 741]]
- 1 edge to [[_COMMUNITY_Module Group 743]]
- 1 edge to [[_COMMUNITY_Module Group 745]]
- 1 edge to [[_COMMUNITY_Module Group 757]]
- 1 edge to [[_COMMUNITY_Module Group 699]]
- 1 edge to [[_COMMUNITY_Module Group 703]]
- 1 edge to [[_COMMUNITY_Module Group 762]]
- 1 edge to [[_COMMUNITY_Module Group 724]]
- 1 edge to [[_COMMUNITY_Module Group 710]]
- 1 edge to [[_COMMUNITY_Module Group 713]]
- 1 edge to [[_COMMUNITY_Module Group 715]]
- 1 edge to [[_COMMUNITY_Module Group 712]]
- 1 edge to [[_COMMUNITY_Module Group 716]]
- 1 edge to [[_COMMUNITY_Module Group 720]]
- 1 edge to [[_COMMUNITY_Module Group 722]]
- 1 edge to [[_COMMUNITY_Module Group 718]]

## Top bridge nodes
- [[TestOutboundPipelineIntegration]] - degree 188, connects to 96 communities
- [[.test_agent_failed_timeout_error_is_sanitized()]] - degree 4, connects to 2 communities
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_form_empty_text_with_message_payload_is_normalized()]] - degree 4, connects to 2 communities