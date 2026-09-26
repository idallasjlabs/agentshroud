---
type: community
cohesion: 0.17
members: 12
---

# TestSetMode

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[A stalemismatched If-None-Match must serve the full new binary (200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[Authenticated request but no firmware on disk → 404 (not a 500empty 200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[Empty allowlist = OTA un-gated any non-empty token is accepted (200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[GET firmwarebin token gate, 200 + quoted SHA-256 ETag, HEAD ETag parity.]] - rationale - gateway/tests/test_voice_gateway.py
- [[If-None-Match equal to the current ETag → 304 with no body.      This is the who]] - rationale - gateway/tests/test_voice_gateway.py
- [[Wire the firmwarebin route to a fake binary + a fixed OTA token allowlist.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_fw_client()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_304_on_matching_if_none_match()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_404_when_absent()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_auth_and_etag()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_stale_if_none_match_returns_body()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_ungated_when_allowlist_empty()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSetMode
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_CollaboratorActivityTracker]]

## Top bridge nodes
- [[_fw_client()]] - degree 7, connects to 1 community
- [[test_firmware_bin_304_on_matching_if_none_match()]] - degree 3, connects to 1 community
- [[test_firmware_bin_404_when_absent()]] - degree 3, connects to 1 community
- [[test_firmware_bin_auth_and_etag()]] - degree 3, connects to 1 community
- [[test_firmware_bin_stale_if_none_match_returns_body()]] - degree 3, connects to 1 community