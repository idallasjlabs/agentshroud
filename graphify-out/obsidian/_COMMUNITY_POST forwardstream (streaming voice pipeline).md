---
type: community
cohesion: 1.00
members: 1
---

# POST /forward/stream (streaming voice pipeline)

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[POST forwardstream (streaming voice pipeline)]] - code - gateway/ingest_api/routes/forward.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/POST_/forward/stream_streaming_voice_pipeline
SORT file.name ASC
```
