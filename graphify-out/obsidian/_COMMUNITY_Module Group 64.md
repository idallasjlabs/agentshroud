---
type: community
cohesion: 0.03
members: 59
---

# Module Group 64

**Cohesion:** 0.03 - loosely connected
**Members:** 59 nodes

## Members
- [[.test_blocked_command_with_fullwidth_mention_and_punctuation_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_blocked_command_with_leading_whitespace_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_encoded_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_file_metadata_question_gets_safe_info()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_file_query_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_high_risk_approval_workflow_question_gets_safe_guidance()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_hypothetical_execution_question_gets_safe_info()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_plugin_discovery_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_web_access_policy_question_with_bare_domain_is_safe()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collaborator_web_access_request_returns_pending_egress_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_filter_disabled_does_not_set_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_healthcheck_local_notice_is_deduped_per_update()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_healthcheck_with_mention_and_punctuation_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_healthcheck_with_zero_width_mention_and_punctuation_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_consecutive_dot_domain_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_internal_suffix_domain_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_ip_url_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_numeric_tld_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_overlong_fqdn_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_overlong_url_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_percent_encoded_control_url_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_non_owner_preflight_cooldown_is_scheme_port_scoped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_approve_command_requires_pending_request()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_healthcheck_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_revoke_command_cannot_revoke_owner()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_owner_status_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_self_diagnose_with_mention_is_handled_locally()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_self_diagnostic_with_punctuation_is_handled_locally_for_collaborator()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unknown_user_repeated_start_still_gets_pending_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Approval preflight should reject domains with non-alphabetic TLDs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Approval workflow questions mentioning system commands should stay informational]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Bare-domain policy questions should be informational, not treated as web executi]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Bot mention + punctuation should still route to local healthcheck handler.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator self-diagnostic punctuation variant should still be local-handled.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator web requests should return deterministic pending-approval wording.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Conceptual file-purpose questions should get safe info without file data access.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Consecutive-dot domains in URLs should not queue preflight approvals.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Domains over 253 chars should be rejected from preflight approval.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Encoded exfiltration prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Fullwidth + mentionpunctuation blocked command variants should still be quarant]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Hypothetical execution policy questions should get safe info, not hard block.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound preflight dedupe should still queue when scheme changes.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Internal file probes must not be misclassified as egress approval requests.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Internalnon-routable pseudo-TLDs should not enter approval queue.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Leading whitespacenewline should not bypass collaborator blocked commands.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Literal IP URL targets should not enter domain approval preflight.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Mentioned self-diagnose variant should still route to local diagnostics handler]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Overly long URLs should be rejected from preflight approval path.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner approve should fail closed when target has no pending request.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner healthcheck should be handled by gateway, not model.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner revoke must fail safely when target is owner id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner status should be handled by gateway with operational summary.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Percent-encoded control bytes in URL should block preflight queueing.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Plugintool auto-discovery inventory prompts should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Same Telegram update_id should not trigger repeated local notices.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown users should still receive pending notice on repeated start during cool]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[When group_mention_only is disabled, eligibility map is not populated.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width + mentionpunctuation healthcheck variants should still route locally]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_wrap_response()]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_64
SORT file.name ASC
```

## Connections to other communities
- 280 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 22 edges to [[_COMMUNITY_Module Group 69]]
- 15 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 3 edges to [[_COMMUNITY_Module Group 260]]
- 3 edges to [[_COMMUNITY_Module Group 445]]
- 2 edges to [[_COMMUNITY_Module Group 308]]
- 1 edge to [[_COMMUNITY_Module Group 673]]
- 1 edge to [[_COMMUNITY_Module Group 676]]
- 1 edge to [[_COMMUNITY_Module Group 675]]
- 1 edge to [[_COMMUNITY_Module Group 671]]
- 1 edge to [[_COMMUNITY_Module Group 674]]
- 1 edge to [[_COMMUNITY_Module Group 672]]

## Top bridge nodes
- [[_wrap_response()]] - degree 217, connects to 12 communities
- [[.test_blocked_command_with_fullwidth_mention_and_punctuation_is_quarantined()]] - degree 7, connects to 1 community
- [[.test_blocked_command_with_leading_whitespace_is_quarantined()]] - degree 7, connects to 1 community
- [[.test_collaborator_encoded_exfil_request_is_blocked_and_quarantined()]] - degree 7, connects to 1 community
- [[.test_collaborator_file_metadata_question_gets_safe_info()]] - degree 7, connects to 1 community
