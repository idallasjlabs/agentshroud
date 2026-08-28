---
type: community
cohesion: 0.03
members: 60
---

# Community 93

**Cohesion:** 0.03 - loosely connected
**Members:** 60 nodes

## Members
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_pairing_code_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_generic_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_content()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_llm_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_slash_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_system_startup_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_numeric_tld_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_scheme_relative_url_queues_https_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_unknown_model_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_draft_payload_tool_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should never receive pairing codes or pairing approval commands.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Cooldown dedupe must not suppress approvals when schemeport risk changes.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains with numeric TLDs should not enter approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider hints without explicit error marker should not trigger rewrit]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicit memory-search command context should keep memory-specific remediation t]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form content should keep healthcheck sandbox text unchanged when SKILL.md marker]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload NO_REPLY punctuation variant should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload approval banners must be redacted for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload embeddingprovider hints without 'error' should keep original text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded draft payloads must not leak raw tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Generic session spawn JSON should be rewritten, not shown raw.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL messages without sandbox context should not trigger sandbox re]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multiline fenced NO_REPLY token should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw timeout errors should be rewritten to deterministic retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Scheme-relative URLs in leaked JSON should normalize to HTTPS approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Slash-separated embeddingprovider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[System startup notice should be deduplicated in a short cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown model errors should be rewritten without leaking raw stack text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_93
SORT file.name ASC
```

## Connections to other communities
- 61 edges to [[_COMMUNITY_Community 80]]
- 58 edges to [[_COMMUNITY_Community 96]]
- 9 edges to [[_COMMUNITY_Community 408]]
- 7 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 7 edges to [[_COMMUNITY_Community 591]]
- 5 edges to [[_COMMUNITY_Community 775]]
- 4 edges to [[_COMMUNITY_Community 1283]]
- 4 edges to [[_COMMUNITY_Community 1284]]
- 4 edges to [[_COMMUNITY_Community 816]]
- 2 edges to [[_COMMUNITY_Community 1135]]
- 2 edges to [[_COMMUNITY_Community 1431]]
- 1 edge to [[_COMMUNITY_Community 1651]]
- 1 edge to [[_COMMUNITY_Community 1632]]
- 1 edge to [[_COMMUNITY_Community 1582]]
- 1 edge to [[_COMMUNITY_Community 1581]]
- 1 edge to [[_COMMUNITY_Community 1641]]
- 1 edge to [[_COMMUNITY_Community 1646]]
- 1 edge to [[_COMMUNITY_Community 1643]]
- 1 edge to [[_COMMUNITY_Community 1642]]
- 1 edge to [[_COMMUNITY_Community 1644]]
- 1 edge to [[_COMMUNITY_Community 1650]]
- 1 edge to [[_COMMUNITY_Community 1649]]
- 1 edge to [[_COMMUNITY_Community 1580]]
- 1 edge to [[_COMMUNITY_Community 1648]]
- 1 edge to [[_COMMUNITY_Community 1647]]
- 1 edge to [[_COMMUNITY_Community 1605]]
- 1 edge to [[_COMMUNITY_Community 1613]]
- 1 edge to [[_COMMUNITY_Community 1607]]
- 1 edge to [[_COMMUNITY_Community 1600]]
- 1 edge to [[_COMMUNITY_Community 1592]]
- 1 edge to [[_COMMUNITY_Community 1597]]
- 1 edge to [[_COMMUNITY_Community 1604]]
- 1 edge to [[_COMMUNITY_Community 1590]]
- 1 edge to [[_COMMUNITY_Community 1639]]
- 1 edge to [[_COMMUNITY_Community 1595]]
- 1 edge to [[_COMMUNITY_Community 1583]]
- 1 edge to [[_COMMUNITY_Community 1584]]
- 1 edge to [[_COMMUNITY_Community 1599]]
- 1 edge to [[_COMMUNITY_Community 1624]]
- 1 edge to [[_COMMUNITY_Community 1619]]
- 1 edge to [[_COMMUNITY_Community 1634]]
- 1 edge to [[_COMMUNITY_Community 1587]]
- 1 edge to [[_COMMUNITY_Community 1591]]
- 1 edge to [[_COMMUNITY_Community 1593]]
- 1 edge to [[_COMMUNITY_Community 1588]]
- 1 edge to [[_COMMUNITY_Community 1660]]
- 1 edge to [[_COMMUNITY_Community 1585]]
- 1 edge to [[_COMMUNITY_Community 1578]]
- 1 edge to [[_COMMUNITY_Community 1655]]
- 1 edge to [[_COMMUNITY_Community 1657]]
- 1 edge to [[_COMMUNITY_Community 1636]]
- 1 edge to [[_COMMUNITY_Community 1596]]
- 1 edge to [[_COMMUNITY_Community 1579]]
- 1 edge to [[_COMMUNITY_Community 1586]]
- 1 edge to [[_COMMUNITY_Community 1652]]
- 1 edge to [[_COMMUNITY_Community 1637]]
- 1 edge to [[_COMMUNITY_Community 1638]]
- 1 edge to [[_COMMUNITY_Community 1659]]
- 1 edge to [[_COMMUNITY_Community 1602]]
- 1 edge to [[_COMMUNITY_Community 1603]]
- 1 edge to [[_COMMUNITY_Community 1601]]
- 1 edge to [[_COMMUNITY_Community 1635]]
- 1 edge to [[_COMMUNITY_Community 1611]]
- 1 edge to [[_COMMUNITY_Community 1610]]
- 1 edge to [[_COMMUNITY_Community 1609]]
- 1 edge to [[_COMMUNITY_Community 1612]]
- 1 edge to [[_COMMUNITY_Community 1617]]
- 1 edge to [[_COMMUNITY_Community 1614]]
- 1 edge to [[_COMMUNITY_Community 1627]]
- 1 edge to [[_COMMUNITY_Community 1615]]
- 1 edge to [[_COMMUNITY_Community 1606]]
- 1 edge to [[_COMMUNITY_Community 1616]]
- 1 edge to [[_COMMUNITY_Community 1623]]
- 1 edge to [[_COMMUNITY_Community 1626]]
- 1 edge to [[_COMMUNITY_Community 1629]]
- 1 edge to [[_COMMUNITY_Community 1628]]
- 1 edge to [[_COMMUNITY_Community 1630]]
- 1 edge to [[_COMMUNITY_Community 1608]]
- 1 edge to [[_COMMUNITY_Community 1631]]
- 1 edge to [[_COMMUNITY_Community 1620]]
- 1 edge to [[_COMMUNITY_Community 1633]]
- 1 edge to [[_COMMUNITY_Community 1621]]
- 1 edge to [[_COMMUNITY_Community 1618]]
- 1 edge to [[_COMMUNITY_Community 1622]]
- 1 edge to [[_COMMUNITY_Community 1625]]
- 1 edge to [[_COMMUNITY_Community 1656]]
- 1 edge to [[_COMMUNITY_Community 1640]]
- 1 edge to [[_COMMUNITY_Community 1589]]
- 1 edge to [[_COMMUNITY_Community 1594]]
- 1 edge to [[_COMMUNITY_Community 1645]]
- 1 edge to [[_COMMUNITY_Community 1653]]
- 1 edge to [[_COMMUNITY_Community 1654]]
- 1 edge to [[_COMMUNITY_Community 1658]]
- 1 edge to [[_COMMUNITY_Community 1598]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 1285]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 96 communities
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - degree 4, connects to 2 communities
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - degree 4, connects to 2 communities
- [[.test_collaborator_pairing_code_leakage_is_redacted_json()]] - degree 4, connects to 2 communities