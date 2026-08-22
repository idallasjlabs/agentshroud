---
source_file: "voice_gateway/server.py"
type: "code"
community: "Voice Latency Guard"
location: "L722"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Voice_Latency_Guard
---

# _call_agent_stream()

## Connections
- [[Route a voice utterance to a proxied agent via the AgentShroud gateway's     POS]] - `rationale_for` [EXTRACTED]
- [[_record_turn_latency()]] - `calls` [EXTRACTED]
- [[_voice_forward_metadata()]] - `calls` [EXTRACTED]
- [[server.py]] - `contains` [EXTRACTED]
- [[test_call_agent_default_body_has_no_metadata()]] - `calls` [EXTRACTED]
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - `calls` [EXTRACTED]
- [[test_call_agent_records_latency_on_read_timeout()]] - `calls` [EXTRACTED]
- [[test_call_agent_records_latency_on_success()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_generic_http_error_falls_back()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_non_streaming_agent_returns_telegram_notice()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_posts_to_forward_stream_endpoint()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - `calls` [EXTRACTED]
- [[test_call_agent_stream_yields_sentences_in_order()]] - `calls` [EXTRACTED]
- [[test_voice_gateway.py]] - `imports` [EXTRACTED]
- [[test_voice_latency_guard.py]] - `imports` [EXTRACTED]
- [[test_ws_volume_command_intercepted()]] - `conceptually_related_to` [INFERRED]
- [[voice_endpoint()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Voice_Latency_Guard