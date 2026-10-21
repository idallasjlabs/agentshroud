---
type: community
members: 27
---

# Phase Review: P0 — Core Pipeline Wiring

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
- [[_make_proxy()_2]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_update()_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[test_telegram_pipeline.py]] - code - gateway/tests/test_telegram_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_Review_P0__Core_Pipeline_Wiring
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 12 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 9 edges to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY__req]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[PipelineResult_1]] - degree 26, connects to 6 communities
- [[test_telegram_pipeline.py]] - degree 15, connects to 2 communities
- [[TestOutboundPipelineWired]] - degree 6, connects to 2 communities
- [[TestInboundFallbackToDirectSanitizer]] - degree 5, connects to 2 communities
- [[TestInboundPipelineBlockedNonOwner]] - degree 5, connects to 2 communities
