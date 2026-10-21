---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "_make_proxy()"
location: "L336-L375"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_make_proxy
---

# test_local_oom_triggers_secondary_failover

## Connections
- [[dot-_local_secondary_failover_request()]] - `references` [INFERRED]
- [[LLMProxy._local_secondary_failover_request]] - `references` [INFERRED]
- [[OOM (503 backend_unavailable from primary local) triggers secondary local…]] - `rationale_for` [EXTRACTED]
- [[_fake_forward()_16]] - `contains` [EXTRACTED]
- [[_fake_forward()_24]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[_openai_ok()]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_make_proxy
