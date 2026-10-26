---
source_file: "gateway/tests/test_llm_proxy.py"
type: "code"
community: "Community 53"
location: "L837-L859"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_53
---

# _run_stream (StreamHead test harness)

## Connections
- [[LLMProxy]] - `calls` [EXTRACTED]
- [[LLMProxy.proxy_messages_streaming]] - `calls` [EXTRACTED]
- [[StreamHead]] - `uses` [INFERRED]
- [[test_streaming_cloud_non_quota_400_also_propagates]] - `calls` [EXTRACTED]
- [[test_streaming_default_contract_yields_only_bytes]] - `calls` [EXTRACTED]
- [[test_streaming_with_head_reports_200_then_chunks]] - `calls` [EXTRACTED]
- [[test_streaming_with_head_reports_upstream_400_and_body]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_53