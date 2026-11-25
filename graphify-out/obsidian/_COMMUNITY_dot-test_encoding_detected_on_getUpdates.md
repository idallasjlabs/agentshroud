---
type: community
members: 11
---

# .test_encoding_detected_on_getUpdates

**Members:** 11 nodes

## Members
- [[dot-process_inbound()_6]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_7]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-process_inbound()_8]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_encoding_detected_on_getUpdates()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_pipeline_not_called_without_text()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Base64-encoded injection via getUpdates must be caught.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[EncodingDetectingPipeline]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[FakePipelineResult]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Pipeline that detects base64-encoded injections.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Updates without text (e.g. photos) should skip the pipeline.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[process_inbound()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_encoding_detected_on_getUpdates
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY__wrap_response]]
- 2 edges to [[_COMMUNITY_dot-_make_proxy]]
- 2 edges to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_PassthroughPipeline]]

## Top bridge nodes
- [[dot-test_encoding_detected_on_getUpdates()]] - degree 7, connects to 2 communities
- [[dot-test_pipeline_not_called_without_text()]] - degree 6, connects to 2 communities
- [[FakePipelineResult]] - degree 5, connects to 1 community
- [[EncodingDetectingPipeline]] - degree 4, connects to 1 community
- [[dot-process_inbound()_6]] - degree 2, connects to 1 community
