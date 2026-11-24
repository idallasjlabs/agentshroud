---
source_file: "gateway/tests/test_llm_proxy_failover.py"
type: "code"
community: "test_llm_proxy_failover.py"
location: "L139"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxy_failoverpy
---

# test_forward_request_default_still_retries_429()

## Connections
- [[Without the interactive flag the 3-retry loop is unchanged (guards the hermes-…]] - `rationale_for` [EXTRACTED]
- [[_no_sleep()]] - `indirect_call` [INFERRED]
- [[asyncio_20]] - `references` [EXTRACTED]
- [[fake_urlopen()_16]] - `contains` [EXTRACTED]
- [[fake_urlopen()_17]] - `indirect_call` [INFERRED]
- [[make_proxy()_1]] - `calls` [EXTRACTED]
- [[test_llm_proxy_failover.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxy_failoverpy
