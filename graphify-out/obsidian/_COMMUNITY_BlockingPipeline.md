---
type: community
members: 21
---

# BlockingPipeline

**Members:** 21 nodes

## Members
- [[dot-process_inbound()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_clean_message_passes_through()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_encoding_detected_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_inbound_text_normalized_before_pipeline()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_owner_message_not_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_pipeline_not_called_without_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[Updates without text (e.g. photos) should skip the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Zero-width obfuscation should be normalized before pipeline evaluation.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[process_inbound()]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/BlockingPipeline
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_FakeRBAC]]
- 9 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 2 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2)]]

## Top bridge nodes
- [[BlockingPipeline]] - degree 10, connects to 3 communities
- [[dot-test_clean_message_passes_through()]] - degree 7, connects to 3 communities
- [[dot-test_encoding_detected_on_getUpdates()]] - degree 7, connects to 3 communities
- [[dot-test_inbound_text_normalized_before_pipeline()]] - degree 7, connects to 3 communities
- [[dot-test_owner_message_not_blocked()]] - degree 7, connects to 3 communities
