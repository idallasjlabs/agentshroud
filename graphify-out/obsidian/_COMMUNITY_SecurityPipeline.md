---
type: community
members: 55
---

# SecurityPipeline

**Members:** 55 nodes

## Members
- [[dot-_redacting_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-set_global_mode()]] - code - gateway/proxy/pipeline.py
- [[dot-test_every_pipeline_module_attr_is_a_lifespan_kwarg()]] - code - gateway/tests/test_docs_accuracy.py
- [[dot-test_non_owner_inbound_query_still_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_owner_inbound_query_not_pii_redacted()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_pipeline_raises_with_only_prompt_guard()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-test_pipeline_raises_without_pii_sanitizer()]] - code - gateway/tests/test_e2e_watchtower.py
- [[dot-to_dict()_3]] - code - gateway/security/canary.py
- [[dot-verify_audit_chain()]] - code - gateway/proxy/pipeline.py
- [[Any_16]] - code
- [[AppState]] - code - gateway/ingest_api/state.py
- [[Attempting to create a pipeline with no PII sanitizer raises RuntimeError.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail proxy check with unhealthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
- [[Container for application-wide state]] - rationale - gateway/ingest_api/state.py
- [[E2E-10 SecurityPipeline refuses to operate without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Even with PromptGuard, pipeline refuses to start without PII sanitizer.]] - rationale - gateway/tests/test_e2e_watchtower.py
- [[Every SecurityPipeline.ALL_MODULE_ATTRS name must be passed as a kwarg in…]] - rationale - gateway/tests/test_docs_accuracy.py
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Main security pipeline that all messages pass through. Wires together…]] - rationale - gateway/proxy/pipeline.py
- [[Non-owner query must still be PII-scrubbed (detector + threshold unchanged).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Owner query must pass through PII sanitisation unchanged; sanitiser not called.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[PII sanitiser mock that simulates two entity redactions.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Pipeline must refuse to start without PII sanitizer (fail-closed).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system. Args pipeline SecurityPipeline instance…]] - rationale - gateway/security/canary.py
- [[SecurityPipeline]] - code - gateway/proxy/pipeline.py
- [[Set global observatory mode for all security modules. Args mode monitor or…]] - rationale - gateway/proxy/pipeline.py
- [[Step 2 PII sanitisation must be skipped for the authenticated owner. Non-owner…]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestE2E10FailClosed]] - code - gateway/tests/test_e2e_watchtower.py
- [[TestInboundPIIOwnerExemption]] - code - gateway/tests/test_pipeline_unit.py
- [[TestLifespanWiresEveryPipelineModule]] - code - gateway/tests/test_docs_accuracy.py
- [[Tests for the canary verification system.]] - rationale - gateway/tests/test_canary.py
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[asyncio_26]] - code
- [[canary.py_2]] - code - gateway/security/canary.py
- [[canary_pipeline()]] - code - gateway/tests/test_canary.py
- [[run_canary()]] - code - gateway/security/canary.py
- [[test_canary.py]] - code - gateway/tests/test_canary.py
- [[test_canary_fails_without_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_message_contains_fake_pii()]] - code - gateway/tests/test_canary.py
- [[test_canary_passes_with_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_result_serialization()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_audit_chain()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_pii_stripping()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_pipeline_fails_closed_without_pii()]] - code - gateway/tests/test_redteam_probes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecurityPipeline
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_asyncio_1]]
- 11 edges to [[_COMMUNITY_PIIConfig]]
- 8 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 7 edges to [[_COMMUNITY_lifespan.py]]
- 7 edges to [[_COMMUNITY_AuditChain]]
- 6 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 5 edges to [[_COMMUNITY_PromptGuard]]
- 4 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_TestObservatoryMode]]
- 3 edges to [[_COMMUNITY_RateLimitGuard]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 2 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_MCPProxy]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_test_web_api_coverage.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]

## Top bridge nodes
- [[SecurityPipeline]] - degree 83, connects to 19 communities
- [[AppState]] - degree 16, connects to 11 communities
- [[test_canary.py]] - degree 27, connects to 7 communities
- [[canary_pipeline()]] - degree 7, connects to 4 communities
- [[run_canary()]] - degree 15, connects to 3 communities
