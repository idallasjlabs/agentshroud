---
type: community
cohesion: 0.04
members: 98
---

# Security Pipeline Core

**Cohesion:** 0.04 - loosely connected
**Members:** 98 nodes

## Members
- [[.__init__()_25]] - code - gateway/proxy/mcp_audit.py
- [[.__init__()_32]] - code - gateway/proxy/pipeline.py
- [[.__init__()_33]] - code - gateway/proxy/pipeline.py
- [[.__init__()_50]] - code - gateway/security/alert_dispatcher.py
- [[.__len__()_1]] - code - gateway/proxy/pipeline.py
- [[._maybe_record_trust_violation()]] - code - gateway/proxy/pipeline.py
- [[._process_inbound_core()]] - code - gateway/proxy/pipeline.py
- [[._process_outbound_core()]] - code - gateway/proxy/pipeline.py
- [[.append()]] - code - gateway/proxy/pipeline.py
- [[.append_block()]] - code - gateway/proxy/pipeline.py
- [[.append_owner_bypass()]] - code - gateway/proxy/pipeline.py
- [[.entries()_1]] - code - gateway/proxy/pipeline.py
- [[.get_stats()_6]] - code - gateway/proxy/pipeline.py
- [[.last_hash()_1]] - code - gateway/proxy/pipeline.py
- [[.process_inbound()_1]] - code - gateway/proxy/pipeline.py
- [[.process_outbound()_2]] - code - gateway/proxy/pipeline.py
- [[.test_append_chain()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_owner_bypass_persists_high_severity()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_append_single()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_audit_chain_hash_chained()]] - code - gateway/tests/test_e2e_watchtower.py
- [[.test_blocked_non_owner_drops_update_and_increments_stats()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_blocked_owner_message_allowed_through_with_sanitized_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_chain_continuity_preserved_across_wrap()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_content_hash_deterministic()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_default_window_is_10k()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_different_content_different_hash()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_entries_returns_copy()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_metadata()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_no_pipeline_falls_back_to_direct_sanitizer()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_outbound_blocked_replaces_text()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_persisted_event_records_true_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_pipeline_exception_allows_owner_through()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_pipeline_exception_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_pipeline_process_inbound_called_with_skip_context_guard()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_pipeline_process_outbound_called_for_send_message()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_send_message_draft_also_runs_outbound_filtering()]] - code - gateway/tests/test_telegram_pipeline.py
- [[.test_tamper_in_retained_window_detected()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_unwrapped_chain_must_anchor_at_genesis()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_chain_valid_after_wrap()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_chain_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_tampered_previous_hash()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_verify_valid()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_window_capped_at_max_entries()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.to_dict()_1]] - code - gateway/proxy/pipeline.py
- [[.total_appended()_1]] - code - gateway/proxy/pipeline.py
- [[.verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[.verify_chain()_1]] - code - gateway/proxy/pipeline.py
- [[A self-consistent window on a forged anchor must fail when the         chain nev]] - rationale - gateway/tests/test_pipeline_unit.py
- [[An entry in the SHA-256 hash chain audit ledger.]] - rationale - gateway/proxy/pipeline.py
- [[Any_18]] - code - gateway/proxy/pipeline.py
- [[Append to the chain with guaranteed SQLite persistence.          Used exclusivel]] - rationale - gateway/proxy/pipeline.py
- [[Audit chain is a hash chain each entry references the previous hash.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[AuditChain]] - code - gateway/proxy/pipeline.py
- [[AuditChainEntry]] - code - gateway/proxy/pipeline.py
- [[Build a TelegramAPIProxy with mocked RBAC and rate limiter.      RBACConfig and]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[FilterResult]] - code - gateway/security/outbound_filter.py
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[Path_5]] - code - gateway/security/alert_dispatcher.py
- [[PipelineAction]] - code - gateway/proxy/pipeline.py
- [[PipelineResult_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[PipelineResult]] - code - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an inbound message through the full security pipeline.          Thin wra]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[Process an outbound response through the security pipeline.          Thin wrappe]] - rationale - gateway/proxy/pipeline.py
- [[Record a trust-score violation and propagate cross-bot decay.          Called on]] - rationale - gateway/proxy/pipeline.py
- [[Record an owner guard-bypass in the tamper-evident chain (SCRUM-95).          Th]] - rationale - gateway/proxy/pipeline.py
- [[Result of filtering agent response content.]] - rationale - gateway/security/outbound_filter.py
- [[Result of running a message through the security pipeline.]] - rationale - gateway/proxy/pipeline.py
- [[SHA-256 hash chain for tamper-evident audit logging.]] - rationale - gateway/proxy/pipeline.py
- [[TestAuditChain]] - code - gateway/tests/test_pipeline_unit.py
- [[TestAuditChainBounded]] - code - gateway/tests/test_pipeline_unit.py
- [[TestInboundFallbackToDirectSanitizer]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineBlockedOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionNonOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineExceptionOwner]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestInboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineBlocked]] - code - gateway/tests/test_telegram_pipeline.py
- [[TestOutboundPipelineWired]] - code - gateway/tests/test_telegram_pipeline.py
- [[Tests for the SHA-256 hash chain.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The fire-and-forget SQLite log must record the entry's actual         previous_h]] - rationale - gateway/tests/test_pipeline_unit.py
- [[The in-memory window must be bounded; full history lives in SQLite.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Verify empty audit chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify single-entry chain is valid.]] - rationale - gateway/tests/test_e2e_proxy.py
- [[Verify the integrity of the retained hash-chain window.          When the bounde]] - rationale - gateway/proxy/pipeline.py
- [[_getUpdates_response()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_pipeline_result()]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_proxy()_4]] - code - gateway/tests/test_telegram_pipeline.py
- [[_make_update()_1]] - code - gateway/tests/test_telegram_pipeline.py
- [[append_owner_bypass writes to the hash chain AND persists a HIGH         'owner_]] - rationale - gateway/tests/test_pipeline_unit.py
- [[deque]] - code - gateway/security/killswitch_monitor.py
- [[pipeline.py]] - code - gateway/proxy/pipeline.py
- [[sendMessageDraft must be suppressed to prevent draft flicker leaks.]] - rationale - gateway/tests/test_telegram_pipeline.py
- [[test_audit_chain_empty_valid()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_audit_chain_single_entry()]] - code - gateway/tests/test_e2e_proxy.py
- [[test_telegram_pipeline.py]] - code - gateway/tests/test_telegram_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Pipeline_Core
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 47 edges to [[_COMMUNITY_Cross-Bot Trust Ledger]]
- 17 edges to [[_COMMUNITY_Egress Domain Allowlist]]
- 12 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Collaborator Prompt Classifiers]]
- 11 edges to [[_COMMUNITY_Slack API Proxy]]
- 10 edges to [[_COMMUNITY_Auth & Exception Types]]
- 10 edges to [[_COMMUNITY_Gateway Test Suite]]
- 9 edges to [[_COMMUNITY_HTTP Forwarder]]
- 8 edges to [[_COMMUNITY_Progressive Trust Config]]
- 4 edges to [[_COMMUNITY_Gateway Security Module]]
- 3 edges to [[_COMMUNITY_Kill Switch Config]]
- 2 edges to [[_COMMUNITY_Approval & FastAPI Ingest]]
- 2 edges to [[_COMMUNITY_SOC Dashboard]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_PromptGuard Encoding Detection]]
- 1 edge to [[_COMMUNITY_Gateway Proxy Layer]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_PII Config & Test Fixtures]]
- 1 edge to [[_COMMUNITY_Gateway Security Module]]

## Top bridge nodes
- [[AuditChain]] - degree 88, connects to 9 communities
- [[PipelineAction]] - degree 52, connects to 9 communities
- [[InjectionAction]] - degree 34, connects to 6 communities
- [[TestAuditChain]] - degree 27, connects to 6 communities
- [[TestAuditChainBounded]] - degree 25, connects to 6 communities