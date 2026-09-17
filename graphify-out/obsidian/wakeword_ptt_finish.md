---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "Community 363"
location: "448"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_363
---

# wakeword_ptt_finish

## Connections
- [[_touch_pressed]] - `calls` [INFERRED]
- [[test_clear_allows_fresh_tap()]] - `calls` [INFERRED]
- [[test_ptt_finish_ends_listening()]] - `calls` [INFERRED]
- [[test_ptt_finish_noop_when_idle()]] - `calls` [INFERRED]
- [[voice_task]] - `calls` [INFERRED]
- [[vt_remote_log]] - `calls` [INFERRED]
- [[vt_remote_log_1]] - `calls` [EXTRACTED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_363