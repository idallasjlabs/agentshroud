---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "Community 90"
location: "L435"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_90
---

# wakeword_clear()

## Connections
- [[reset_all()]] - `calls` [INFERRED]
- [[test_clear_allows_fresh_tap()]] - `calls` [INFERRED]
- [[test_ptt_finish_ends_listening()]] - `calls` [INFERRED]
- [[test_ptt_finish_noop_when_idle()]] - `calls` [INFERRED]
- [[test_push_frame_suppressed_while_triggered()]] - `calls` [INFERRED]
- [[test_tap_in_idle_starts_listen()]] - `calls` [INFERRED]
- [[test_vad_timeout_fires_without_audio()]] - `calls` [INFERRED]
- [[voice_task()]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]
- [[wakeword.c_1]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_90