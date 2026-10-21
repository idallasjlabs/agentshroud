---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "TestCollaboratorPromptClassifiers"
location: "L443"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestCollaboratorPromptClassifiers
---

# test_local_oom_failover_disabled_does_not_retry()

## Connections
- [[When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry.]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_14]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/TestCollaboratorPromptClassifiers
