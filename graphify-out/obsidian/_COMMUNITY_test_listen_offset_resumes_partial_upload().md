---
type: community
cohesion: 0.29
members: 7
---

# test_listen_offset_resumes_partial_upload()

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[A drop mid-upload must not force a full resend the next connection sends…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_capture_transcribe()]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_transcribe()_1]] - code - gateway/tests/test_voice_gateway.py
- [[pcm_chunks must stop growing once _PCM_MAX_BYTES is reached.      A device that]] - rationale - gateway/tests/test_voice_gateway.py
- [[test_listen_offset_resumes_partial_upload()]] - code - gateway/tests/test_voice_gateway.py
- [[test_pcm_buffer_bounded()]] - code - gateway/tests/test_voice_gateway.py
- [[test_pcm_buffer_bounded()_1]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_listen_offset_resumes_partial_upload
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[test_listen_offset_resumes_partial_upload()]] - degree 6, connects to 2 communities
- [[test_pcm_buffer_bounded()]] - degree 4, connects to 2 communities
- [[test_pcm_buffer_bounded()_1]] - degree 2, connects to 1 community