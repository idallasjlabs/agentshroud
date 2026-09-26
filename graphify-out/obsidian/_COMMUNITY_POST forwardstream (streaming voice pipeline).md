---
type: community
cohesion: 1.00
members: 1
---

# POST /forward/stream (streaming voice pipeline)

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[CVE Triage Report Cron Prompt]] - document - docker/config/openclaw/cron/prompts/cve-triage-report.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/POST_/forward/stream_streaming_voice_pipeline
SORT file.name ASC
```
