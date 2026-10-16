---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "test_llm_proxy.py"
location: "L893-L902"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_llm_proxypy
---

# test_streaming_cloud_non_quota_400_also_propagates

## Connections
- [[A cloud 400 that is NOT a quota wall must surface as a 400, not a 200.]] - `rationale_for` [EXTRACTED]
- [[StreamHead]] - `uses` [INFERRED]
- [[_run_stream (StreamHead test harness)]] - `calls` [EXTRACTED]
- [[asyncio_3]] - `references` [EXTRACTED]
- [[test_llm_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_llm_proxypy
