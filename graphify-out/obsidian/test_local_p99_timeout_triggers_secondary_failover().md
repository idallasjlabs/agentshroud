---
source_file: "gateway/tests/test_llm_proxy_local_parity.py"
type: "code"
community: "Community 49"
location: "L377"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_49
---

# test_local_p99_timeout_triggers_secondary_failover()

## Connections
- [[_fake_forward()_9]] - `contains` [EXTRACTED]
- [[_fake_forward()_15]] - `indirect_call` [INFERRED]
- [[_make_proxy()]] - `calls` [EXTRACTED]
- [[_openai_ok()]] - `calls` [EXTRACTED]
- [[asyncio_2]] - `references` [EXTRACTED]
- [[p99 timeout (TimeoutError on primary local) triggers secondary local model.]] - `rationale_for` [EXTRACTED]
- [[test_llm_proxy_local_parity.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_49