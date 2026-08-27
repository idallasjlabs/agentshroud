---
type: community
members: 28
---

# Community 117

**Members:** 28 nodes

## Members
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Convert an Anthropic message content field to OpenAI format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Flatten Anthropic system prompt (string or content-block list) to plain text.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[If openai_to_gemini_request raises, the request must still be     forwarded (unm]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[Regression don't break the existing v1messages path.]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[The combined path v1chatcompletions with model=claude- must     end up POST]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[The combined path v1chatcompletions with model=gemini- must end     up POST]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[Translate an OpenAI v1chatcompletions request body to Anthropic v1messages.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_content_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_system_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_random_msg_id()_1]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_openai_translator.py]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[client()_3]] - code - gateway/tests/test_chat_completions_alias.py
- [[openai_to_anthropic_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[test_anthropic_to_openai_response_envelope()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_chat_completions_alias.py]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_passes_correct_path_to_proxy()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_chat_completions_alias_routes_to_v1_path()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_claude_via_openai_path.py]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_gemini_via_openai_path.py]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_get_chat_completions_alias_also_routes()]] - code - gateway/tests/test_chat_completions_alias.py
- [[test_openai_to_anthropic_request_strips_system_role()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_proxy_rewrites_claude_via_openai_path()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_proxy_rewrites_gemini_via_openai_path()]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_root_v1_messages_still_works_unchanged()]] - code - gateway/tests/test_chat_completions_alias.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_117
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 126]]
- 7 edges to [[_COMMUNITY_Community 79]]
- 2 edges to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 40]]
- 1 edge to [[_COMMUNITY_Community 142]]
- 1 edge to [[_COMMUNITY_Community 109]]

## Top bridge nodes
- [[anthropic_openai_translator.py]] - degree 8, connects to 2 communities
- [[anthropic_to_openai_response()]] - degree 7, connects to 2 communities
- [[openai_to_anthropic_request()]] - degree 6, connects to 2 communities
- [[test_gemini_via_openai_path.py]] - degree 5, connects to 2 communities
- [[test_claude_via_openai_path.py]] - degree 9, connects to 1 community