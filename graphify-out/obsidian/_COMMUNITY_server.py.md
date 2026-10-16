---
type: community
cohesion: 0.22
members: 9
---

# server.py

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[Build the per-device OTA token allowlist (SCRUM-58).      Owner-gated rollout o]] - rationale - voice_gateway/server.py
- [[Constant-time allowlist check for an OTA ``token=`` value.      Returns True wh]] - rationale - voice_gateway/server.py
- [[Request_10]] - code - voice_gateway/server.py
- [[Response_1]] - code - voice_gateway/server.py
- [[Serve the current ESP32 firmware binary for OTA (SCRUM-58).      Contract expect]] - rationale - voice_gateway/server.py
- [[_get_firmware_etag()]] - code - voice_gateway/server.py
- [[_load_ota_tokens()]] - code - voice_gateway/server.py
- [[_ota_token_ok()]] - code - voice_gateway/server.py
- [[firmware_bin()]] - code - voice_gateway/server.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/serverpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_voice_latency_guard.py]]

## Top bridge nodes
- [[firmware_bin()]] - degree 6, connects to 1 community
- [[_ota_token_ok()]] - degree 4, connects to 1 community
- [[_load_ota_tokens()]] - degree 3, connects to 1 community
- [[_get_firmware_etag()]] - degree 2, connects to 1 community
