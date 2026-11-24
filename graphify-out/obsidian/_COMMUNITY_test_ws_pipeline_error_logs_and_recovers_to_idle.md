---
type: community
members: 3
---

# test_ws_pipeline_error_logs_and_recovers_to_idle

**Members:** 3 nodes

## Members
- [[When the STT→LLM→TTS pipeline raises, the inner exception handler must 1. log…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_failing_transcribe()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ws_pipeline_error_logs_and_recovers_to_idle
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - degree 4, connects to 2 communities
