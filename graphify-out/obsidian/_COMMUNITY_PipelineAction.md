---
type: community
cohesion: 0.18
members: 27
---

# PipelineAction

**Cohesion:** 0.18 - loosely connected
**Members:** 27 nodes

## Members
- [[dot-test_blocked_non_owner_drops_update_and_increments_stats()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_blocked_owner_message_allowed_through_with_sanitized_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_no_pipeline_falls_back_to_direct_sanitizer()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_outbound_blocked_replaces_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_exception_allows_owner_through()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_exception_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_inbound_called_with_skip_context_guard()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_outbound_called_for_send_message()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_send_message_draft_also_runs_outbound_filtering()]] - code - gateway/tests/test_telegram_pipeline.py
- [[Build a TelegramAPIProxy with mocked RBAC and rate limiter.      RBACConfig and]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[PipelineResult]] - code - gateway/tests/test_telegram_pipeline.py
- [[PipelineResult_1]] - code - gateway/proxy/pipeline.py
- [[Result of running a message through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[TestInboundFallbackToDirectSanitizer]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineBlocked]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[_getUpdates_response()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_pipeline_result()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_proxy()_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_update()]] - code - gateway/tests/test_telegram_pipeline.py
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[test_telegram_pipeline.py]] - code - gateway/tests/test_telegram_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PipelineAction
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AuditChain]]
- 12 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 9 edges to [[_COMMUNITY_AsyncMock]]
- 6 edges to [[_COMMUNITY_PipelineAction_1]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[PipelineResult_1]] - degree 26, connects to 7 communities
- [[test_telegram_pipeline.py]] - degree 15, connects to 2 communities
- [[TestOutboundPipelineWired]] - degree 6, connects to 2 communities
- [[TestInboundFallbackToDirectSanitizer]] - degree 5, connects to 2 communities
- [[TestInboundPipelineBlockedNonOwner]] - degree 5, connects to 2 communities
