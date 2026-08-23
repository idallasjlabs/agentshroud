---
source_file: "firmware/voice-terminal/main/wakeword.c"
type: "code"
community: "Playback State (test_playback_state)"
location: "L494"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Playback_State_test_playback_state
---

# wakeword_tts_playing()

## Connections
- [[_on_vg_state()]] - `calls` [INFERRED]
- [[rlog_task()]] - `calls` [INFERRED]
- [[test_drain_clears_playing_and_returns_idle()]] - `calls` [INFERRED]
- [[test_drain_keeps_face_off_idle_when_retriggered()]] - `calls` [INFERRED]
- [[test_gate_open_sets_speaking_and_tts_playing()]] - `calls` [INFERRED]
- [[test_gate_stays_closed_leaves_state_idle()]] - `calls` [INFERRED]
- [[voice_task()]] - `calls` [INFERRED]
- [[wakeword.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Playback_State_test_playback_state