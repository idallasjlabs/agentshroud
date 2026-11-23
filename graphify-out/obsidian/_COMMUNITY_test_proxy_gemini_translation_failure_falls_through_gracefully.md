---
type: community
members: 11
---

# test_proxy_gemini_translation_failure_falls_through_gracefully

**Members:** 11 nodes

## Members
- [[Gemini-model-via-OpenAI-path translation. Mirrors…]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[If openai_to_gemini_request raises, the request must still be forwarded…]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[The combined path v1chatcompletions with model=gemini- must end up POSTing…]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[_broken_translator()]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[asyncio_23]] - code
- [[fake_open()_1]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[mock_forward()_16]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[mock_forward()_17]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_gemini_via_openai_path.py]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - code - gateway/tests/test_gemini_via_openai_path.py
- [[test_proxy_rewrites_gemini_via_openai_path()]] - code - gateway/tests/test_gemini_via_openai_path.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_proxy_gemini_translation_failure_falls_through_gracefully
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_test_anthropic_openai_translator.py]]

## Top bridge nodes
- [[test_gemini_via_openai_path.py]] - degree 5, connects to 2 communities
- [[test_proxy_gemini_translation_failure_falls_through_gracefully()]] - degree 7, connects to 1 community
- [[test_proxy_rewrites_gemini_via_openai_path()]] - degree 6, connects to 1 community
