---
type: community
cohesion: 0.05
members: 79
---

# SecurityPipeline (2)

**Cohesion:** 0.05 - loosely connected
**Members:** 79 nodes

## Members
- [[dot-_maybe_record_trust_violation()]] - code - gateway/proxy/pipeline.py
- [[dot-_missing_()]] - code - gateway/security/cross_bot_trust_ledger.py
- [[dot-_process_inbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-_process_outbound_core()]] - code - gateway/proxy/pipeline.py
- [[dot-_redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-append()_1]] - code - gateway/proxy/pipeline.py
- [[dot-append_block()]] - code - gateway/proxy/pipeline.py
- [[dot-append_owner_bypass()]] - code - gateway/proxy/pipeline.py
- [[dot-get_stats()_17]] - code - gateway/proxy/pipeline.py
- [[dot-process_inbound()_9]] - code - gateway/proxy/pipeline.py
- [[dot-process_outbound()_7]] - code - gateway/proxy/pipeline.py
- [[dot-set_global_mode()]] - code - gateway/proxy/pipeline.py
- [[dot-test_blocked_non_owner_drops_update_and_increments_stats()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_blocked_owner_message_allowed_through_with_sanitized_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_no_pipeline_falls_back_to_direct_sanitizer()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_outbound_blocked_replaces_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_pipeline_exception_allows_owner_through()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_exception_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_inbound_called_with_skip_context_guard()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_process_outbound_called_for_send_message()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-test_pipeline_raises_with_only_prompt_guard()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_pipeline_raises_without_pii_sanitizer()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_security_pipeline_set_global_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_security_pipeline_set_global_mode_missing_components()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_send_message_draft_also_runs_outbound_filtering()]] - code - gateway/tests/test_telegram_pipeline.py
- [[dot-to_dict()_11]] - code - gateway/proxy/pipeline.py
- [[dot-verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[dot-verify_chain()_2]] - code - gateway/proxy/pipeline.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_67]] - code - gateway/proxy/pipeline.py
- [[Append to the chain with guaranteed SQLite persistence.          Used exclusivel]] - rationale - gateway/proxy/pipeline.py
- [[Attempting to create a pipeline with no PII sanitizer raises RuntimeError.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[BotIncidentSeverity]] - code - gateway/security/cross_bot_trust_ledger.py
- [[Build a TelegramAPIProxy with mocked RBAC and rate limiter.      RBACConfig and]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Even with PromptGuard, pipeline refuses to start without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[FilterResult_1]] - code - gateway/security/outbound_filter.py
- [[Main security pipeline that all messages pass through.      Wires together Prom]] - rationale - gateway/proxy/pipeline.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Ordered severity levels for cross-bot incidents.      Values map to IEC 62443 SL]] - rationale - gateway/security/cross_bot_trust_ledger.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PipelineAction]] - code - gateway/proxy/pipeline.py
- [[PipelineResult]] - code - gateway/tests/test_telegram_pipeline.py
- [[PipelineResult_1]] - code - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.          Thin wra]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.          Thin wrappe]] - rationale - gateway/proxy/pipeline.py
- [[Record a trust-score violation and propagate cross-bot decay.          Called on]] - rationale - gateway/proxy/pipeline.py
- [[Record an owner guard-bypass in the tamper-evident chain (SCRUM-95).          Th]] - rationale - gateway/proxy/pipeline.py
- [[Result of filtering agent response content.]] - rationale - gateway/security/outbound_filter.py
- [[Result of running a message through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[SecurityPipeline_1]] - code - gateway/proxy/pipeline.py
- [[Set global observatory mode for all security modules.          Args]] - rationale - gateway/proxy/pipeline.py
- [[Test SecurityPipeline.set_global_mode method.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test set_global_mode handles missing components gracefully.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestE2E10FailClosed]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestInboundFallbackToDirectSanitizer]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineBlocked]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[Verify the integrity of the retained hash-chain window.          When the bounde]] - rationale - gateway/proxy/pipeline.py
- [[WS-E RT-2 Inbound Encoding Bypass Fix Rationale]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[_getUpdates_response()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_pipeline_result()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_proxy()_3]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_update()_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[pipeline.py_1]] - code - gateway/proxy/pipeline.py
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[test_telegram_pipeline.py]] - code - gateway/tests/test_telegram_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityPipeline_2
SORT file.name ASC
```

## Connections to other communities
- 44 edges to [[_COMMUNITY_KeyVaultConfig]]
- 28 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 17 edges to [[_COMMUNITY_AuditChain]]
- 13 edges to [[_COMMUNITY_MCPPermissionManager]]
- 13 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 12 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 12 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 11 edges to [[_COMMUNITY_socrouter.py]]
- 10 edges to [[_COMMUNITY_api.py (2)]]
- 9 edges to [[_COMMUNITY_AgentTarget]]
- 8 edges to [[_COMMUNITY_test_forward_stream.py]]
- 8 edges to [[_COMMUNITY_test_agent_cve_registry.py (2)]]
- 7 edges to [[_COMMUNITY_AgentTarget (2)]]
- 6 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 4 edges to [[_COMMUNITY_CICD Pipeline Advisor (SKILL)]]
- 4 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 3 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 3 edges to [[_COMMUNITY_Any]]
- 3 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 3 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (2)]]
- 2 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 2 edges to [[_COMMUNITY_TestSecurityPipelineChainLatency]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (4)]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_WebhookReceiver]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming) (2)]]
- 1 edge to [[_COMMUNITY_MCPToolCall]]
- 1 edge to [[_COMMUNITY__pcm_bytes]]

## Top bridge nodes
- [[SecurityPipeline_1]] - degree 138, connects to 26 communities
- [[PipelineAction]] - degree 49, connects to 8 communities
- [[TestE2E10FailClosed]] - degree 15, connects to 8 communities
- [[pipeline.py_1]] - degree 13, connects to 6 communities
- [[PipelineResult_1]] - degree 26, connects to 5 communities
