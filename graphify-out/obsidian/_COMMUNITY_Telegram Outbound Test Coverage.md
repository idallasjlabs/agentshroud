---
type: community
cohesion: 0.03
members: 61
---

# Telegram Outbound Test Coverage

**Cohesion:** 0.03 - loosely connected
**Members:** 61 nodes

## Members
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_block_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_security_monitoring_threshold_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_pipeline_block_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_preserved_without_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_with_punctuation_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_numeric_tld_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_truncated_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Control characters in leaked URL should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains with numeric TLDs should not enter approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload threshold disclosures should normalize to policy-block notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload timeout rewrites should also map to protected unavailable notice fo]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload user-id enrollment leakage should also be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded sendMessage bodies must also be scanned by the pipeline.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses message fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, owner messages should still go through.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy bracket-style block notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped with punctuation should still be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner HTML formatting should preserve parse_mode.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner form messages still pass through when the pipeline crashes.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Percent-encoded control bytes should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked form payloads to non-owners must be replaced with a safe notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated identical web_fetch leaks should not spam approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notices should be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should still apply when sender forgets system header.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Truncated 'current model' replies should be rewritten to deterministic model hin]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Variant wording should still map to generic runtime guidance by default.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Wording variants for healthcheck SKILL.md sandbox errors should be rewritten.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Outbound_Test_Coverage
SORT file.name ASC
```

## Connections to other communities
- 62 edges to [[_COMMUNITY_Telegram Outbound Test Rationale]]
- 60 edges to [[_COMMUNITY_Telegram Proxy Outbound Tests]]
- 9 edges to [[_COMMUNITY_Module Group 217]]
- 7 edges to [[_COMMUNITY_Module Group 287]]
- 5 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 5 edges to [[_COMMUNITY_Module Group 338]]
- 4 edges to [[_COMMUNITY_Module Group 390]]
- 2 edges to [[_COMMUNITY_Module Group 497]]
- 1 edge to [[_COMMUNITY_Authentication & Rate Limiting]]
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
- 1 edge to [[_COMMUNITY_Module Group 446]]
- 1 edge to [[_COMMUNITY_Module Group 472]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 101 communities
- [[.test_form_outbound_pipeline_block_non_owner()]] - degree 5, connects to 3 communities
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - degree 4, connects to 2 communities
- [[.test_collaborator_form_high_risk_leakage_text_is_normalized()]] - degree 4, connects to 2 communities
- [[.test_collaborator_legacy_block_notice_is_normalized_json()]] - degree 4, connects to 2 communities
