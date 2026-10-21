---
type: community
members: 12
---

# Post-v1.0.0 — Deferred

**Members:** 12 nodes

## Members
- [[Extract the system instruction as plain text (camelCase or snake_case key).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Flatten a Gemini parts list to plain text (text parts only).]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Flatten an OpenAI message's content (string or content-block list) to     Gemini]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[Translate a Gemini generateContent response to OpenAI chatcompletions     shape]] - rationale - gateway/proxy/gemini_openai_translator.py
- [[_openai_content_to_parts()]] - code - gateway/proxy/gemini_openai_translator.py
- [[_parts_to_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[_system_instruction_text()]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_openai_translator.py]] - code - gateway/proxy/gemini_openai_translator.py
- [[gemini_to_openai_response()]] - code - gateway/proxy/gemini_openai_translator.py
- [[test_gemini_to_openai_response_empty_candidates_yields_empty_text()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_response_envelope()]] - code - gateway/tests/test_gemini_openai_translator.py
- [[test_gemini_to_openai_response_max_tokens_finish_reason()]] - code - gateway/tests/test_gemini_openai_translator.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Post-v100__Deferred
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_DELIVERABLE 3 — v0.8.0 Implementation Items]]

## Top bridge nodes
- [[gemini_openai_translator.py]] - degree 8, connects to 2 communities
- [[gemini_to_openai_response()]] - degree 8, connects to 2 communities
- [[_parts_to_text()]] - degree 5, connects to 1 community
- [[_system_instruction_text()]] - degree 4, connects to 1 community
- [[_openai_content_to_parts()]] - degree 3, connects to 1 community
