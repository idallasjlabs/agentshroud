---
type: community
cohesion: 0.11
members: 18
---

# Community 510

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.test_default_collab_outbound_still_blocked_by_leakage_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_default_disclosure_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_full_access_collaborator_passes_despite_middleware_block()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_full_access_disclosure_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_full_access_outbound_not_blocked_by_leakage_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_per_user_mode_override_controls_outbound_filter()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_project_scoped_collaborator_still_blocked_by_middleware()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Middleware block must be bypassed for full_access collaborators.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Per-user mode override is respected by the outbound filter.          A collabora]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFullAccessMiddlewareBypass]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access bypass applies even when the message has no interrogative marker.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborator must receive the general-access disclosure message.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborator outbound must pass through even when leakage filter wou]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[full_access collaborators must pass through middleware and secondary pipeline bl]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[local_only collaborator must receive the restricted-scope disclosure message.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[local_only collaborators must still be blocked by the leakage filter.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[project_scoped collaborators are still blocked when middleware blocks (non-multi]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_510
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Telegram Proxy Inbound]]
- 4 edges to [[_COMMUNITY_Community 31]]
- 1 edge to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Adversarial Injection Guards]]

## Top bridge nodes
- [[TestFullAccessMiddlewareBypass]] - degree 13, connects to 4 communities
- [[.test_full_access_collaborator_passes_despite_middleware_block()]] - degree 6, connects to 2 communities
- [[.test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative()]] - degree 6, connects to 2 communities
- [[.test_project_scoped_collaborator_still_blocked_by_middleware()]] - degree 6, connects to 2 communities
- [[.test_default_collab_outbound_still_blocked_by_leakage_filter()]] - degree 4, connects to 1 community