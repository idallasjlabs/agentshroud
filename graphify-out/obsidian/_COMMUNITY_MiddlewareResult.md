---
type: community
members: 31
---

# MiddlewareResult

**Members:** 31 nodes

## Members
- [[dot-test_default_collab_outbound_still_blocked_by_leakage_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_default_disclosure_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_defaults()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_denied_with_reason()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_full_access_collaborator_passes_despite_middleware_block()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_full_access_disclosure_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_full_access_outbound_not_blocked_by_leakage_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_per_user_mode_override_controls_outbound_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_project_scoped_collaborator_still_blocked_by_middleware()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Middleware block must be bypassed for full_access collaborators.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[MiddlewareResult]] - code - gateway/ingest_api/middleware.py
- [[Per-user mode override is respected by the outbound filter. A collaborator…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Result from middleware processing.]] - rationale - gateway/ingest_api/middleware.py
- [[TestFullAccessMiddlewareBypass]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestMiddlewareResult]] - code - gateway/tests/test_middleware_coverage.py
- [[fake_notify_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_notify_blocked()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_notify_blocked()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_send_text()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access bypass applies even when the message has no interrogative marker.…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborator must receive the general-access disclosure message.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborator outbound must pass through even when leakage filter…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborators must pass through middleware and secondary pipeline…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[local_only collaborator must receive the restricted-scope disclosure message.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[local_only collaborators must still be blocked by the leakage filter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[process_request()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[process_request()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[process_request()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[project_scoped collaborators are still blocked when middleware blocks (non-…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareResult
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY__wrap_response]]
- 8 edges to [[_COMMUNITY_asyncio]]
- 4 edges to [[_COMMUNITY_dot-process_request]]
- 3 edges to [[_COMMUNITY_app]]
- 3 edges to [[_COMMUNITY_dot-_extract_first_egress_target]]
- 2 edges to [[_COMMUNITY_test_file_sandbox_message_gate.py]]
- 2 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 2 edges to [[_COMMUNITY_dot-_make_proxy]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_dot-_looks_like_safe_collaborator_info_query]]

## Top bridge nodes
- [[MiddlewareResult]] - degree 20, connects to 6 communities
- [[dot-test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative()]] - degree 10, connects to 3 communities
- [[dot-test_default_collab_outbound_still_blocked_by_leakage_filter()]] - degree 5, connects to 3 communities
- [[dot-test_full_access_outbound_not_blocked_by_leakage_filter()]] - degree 5, connects to 3 communities
- [[dot-test_per_user_mode_override_controls_outbound_filter()]] - degree 5, connects to 3 communities
