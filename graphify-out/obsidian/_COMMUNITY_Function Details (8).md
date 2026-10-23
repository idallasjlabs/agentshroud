---
type: community
cohesion: 0.17
members: 15
---

# Function Details (8)

**Cohesion:** 0.17 - loosely connected
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
TABLE source_file, type FROM #community/Function_Details_8
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 2 edges to [[_COMMUNITY_7. Security findings]]
- 1 edge to [[_COMMUNITY_agentshroud-gateway service (proxy mode) (2)]]

## Top bridge nodes
- [[test_claude_via_openai_path.py]] - degree 9, connects to 3 communities
- [[anthropic_openai_translator.py]] - degree 7, connects to 1 community
- [[_random_msg_id()]] - degree 4, connects to 1 community
- [[_anthropic_content_to_openai()]] - degree 3, connects to 1 community
- [[_anthropic_system_to_openai()]] - degree 3, connects to 1 community
