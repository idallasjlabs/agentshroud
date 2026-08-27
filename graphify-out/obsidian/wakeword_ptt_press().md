---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "Community 375"
location: "L445"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_375
---

# wakeword_ptt_press()

## Connections
- [[_ptt_start()]] - `calls` [EXTRACTED]
- [[_touch_pressed()]] - `calls` [INFERRED]
- [[_touch_start_only()]] - `calls` [INFERRED]
- [[do_tap()]] - `calls` [INFERRED]
- [[test_drain_keeps_face_off_idle_when_retriggered()]] - `calls` [INFERRED]
- [[test_playback_state.c (host-native unit tests, SCRUM-59)]] - `calls` [EXTRACTED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_375