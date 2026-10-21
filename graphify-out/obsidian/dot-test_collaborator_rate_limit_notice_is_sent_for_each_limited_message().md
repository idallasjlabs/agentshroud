---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "AgentShroud: Enterprise Governance for Autonomous AI Agents (3)"
location: "L3775"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentShroud_Enterprise_Governance_for_Autonomous_AI_Agents_3
---

# .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Repeated rate-limited messages should each receive a deterministic notice.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_rate_notice()]] - `contains` [EXTRACTED]
- [[fake_rate_notice()_2]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AgentShroud_Enterprise_Governance_for_Autonomous_AI_Agents_3
