---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "FakeRBAC"
location: "L1686"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/FakeRBAC
---

# .test_unapproved_collaborator_slash_command_with_mention_and_punctuation_is_quarantined()

## Connections
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[PassthroughPipeline]] - `calls` [EXTRACTED]
- [[TestInboundPipelineOnGetUpdates]] - `method` [EXTRACTED]
- [[Unknown collaborator slash commands should be blocked by default.]] - `rationale_for` [EXTRACTED]
- [[_make_update()]] - `calls` [EXTRACTED]
- [[_wrap_response()]] - `calls` [EXTRACTED]
- [[asyncio]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/FakeRBAC
