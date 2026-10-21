---
type: community
members: 5
---

# 8D Root Cause Analysis (2)

**Members:** 5 nodes

## Members
- [[Audio clicking fix — TTS resume dedup + dither + voice-gateway cpuset widen]] - rationale - CHANGELOG.md
- [[ESP32 live model label fix — server-authoritative label push]] - rationale - CHANGELOG.md
- [[Firmware TLS connect reliability — timeout 5s to 10s (DERP handshake race)]] - rationale - CHANGELOG.md
- [[Streaming direct voice path (_call_llm_stream) — avoids blocking full-reply wait]] - rationale - CHANGELOG.md
- [[v1.6.0 Release — Voice Terminal]] - rationale - CHANGELOG.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/8D_Root_Cause_Analysis_2
SORT file.name ASC
```
