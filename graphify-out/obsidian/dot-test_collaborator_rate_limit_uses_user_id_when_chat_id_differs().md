---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "AgentShroud: Enterprise Governance for Autonomous AI Agents (3)"
location: "L3738"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentShroud_Enterprise_Governance_for_Autonomous_AI_Agents_3
---

# .test_collaborator_rate_limit_uses_user_id_when_chat_id_differs()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[Rate-limit notice path should key retry window by user_id, not chat_id.]] - `rationale_for` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[fake_rate_notice()_2]] - `indirect_call` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/AgentShroud_Enterprise_Governance_for_Autonomous_AI_Agents_3
