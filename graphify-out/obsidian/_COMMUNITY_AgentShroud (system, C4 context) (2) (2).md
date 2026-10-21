---
type: community
members: 9
---

# AgentShroud (system, C4 context) (2) (2)

**Members:** 9 nodes

## Members
- [[Build the per-device OTA token allowlist (SCRUM-58).      Owner-gated rollout o]] - rationale - voice_gateway/server.py
- [[Constant-time allowlist check for an OTA ``token=`` value.      Returns True wh]] - rationale - voice_gateway/server.py
- [[Request]] - code - voice_gateway/server.py
- [[Response]] - code - voice_gateway/server.py
- [[Serve the current ESP32 firmware binary for OTA (SCRUM-58).      Contract expect]] - rationale - voice_gateway/server.py
- [[_get_firmware_etag()]] - code - voice_gateway/server.py
- [[_load_ota_tokens()]] - code - voice_gateway/server.py
- [[_ota_token_ok()]] - code - voice_gateway/server.py
- [[firmware_bin()]] - code - voice_gateway/server.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_system_C4_context_2_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ProgressiveLockdown]]

## Top bridge nodes
- [[firmware_bin()]] - degree 6, connects to 1 community
- [[_ota_token_ok()]] - degree 4, connects to 1 community
- [[_load_ota_tokens()]] - degree 3, connects to 1 community
- [[_get_firmware_etag()]] - degree 2, connects to 1 community
