---
type: community
members: 24
---

# _mock_response

**Members:** 24 nodes

## Members
- [[Build a fake httpx.Response whose .json() returns body.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Empty choices list raises ForwardError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[Malformed OpenAI response (missing choices) raises ForwardError, not KeyError.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[The OpenAI payload must include a non-empty model field.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[_mock_response()]] - code - gateway/tests/test_router_openai_translation.py
- [[asyncio_65]] - code
- [[forward_to_agent extracts choices0.message.content and returns a string.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent passes response.json() through unchanged for chat targets.]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends the generic {content, ledger_id, ...} body for chat…]] - rationale - gateway/tests/test_router_openai_translation.py
- [[forward_to_agent sends {model, messages} when chat_path ends…]] - rationale - gateway/tests/test_router_openai_translation.py
- [[mock_post()_4]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_5]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_6]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_7]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_8]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_9]] - code - gateway/tests/test_router_openai_translation.py
- [[mock_post()_10]] - code - gateway/tests/test_router_openai_translation.py
- [[test_generic_target_returns_json_as_is()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_generic_target_sends_content_body()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_empty_choices_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_malformed_response_raises_forward_error()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_payload_includes_model()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_returns_content_string()]] - code - gateway/tests/test_router_openai_translation.py
- [[test_openai_target_sends_messages_body()]] - code - gateway/tests/test_router_openai_translation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_mock_response
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 7 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_test_forward_stream.py]]

## Top bridge nodes
- [[test_openai_empty_choices_raises_forward_error()]] - degree 7, connects to 3 communities
- [[test_openai_malformed_response_raises_forward_error()]] - degree 7, connects to 3 communities
- [[test_generic_target_returns_json_as_is()]] - degree 6, connects to 2 communities
- [[test_generic_target_sends_content_body()]] - degree 6, connects to 2 communities
- [[test_openai_payload_includes_model()]] - degree 6, connects to 2 communities
