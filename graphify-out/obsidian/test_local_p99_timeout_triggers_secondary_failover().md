---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "TestCollaboratorPromptClassifiers"
location: "L377"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestCollaboratorPromptClassifiers
---

# test_local_p99_timeout_triggers_secondary_failover()

## Connections
- [[_fake_forward()_17]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[_openai_ok()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestCollaboratorPromptClassifiers
