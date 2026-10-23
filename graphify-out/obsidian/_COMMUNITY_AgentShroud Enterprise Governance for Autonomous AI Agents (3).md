---
type: community
cohesion: 0.22
members: 9
---

# AgentShroud: Enterprise Governance for Autonomous AI Agents (3)

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[If notice send fails, cooldown should not suppress the next retry attempt.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_rate_notice()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Enterprise_Governance_for_Autonomous_AI_Agents_3
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 3 edges to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]
- 3 edges to [[_COMMUNITY_asyncio]]

## Top bridge nodes
- [[dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - degree 9, connects to 3 communities
- [[dot-test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - degree 9, connects to 3 communities
- [[dot-test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - degree 8, connects to 3 communities
