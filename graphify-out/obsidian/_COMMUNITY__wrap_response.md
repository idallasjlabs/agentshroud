---
type: community
members: 52
---

# _wrap_response

**Members:** 52 nodes

## Members
- [[dot-test_blocked_command_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_blocked_command_uppercase_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_blocked_command_with_mention_and_punctuation_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_blocked_command_with_zero_width_mention_and_punctuation_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_allowlist_bypass_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_command_blocking_question_gets_safe_info_not_denial()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_model_switch_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_secret_value_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_healthcheck_word_with_punctuation_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_model_status_command_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_bare_domain_triggers_egress_preflight_approval()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_domain_like_token_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_malformed_hyphen_domain_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_malformed_url_normalizes_for_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_numeric_tld_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_percent_encoded_control_url_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_oversized_document_update_is_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_help_uses_local_notice_and_includes_revoke()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_revoke_command_requires_target_user_id()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[model should be answered by gateway directly (no model invocation).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Allowlistredirect-bypass prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Approval preflight should reject domains with non-alphabetic TLDs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Bare domains without scheme should still queue preflight egress approval.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Blocked collaborator commands should be retained in quarantine store.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator command-policy questions should get informative guidance, not hard…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator modelprovider switching requests should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Direct secrettoken value requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Domain-like tokens followed by identifier chars should not be treated as URLs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size  limit must be dropped (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Leading-dot hosts should be normalized before preflight approval check.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Malformed domain labels in URLs should not queue preflight approvals.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Mention + punctuation variants should still be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Non-slash healthcheck command with punctuation should still be local-handled.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner help should be handled locally and include admin approval commands.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner revoke without target should return usage guidance.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Percent-encoded control bytes in URL should block preflight queueing.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Uppercase collaborator blocked commands should still be quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width + mentionpunctuation blocked command variants should still be…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_wrap_response()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_26]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_27]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_28]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_29]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_30]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_31]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_28]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_29]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_30]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_31]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_32]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response
SORT file.name ASC
```

## Connections to other communities
- 160 edges to [[_COMMUNITY_FakeRBAC]]
- 37 edges to [[_COMMUNITY_dot-_make_proxy]]
- 33 edges to [[_COMMUNITY_fake_urlopen]]
- 30 edges to [[_COMMUNITY_asyncio_7]]
- 20 edges to [[_COMMUNITY_fake_owner_notice]]
- 10 edges to [[_COMMUNITY_dot-test_collaborator_web_access_imperative_with_url_queues_owner_approval]]
- 6 edges to [[_COMMUNITY_BlockingPipeline]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 3 edges to [[_COMMUNITY_dot-test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative]]
- 3 edges to [[_COMMUNITY_dot-test_collaborator_rate_limit_resets_after_window]]
- 3 edges to [[_COMMUNITY_dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message]]
- 3 edges to [[_COMMUNITY_dot-test_proxy_request_returns_ack_only_updates_when_all_dropped]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_direct_file_query_returns_protect_file_notice]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_rate_limit_notice_includes_retry_window]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_with_fullwidth_chars_is_handled_locally]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_with_leading_whitespace_is_handled_locally]]
- 1 edge to [[_COMMUNITY_dot-test_owner_pending_command_shows_pending_active_and_revoked]]
- 1 edge to [[_COMMUNITY_dot-test_self_diagnose_with_mention_is_handled_locally]]
- 1 edge to [[_COMMUNITY_dot-test_self_diagnose_with_zero_width_char_is_handled_locally]]
- 1 edge to [[_COMMUNITY_dot-test_self_diagnostic_with_punctuation_is_handled_locally_for_collaborator]]

## Top bridge nodes
- [[_wrap_response()]] - degree 236, connects to 20 communities
- [[dot-test_collaborator_command_blocking_question_gets_safe_info_not_denial()]] - degree 9, connects to 3 communities
- [[dot-test_healthcheck_word_with_punctuation_is_handled_locally()]] - degree 9, connects to 3 communities
- [[dot-test_model_status_command_is_handled_locally()]] - degree 9, connects to 3 communities
- [[dot-test_owner_help_uses_local_notice_and_includes_revoke()]] - degree 9, connects to 3 communities
