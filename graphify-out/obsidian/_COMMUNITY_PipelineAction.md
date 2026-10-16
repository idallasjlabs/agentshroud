---
type: community
cohesion: 0.10
members: 48
---

# PipelineAction

**Cohesion:** 0.10 - loosely connected
**Members:** 48 nodes

## Members
- [[dot-_maybe_record_trust_violation()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_inbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_outbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-append()]] - code - gateway/proxy/pipeline.py
- [[dot-append_block()]] - code - gateway/proxy/pipeline.py
- [[dot-append_owner_bypass()]] - code - gateway/proxy/pipeline.py
- [[dot-entries()]] - code - gateway/proxy/pipeline.py
- [[dot-process_inbound()_3]] - code - gateway/proxy/pipeline.py
- [[dot-process_outbound()_3]] - code - gateway/proxy/pipeline.py
- [[dot-test_blocked_non_owner_drops_update_and_increments_stats()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_blocked_owner_message_allowed_through_with_sanitized_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_no_pipeline_falls_back_to_direct_sanitizer()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_outbound_blocked_replaces_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_exception_allows_owner_through()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_exception_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_inbound_called_with_skip_context_guard()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_outbound_called_for_send_message()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_send_message_draft_also_runs_outbound_filtering()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-to_dict()_2]] - code - gateway/proxy/pipeline.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_10]] - code - gateway/proxy/pipeline.py
- [[Append to the chain with guaranteed SQLite persistence.          Used exclusivel]] - rationale - gateway/proxy/pipeline.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[Build a TelegramAPIProxy with mocked RBAC and rate limiter.      RBACConfig and]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[PipelineAction]] - code - gateway/proxy/pipeline.py
- [[PipelineResult]] - code - gateway/tests/test_telegram_pipeline.py
- [[PipelineResult_1]] - code - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.          Thin wra]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.          Thin wrappe]] - rationale - gateway/proxy/pipeline.py
- [[Record a trust-score violation and propagate cross-bot decay.          Called on]] - rationale - gateway/proxy/pipeline.py
- [[Record an owner guard-bypass in the tamper-evident chain (SCRUM-95).          Th]] - rationale - gateway/proxy/pipeline.py
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
- [[_make_proxy()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_update()_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[test_telegram_pipeline.py]] - code - gateway/tests/test_telegram_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PipelineAction
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_PIIConfig]]
- 13 edges to [[_COMMUNITY_OutboundInfoFilter]]
- 12 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 9 edges to [[_COMMUNITY_AsyncMock]]
- 7 edges to [[_COMMUNITY_AuditChain]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 4 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 4 edges to [[_COMMUNITY_InjectionAction]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY__FakeAttack]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_EnvelopeSigner]]
- 1 edge to [[_COMMUNITY_KeyVault]]

## Top bridge nodes
- [[PipelineAction]] - degree 50, connects to 13 communities
- [[PipelineResult_1]] - degree 26, connects to 7 communities
- [[Any_10]] - degree 14, connects to 6 communities
- [[AuditChainEntry]] - degree 11, connects to 5 communities
- [[test_telegram_pipeline.py]] - degree 15, connects to 1 community
