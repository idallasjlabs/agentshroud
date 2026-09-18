---
type: community
cohesion: 0.60
members: 5
---

# translate_openai_sse_to_anthropic()

**Cohesion:** 0.60 - moderately connected
**Members:** 5 nodes

## Members
- [[Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events.      Yi]] - rationale - gateway/proxy/anthropic_openai_sse_translator.py
- [[_random_msg_id()]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[_sse()]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[anthropic_openai_sse_translator.py]] - code - gateway/proxy/anthropic_openai_sse_translator.py
- [[translate_openai_sse_to_anthropic()]] - code - gateway/proxy/anthropic_openai_sse_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/translate_openai_sse_to_anthropic
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages]]

## Top bridge nodes
- [[translate_openai_sse_to_anthropic()]] - degree 7, connects to 2 communities