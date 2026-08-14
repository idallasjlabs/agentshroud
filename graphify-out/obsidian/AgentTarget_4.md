---
source_file: "gateway/ingest_api/router.py"
type: "code"
community: "Slack API Proxy"
location: "L116"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Slack_API_Proxy
---

# AgentTarget

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[._build_forward_payload()]] - `references` [EXTRACTED]
- [[.forward_to_agent()]] - `references` [EXTRACTED]
- [[.forward_to_agent_stream()]] - `references` [EXTRACTED]
- [[.health_check()]] - `references` [EXTRACTED]
- [[.list_targets()]] - `references` [EXTRACTED]
- [[.register_bots()]] - `calls` [EXTRACTED]
- [[.resolve_target()]] - `references` [EXTRACTED]
- [[_make_stream_app_state()]] - `calls` [INFERRED]
- [[_target()]] - `calls` [INFERRED]
- [[test_forward_stream_rejects_non_openai_compat_target()]] - `calls` [INFERRED]
- [[test_stream_ignores_lines_without_data_prefix()]] - `calls` [INFERRED]
- [[test_stream_payload_sets_stream_true()]] - `calls` [INFERRED]
- [[test_stream_raises_forward_error_on_connect_failure()]] - `calls` [INFERRED]
- [[test_stream_raises_forward_error_on_http_status_error()]] - `calls` [INFERRED]
- [[test_stream_raises_forward_error_on_malformed_json()]] - `calls` [INFERRED]
- [[test_stream_rejects_non_openai_compat_target()]] - `calls` [INFERRED]
- [[test_stream_skips_chunk_missing_choices_key_and_continues()]] - `calls` [INFERRED]
- [[test_stream_yields_content_deltas_in_order()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Slack_API_Proxy