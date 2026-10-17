---
source_file: "gateway/proxy/llm_proxy.py"
type: "code"
community: "TestStreamingProxyStatusPropagation"
location: "L197-L211"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/TestStreamingProxyStatusPropagation
---

# StreamHead

## Connections
- [[dot-proxy_messages_streaming()]] - `calls` [EXTRACTED]
- [[dot-test_upstream_200_streams_sse_as_before()]] - `calls` [EXTRACTED]
- [[dot-test_upstream_400_returns_400_with_body()]] - `calls` [EXTRACTED]
- [[First item yielded by proxy_messages_streaming(with_head=True). Carries the…]] - `rationale_for` [EXTRACTED]
- [[LLMProxy.proxy_messages_streaming]] - `shares_data_with` [EXTRACTED]
- [[TestStreamingProxyStatusPropagation]] - `uses` [INFERRED]
- [[_run_stream (StreamHead test harness)]] - `uses` [INFERRED]
- [[_stream()]] - `calls` [EXTRACTED]
- [[llm_api_proxy (v1{path} LLM reverse proxy route)]] - `shares_data_with` [EXTRACTED]
- [[llm_proxy.py_2]] - `contains` [EXTRACTED]
- [[test_llm_proxy.py]] - `imports` [EXTRACTED]
- [[test_main_endpoints.py]] - `imports` [EXTRACTED]
- [[test_streaming_cloud_non_quota_400_also_propagates]] - `uses` [INFERRED]
- [[test_streaming_connect_failure_keeps_in_stream_error_frame]] - `uses` [INFERRED]
- [[test_streaming_with_head_reports_200_then_chunks]] - `uses` [INFERRED]
- [[test_streaming_with_head_reports_upstream_400_and_body]] - `uses` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/TestStreamingProxyStatusPropagation
