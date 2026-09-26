---
type: community
cohesion: 0.21
members: 12
---

# TestSSRFBlocking

**Cohesion:** 0.21 - loosely connected
**Members:** 12 nodes

## Members
- [[Emit a structured per-transcription latency record for the STT AB.      Tags ea]] - rationale - voice_gateway/stt.py
- [[Read WHISPER_MODEL_SIZE from the environment and validate it (AB knob).]] - rationale - voice_gateway/stt.py
- [[Release the loaded model (for testing  memory pressure).]] - rationale - voice_gateway/stt.py
- [[Resolve a requested Whisper model size, with a safe default fallback.      Pure]] - rationale - voice_gateway/stt.py
- [[Transcribe raw 16-bit signed PCM mono audio to text.      Args         pcm_byte]] - rationale - voice_gateway/stt.py
- [[_get_model()]] - code - voice_gateway/stt.py
- [[_resolve_model_size()]] - code - voice_gateway/stt.py
- [[record_transcription_latency()]] - code - voice_gateway/stt.py
- [[reset_model()]] - code - voice_gateway/stt.py
- [[select_model_size()]] - code - voice_gateway/stt.py
- [[stt.py]] - code - voice_gateway/stt.py
- [[transcribe()]] - code - voice_gateway/stt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSSRFBlocking
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_.claudesettings.json (hook + permission wiring)]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]

## Top bridge nodes
- [[stt.py]] - degree 9, connects to 3 communities