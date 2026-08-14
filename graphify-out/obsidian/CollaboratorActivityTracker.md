---
source_file: "gateway/security/collaborator_tracker.py"
type: "code"
community: "HTTP Forwarder"
location: "L42"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/HTTP_Forwarder
---

# CollaboratorActivityTracker

## Connections
- [[.__init__()_59]] - `method` [EXTRACTED]
- [[._append_contributor_log()]] - `method` [EXTRACTED]
- [[._coerce_timestamp()]] - `method` [EXTRACTED]
- [[._normalize_preview()]] - `method` [EXTRACTED]
- [[._normalize_username()]] - `method` [EXTRACTED]
- [[.get_activity()]] - `method` [EXTRACTED]
- [[.get_activity_summary()]] - `method` [EXTRACTED]
- [[.get_health()_1]] - `method` [EXTRACTED]
- [[.record_activity()]] - `method` [EXTRACTED]
- [[.test_failed_write_makes_unhealthy()]] - `calls` [EXTRACTED]
- [[.test_initial_state_healthy()]] - `calls` [EXTRACTED]
- [[CollaboratorActivityTracker_1]] - `uses` [INFERRED]
- [[Path_31]] - `uses` [INFERRED]
- [[TelegramAPIProxy_3]] - `uses` [INFERRED]
- [[TestBuildCollaboratorSafeInfoResponse]] - `uses` [INFERRED]
- [[TestDefaultBotId]] - `uses` [INFERRED]
- [[TestDomainValidationHelper]] - `uses` [INFERRED]
- [[TestEgressBannerRedactionNoOwnerNotice]] - `uses` [INFERRED]
- [[TestEgressTargetExtraction]] - `uses` [INFERRED]
- [[TestForwardToTelegramTimeouts]] - `uses` [INFERRED]
- [[TestInternalBannerMatcher]] - `uses` [INFERRED]
- [[TestLooksLikeSafeCollaboratorInfoQuery]] - `uses` [INFERRED]
- [[TestMultipartOutboundPipeline]] - `uses` [INFERRED]
- [[TestOutboundClassifierHelpers]] - `uses` [INFERRED]
- [[TestOutboundPipelineIntegration]] - `uses` [INFERRED]
- [[TestOutboundScanUnification]] - `uses` [INFERRED]
- [[TestOutboundTextFieldResolution]] - `uses` [INFERRED]
- [[TestOwnerActivityNotice]] - `uses` [INFERRED]
- [[TestOwnerMirrorCoalescing]] - `uses` [INFERRED]
- [[TestParseModeStrippedAfterPIIRedaction]] - `uses` [INFERRED]
- [[TestPendingNoticeIncludesEgressSection]] - `uses` [INFERRED]
- [[TestReplayBufferOffsetParsing]] - `uses` [INFERRED]
- [[TestRuntimeRewriteHelpers]] - `uses` [INFERRED]
- [[TestTelegram400Retry]] - `uses` [INFERRED]
- [[TestTrackerGetHealth]] - `uses` [INFERRED]
- [[TestWebSearchLog]] - `uses` [INFERRED]
- [[Tracks collaborator messages at the gateway level.      Records every inbound me]] - `rationale_for` [EXTRACTED]
- [[collaborator_tracker.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_collaborator_tracker.py]] - `imports` [EXTRACTED]
- [[test_fixture_uid_writes_blocked()]] - `calls` [EXTRACTED]
- [[test_lifespan_prune.py]] - `imports` [EXTRACTED]
- [[test_owner_display_name_overrides_pipe()]] - `calls` [EXTRACTED]
- [[test_prune_keeps_real_uid_markdown()]] - `calls` [EXTRACTED]
- [[test_prune_walks_all_contributor_dirs()]] - `calls` [EXTRACTED]
- [[test_real_uid_writes_unblocked()]] - `calls` [EXTRACTED]
- [[test_telegram_proxy_outbound.py]] - `imports` [EXTRACTED]
- [[test_test_user_prefix_blocked()]] - `calls` [EXTRACTED]
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - `calls` [EXTRACTED]
- [[tracker()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/HTTP_Forwarder