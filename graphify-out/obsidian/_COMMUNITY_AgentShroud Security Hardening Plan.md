---
type: community
cohesion: 0.10
members: 23
---

# AgentShroud Security Hardening Plan

**Cohesion:** 0.10 - loosely connected
**Members:** 23 nodes

## Members
- [[Anthropic v1messages response → OpenAI v1chatcompletions envelope.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[If openai_to_gemini_request raises, the request must still be     forwarded (unm]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[Regression don't break the existing v1messages path.]] - rationale - gateway/tests/test_chat_completions_alias.py
- [[The combined path v1chatcompletions with model=claude- must     end up POST]] - rationale - gateway/tests/test_claude_via_openai_path.py
- [[The combined path v1chatcompletions with model=gemini- must end     up POST]] - rationale - gateway/tests/test_gemini_via_openai_path.py
- [[Translate an OpenAI v1chatcompletions request body to Anthropic v1messages.]] - rationale - gateway/proxy/anthropic_openai_translator.py
- [[anthropic_to_openai_response()]] - code - gateway/proxy/anthropic_openai_translator.py
- [[client()_3]] - code - gateway/tests/test_chat_completions_alias.py
- [[llm_proxy.py]] - code - gateway/proxy/llm_proxy.py
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
TABLE source_file, type FROM #community/AgentShroud_Security_Hardening_Plan
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_soc.js]]
- 6 edges to [[_COMMUNITY_test_gemini_openai_translator.py]]
- 6 edges to [[_COMMUNITY_SecureBrowser]]
- 2 edges to [[_COMMUNITY_test_trust_manager.py]]
- 2 edges to [[_COMMUNITY_Skill UI Expert (UI)]]
- 1 edge to [[_COMMUNITY_AgentShroud Project Terminology]]
- 1 edge to [[_COMMUNITY_graphify Skill]]
- 1 edge to [[_COMMUNITY_Oracle — Feedback Analyst]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]

## Top bridge nodes
- [[llm_proxy.py]] - degree 16, connects to 7 communities
- [[anthropic_to_openai_response()]] - degree 8, connects to 3 communities
- [[openai_to_anthropic_request()]] - degree 7, connects to 3 communities
- [[test_gemini_via_openai_path.py]] - degree 5, connects to 2 communities
- [[test_claude_via_openai_path.py]] - degree 9, connects to 1 community