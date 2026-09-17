---
type: community
cohesion: 0.11
members: 18
---

# Community 521

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-process_inbound()_7]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_8]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_9]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_clean_message_passes_through()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_encoding_detected_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_inbound_text_normalized_before_pipeline()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_message_not_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_prompt_injection_blocked_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Base64-encoded injection via getUpdates must be caught.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[BlockingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[EncodingDetectingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[FakePipelineResult]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Normal messages must pass through the pipeline unmodified.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner messages must pass even if the pipeline would block them.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that blocks any message containing injection keywords.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that detects base64-encoded injections.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Prompt injection via getUpdates must be blocked by the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width obfuscation should be normalized before pipeline evaluation.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_521
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 8 edges to [[_COMMUNITY_Telegram Lockdown & Collaborator UX Tests]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 3 edges to [[_COMMUNITY_Community 119]]
- 3 edges to [[_COMMUNITY_Collaborator Activity & Telegram Proxy]]
- 1 edge to [[_COMMUNITY_Community 419]]
- 1 edge to [[_COMMUNITY_Community 69]]
- 1 edge to [[_COMMUNITY_Community 608]]

## Top bridge nodes
- [[BlockingPipeline]] - degree 13, connects to 7 communities
- [[EncodingDetectingPipeline]] - degree 7, connects to 4 communities
- [[FakePipelineResult]] - degree 7, connects to 4 communities
- [[dot-test_clean_message_passes_through()]] - degree 7, connects to 2 communities
- [[dot-test_encoding_detected_on_getUpdates()]] - degree 7, connects to 2 communities