---
type: community
members: 13
---

# mcp_config.py

**Members:** 13 nodes

## Members
- [[Feed raw SSE bytes into the translator and collect Anthropic events.]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Tool-call-only SSE stream must produce tool_use at index 0 (no text gap).]] - rationale - gateway/tests/test_anthropic_openai_translator.py
- [[Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events.      Yi]] - rationale - gateway/proxy/anthropic_openai_sse_translator.py
- [[_collect_sse()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[_random_msg_id()_1]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[_sse()]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[anthropic_openai_sse_translator.py]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[test_sse_translator_basic_text_stream()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_empty_stream_emits_full_sequence()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_model_preserved_in_message_start()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_stop_reason_propagated()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[test_sse_translator_tool_call_only_starts_at_index_0()]] - code - gateway/tests/test_anthropic_openai_translator.py
- [[translate_openai_sse_to_anthropic()]] - code - gateway/proxy/anthropic_openai_sse_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mcp_configpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]

## Top bridge nodes
- [[_collect_sse()]] - degree 8, connects to 1 community
- [[translate_openai_sse_to_anthropic()]] - degree 6, connects to 1 community
- [[test_sse_translator_tool_call_only_starts_at_index_0()]] - degree 3, connects to 1 community
- [[test_sse_translator_basic_text_stream()]] - degree 2, connects to 1 community
- [[test_sse_translator_empty_stream_emits_full_sequence()]] - degree 2, connects to 1 community
