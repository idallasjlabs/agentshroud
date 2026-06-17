---
type: community
cohesion: 0.03
members: 63
---

# Telegram Proxy Outbound Tests

**Cohesion:** 0.03 - loosely connected
**Members:** 63 nodes

## Members
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_agent_failed_prefix_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_html_code_markup_is_stripped_and_parse_mode_removed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_protected_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_security_monitoring_threshold_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_web_fetch_json_queues_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_case_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_distinct_system_notices()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_filename_reference_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_is_rewritten_to_actionable_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_unknown_model_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound HTML codepre markup should be stripped to plain text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should receive protected unavailable notice for timeout rewrite va]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Different system notices should both be forwarded.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedded web_fetch JSON should still queue interactive egress approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Empty text field must not bypass filtering when content contains tool payload.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicit memory-search command context should keep memory-specific remediation t]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Filename-like references must not be interpreted as egress domains.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep healthcheck SKILL.md text unchanged when sandbox hint i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload NO_REPLY punctuation variant should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy 'Protected' wording should normalize to canonical protected]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck sandbox messages without SKILL.md marker should not trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field with embeddingprovider hints but no error keyword should rem]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy internal tool-output suppression string should normalize to Protect wordi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mixed-case wording variants should still trigger generic runtime guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multiline fenced NO_REPLY token should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pure web_fetch tool-call JSON should be rewritten to user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOwnerMirrorCoalescing]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Threshold status disclosures should normalize to collaborator policy-block notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown model errors should be rewritten without leaking raw stack text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_mirror_to_owner_if_collaborator must coalesce within the window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Proxy_Outbound_Tests
SORT file.name ASC
```

## Connections to other communities
- 62 edges to [[_COMMUNITY_Telegram Outbound Test Rationale]]
- 60 edges to [[_COMMUNITY_Telegram Outbound Test Coverage]]
- 9 edges to [[_COMMUNITY_Module Group 217]]
- 7 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 7 edges to [[_COMMUNITY_Module Group 287]]
- 5 edges to [[_COMMUNITY_Module Group 338]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 2 edges to [[_COMMUNITY_Module Group 140]]
- 2 edges to [[_COMMUNITY_Module Group 497]]
- 1 edge to [[_COMMUNITY_Module Group 749]]
- 1 edge to [[_COMMUNITY_Module Group 762]]
- 1 edge to [[_COMMUNITY_Module Group 765]]
- 1 edge to [[_COMMUNITY_Module Group 714]]
- 1 edge to [[_COMMUNITY_Module Group 735]]
- 1 edge to [[_COMMUNITY_Module Group 737]]
- 1 edge to [[_COMMUNITY_Module Group 740]]
- 1 edge to [[_COMMUNITY_Module Group 747]]
- 1 edge to [[_COMMUNITY_Module Group 750]]
- 1 edge to [[_COMMUNITY_Module Group 751]]
- 1 edge to [[_COMMUNITY_Module Group 752]]
- 1 edge to [[_COMMUNITY_Module Group 753]]
- 1 edge to [[_COMMUNITY_Module Group 754]]
- 1 edge to [[_COMMUNITY_Module Group 755]]
- 1 edge to [[_COMMUNITY_Module Group 756]]
- 1 edge to [[_COMMUNITY_Module Group 757]]
- 1 edge to [[_COMMUNITY_Module Group 758]]
- 1 edge to [[_COMMUNITY_Module Group 759]]
- 1 edge to [[_COMMUNITY_Module Group 760]]
- 1 edge to [[_COMMUNITY_Module Group 761]]
- 1 edge to [[_COMMUNITY_Module Group 763]]
- 1 edge to [[_COMMUNITY_Module Group 764]]
- 1 edge to [[_COMMUNITY_Module Group 766]]
- 1 edge to [[_COMMUNITY_Module Group 767]]
- 1 edge to [[_COMMUNITY_Module Group 677]]
- 1 edge to [[_COMMUNITY_Module Group 678]]
- 1 edge to [[_COMMUNITY_Module Group 679]]
- 1 edge to [[_COMMUNITY_Module Group 680]]
- 1 edge to [[_COMMUNITY_Module Group 681]]
- 1 edge to [[_COMMUNITY_Module Group 682]]
- 1 edge to [[_COMMUNITY_Module Group 683]]
- 1 edge to [[_COMMUNITY_Module Group 684]]
- 1 edge to [[_COMMUNITY_Module Group 685]]
- 1 edge to [[_COMMUNITY_Module Group 686]]
- 1 edge to [[_COMMUNITY_Module Group 687]]
- 1 edge to [[_COMMUNITY_Module Group 688]]
- 1 edge to [[_COMMUNITY_Module Group 689]]
- 1 edge to [[_COMMUNITY_Module Group 690]]
- 1 edge to [[_COMMUNITY_Module Group 691]]
- 1 edge to [[_COMMUNITY_Module Group 692]]
- 1 edge to [[_COMMUNITY_Module Group 693]]
- 1 edge to [[_COMMUNITY_Module Group 694]]
- 1 edge to [[_COMMUNITY_Module Group 695]]
- 1 edge to [[_COMMUNITY_Module Group 696]]
- 1 edge to [[_COMMUNITY_Module Group 697]]
- 1 edge to [[_COMMUNITY_Module Group 698]]
- 1 edge to [[_COMMUNITY_Module Group 699]]
- 1 edge to [[_COMMUNITY_Module Group 700]]
- 1 edge to [[_COMMUNITY_Module Group 701]]
- 1 edge to [[_COMMUNITY_Module Group 702]]
- 1 edge to [[_COMMUNITY_Module Group 703]]
- 1 edge to [[_COMMUNITY_Module Group 704]]
- 1 edge to [[_COMMUNITY_Module Group 705]]
- 1 edge to [[_COMMUNITY_Module Group 706]]
- 1 edge to [[_COMMUNITY_Module Group 707]]
- 1 edge to [[_COMMUNITY_Module Group 708]]
- 1 edge to [[_COMMUNITY_Module Group 709]]
- 1 edge to [[_COMMUNITY_Module Group 710]]
- 1 edge to [[_COMMUNITY_Module Group 711]]
- 1 edge to [[_COMMUNITY_Module Group 712]]
- 1 edge to [[_COMMUNITY_Module Group 713]]
- 1 edge to [[_COMMUNITY_Module Group 715]]
- 1 edge to [[_COMMUNITY_Module Group 716]]
- 1 edge to [[_COMMUNITY_Module Group 717]]
- 1 edge to [[_COMMUNITY_Module Group 718]]
- 1 edge to [[_COMMUNITY_Module Group 719]]
- 1 edge to [[_COMMUNITY_Module Group 720]]
- 1 edge to [[_COMMUNITY_Module Group 721]]
- 1 edge to [[_COMMUNITY_Module Group 722]]
- 1 edge to [[_COMMUNITY_Module Group 723]]
- 1 edge to [[_COMMUNITY_Module Group 724]]
- 1 edge to [[_COMMUNITY_Module Group 725]]
- 1 edge to [[_COMMUNITY_Module Group 726]]
- 1 edge to [[_COMMUNITY_Module Group 727]]
- 1 edge to [[_COMMUNITY_Module Group 728]]
- 1 edge to [[_COMMUNITY_Module Group 729]]
- 1 edge to [[_COMMUNITY_Module Group 730]]
- 1 edge to [[_COMMUNITY_Module Group 731]]
- 1 edge to [[_COMMUNITY_Module Group 732]]
- 1 edge to [[_COMMUNITY_Module Group 733]]
- 1 edge to [[_COMMUNITY_Module Group 734]]
- 1 edge to [[_COMMUNITY_Module Group 736]]
- 1 edge to [[_COMMUNITY_Module Group 738]]
- 1 edge to [[_COMMUNITY_Module Group 739]]
- 1 edge to [[_COMMUNITY_Module Group 741]]
- 1 edge to [[_COMMUNITY_Module Group 742]]
- 1 edge to [[_COMMUNITY_Module Group 743]]
- 1 edge to [[_COMMUNITY_Module Group 744]]
- 1 edge to [[_COMMUNITY_Module Group 745]]
- 1 edge to [[_COMMUNITY_Module Group 746]]
- 1 edge to [[_COMMUNITY_Module Group 748]]
- 1 edge to [[_COMMUNITY_Module Group 390]]
- 1 edge to [[_COMMUNITY_Module Group 472]]
- 1 edge to [[_COMMUNITY_Module Group 446]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 217, connects to 103 communities
- [[TestOwnerMirrorCoalescing]] - degree 8, connects to 3 communities
- [[.test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[.test_collaborator_agent_failed_prefix_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - degree 4, connects to 2 communities