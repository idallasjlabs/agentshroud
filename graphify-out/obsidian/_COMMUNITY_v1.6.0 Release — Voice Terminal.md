---
type: community
cohesion: 0.40
members: 5
---

# v1.6.0 Release — Voice Terminal

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[Audio clicking fix — TTS resume dedup + dither + voice-gateway cpuset widen]] - rationale - CHANGELOG.md
- [[ESP32 live model label fix — server-authoritative label push]] - rationale - CHANGELOG.md
- [[Firmware TLS connect reliability — timeout 5s to 10s (DERP handshake race)]] - rationale - CHANGELOG.md
- [[Streaming direct voice path (_call_llm_stream) — avoids blocking full-reply wait]] - rationale - CHANGELOG.md
- [[v1.6.0 Release — Voice Terminal]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/v160_Release__Voice_Terminal
SORT file.name ASC
```
