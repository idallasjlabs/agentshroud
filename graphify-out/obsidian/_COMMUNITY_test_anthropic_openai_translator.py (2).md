---
type: community
members: 15
---

# test_anthropic_openai_translator.py (2)

**Members:** 15 nodes

## Members
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Convert an Anthropic message content field to OpenAI format.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Flatten Anthropic system prompt (string or content-block list) to plain text.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[The combined path v1chatcompletions with model=claude- must     end up POST]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[Translate an OpenAI v1chatcompletions request body to Anthropic v1messages.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_content_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_anthropic_system_to_openai()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[_random_msg_id()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_openai_translator.py]] - code - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[openai_to_anthropic_request()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[test_anthropic_to_openai_response_envelope()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_claude_via_openai_path.py]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_openai_to_anthropic_request_strips_system_role()]] - code - gateway/tests/test_claude_via_openai_path.py
- [[test_proxy_rewrites_claude_via_openai_path()]] - code - gateway/tests/test_claude_via_openai_path.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_anthropic_openai_translatorpy_2
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_anthropic_openai_translator.py]]
- 3 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_test_claude_via_openai_path.py]]

## Top bridge nodes
- [[test_claude_via_openai_path.py]] - degree 9, connects to 2 communities
- [[anthropic_openai_translator.py]] - degree 7, connects to 1 community
- [[_random_msg_id()]] - degree 4, connects to 1 community
- [[_anthropic_content_to_openai()]] - degree 3, connects to 1 community
- [[_anthropic_system_to_openai()]] - degree 3, connects to 1 community
