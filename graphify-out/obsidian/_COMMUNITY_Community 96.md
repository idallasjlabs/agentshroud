---
type: community
cohesion: 0.04
members: 58
---

# Community 96

**Cohesion:** 0.04 - loosely connected
**Members:** 58 nodes

## Members
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_caption_tool_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_form_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_preserved_without_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_case_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pii_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pipeline_receives_trust_level()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_delayed_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_duplicate_no_reply_messages_return_deterministic_reply()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_invalid_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive internal egress approval banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Control characters in leaked URL should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form caption field should be filtered the same as textdraftmessage fields.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should be rewritten for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type must not bypass outbound JSON leak filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mixed-case wording variants should still trigger generic runtime guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-domain hosts should not queue egress approval requests.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner HTML formatting should preserve parse_mode.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Phone numbers in outbound messages must be redacted by PII sanitizer.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Proxy should pass ownernon-owner trust level into outbound pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated NO_REPLY payloads should still return deterministic non-empty replies.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing markdown backtick in leaked URL should normalize for approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is se]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_96
SORT file.name ASC
```

## Connections to other communities
- 61 edges to [[_COMMUNITY_Community 80]]
- 58 edges to [[_COMMUNITY_Community 93]]
- 9 edges to [[_COMMUNITY_Community 408]]
- 7 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 7 edges to [[_COMMUNITY_Community 591]]
- 5 edges to [[_COMMUNITY_Community 775]]
- 4 edges to [[_COMMUNITY_Community 1283]]
- 4 edges to [[_COMMUNITY_Community 1284]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Adversarial Injection Guards]]
- 2 edges to [[_COMMUNITY_Community 1431]]
- 2 edges to [[_COMMUNITY_Community 1135]]
- 1 edge to [[_COMMUNITY_Community 1645]]
- 1 edge to [[_COMMUNITY_Community 1652]]
- 1 edge to [[_COMMUNITY_Community 1579]]
- 1 edge to [[_COMMUNITY_Community 1586]]
- 1 edge to [[_COMMUNITY_Community 1592]]
- 1 edge to [[_COMMUNITY_Community 1597]]
- 1 edge to [[_COMMUNITY_Community 1600]]
- 1 edge to [[_COMMUNITY_Community 1607]]
- 1 edge to [[_COMMUNITY_Community 1613]]
- 1 edge to [[_COMMUNITY_Community 1619]]
- 1 edge to [[_COMMUNITY_Community 1624]]
- 1 edge to [[_COMMUNITY_Community 1632]]
- 1 edge to [[_COMMUNITY_Community 1634]]
- 1 edge to [[_COMMUNITY_Community 1635]]
- 1 edge to [[_COMMUNITY_Community 1636]]
- 1 edge to [[_COMMUNITY_Community 1637]]
- 1 edge to [[_COMMUNITY_Community 1638]]
- 1 edge to [[_COMMUNITY_Community 1639]]
- 1 edge to [[_COMMUNITY_Community 1640]]
- 1 edge to [[_COMMUNITY_Community 1641]]
- 1 edge to [[_COMMUNITY_Community 1642]]
- 1 edge to [[_COMMUNITY_Community 1643]]
- 1 edge to [[_COMMUNITY_Community 1644]]
- 1 edge to [[_COMMUNITY_Community 1646]]
- 1 edge to [[_COMMUNITY_Community 1647]]
- 1 edge to [[_COMMUNITY_Community 1648]]
- 1 edge to [[_COMMUNITY_Community 1649]]
- 1 edge to [[_COMMUNITY_Community 1650]]
- 1 edge to [[_COMMUNITY_Community 1651]]
- 1 edge to [[_COMMUNITY_Community 1653]]
- 1 edge to [[_COMMUNITY_Community 1654]]
- 1 edge to [[_COMMUNITY_Community 1655]]
- 1 edge to [[_COMMUNITY_Community 1656]]
- 1 edge to [[_COMMUNITY_Community 1657]]
- 1 edge to [[_COMMUNITY_Community 1658]]
- 1 edge to [[_COMMUNITY_Community 1659]]
- 1 edge to [[_COMMUNITY_Community 1660]]
- 1 edge to [[_COMMUNITY_Community 1578]]
- 1 edge to [[_COMMUNITY_Community 1580]]
- 1 edge to [[_COMMUNITY_Community 1581]]
- 1 edge to [[_COMMUNITY_Community 1582]]
- 1 edge to [[_COMMUNITY_Community 1583]]
- 1 edge to [[_COMMUNITY_Community 1584]]
- 1 edge to [[_COMMUNITY_Community 1585]]
- 1 edge to [[_COMMUNITY_Community 1587]]
- 1 edge to [[_COMMUNITY_Community 1588]]
- 1 edge to [[_COMMUNITY_Community 1589]]
- 1 edge to [[_COMMUNITY_Community 1590]]
- 1 edge to [[_COMMUNITY_Community 1591]]
- 1 edge to [[_COMMUNITY_Community 1593]]
- 1 edge to [[_COMMUNITY_Community 1594]]
- 1 edge to [[_COMMUNITY_Community 1595]]
- 1 edge to [[_COMMUNITY_Community 1596]]
- 1 edge to [[_COMMUNITY_Community 1598]]
- 1 edge to [[_COMMUNITY_Community 1599]]
- 1 edge to [[_COMMUNITY_Community 1601]]
- 1 edge to [[_COMMUNITY_Community 1602]]
- 1 edge to [[_COMMUNITY_Community 1603]]
- 1 edge to [[_COMMUNITY_Community 1604]]
- 1 edge to [[_COMMUNITY_Community 1605]]
- 1 edge to [[_COMMUNITY_Community 1606]]
- 1 edge to [[_COMMUNITY_Community 1608]]
- 1 edge to [[_COMMUNITY_Community 1609]]
- 1 edge to [[_COMMUNITY_Community 1610]]
- 1 edge to [[_COMMUNITY_Community 1611]]
- 1 edge to [[_COMMUNITY_Community 1612]]
- 1 edge to [[_COMMUNITY_Community 1614]]
- 1 edge to [[_COMMUNITY_Community 1615]]
- 1 edge to [[_COMMUNITY_Community 1616]]
- 1 edge to [[_COMMUNITY_Community 1617]]
- 1 edge to [[_COMMUNITY_Community 1618]]
- 1 edge to [[_COMMUNITY_Community 1620]]
- 1 edge to [[_COMMUNITY_Community 1621]]
- 1 edge to [[_COMMUNITY_Community 1622]]
- 1 edge to [[_COMMUNITY_Community 1623]]
- 1 edge to [[_COMMUNITY_Community 1625]]
- 1 edge to [[_COMMUNITY_Community 1626]]
- 1 edge to [[_COMMUNITY_Community 1627]]
- 1 edge to [[_COMMUNITY_Community 1628]]
- 1 edge to [[_COMMUNITY_Community 1629]]
- 1 edge to [[_COMMUNITY_Community 1630]]
- 1 edge to [[_COMMUNITY_Community 1631]]
- 1 edge to [[_COMMUNITY_Community 1633]]
- 1 edge to [[_COMMUNITY_Community 816]]
- 1 edge to [[_COMMUNITY_Community 1285]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 220, connects to 97 communities
- [[TestDefaultBotId]] - degree 9, connects to 3 communities
- [[.test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_form_caption_tool_payload_is_normalized()]] - degree 4, connects to 2 communities