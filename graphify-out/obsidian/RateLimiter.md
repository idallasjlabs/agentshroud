---
source_file: "gateway/ingest_api/auth.py"
type: "code"
community: "Gateway Test Suite"
location: "L30"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# RateLimiter

## Connections
- [[.__init__()_14]] - `method` [EXTRACTED]
- [[.__init__()_38]] - `calls` [EXTRACTED]
- [[.check()]] - `method` [EXTRACTED]
- [[.test_collaborator_rate_limit_notice_falls_back_without_markdown()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_notice_includes_retry_window()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_notice_retries_next_message_when_send_fails()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_resets_after_window()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_retry_after_seconds_uses_window()]] - `calls` [EXTRACTED]
- [[.test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()]] - `calls` [EXTRACTED]
- [[Any_20]] - `uses` [INFERRED]
- [[AsyncMock]] - `uses` [INFERRED]
- [[BlockingPipeline]] - `uses` [INFERRED]
- [[EncodingDetectingPipeline]] - `uses` [INFERRED]
- [[FakePipelineResult_1]] - `uses` [INFERRED]
- [[FakeRBAC_1]] - `uses` [INFERRED]
- [[GatewayConfig_1]] - `uses` [INFERRED]
- [[PassthroughPipeline_1]] - `uses` [INFERRED]
- [[Simple token-bucket rate limiter      Limits requests per client IP to prevent r]] - `rationale_for` [EXTRACTED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[TestBotIsMentioned]] - `uses` [INFERRED]
- [[TestCollaboratorPromptClassifiers]] - `uses` [INFERRED]
- [[TestCollaboratorRateLimitRecovery]] - `uses` [INFERRED]
- [[TestCommandTokenNormalization]] - `uses` [INFERRED]
- [[TestFileDownload]] - `uses` [INFERRED]
- [[TestFullAccessMiddlewareBypass]] - `uses` [INFERRED]
- [[TestGroupMentionFilter]] - `uses` [INFERRED]
- [[TestGroupPresenceProbe]] - `uses` [INFERRED]
- [[TestInboundPipelineOnGetUpdates]] - `uses` [INFERRED]
- [[TestIsGroupMessage]] - `uses` [INFERRED]
- [[TestNoResponseGuarantee]] - `uses` [INFERRED]
- [[TestPerBotGroupMentionFilter]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUX]] - `uses` [INFERRED]
- [[TestStrangerRateLimit]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[auth.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_auth.py]] - `imports` [EXTRACTED]
- [[test_rate_limiter()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_allows_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_blocks_excess_requests()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_separate_clients()]] - `calls` [EXTRACTED]
- [[test_rate_limiter_window_cleanup()]] - `calls` [EXTRACTED]
- [[test_security.py]] - `imports` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite