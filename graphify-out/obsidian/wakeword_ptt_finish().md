---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "wakeword.c"
location: "L448"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/wakewordc
---

# wakeword_ptt_finish()

## Connections
- [[_touch_pressed()]] - `calls` [INFERRED]
- [[test_clear_allows_fresh_tap()]] - `calls` [INFERRED]
- [[test_ptt_finish_ends_listening()]] - `calls` [INFERRED]
- [[test_ptt_finish_noop_when_idle()]] - `calls` [INFERRED]
- [[voice_task()]] - `calls` [INFERRED]
- [[vt_remote_log()]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/wakewordc
